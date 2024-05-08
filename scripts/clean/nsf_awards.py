import zipfile
import xml.etree.ElementTree as ET
import pandas as pd
from pathlib import Path
from tqdm import tqdm

def flatten(element, path=''):
    """
    Recursively extract all values, creating a flat dictionary
    with paths as keys and text as values.
    """
    # Dictionary to store the extracted data
    data = {}
    
    # Determine the path prefix for nested elements
    path = f"{path}{element.tag}." if path else f"{element.tag}."
    
    # Loop through each child element recursively
    for child in element:
        child_data = flatten(child, path)
        for k, v in child_data.items():
            if k in data:
                if isinstance(data[k], list):
                    data[k].append(v)
                else:
                    data[k] = [data[k], v]
            else:
                data[k] = v
    
    # If the element has text, consider it a value
    if element.text and element.text.strip():
        text_key = path[:-1]  # Remove trailing dot
        if text_key in data:
            if isinstance(data[text_key], list):
                data[text_key].append(element.text.strip())
            else:
                data[text_key] = [data[text_key], element.text.strip()]
        else:
            data[text_key] = element.text.strip()
    
    return data

def get_award_df(fname):
    all_awards = []
    with zipfile.ZipFile(fname, 'r') as zip_file:
        for xmlfile in zip_file.namelist():
            try:
                with zip_file.open(xmlfile) as f:
                    tree = ET.parse(f)
                    root = tree.getroot()
                
                for award in root.findall('Award'):
                    awards = flatten(award)
                
                all_awards.append(awards)
                
            except:
                print(f"Failed to process {xmlfile}")
    
    # print(f"{len(all_awards)/len(zip_file.namelist())} are parsed just fine ({fname})")

    df = pd.DataFrame(all_awards)
    
    df.columns = df.columns.str.replace("Award.", "")
    df.columns = df.columns.str.replace(".", "_")
    
    col2keep = ["AwardTitle", "AwardEffectiveDate", "AwardInstrument_Value", 
                'AwardAmount', 'Institution_StateName', 'Institution_Name', 
                "Organization_Directorate_LongName", 
                'Investigator_RoleCode', 
                'Investigator_PI_FULL_NAME', 
                "Institution_CityName"]
    
    col2keep = set(col2keep) & set(df.columns)
    
    df = df[list(col2keep)]
    
    # Im LAZY; it'll be easier to reuse same functions i wrote the the ERC dashboard
    df['Call_Year'] = df.AwardEffectiveDate.str.split("/").map(lambda x: x[-1]).astype(int)

    nsf2erc = {
        "AwardTitle": "Project_Title",
        "AwardAmount": "EU_contribution", 
        "Institution_Name":"Host_Institution(s)", 
        "Organization_Directorate_LongName": "Domain",
        "AwardInstrument_Value": "Grant_Type",
    }

    df.columns = df.columns.map(lambda x: nsf2erc[x] if x in nsf2erc else x)

    # Taking care of co-PIs
    df['Investigator_RoleCode'] = df['Investigator_RoleCode'].map(lambda x: x if isinstance(x, list) else [x])
    df['Investigator_PI_FULL_NAME'] = df['Investigator_PI_FULL_NAME'].map(lambda x: x if isinstance(x, list) else [x])

    researchers=[]
    for names, roles in zip(df['Investigator_PI_FULL_NAME'], df['Investigator_RoleCode']):
            PI_found = False
            for name, role in zip(names, roles):
                # HERE WE SIMPLY GRAB THE FIRST PI WE FIND
                if role == 'Principal Investigator':
                    PI_found = True
                    researchers.append(name)
                    break
            
            if PI_found == False:
                researchers.append(None)

    df['Researcher(s)'] = researchers
    
    # rare but it happens
    df = df[~df['Researcher(s)'].isna()]

    # sometimes there are multiple institutions; we grab the first one.
    df["Institution_StateName"] = df["Institution_StateName"].map(lambda x: x[0] if isinstance(x, list) else x)
    df["Institution_CityName"] = df["Institution_CityName"].map(lambda x: x[0] if isinstance(x, list) else x)
    df["Host_Institution(s)"] = df["Host_Institution(s)"].map(lambda x: x[0] if isinstance(x, list) else x)
    
    df = df[~df["Institution_StateName"].isna()]

    # Lets keep as light as possible for now
    df.drop(columns=['Investigator_RoleCode', 'Investigator_PI_FULL_NAME', 'AwardEffectiveDate'], inplace=True)

    return df

def main():
    input_dir = Path("../../data/raw/nsf_awards/")
    output_dir = Path("../../docs/data/")
    fnames = list(input_dir.glob("*.zip"))
    dfs = []
    for fname in tqdm(fnames, total=len(fnames)):
        # thissss is sloow but whatev forn now
        dfs.append(get_award_df(fname))
    
    all_df = pd.concat(dfs, axis=0).reset_index(drop=True)
    all_df = all_df[all_df['EU_contribution'].astype(float) > 0]

    cols2keep = ['Call_Year', 'Grant_Type', 'EU_contribution' , 'Institution_StateName', 'Project_Title', 'Researcher(s)', 'Domain', 'Host_Institution(s)', 'Institution_CityName']
    
    all_df = all_df[cols2keep]

    all_df = all_df[(all_df.Call_Year > 1960) & all_df.Call_Year < 2024]

    all_df.to_parquet(output_dir / "nsf_awards.parquet")
        

if __name__ == "__main__":
    main()