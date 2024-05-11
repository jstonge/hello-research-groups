---
theme: dashboard
toc: false
title: Visualize nsf humanities
sql:
  data: ./data/nsf_humanities.parquet
---

<div class="hero">
  <h1>Exploring National Endowment of humanities</h1>
  <h2>A small exploration of the data available from <a href="https://www.neh.gov/grants/listing">https://www.neh.gov/grants/listing</a>.</h2>
</div>

<div class="warning">At the moment, the following are grants awared is just for individual recipients. I still need to add organizational recipients.</div>

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
const select_grant = view(Inputs.table(uniqGrants))
```


```sql id=[...money_overtime2]
SELECT 
  year_awarded, grant_program_name, SUM(approved_award_total) as tot
FROM data
WHERE 
  year_awarded > 1959 AND year_awarded < 2024 
GROUP BY year_awarded, grant_program_name 
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
        Plot.lineY(money_overtime2.filter(d => select_grant.map(d=>d.grant_program_name).includes(d["grant_program_name"])), Plot.windowY(
          {k:5},
          {x: "year_awarded", y: "tot", stroke: "grant_program_name"})),
        Plot.dotY(money_overtime2.filter(d => select_grant.map(d=>d.grant_program_name).includes(d["grant_program_name"])), Plot.windowY(
          {k:1},
          {x: "year_awarded", y: "tot", stroke: "grant_program_name", tip: true}))
      ]
    })
)}
</div>


## By division

See [here](https://www.neh.gov/divisions-offices) for a description of the division. I still need to write some tests to make sure the data is all here. I find suspicious that the division of "Public Programs" has so many missing years:

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


```sql id=[...uniqFOS] 
SELECT primary_humanities_discipline as FoS, COUNT(year_awarded) as awarded_count
FROM data
GROUP BY primary_humanities_discipline
HAVING COUNT(primary_humanities_discipline) > 5
ORDER BY primary_humanities_discipline
```
<!-- 
```sql id=uniqFOS
SELECT DISTINCT primary_humanities_discipline as FoS
FROM data
GROUP BY year_awarded, primary_humanities_discipline 
HAVING COUNT(approved_award_total > 5)
ORDER BY primary_humanities_discipline
``` -->

```js
const select = view(Inputs.table(uniqFOS))
```

```sql id=money_overtime_fos
SELECT 
  year_awarded, primary_humanities_discipline as FoS, SUM(approved_award_total) as tot
FROM data
WHERE 
  year_awarded > 1959 AND year_awarded < 2023
GROUP BY year_awarded, primary_humanities_discipline 
ORDER BY year_awarded
```

```js
const data_f = [...money_overtime_fos].filter(d => sel_fos.includes(d["FoS"]))
```

```js
const sel_fos = select.length == 143 ? ['American Literature'] : select.map(d=>d["FoS"])
```


<div>${resize((width) => 
Plot.plot({
      width,
      marginLeft: 100,
      y: {grid: true, type: "log"},
      color: {legend: true},
      marks: [
        Plot.ruleY([0]),
        Plot.lineY(data_f, Plot.windowY(
          {k: 5},
          {x: "year_awarded", y: "tot", stroke: "FoS", tip: true}
          )),
        Plot.dotY(data_f, Plot.windowY(
          {k: 1},
          {x: "year_awarded", y: "tot", stroke: "FoS"}
          ))
      ]
    })
)}
</div>





```js
Inputs.table(data_f)
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
