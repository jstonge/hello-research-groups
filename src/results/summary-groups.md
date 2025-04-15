---
sql:
    training: ../data/training_data.parquet
---

# Summary database

<div class="grid grid-cols-4">
  <div class="card">
    <h2>Unique authors</h2>
    <span class="big">${[...uniq_name].length}</span>
  </div>
</div>


---


## Collaboration patterns across domains/career stage

<div class="grid grid-cols-2">
    <div><br>
    For each college/career stage, what is the proportion/count of collaborations with researchers who are either younger, same age, or older? In the the default setting, we can see that, for example, people from the physical sciences collaborate more extensively early on (during Phd; see last table for department to 'college' mapping), but engineering people catch up during their postDoc years. Humanists work more by themselves.
    </div>
    <div class="warning">The data is unbalanced. Some college/career stage values might be still slightly misleading as there are only few individuals within each. This is the cost to pay to show proportion that are easy to compare. 
    </div>
</div>

```js
const f = view(Inputs.form({
    tog: Inputs.toggle({
        label: "normalize (by the sum proportional to the facet total)"
        }),
    facet: Inputs.select(['career_stage', 'college'], {
        label: "facet variable"
        }
    )
}))
```

<div>${resize((width) => 
Plot.plot({
    width,
    height: 400,
    marginBottom: f.facet === "college" ? 40 : 100,
    marginTop: 35,
    marginRight: 50,
    color: {
        legend: true,
        range: ["#FDE725FF", "#20A387FF", "#404788FF"], 
        domain: ["younger", "same_age", "older"]
    },
    y: {
        grid: true,
        percent: f.tog ? true : false,
        label: f.tog ? "collab %" : "# collabs"
        },
    x: { tickRotate: 45 },
    fx: {
        label: "Career stage (numbers represent cutpoints, e.g. <4, <7, <12, <17, and <30 years since first publication)",
        },
    marks: [
        Plot.barY(training1, Plot.groupX(
            { y: f.tog ? "proportion-facet" : "mean" }, 
            { x: f.facet === "college" ? "career_stage" : 'college',
              y: "val", fill: "age_bucket",  fx: f.facet,
              offset: f.tog ? "normalize" : null })),
        Plot.ruleY([0])
    ]
})
)}
</div>


<div class="grid grid-cols-2">
    <div class="card">
        <h3>Normalized: Comparing relative proportion of collaboration for two different facets showing different aspect of the data:</h3>
        <li>
        <em>college facet</em>: within college, how do collaboration with people of different author age strata changes over time? This facet focuses on comparing colleges for a given career stage. For instance, `computer scientists` collaborating extensively with younger folks. 
        </li>
        <li>
        <em>career stage facet</em>: within career stage, how do collaboration with people of different author age strata changes across colleges? This facet focuses on comparing career stage across colleges. For instance, `engineering` people seems to be collaborating with more senior researchers than other colleges.
        </li>
    </div>
    <div class="card">
        <h3>Raw count: Comparing how many total collaborators with bar heights.</h3> The meaning for facets is the same than when y-axis is normalized.
    </div>
</div>
<div class="card"  style="padding: 0;">
    ${Inputs.table(training1)}
</div>

```sql id=training1
WITH long_table AS (
    UNPIVOT training
    ON younger, same_age, older 
    INTO
        NAME age_bucket
        VALUE val
)
SELECT 
  age_bucket, val, college,
  CASE 
    WHEN author_age <= 4 THEN 4 
    WHEN author_age <= 7 THEN 7 
    WHEN author_age <= 12 THEN 12 
    WHEN author_age <= 17 THEN 17
    WHEN author_age <= 30 THEN 30
    ELSE 999
    END AS career_stage
  FROM long_table
  WHERE college in ('Humanities', 'Social Sciences', 'Physical Science', 'Computer Science', 'Biological Sciences', 'Psychological Science') AND career_stage != 999 AND age_bucket is not NULL
```

#### Raw table

```sql
SELECT * FROM training
```

---

## Professors' collaboration rate with younger academics (>7 years younger)

Each tick is a faculty's rate of collaboration with collaborators seven years younger than them (cut point is the average time in our data to get from first publication to tenure-track position). 

```js
const sel_fos = view(Inputs.select(
    Array.from(new Set([...uniq_name].map(d=>d.college))
    ), { multiple: 4 }))
```

```js
const sel_fos_safe = sel_fos.length === 0 ? ['Physical Science', 'Social Sciences', 'Computer Science', 'Humanities'
] : sel_fos
```

<div>${resize((width) => 
Plot.plot({
  width,
  height: 400,
  marginBottom: 50,
  marginTop: 30,
  y: { grid: true }, 
  x: {label: "Time Since First Pub (author age)"},
  color: {legend: true},
  marks: [
    Plot.frame(),
    Plot.ruleX([8], { dx: -18,  strokeDasharray: 3 }),
    Plot.tickY(
        training_all.filter(d=>sel_fos_safe.includes(d['college'])),
        { x: "author_age", y: "changing_rate", z: "name", 
          stroke: "college", strokeOpacity: 0.5, tip: true, 
          title: d => `${d.name}\nrate collab: ${d.changing_rate.toFixed(2)}`,
          fx: "has_research_group", sort: {x: "x"} }
    ),
    Plot.lineY(
      training_all.filter(d=>sel_fos_safe.includes(d['college'])),
        Plot.groupX(
            { y: "median" },
            { x: "author_age", y: "changing_rate", stroke: "college", fx: "has_research_group", 
            strokeWidth: 4, sort: {x: "-y"} },
          )
    ),
    Plot.axisY({anchor: "left"})
  ]
})
)}
</div>

```sql id=[...training_all] 
  SELECT DISTINCT name, changing_rate, college, author_age, has_research_group::CHAR as has_research_group
  FROM training 
  WHERE 
    changing_rate < 40 AND 
    author_age < 29 AND 
    college in ('Humanities', 'Social Sciences', 'Physical Science', 'Computer Science', 'Biological Sciences', 'Mathematical Sciences', 'Psychological Science') AND
    has_research_group is not NULL AND has_research_group != -1.0
  ORDER BY author_age
```


---

## Collaboration ''norms''

We are interested in the relationship between group size, collaboration norms, and the emergence of computational works. More precisely, we want to know whether strong collaboration patterns could help humanities transitioning into the computational realm. 

At the moment, we simply calculate `density` of interactions among faculties' younger collaboraters as proxy for collaboration norms. The idea is that a group with strong collaboration norms is characterized by early career researchers working togeher early on.

One issue with density is that it doesn't take into account the recurrent relationships, aka whether younger folks keep collaborating on each others' papers.

```js
Plot.plot({
  width: 800,
  height: 500,
  marginLeft: 35,
  marginBottom: 50,
  color: { legend: true, scheme: "viridis" },
  x: { label: "changing rate" },
  y: { label: "density" },
  marks: [
    Plot.cell(
        training_all_agg.filter(
            d => d.density < 1.00 & d.density > 0.
        ), 
    Plot.bin(
        { fill: "proportion" }, 
        { x: d => parseInt(d["changing_rate"].toFixed(1)), 
          y: d => parseFloat(d["density"].toFixed(1)), 
          fx: "has_research_group" }
    )),
    Plot.frame()
  ]
})
```

```sql id=[...training_all_agg] 
SELECT name, changing_rate, MEAN(density) as density, has_research_group
FROM training 
WHERE changing_rate < 40 AND author_age < 30 AND has_research_group is not NULL AND has_research_group != -1
GROUP BY name, changing_rate, has_research_group
```



```sql id=uniq_name 
SELECT name, has_research_group, college
FROM training 
WHERE has_research_group is not NULL and college not in ('Agriculture', 'Health', 'Medical Sciences', 'Education', 'Language')  AND has_research_group != -1
GROUP BY name, has_research_group, college
ORDER BY name
```




