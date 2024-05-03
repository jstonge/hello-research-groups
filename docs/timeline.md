---
theme: dashboard
title: Scientific collab timeline
toc: false
---

# Scientific collab timeline dashboard
## How do collabs and individual productivity coevolve over time?

```js
const formInput = Inputs.form({
  targets: Inputs.select([...uniqAuthors].map(d=>d.name), { multiple: 5, label: "Author" }),
  a_nc: Inputs.select(["age_diff", "acquaintance", "shared_institution"], 
    {label: "Select color", value: "age_diff"}),
  a_r: Inputs.select(["yearly_collabo", "all_times_collabo"], {label: "Author node size", value: 'all_times_collabo'}),
  p_r: Inputs.select(["", "cited_by_count"], {label: "Paper node size", value: "cited_by_count"}),
  yaxis: Inputs.select(["pub_date", "age_std"], {label: "Y-axis", value: "year"}),
  yaxis_ts: Inputs.select(["total_coauth", "younger_shared_inst", "younger", "new_collab"], {label: "Timeseries Y-axis", value: "total_coauth"})
});

const form = Generators.input(formInput)
```

<div class="grid grid-cols-3">
<div class="grid-colspan-1"><br><br><br>${formInput}</div>
<div class="card grid-colspan-2">
 ${Plot.plot({
    width:1000,
    marginLeft: 30,
    marginRight: 0,
    height: 400,
    y: { grid: true },
    x: { label: "author academic age" },
    color: {
      legend: true, type: "ordinal", 
      domain: ["Has research group", "No group"], 
      range: ["lightblue", "orange"], 
    },
    marks: [
      Plot.dot(training, {
        x: "author_age", y: form.yaxis_ts, z: "name" 
      }),
      Plot.line(training, Plot.windowY({k: 3}, {
        x: "author_age", y: form.yaxis_ts, z: "name", stroke: d => d["has_research_group"] === "1.0" ? "Has research group" : "No group", strokeOpacity: 0.6
      }))
    ]
  })}
</div>
</div>

<div class="grid grid-cols-2">
<div>${
Plot.plot({
        style: "overflow: visible;",
        height:800,
        marginLeft: 30,
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
        })
}
</div>

<div>${
Plot.plot({
        style: "overflow: visible;",
        height: 800,
        marginLeft: 120,
        y: { grid: true, reverse: true, inset: 50 }, 
        r: { range: [4, 10] },
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
            title: d => `Title: ${d.title}\nDate:${d.pub_date}`,
            tip: true
          }))
        ]
        })
}
</div>
</div>

```js
const db = DuckDBClient.of({ 
  coauthor: FileAttachment("../data/processed/coauthor_augmented.parquet"),
  paper: FileAttachment("../data/processed/paper_tidy.parquet"),
  author: FileAttachment("../data/processed/data/author_tidy.parquet"),
  training: FileAttachment("../data/training/training_data.csv")
})
```

```js
const uniqAuthors = db.query(`SELECT DISTINCT(name) FROM coauthor ORDER BY name`)
```

```js
const selected_authors = form.targets.length > 0 ? form.targets : ['Aaron Clauset']
```


## Coauthor table


```js
const coauthor = db.query(`
  SELECT age_std::DATE as age_std, pub_date::DATE as pub_date, * FROM coauthor 
  WHERE name in (${selected_authors.map(d => '\''+d+'\'').join()})
`)
```

<div class="card" style="padding: 0;">${Inputs.table(coauthor)}</div>

## Paper table

```js
const paper = db.query(`
  SELECT *, a.age_std::DATE as age_std
  FROM paper p
  LEFT JOIN author a
  ON p.ego_aid = a.aid AND p.pub_year = a.pub_year
  WHERE name in (${selected_authors.map(d => '\''+d+'\'').join()})
`)
```

<div class="card" style="padding: 0;">${Inputs.table(paper)}</div>


## Training data

```js
const training = db.query(`
  SELECT has_research_group::CHAR as has_research_group, * FROM training 
  WHERE name in (${selected_authors.map(d => '\''+d+'\'').join()})
  ORDER BY pub_year
`)
```

```js
const no_groups = db.query(`
  SELECT * FROM training 
  WHERE has_research_group = 0
  ORDER BY pub_year
`)
```
<div class="card" style="padding: 0;">${Inputs.table(no_groups)}</div>

```js
function p_r(d) {
        switch (form.p_r) {
        case 'nb_coauthor':
          return d.author === null ? 0 : d.author.split(", ").length;
        case '':
          return 0.1;
        case 'cited_by_count':
          return d['cited_by_count'];
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