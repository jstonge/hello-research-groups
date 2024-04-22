---
theme: air
title: Scientific collab timeline
toc: false
sql:
  coauthor: ./data/coauthor.csv 
  author: ./data/author.csv 
  paper: ./data/paper.csv 
---

# Scientific collab timeline dashboard
## How do collabs and individual productivity coevolve over time?

<div class="grid grid-cols-2">
  <div>
    <ul>
      <li> <ins>ego</ins> is the selected author in parameters</li>
      <li> On the left, each node is a unique collaborator. On the right, each node is an article.</li>
      <li> <ins>new collab of collab</ins> are triadic closures, aka new authors that were selected from one of ego's collaborator of collaborator.</li>
      <li> Institutions is the result of coloring people with the same institutions than the guessed home institution of ego. We guess ego's institution based a simple majority rule institutions in any given year.</li>
      <li> The data was gathered using the new API provided by <a href="https://openalex.org/">OpenAlex new API</a>
    </ul>
  </div>
  <div class="card"">
    <h2>Choose parameters</h2>
    <br>
    ${formInput}
  </div>
</div>

```js
const formInput = Inputs.form({
  targets: Inputs.select([...uniqAuthors].map(d => d.target), {label: "Author", value: "Laurent Hébert-Dufresne"}),
  a_nc: Inputs.select(
    ["acquaintance", "shared_institutions", "institutions"], 
    {label: "Select color", value: 'shared_institutions', disabled:true}
    ),
  a_r: Inputs.select(["yearly_collabo", "all_times_collabo"], {label: "Author node size", value: 'all_times_collabo', disabled: true}),
  p_r: Inputs.select(["", "cited_by_count", "nb_coauthor"], {label: "Paper node size", value: "tot_citation", disabled: true}),
  yaxis: Inputs.select(["year", "author_age"], {label: "Y-axis", value: "year", disabled: true})
});

const form = Generators.input(formInput);
```

```js
Plot.legend({color: {
  fillOpacity: 0.7,
  range: ["orange", "lightblue", "darkred"], 
  domain: ["younger (<-7)", "same_age (>=-7)","older (>7)",]}
  })
```

```js
Plot.plot({
  style: "overflow: visible;",
  height: 1000,
  width: 1200,
  marginLeft: 220,
  color: { legend: true },
  y: { grid: true, reverse: true, inset: 50, label: null  },
  fx: { padding: 0.03, axis: "top" },
  marks: [
    Plot.dot(coauthor, Plot.dodgeX("middle", {
      y: "pub_date", 
      fill: d => d["age_diff"] > -7 ? 
                    d["age_diff"] > 7 ? "darkred" : 
                      "lightblue" :
                        "orange", 
      stroke: 'black', 
      strokeWidth: 0.3, 
      fillOpacity: 0.7, 
      fx: "type", 
      r:8,
      title: d => `${d["coauthor_name"]}`,
      tip: true
    })),
    Plot.text(
        coauthor, 
          Plot.dodgeX("middle", {
            y: "pub_date", 
            fx: "type",
            title: "coauthor_age",
            text: "coauthor_age",
            r: 8
        })),
  ]
})
```

## Raw table

```js
Inputs.table(coauthor)
```


```sql id=uniqAuthors
SELECT DISTINCT(target) FROM coauthor
```

```sql id=coauthor
WITH Combined AS (
    SELECT coauthor.type, coauthor.target, coauthor.aid, coauthor.pub_date, coauthor.pub_year, coauthor.title as coauthor_name, author.author_age as coauthor_age, 
    FROM coauthor
    LEFT JOIN author
    ON coauthor.aid = author.aid AND coauthor.pub_year = author.pub_year
    WHERE author.author_age < 25
)

SELECT DISTINCT p.author_age_i as target_age, c.aid, c.type, c.target, c.pub_date, 
                c.pub_year, c.coauthor_name, c.coauthor_age,
                (c.coauthor_age - p.author_age_i) AS age_diff
FROM paper p
JOIN Combined c
ON p.target = c.target AND p.pub_year = c.pub_year
WHERE p.target = ${form.targets};
```

<!-- ```js
const selected_targets = form.targets.length > 0 ? form.targets : ['Laurent Hébert‐Dufresne'] 
```

```js
trajectory([...paper_dat_multi], {form:form, width:form_hw.w, height:form_hw.h})
```

```js
const form_hw = view(Inputs.form({
  h: Inputs.range([800, 2000], {label: "Custom Height", step: 10, value: 1000}),
  w: Inputs.range([800, 2500], {label: "Custom Width", step: 10, value: 1200})
}))
```

```sql id=paper_dat_multi
SELECT * FROM timeline WHERE target = ${selected_targets[0]}
```

```sql id=uniqAuthors display
SELECT DISTINCT(target) FROM timeline ORDER BY target
```

```js
import {trajectory} from "./components/trajectory.js";
``` -->