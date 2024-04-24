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
  ${ plot_legend() }
  <div class="grid grid-cols-2">
    <div class="card">${resize((width) => plot_data(coauthor, { width }))}</div>
    <div class="card">${resize((width) => plot_data(paper, { width }))}</div>
  </div>
</div>

```js
const formInput = Inputs.form({
  targets: Inputs.select([...uniqAuthors].map(d => d.target), { multiple: 5, label: "Author" }),
  a_nc: Inputs.select(
    ["age_diff", "acquaintance", "shared_institutions", "institutions"], 
    {label: "Select color", value: "age_diff"}
    ),
  a_r: Inputs.select(["yearly_collabo", "all_times_collabo"], {label: "Author node size", value: 'all_times_collabo'}),
  p_r: Inputs.select(["", "cited_by_count"], {label: "Paper node size", value: "cited_by_count"}),
  yaxis: Inputs.select(["year", "author_age"], {label: "Y-axis", value: "year", disabled: true})
});

const form = Generators.input(formInput);
```

```js
function plot_data(data, { width } = {}) {
  return Plot.plot({
    style: "overflow: visible;",
    height: 800,
    width,
    marginLeft: 120,
    y: { grid: true, reverse: true, inset: 50, label: null  },
    fx: { label: null, padding: 0.03, axis: "top" },
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
        title: d => d.type === 'paper' ? `cited_count: ${d.cited_by_count}` : `name: ${d.coauthor_name}`,
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

## Coauthor table

```sql id=uniqAuthors
SELECT DISTINCT(target) FROM coauthor
```

```sql id=coauthor display
SELECT c.type, c.pub_date, c.target, c.all_times_collabo, c.yearly_collabo, c.target_type,
       c.title as coauthor_name, a.author_age as coauthor_age, a2.author_age,
       (a2.author_age-a.author_age) AS age_diff
FROM coauthor c
LEFT JOIN author a
ON c.aid = a.aid AND c.pub_year = a.pub_year
LEFT JOIN author a2
ON c.target = a2.display_name AND c.pub_year = a2.pub_year
WHERE c.target = ${form.targets[0] === undefined ? 'Josh Bongard' : form.targets[0]} 
```

```sql id=paper
SELECT p.type, p.target, p.aid, p.pub_date, p.pub_year, p.title, 
       p.target_type, a.author_age, NULL AS age_diff, a.first_pub_year,
       p.cited_by_count
FROM paper p
LEFT JOIN author a
ON p.aid = a.aid AND p.pub_year = a.pub_year
WHERE target = ${form.targets[0] === undefined ? 'Josh Bongard' : form.targets[0]}
```

<!-- HELPERS -->

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

function a_nc(d) {
        switch (form.a_nc) {
        case 'age_diff':
          switch (true) {
              case d.age_diff < -15 :
                return "#404788FF"
              case d.age_diff >= -15 && d.age_diff < -7:
                return "#B8DE29FF"
              case d.age_diff >= -7 && d.age_diff <= 7:
                return "#20A387FF"
              case d.age_diff > 7 && d.age_diff <= 15 :
                  return "#2D708EFF" 
              case d.age_diff > 15:
                return "#FDE725FF"
            };
      }
    }
```
