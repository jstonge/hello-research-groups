---
theme: dashboard
title: Scientific collab timeline
toc: false
---

# Scientific collab timeline dashboard
## How do collabs and individual productivity coevolve over time?

```js
const form = view(Inputs.form({
  targets: Inputs.select([...uniqAuthors].map(d=>d.name), { multiple: 5, label: "Author" }),
  a_nc: Inputs.select(["age_diff", "acquaintance", "shared_institutions"], 
    {label: "Select color", value: "age_diff"}),
  a_r: Inputs.select(["yearly_collabo", "all_times_collabo"], {label: "Author node size", value: 'all_times_collabo'}),
  p_r: Inputs.select(["", "cited_by_count", "nb_coauthors"], {label: "Paper node size", value: "cited_by_count"}),
  yaxis: Inputs.select(["pub_date", "age_std"], {label: "Y-axis", value: "year"}),
  yaxis_ts: Inputs.select(["total_coauth", "younger_shared_inst", "younger", "new_collab", "density"], {label: "Timeseries Y-axis", value: "total_coauth"})
}));
```

```js
Plot.plot({
    width:1000,
    style: "overflow: visible;",
    marginLeft: 35,
    marginRight: 30,
    nice: true,
    height: 400,
    y: { grid: true, label: form.yaxis_ts },
    x: { label: "author academic age" },
    color: {
      legend: true, type: "ordinal", 
      domain: ["1.0", "0.0"], 
      range: ["lightblue", "orange"], 
    },
    marks: [
      Plot.dotY(training, {  
        x: form.targets.length > 1 ? "author_age" : "pub_year", y: form.yaxis_ts, z: "name"   
      }),
      Plot.lineY(training, Plot.windowY({ k : 5 }, {
        x: form.targets.length > 1 ? "author_age" : "pub_year", 
        y: form.yaxis_ts, z: "name", stroke: "has_research_group" ,strokeOpacity: 0.8
      })),
      Plot.lineY(form.yaxis_ts === 'younger' ? training : "", {
        x: form.targets.length > 1 ? "author_age" : "pub_year", 
        y: "changing_rate", strokeOpacity: 0.7, z: "name",
        strokeDasharray: 3,
      })
    ],
    caption: "p.s. dash line is the estimate rates from a change point model with two assumed switchpoints",
  })
```


```js
Plot.plot({
  title: "Professors' collaboration rate with younger academics (>7 years younger)",
  width: 1200,
  height: 400,
  marginLeft: 35,
  marginRight: 120,
  fy: { marginRight: 120 },
  y: {grid: true}, 
  // color: {
  //     legend: true, type: "ordinal", 
  //     domain: ["has research group", "no research group"], 
  //     range: ["lightblue", "orange"], 
  // },
  marks: [
    Plot.frame(),
    Plot.ruleX([8], { dx: -18,  strokeDasharray: 3 }),
    Plot.tickY(training_all, {
      x: "author_age", y: "changing_rate", z: "name", stroke: "college", strokeOpacity: 0.5, fx: "has_research_group",
      sort: {x: "x"}
    }),
    //   Plot.tickY([...training_all].filter(d=>d.has_research_group=="1.0"), {
    //     x: "author_age", y: "changing_rate", z: "name", stroke: "lightblue", strokeOpacity: 0.3
    //   }),
    Plot.lineY(
      training_all,
          Plot.groupX(
            { y: "median" },
            { x: "author_age", y: "changing_rate", stroke: "college", fx: "has_research_group", 
              strokeWidth: 4, tip: true, sort: {x: "-y"} },
          )
    ),
    // Plot.tickY(
    //           [...training_all].filter(d=>d.has_research_group=="1.0"),
    //           Plot.groupX(
    //             {y: "median"},
    //             {x: "author_age", y: "changing_rate", stroke: "#6495ED", strokeWidth: 4, sort: {x: "-y"}}
    //           )
    // ),
    Plot.axisY({anchor: "left"})
  ]
})
```

```js
Plot.plot({
  title: "density ~ rate of young collabs",
  width: 800,
  height: 500,
  marginLeft: 35,
  marginBottom: 50,
  color: {legend: true, scheme: "viridis"},
  x: { label: "changing rate" },
  y: { label: "density" },
  marks: [
    Plot.cell([...training_all_agg].filter(d => d.density < 1.00 & d.density > 0.), Plot.bin({ fill: "proportion" }, {
      x: d => parseInt(d["changing_rate"].toFixed(1)), y: d => parseFloat(d["density"].toFixed(1)), fx: "has_research_group"
    })),
    Plot.frame()
  ]
})
```

```js
Plot.plot({
        style: "overflow: visible;",
        width: 1000,
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
        })
```

```js
Plot.plot({
        style: "overflow: visible;",
        width: 1000,
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
})
```

<!-- <div class="grid grid-cols-3">
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
</div> -->

<!-- <div class="grid grid-cols-2">
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
</div> -->

<!-- <div>${
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
</div> -->

```js
const db = DuckDBClient.of({ 
  coauthor: FileAttachment("./data/processed/coauthor.csv"),
  paper: FileAttachment("./data/processed/paper.csv"),
  author: FileAttachment("./data/processed/author.csv"),
  training: FileAttachment("./data/training/training_data.csv")
})
```

```js
db
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

```js
Inputs.table(coauthor)
```

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

```js
Inputs.table(paper)
```

## Training data

```js
const training = db.query(`
  SELECT has_research_group::CHAR as has_research_group, * FROM training 
  WHERE name in (${selected_authors.map(d => '\''+d+'\'').join()})
  ORDER BY pub_year
`)
```

```js
const training_all_agg = db.query(`
  SELECT name, changing_rate, MEAN(density) as density, has_research_group
  FROM training 
  WHERE changing_rate < 40 AND author_age < 30 AND has_research_group is not NULL
  GROUP BY name, changing_rate, has_research_group

`)
```

```js
const training_all = db.query(`
  SELECT DISTINCT name, changing_rate, college, author_age, has_research_group::CHAR as has_research_group
  FROM training 
  WHERE changing_rate < 40 AND author_age < 30 AND college not in ('Cognitive Sciences', 'Languages', 'Education', 'Health Sciences') AND has_research_group is not NULL
  ORDER BY author_age
`)
```

```js
Inputs.table(training_all)
```

```js
Plot.plot({
  marginBottom: 100,
  marginLeft: 200,
  y: {label: null},
  x: {grid: true},
  color: {legend: true, type: "ordinal", range: ["lightblue", "orange"]},
  marks: [
    Plot.barX(training_all, Plot.groupY({x: "count"}, {y: "college", fill: "has_research_group", sort: {y: "-x"}})),
    Plot.gridX(),
    Plot.ruleX([0])
  ]
})
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
