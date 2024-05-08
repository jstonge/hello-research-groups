---
theme: dashboard
title: Summary data
toc: false
sql:
    training: ./data/training_data.parquet
---

# Summary database

<div class="grid grid-cols-4">
  <div class="card">
    <h2>Unique authors</h2>                                                                         
    <span class="big">${[...uniq_name].length}</span>
  </div>
</div>


## Collaboration patterns


<div>${resize((width) => 
Plot.plot({
  width,
  marginBottom: 100,
  color: {scheme: "spectral", legend: true},
  y: {grid: true},
  x: {tickRotate: 45},
  fx: {
    label: "career stage (numbers represent cutpoints, e.g. <4, <7, <12, <17, and <30 years since first publication)",
    },
  marks: [
    Plot.barY(training1, {
      x: "college", y: "mean_collab", 
      fill: "age_bucket", fx: "career_stage", 
      }),
    Plot.ruleY([0])
  ]
})
)}
</div>

## Professors' collaboration rate with younger academics (>7 years younger)

<div>${resize((width) => 
Plot.plot({
  width,
  height: 400,
  y: {grid: true}, 
  color: {legend: true},
  marks: [
    Plot.frame(),
    Plot.ruleX([8], { dx: -18,  strokeDasharray: 3 }),
    Plot.tickY(training_all, {
      x: "author_age", y: "changing_rate", z: "name", stroke: "college", strokeOpacity: 0.5, fx: "has_research_group",
      sort: {x: "x"}
    }),
    Plot.lineY(
      training_all,
          Plot.groupX(
            { y: "median" },
            { x: "author_age", y: "changing_rate", stroke: "college", fx: "has_research_group", 
              strokeWidth: 4, tip: true, sort: {x: "-y"} },
          )
    ),
    Plot.axisY({anchor: "left"})
  ]
})
)}
</div>

## Collaboration patterns

We are intersted in the relationship between group size, collaboration norms, and the emergence of computational works. More precisely, we want to know whether strong collaboration patterns could help humanities transitioning into the computational realm. 

At the moment, we simply calculate `density` of interactions among faculties' younger collaboraters. The idea is that a group with strong collaboration norms is characterized by early career researchers working togeher early on.

One issue with density is that it doesn't take into account the recurrent relationships, aka whether younger folks keep collaborating on each others' papers.

```js
Plot.plot({
  width: 800,
  height: 500,
  marginLeft: 35,
  marginBottom: 50,
  color: {legend: true, scheme: "viridis"},
  x: { label: "changing rate" },
  y: { label: "density" },
  marks: [
    Plot.cell(training_all_agg.filter(d => d.density < 1.00 & d.density > 0.), Plot.bin({ fill: "proportion" }, {
      x: d => parseInt(d["changing_rate"].toFixed(1)), y: d => parseFloat(d["density"].toFixed(1)), fx: "has_research_group"
    })),
    Plot.frame()
  ]
})
```

## Balancing annotations

To study group size across field of sciences, we would as many faculties with and without resarch groups in each domain. At the moment, we oversampled faculties with research groups because we were interested in characterizing group size.

<div>${resize((width) => 
Plot.plot({
  width,
  fx: {ticksRotation: 90},
  color: {legend: true, type: "ordinal", range: ["lightblue", "orange"]},
  marks: [
    Plot.barY(uniq_name, Plot.groupX({ y: "count" }, {
      x: "has_research_group", fill: "has_research_group", fx: "college", sort: {x: "-y"}
      })),
    Plot.gridY(),
    Plot.ruleY([0])
  ]
})
)}
</div>

## Training data

This is the data wrangled into aggregated table we ought to use for training.

```sql
SELECT * FROM training
```

```sql  id=training1 
WITH long_table AS (
    UNPIVOT training
    ON younger, same_age, older 
    INTO
        NAME age_bucket
        VALUE val
)
SELECT 
  age_bucket, MEAN(val) as mean_collab, college,
  CASE 
    WHEN author_age <= 4 THEN 4 
    WHEN author_age <= 7 THEN 7 
    WHEN author_age <= 12 THEN 12 
    WHEN author_age <= 17 THEN 17
    WHEN author_age <= 30 THEN 30
    ELSE 999
    END AS career_stage
  FROM long_table
  WHERE college in ('Humanities', 'Social Sciences', 'Physical Sciences', 'Engineering', 'Computer Science') AND career_stage != 999
  GROUP BY college, career_stage, age_bucket
```

```sql id=uniq_name 
SELECT name, has_research_group, college
FROM training 
WHERE has_research_group is not NULL and college not in ('Agriculture', 'Health', 'Medical Sciences', 'Education', 'Language')  AND has_research_group != -1
GROUP BY name, has_research_group, college
ORDER BY name
```

```sql id=[...training_all_agg] 
SELECT name, changing_rate, MEAN(density) as density, has_research_group
FROM training 
WHERE changing_rate < 40 AND author_age < 30 AND has_research_group is not NULL AND has_research_group != -1
GROUP BY name, changing_rate, has_research_group
```

```sql id=training_all 
  SELECT DISTINCT name, changing_rate, college, author_age, has_research_group::CHAR as has_research_group
  FROM training 
  WHERE 
    changing_rate < 40 AND 
    author_age < 30 AND 
    College not in ('Agriculture', 'Health', 'Medical Sciences', 'Education', 'Language') AND
    has_research_group is not NULL AND has_research_group != -1.0
  ORDER BY author_age
```

# Data quality check

Checking author age. most often if above 50 years old it is a glitch in min paper year that needs to be fixed. Right now we are doing it manually.

```sql
SELECT name, MAX(author_age) as author_age, department FROM training WHERE author_age > 50 GROUP BY name, department 
```

# Department to category mapping

```js
Inputs.table([
    {
        "department": "Psychology",
        "category": "Psychological Science"
    },
    {
        "department": "Computer Science",
        "category": "Computer Science"
    },
    {
        "department": "Mathematics and Statistics",
        "category": "Mathematical Sciences"
    },
    {
        "department": "Human Development",
        "category": "Social Sciences"
    },
    {
        "department": "School of Information",
        "category": "Computer Science"
    },
    {
        "department": "Electrical Engineering and Computer Sciences",
        "category": "Computer Science"
    },
    {
        "department": "Biology",
        "category": "Biological Sciences"
    },
    {
        "department": "Computer science",
        "category": "Computer Science"
    },
    {
        "department": "Information Science",
        "category": "Information Science"
    },
    {
        "department": "Computer Engineering and Mathematics",
        "category": "Computer Science"
    },
    {
        "department": "Linguistics",
        "category": "Humanities"
    },
    {
        "department": "anthropology",
        "category": "Social Sciences"
    },
    {
        "department": "Electrical and Biomedical Engineering",
        "category": "Computer Science"
    },
    {
        "department": "Physics",
        "category": "Physical Science"
    },
    {
        "department": "Community Development and Applied Economics",
        "category": "Social Sciences"
    },
    {
        "department": "Electrical & Computer Engineering",
        "category": "Computer Science"
    },
    {
        "department": "Nutrition and Food Sciences",
        "category": "Agriculture"
    },
    {
        "department": "English",
        "category": "Humanities"
    },
    {
        "department": "Civil and Environmental Engineering",
        "category": "Engineering"
    },
    {
        "department": "Electrical Engineering & Computer Sciences",
        "category": "Computer Science"
    },
    {
        "department": "Grossman School of Business",
        "category": "Business"
    },
    {
        "department": "College of Engineering and Mathematical Sciences",
        "category": "Engineering"
    },
    {
        "department": "Microbiology and Molecular Genetics",
        "category": "Biological Sciences"
    },
    {
        "department": "Network Science Institute",
        "category": "Computer Science"
    },
    {
        "department": "Pathology and Laboratory Medicine",
        "category": "Medical Sciences"
    },
    {
        "department": "Public health Sciences",
        "category": "Health"
    },
    {
        "department": "Mathematics & Statistics",
        "category": "Mathematical Sciences"
    },
    {
        "department": "Communication Studies",
        "category": "Social Sciences"
    },
    {
        "department": "Political Science",
        "category": "Social Sciences"
    },
    {
        "department": "Cell and Molecular Biology",
        "category": "Biological Sciences"
    },
    {
        "department": "Business",
        "category": "Business"
    },
    {
        "department": "Public Policy",
        "category": "Social Sciences"
    },
    {
        "department": "Urban Studies and Planning",
        "category": "Social Sciences"
    },
    {
        "department": "History and French Studies",
        "category": "Humanities"
    },
    {
        "department": "Cognitive Neuroscience",
        "category": "Psychological Science"
    },
    {
        "department": "Environment and Natural Resources",
        "category": "Earth Science"
    },
    {
        "department": "Information School",
        "category": "Computer Science"
    },
    {
        "department": "Business and Economics",
        "category": "Business"
    },
    {
        "department": "Neuroscience",
        "category": "Psychological Science"
    },
    {
        "department": "Philosophy",
        "category": "Humanities"
    },
    {
        "department": "Molecular Physiology and Biophysics",
        "category": "Health"
    },
    {
        "department": "Science, Technology, and Society",
        "category": "Social Sciences"
    },
    {
        "department": "History",
        "category": "Humanities"
    },
    {
        "department": "Human Ecology",
        "category": "Social Sciences"
    },
    {
        "department": "Experimental Psychology",
        "category": "Psychological Science"
    },
    {
        "department": "Statistics & Data Science",
        "category": "Mathematical Sciences"
    },
    {
        "department": "Santa Fe Institute",
        "category": "Social Sciences"
    },
    {
        "department": "French",
        "category": "Language"
    },
    {
        "department": "History",
        "category": "Humanities"
    },
    {
        "department": "Bioengineering, Electrical & Systems Engineering",
        "category": "Engineering"
    },
    {
        "department": "Physics & Astronomy",
        "category": "Physical Science"
    },
    {
        "department": "Neurology",
        "category": "Medical Sciences"
    },
    {
        "department": "Psychiatry",
        "category": "Medical Sciences"
    },
    {
        "department": "Anthropology",
        "category": "Social Sciences"
    },
    {
        "department": "Orthopaedics",
        "category": "Medical Sciences"
    },
    {
        "department": "Surgery",
        "category": "Medical Sciences"
    },
    {
        "department": "Psychological science",
        "category": "Psychological Science"
    },
    {
        "department": "Communications",
        "category": "Social Sciences"
    },
    {
        "department": "Sociology",
        "category": "Social Sciences"
    },
    {
        "department": "Rubenstein School of Environment and Natural Resources",
        "category": "Earth Science"
    },
    {
        "department": "College of Education and Social Services",
        "category": "Education"
    },
    {
        "department": "Obstetrics, Gynecology and Reproductive Sciences",
        "category": "Medical Sciences"
    },
    {
        "department": "Communication Sciences and Disorders",
        "category": "Psychological Science"
    },
    {
        "department": "Plant and Soil Science",
        "category": "Biological Sciences"
    },
    {
        "department": "Biomedical and Health Sciences",
        "category": "Medical Sciences"
    },
    {
        "department": "Pharmacology",
        "category": "Medical Sciences"
    },
    {
        "department": "Plant Biology",
        "category": "Biological Sciences"
    },
    {
        "department": "Information Sciences and Technology",
        "category": "Information Science"
    },
    {
        "department": "School of Interactive Computing",
        "category": "Computer Science"
    },
    {
        "department": "Mathematics and Computer Science",
        "category": "Mathematical Sciences"
    },
    {
        "department": "Psychological Science",
        "category": "Psychological Science"
    },
    {
        "department": "Chemical Engineering",
        "category": "Engineering"
    },
    {
        "department": "Swine nutrition & management",
        "category": "Agriculture"
    },
    {
        "department": "Chemistry",
        "category": "Chemical Science"
    },
    {
        "department": "Materials Science and Engineering",
        "category": "Engineering"
    },
    {
        "department": "Education and Social Services",
        "category": "Education"
    },
    {
        "department": "Diagnostic Medicine and pathobiology",
        "category": "Medical Sciences"
    },
    {
        "department": "French and Italian",
        "category": "Language"
    },
    {
        "department": "Human Evolutionary Biology",
        "category": "Biological Sciences"
    },
    {
        "department": "Brain and Cognitive Sciences",
        "category": "Psychological Science"
    },
    {
        "department": "Community Development & Applied Economics",
        "category": "Social Sciences"
    },
    {
        "department": "Information science",
        "category": "Computer Science"
    },
    {
        "department": "Communication",
        "category": "Social Sciences"
    },
    {
        "department": "Industrial Engineering and Operations Research",
        "category": "Engineering"
    },
    {
        "department": "Communication sciences and disorders",
        "category": "Psychological Science"
    },
    {
        "department": "English and Quantitative Theory and Methods",
        "category": "Humanities"
    },
    {
        "department": "Geography and Geosciences",
        "category": "Earth Science"
    },
    {
        "department": "Natural Resources and the Environment",
        "category": "Earth Science"
    },
    {
        "department": "Environmental Science and Policy",
        "category": "Earth Science"
    },
    {
        "department": "Biochemistry",
        "category": "Chemical Science"
    },
    {
        "department": "Statistics",
        "category": "Mathematical Sciences"
    },
    {
        "department": "Psychological and Behavioural Science",
        "category": "Psychological Science"
    },
    {
        "department": "Chemical and Biological Engineering",
        "category": "Engineering"
    },
    {
        "department": "Economics",
        "category": "Social Sciences"
    },
    {
        "department": "Mechanical Engineering",
        "category": "Engineering"
    },
    {
        "department": "Human Development and Family Science",
        "category": "Social Sciences"
    },
    {
        "department": "Geology",
        "category": "Earth Science"
    },
    {
        "department": "Biomedical and Health Science",
        "category": "Medical Sciences"
    },
    {
        "department": "Classics",
        "category": "Humanities"
    },
    {
        "department": "Computational Psychiatry",
        "category": "Psychological Science"
    },
    {
        "department": "Evolution and Ecology",
        "category": "Biological Sciences"
    },
    {
        "department": "Anesthesiology",
        "category": "Medical Sciences"
    },
    {
        "department": "Family Medicine",
        "category": "Medical Sciences"
    },
    {
        "department": "Electrical, Computer, and Energy Engineering",
        "category": "Computer Science"
    },
    {
        "department": "Brain and Cognitive Sciences",
        "category": "Psychological Science"
    },
    {
        "department": "Molecular Sciences",
        "category": "Biological Sciences"
    },
    {
        "department": "Rehabilitation and Movement Science",
        "category": "Health"
    },
    {
        "department": "School of Economics",
        "category": "Social Sciences"
    },
    {
        "department": "Higher Education and Student Affairs Administration",
        "category": "Education"
    },
    {
        "department": "African Studies Program",
        "category": "Humanities"
    },
    {
        "department": "Library Science",
        "category": "Information Science"
    },
    {
        "department": "Informatics and Computing",
        "category": "Computer Science"
    },
    {
        "department": "Spatial Sciences",
        "category": "Humanities"
    },
    {
        "department": "Philosophy & Religious Studies",
        "category": "Humanities"
    },
    {
        "department": "Spanish and Portuguese",
        "category": "Humanities"
    },
    {
        "department": "Comparative Literature",
        "category": "Humanities"
    },
    {
        "department": "School of Fisheries, Aquaculture & Aquatic Sciences",
        "category": "Biological Sciences"
    },
    {
        "department": "Geography",
        "category": "Earth Science"
    },
    {
        "department": "Applied Ecology",
        "category": "Biological Sciences"
    },
    {
        "department": "Plant Science and Conservation",
        "category": "Biological Sciences"
    },
    {
        "department": "Systems and Computer Engineering",
        "category": "Computer Science"
    },
    {
        "department": "Medicine",
        "category": "Medical Sciences"
    },
    {
        "department": "Chemical and Biomolecular Engineering",
        "category": "Engineering"
    },
    {
        "department": "Forestry",
        "category": "Biological Sciences"
    },
    {
        "department": "Biological Sciences",
        "category": "Biological Sciences"
    },
    {
        "department": "Wildlife Biology",
        "category": "Biological Sciences"
    },
    {
        "department": "Ecosystem and Conservation Sciences",
        "category": "Earth Science"
    },
    {
        "department": "Rangeland and Restoration Ecology",
        "category": "Earth Science"
    },
    {
        "department": "Electrical and Computer Engineering",
        "category": "Computer Science"
    },
    {
        "department": "Molecular Biology",
        "category": "Biological Sciences"
    },
    {
        "department": "Environment and Society",
        "category": "Social Sciences"
    },
    {
        "department": "Biosciences",
        "category": "Biological Sciences"
    },
    {
        "department": "Chemical and Biochemical Engineering",
        "category": "Engineering"
    },
    {
        "department": "Biomedical Engineering",
        "category": "Engineering"
    },
    {
        "department": "Cell biology and Physiology",
        "category": "Health"
    }
])
```

