---
theme: air
title: Scientific collab timeline
toc: false
sql:
  coauthor: ./data/coauthor.parquet
  paper: ./data/paper.parquet
  author: ./data/author.parquet
  training: ./data/training_data.parquet
---

# Scientific collab timeline dashboard
## How do collabs and individual productivity coevolve over time?


```js
const formInput = Inputs.form({
  targets: Inputs.select([...uniqAuthors].map(d=>d.name), { multiple: 5, label: "Author" }),
  a_nc: Inputs.select(["age_diff", "acquaintance", "shared_institutions"], 
    {label: "Select color", value: "age_diff"}),
  a_r: Inputs.select(["yearly_collabo", "all_times_collabo"], {label: "Author node size", value: 'all_times_collabo'}),
  p_r: Inputs.select(["", "cited_by_count", "nb_coauthors"], {label: "Paper node size", value: "cited_by_count"}),
  yaxis: Inputs.select(["pub_date", "age_std"], {label: "Y-axis", value: "year"}),
  yaxis_ts: Inputs.select(["total_coauth", "younger_shared_inst", "younger", "new_collab", "density"], {label: "Timeseries Y-axis", value: "total_coauth"})
});
const form = Generators.input(formInput)
```

<div class="grid grid-cols-2">
  <div>In the lineplot on the right, we show the changing rates for a selected author. Right now, we force the model to find a switchpoint in between an early and late rate. We still need to do model selection to determine if the switchpoint is necessary or not. <br><br> ${formInput}</div>
  <div >${resize((width) => 
  Plot.plot({
    title: "switch point for selected authors",
    width,
    height: 320,
    y: {grid: true, label: "Collabo younger author"}, 
    color: {legend: true, range: ["red", "black", "lightgrey"], domain: ["younger", "same_age", "older"]},
    marks: [
      Plot.frame(),
      Plot.lineY(trainingEgo, { x: "author_age", y: "changing_rate", 
                strokeWidth: 1, strokeDasharray: 3, stroke: "red",
              },     
      ),
      Plot.dotY(
        trainingEgo, { x: "author_age", y: "younger", stroke: "red"},     
      ),
      Plot.dotY(
        trainingEgo, { x: "author_age", y: "same_age", stroke: "black"},     
      ),
      Plot.dotY(
        trainingEgo, { x: "author_age", y: "older", stroke: "lightgrey"},     
      )
    ]
  })
  )}
  </div>
</div>


<div class="card grid grid-cols-2">
<div>${resize((width) => 
Plot.plot({
        style: "overflow: visible;",
        width,
        height: 800,
        marginLeft: 35,
        fx: { label: null, padding: 0.03, axis: "top" },
        y: { grid: true, reverse: true, inset: 50 }, 
        r: { range: [1, 10] },
        marks: [
          Plot.dot(coauthor, Plot.dodgeX("middle", {
            fx: "name",
            y: d => d[form.yaxis], 
            fill: d => form.a_nc === 'age_diff' ? age_bucket(d) : d[form.a_nc],
            r: d => d[form.a_r], 
            stroke: 'black', 
            strokeWidth: 0.3, 
            fillOpacity: 0.7, 
            title: d => `${d.coauth_name}`,
            tip: true
          }))
        ]
        }))
}
</div>
<div>${resize((width) => 
  Plot.plot({
        style: "overflow: visible;",
        width,
        height: 800,
        marginLeft: 35,
        y: { grid: true, reverse: true, inset: 50 }, 
        r: { range: [1, 10] },
        fx: { label: null, padding: 0.03, axis: "top" },
        marks: [
          Plot.dot(paper, Plot.dodgeX("middle", {
            fx: "ego_aid",
            y: d => d[form.yaxis], 
            fill: 'grey',
            r: d => p_r(d), 
            stroke: 'black', 
            strokeWidth: 0.3, 
            fillOpacity: 0.7, 
            title: d => `Title: ${d.title}\n#coauthors: ${d.authors.split(", ").length}`,
            tip: true
          }))
        ]
}))
}
</div>
</div>

```js
const selected_authors = form.targets.length > 1 ? form.targets[0] : 'Aaron Clauset'
```

```js
form.targets
```

## Coauthor table

```sql id=coauthor
SELECT age_std::DATE as age_std, pub_date::DATE as pub_date, * FROM coauthor 
WHERE name = ${selected_authors}
```

```js
Inputs.table(coauthor)
```

## Paper table

```sql id=paper
SELECT *, a.age_std::DATE as age_std
FROM paper p
LEFT JOIN author a
ON p.ego_aid = a.aid AND p.pub_year = a.pub_year
WHERE name = ${selected_authors}
```

```js
Inputs.table(paper)
```

## training table

```sql id=trainingEgo
  SELECT DISTINCT name, changing_rate, college, author_age, younger, same_age, older, has_research_group::CHAR as has_research_group
  FROM training 
  WHERE name = ${selected_authors}
  ORDER BY author_age
```

```sql
SELECT * FROM training
```


```sql id=uniqAuthors
SELECT DISTINCT name FROM coauthor ORDER BY name
```


```js
function p_r(d) {
        switch (form.p_r) {
        case 'nb_coauthor':
          return d.author === null ? 0 : d.author.split(", ").length;
        case '':
          return 0.1;
        case 'cited_by_count':
          return d['cited_by_count'];
        case 'nb_coauthors':
          return d.authors.split(", ").length;
      }
    }
```

```js
function age_bucket(d) {
          switch (true) {
              case d.age_diff > 7 : 
                return "#404788FF"
              case d.age_diff <= 7 && d.age_diff >= -7:
                return "#20A387FF"
              case d.age_diff < -7:
                return "#FDE725FF"
            };
  }
```
