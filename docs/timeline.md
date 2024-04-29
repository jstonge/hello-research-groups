---
theme: dashboard
title: Scientific collab timeline
toc: false
sql:
  coauthor: ./data/coauthor.csv 
  author: ./data/author.csv 
  paper: ./data/paper.csv 
---

# Scientific collab timeline dashboard
## How do collabs and individual productivity coevolve over time?

<div class="grid grid-cols-4">
  <div class="card">
    <h2>Unique authors</h2>
    <span class="big">${[...uniqAuthors].length}</span>
  </div>
  <div class="card">
    <h2>Total #coauthors from ${selected_author}</h2>
    <span class="big">${[...coauthor].length}</span>
  </div>
  <div class="card">
    <h2>Total #papers from ${selected_author}</h2>
    <span class="big">${[...paper].length}</span>
  </div>
</div>

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

<div>
  <div class="grid grid-cols-2">
    <div class="card">${resize((width) => plot_data(coauthor, { width }))}</div>
    <div class="card">${resize((width) => plot_data(paper, { width }))}</div>
  </div>
</div>

```js
const formInput = Inputs.form({
  targets: Inputs.select([...uniqAuthors].map(d => d.target), { multiple: 5, label: "Author" }),
  a_nc: Inputs.select(
    ["age_diff", "acquaintance", "shared_institutions"], 
    {label: "Select color", value: "age_diff"}
    ),
  a_r: Inputs.select(["yearly_collabo", "all_times_collabo"], {label: "Author node size", value: 'all_times_collabo'}),
  p_r: Inputs.select(["", "cited_by_count"], {label: "Paper node size", value: "cited_by_count"}),
  yaxis: Inputs.select(["year", "author_age"], {label: "Y-axis", value: "year", disabled: true})
});

const form = Generators.input(formInput);
```

```js
const selected_author = form.targets[0] === undefined ? 'Laurent Hébert‐Dufresne' : form.targets[0]
```

```sql id=uniqAuthors
SELECT DISTINCT(target) FROM coauthor ORDER BY target
```

## Coauthor table

```sql id=coauthor display
SELECT c.pub_date, c.target as ego, a2.aid, c.shared_institutions, a2.author_age as ego_age, a2.first_pub_year as ego_min_year, 
       c.title as coauthor_name, 
       a.pub_year,
       a.first_pub_year as coauthor_min_year,
       c.all_times_collabo, c.yearly_collabo, 
       c.acquaintance,
       a.author_age as coauthor_age,
       (a2.author_age-a.author_age) AS age_diff,
       c.type, c.target_type
FROM coauthor c
LEFT JOIN 
  author a ON c.aid = a.aid AND c.pub_year = a.pub_year
LEFT JOIN 
  author a2 ON c.target = a2.display_name AND c.pub_year = a2.pub_year
WHERE 
  c.target = ${selected_author}  AND a.pub_year < 2024
ORDER BY a.pub_year
```
## Paper table

```sql id=paper display
SELECT p.pub_date, p.pub_year, p.target, p.aid, p.title, 
       p.cited_by_count, p.target_type, p.type
FROM paper p
LEFT JOIN author a
ON p.aid = a.aid AND p.pub_year = a.pub_year
WHERE target = ${selected_author} AND a.pub_year < 2024
```

<!-- HELPERS -->

```js
function plot_data(data, { width } = {}) {
  return Plot.plot({
    style: "overflow: visible;",
    height: 800,
    width,
    marginLeft: 120,
    y: { grid: true, reverse: true, inset: 50, label: null  },
    fx: { label: null, padding: 0.03, axis: "top" },
    color: { legend: true }, 
    r: { range: [1, 10] },
    marks: [
      Plot.dot(data, Plot.dodgeX("middle", {
        y: "pub_date", 
        fx: "target_type",
        fill: d =>  d.type === 'paper' ?  "grey" : a_nc(d),
        r: d => d.type === 'paper' ?  p_r(d) : d[form.a_r],
        stroke: 'black', 
        strokeWidth: 0.3, 
        fillOpacity: 0.7, 
        title: d => d.type === 'paper' ? `title: ${d.title}\ncited_count: ${d.cited_by_count}` : `name: ${d.coauthor_name}`,
        tip: true
      })),
      Plot.text(
          data, 
            Plot.dodgeX("middle", {
              fx: "target_type",
              y: "pub_date", 
              r: d => d.type === 'paper' ?  p_r(d) : null,
              title: "coauthor_age",
              text: "coauthor_age",
          })),
    ]
  })
}
```

```js
function plot_legend() {
  return Plot.legend({color: {
  fillOpacity: 0.7,
  // range: ["orange", "lightblue", "darkred"], 
  range: ["#FDE725FF", "#B8DE29FF", "#20A387FF", "#2D708EFF", "#404788FF"], 
  domain: ["much younger (∞,-15)", "younger [-15, -7)", "same_age [-7, 7]", "older (7, 15]", "much older (15, ∞)"]
  },
  })
}
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
      }
    }
```

```js
function age_bucket(d) {
          switch (true) {
              case d.age_diff < -7 : 
                return "much older (15, ∞)"
              // case d.age_diff >= -15 && d.age_diff < -7:
              //   return  "older (7, 15]"
              case d.age_diff >= -7 && d.age_diff <= 7:
                return "same_age [-7, 7]"
              // case d.age_diff > 7 && d.age_diff <= 15 :
              //     return "younger [-15, -7)" 
              case d.age_diff > 7:
                return "much younger (∞,-15)"
            };
  }
```

```js
function a_nc(d) {
        switch (form.a_nc) {
        case 'age_diff':
          return age_bucket(d);
        case 'shared_institutions': {
          return d.shared_institutions
        }
        case 'acquaintance': {
          return d.acquaintance
        }
      }
}
```