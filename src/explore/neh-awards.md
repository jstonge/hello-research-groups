---
sql:
  data: ../data/neh_awards.parquet
---

<div class="hero">
  <h1>Exploring National Endowment of humanities</h1>
  <h2>A small exploration of the data available from <a href="https://www.neh.gov/grants/listing">https://www.neh.gov/grants/listing</a>.</h2>
  <div class="grid grid-cols-4">
      <div class="card">
      <h2>Min awarded/year</h2>
          <span class="big">${minAward['totAwarded'].toFixed()}M</span> (${minAward['year_awarded']})
      </div>
      <div class="card">
      <h2>Max awarded/year</h2>
      <span class="big">${maxAward['totAwarded'].toFixed()}M</span> (${maxAward['year_awarded']})
      </div>
  </div>
</div>

```sql id=[...totalAwarded]
SELECT SUM(approved_award_total)/1000000 as totAwarded, year_awarded
FROM data 
GROUP BY year_awarded 
```
```js
const [minA, maxA] = d3.extent(totalAwarded, d=>d.totAwarded)
```
```js
const maxAward = totalAwarded.filter(d => d.totAwarded === maxA)[0]
const minAward = totalAwarded.filter(d => d.totAwarded === minA)[0]
```


## Grant program name

Pick and choose the grant program name. See [here](https://www.neh.gov/grants/match-your-project) for a description of the grant programs:

```sql id=[...uniqGrants] 
SELECT grant_program_name as grant_program_name, COUNT(year_awarded) as awarded_count
FROM data
GROUP BY grant_program_name
HAVING COUNT(grant_program_name) > 5
ORDER BY grant_program_name
```

```js
const search_grants = view(Inputs.search(uniqGrants))
```

```js
const select_grant = view(Inputs.table(search_grants))
```

```js
const select_grants_safe = select_grant.length === 236 ? // eyeballed
  ['State Humanities Councils General Operating Support Grants', 'Summer Stipends', 'Basic Research', 
   'Humanities Projects in Media', 'Humanities Projects in Libraries and Archives', 
   'Digital Humanities Start-Up Grants'] : 
  select_grant.map(d=>d.grant_program_name)
```

<div>${resize((width) => 
Plot.plot({
      width,
      marginLeft: 100,
      y: { grid: true, type: "log" },
      color: { legend: true },
      marks: [
        Plot.ruleY([0]),
        Plot.lineY(
          money_overtime2.filter(d => select_grants_safe.includes(d["grant_program_name"])), 
          Plot.windowY(
          { k:5 },
          { x: "year_awarded", y: "tot", stroke: "grant_program_name" }
        )),
        Plot.dotY(
          money_overtime2.filter(d => select_grants_safe.includes(d["grant_program_name"])), 
          Plot.windowY(
            { k:1 },
            { x: "year_awarded", y: "tot", stroke: "grant_program_name", tip: true }
          ))
      ]
    })
)}
</div>

```sql id=[...money_overtime2]
SELECT 
  year_awarded, grant_program_name, SUM(approved_award_total) as tot
FROM data
WHERE 
  year_awarded > 1959 AND year_awarded < 2024 
GROUP BY year_awarded, grant_program_name 
ORDER BY year_awarded
```

## By division

```sql id=money_overtime
SELECT 
  year_awarded, division_or_office, SUM(approved_award_total) as tot
FROM data
WHERE 
  year_awarded > 1959 AND year_awarded < 2024 
GROUP BY year_awarded, division_or_office 
ORDER BY year_awarded
```

<div>${resize((width) => 
Plot.plot({
      width,
      marginLeft: 100,
      y: {grid: true, type: "log"},
      color: {legend: true},
      marks: [
        Plot.ruleY([0]),
        Plot.lineY(money_overtime, {x: "year_awarded", y: "tot", stroke: "division_or_office"}),
        Plot.dotY(money_overtime, {x: "year_awarded", y: "tot", stroke: "division_or_office", tip: true})
      ]
    })
)}
</div>

I was surprised by the digital humanities. It turns out that now they mostly award money to organizational recipients (they are missing at the moment). I dunnow why. The money is probably for bigger project, more infrastructure projects which i find interesting. 

```js
Plot.plot({
      width,
      marginLeft: 100,
      y: {grid:true, label: "Total count awards"},
      marks: [
        Plot.ruleY([0]),
        Plot.rectY(money_overtime, Plot.groupX({y: "count"}, {x: "division_or_office", y: "tot", fill: "division_or_office", stroke: "black"})),
      ]
    })
```

## By field of science

```js
const search_fos = view(Inputs.search(uniqFOS))
```

```js
const sel_fos = view(Inputs.table(search_fos))
```

```js
const select_fos_safe = sel_fos.length === 156 ? 
  ['Archaeology', 'U.S. History', 'Art History and Criticism', 'American Studies',  'Anthropology', 
    'History of Religion', 'Gender Studies', 'Russian History'
  ] : 
  sel_fos.map(d=>d.FoS)
```

<div>${resize((width) => 
Plot.plot({
      width,
      marginLeft: 100,
      marginRight: 140,
      y: {grid: true, type: "log"},
      color: {legend: true},
      marks: [
        Plot.ruleY([0]),
        Plot.lineY(
          [...money_overtime_fos].filter(d => select_fos_safe.includes(d["FoS"])), 
          Plot.windowY(
            {k: 5},
            {x: "year_awarded", y: "tot", stroke: "FoS"}
          )),
        Plot.text(
          [...money_overtime_fos].filter(d => select_fos_safe.includes(d["FoS"])), 
          Plot.selectLast(
            Plot.windowY(
              { k: 5 },
              { x: "year_awarded", y: "tot", text: "FoS", z: "FoS", frameAnchor: "left", dx: 15 })
            )
        ),
        Plot.dotY(
          [...money_overtime_fos].filter(d => select_fos_safe.includes(d["FoS"])), 
          Plot.windowY(
            {k: 1},
            {x: "year_awarded", y: "tot", stroke: "FoS", tip: true}
          ))
      ]
    })
)}
</div>

```sql id=money_overtime_fos
SELECT 
  year_awarded, primary_humanities_discipline as FoS, SUM(approved_award_total) as tot
FROM data
WHERE 
  year_awarded > 1959 AND year_awarded < 2023
GROUP BY year_awarded, primary_humanities_discipline 
ORDER BY year_awarded
```

```sql id=[...uniqFOS] 
SELECT primary_humanities_discipline as FoS, COUNT(year_awarded) as awarded_count
FROM data
GROUP BY primary_humanities_discipline
HAVING COUNT(primary_humanities_discipline) > 5
ORDER BY primary_humanities_discipline
```


## raw data

```sql id=raw_Dat
SELECT * FROM data
```

```js
const found = view(Inputs.search(raw_Dat))
```

```js
Inputs.table(found)
```

<style>

.custom-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr); /* Defines a 4-column layout */
  gap: 10px; /* Spacing between cards */
}

/* Specific sizes for each card */
.card-a { grid-column: span 1; } /* Card A takes up 2 columns */
.card-b { grid-column: span 3; } /* Card B takes up 1 column */
.card-c { grid-column: span 2; } /* Card B takes up 1 column */

.hero {
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: var(--sans-serif);
  margin: 4rem 0 8rem;
  text-wrap: balance;
  text-align: center;
}

.hero h1 {
  margin: 2rem 0;
  max-width: none;
  font-size: 14vw;
  font-weight: 300;
  line-height: 1.2;
  background: linear-gradient(30deg, var(--theme-foreground-focus), currentColor);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

@media (min-width: 640px) {
  .hero h1 {
    font-size: 90px;
  }
}

</style>
