---
sql:
  coauthor: ../data/coauthor.parquet
  paper: ../data/paper.parquet
  author: ../data/author.parquet
  training: ../data/training_data.parquet
---

# Summary database

Here is the summary of our 4 tables, and the information we wrangle from them:

<div class="grid grid-cols-4">
    <div class="card">
    <h2>Uniq Name in Paper table</h2>
        <span class="big">${uniq_name_paper.length}</span>
    </div>
    <div class="card">
    <h2>Coauthor table</h2>
        <span class="big">${uniq_name_coauthor.length}</span>
    </div>
    <div class="card">
    <h2>Author table</h2>
        <span class="big">${uniq_name_author.length}</span>
    </div>
    <div class="card">
    <h2>Training table</h2>
        People: <span class="big">${uniq_name_training.length}</span>
    </div>
</div>


<div class="grid grid-cols-4">
    <div class="card" style="padding: 0;">
    ${Inputs.table(uniq_name_paper)}
    </div>
    <div class="card" style="padding: 0;">
    ${Inputs.table(uniq_name_coauthor)}
    </div>
    <div class="card" style="padding: 0;">
    ${Inputs.table(uniq_name_author)}
    </div>
    <div class="card" style="padding: 0;">
    ${Inputs.table(uniq_name_training)}
    </div>
</div>

<div class="grid grid-cols-4">
    <div>
    </div>
    <div>
    </div>
    <div>
    </div>
    <div class="card" style="padding: 0;">
    ${Inputs.table(d3.flatRollup(uniq_college_training, v => v.length, d => d.college), {header: {0: 'College', 1: '# people'}})}
    </div>
</div>

<div class="grid grid-cols-4">
    <div>
    </div>
    <div>
    </div>
    <div>
    </div>
    <div class="card" style="padding: 0;">
    ${Inputs.table(d3.flatRollup(uniq_dept_training, v => v.length, d => d.department), {header: {0: 'Department', 1: '# people'}})}
    </div>
</div>

```sql id=[...uniq_name_paper]
SELECT COUNT(name) as n_papers, name FROM paper GROUP BY  name 
```
```sql id=[...uniq_name_coauthor]
SELECT COUNT(name) as n_coauthors, name FROM coauthor GROUP BY name 
```
```sql id=[...uniq_name_author]
SELECT COUNT(display_name) as author_age, display_name FROM author GROUP BY display_name
```
```sql id=[...uniq_name_training]
SELECT COUNT(name) as n, name FROM training GROUP BY name
```
```sql id=[...uniq_college_training]
SELECT COUNT(college) as n_authors, college FROM training GROUP BY college, name ORDER BY college
```
```sql id=[...uniq_dept_training]
SELECT COUNT(department) as n_authors, department FROM training GROUP BY department, name ORDER BY department
```

---

## Department to Category mapping

Validity assessment of our department to college mapping:

```sql
SELECT DISTINCT name, department, college FROM training
```

---


## Balancing annotations

To study group size across field of sciences, we would as many faculties with and without resarch groups in each domain. At the moment, we oversampled faculties with research groups because we were interested in characterizing group size.


<div>${resize((width) => balancing_annots(uniq_name, { width, title: "Overall College/Category/Field of science", facet_var: "college"}) )}
</div>

<div>${resize((width) => balancing_annots(uniq_dept_hum, { width, title: "The Humanities, by department", facet_var: "department"}) )}
</div>

<div>${resize((width) => balancing_annots(uniq_dept_soc, { width, title: "The Social sciences, by department", facet_var: "department"}) )}
</div>

<div>${resize((width) => balancing_annots(uniq_dept_bio, { width, title: "The Biological sciences, by department", facet_var: "department"}) )}
</div>

<div>${resize((width) => balancing_annots(uniq_dept_phys, { width, title: "The Physical sciences, by department", facet_var: "department"}) )}
</div>

```sql id=uniq_dept_hum
SELECT name, has_research_group, department
FROM training 
WHERE has_research_group is not NULL and college in ('Humanities')  AND has_research_group != -1
GROUP BY name, has_research_group, department
ORDER BY name
```

```sql id=uniq_dept_bio
SELECT name, has_research_group, department
FROM training 
WHERE has_research_group is not NULL and college in ('Biological Sciences')  AND has_research_group != -1
GROUP BY name, has_research_group, department
ORDER BY name
```

```sql id=uniq_dept_phys
SELECT name, has_research_group, department
FROM training 
WHERE has_research_group is not NULL and college in ('Physical Science')  AND has_research_group != -1
GROUP BY name, has_research_group, department
ORDER BY name
```

```sql id=uniq_dept_soc
SELECT name, has_research_group, department
FROM training 
WHERE has_research_group is not NULL and college in ('Social Sciences')  AND has_research_group != -1
GROUP BY name, has_research_group, department
ORDER BY name
```

```js
function balancing_annots(data, {width, facet_var, title} = {}) {
    return Plot.plot({
        title,
        width,
        height: 300,
        marginTop: 60,
        marginRight: 120,
        fx: { tickRotate: -10, label: null },
        color: {legend: true, type: "ordinal", range: ["lightblue", "orange"]},
        marks: [
            Plot.barY(data, Plot.groupX({ y: "count" }, {
            x: "has_research_group", fill: "has_research_group", fx: facet_var, sort: {x: "-y"}
            })),
            Plot.gridY(),
            Plot.ruleY([0])
        ]
        })
} 
```

---

# Data quality check 

### Author age

Checking author age. most often if above 50 years old it is a glitch in min paper year that needs to be fixed. Right now we are doing it manually.

```sql
SELECT name, MAX(author_age) as author_age, department FROM training WHERE author_age > 50 GROUP BY name, department 
```

```sql id=uniq_name 
SELECT name, has_research_group, college
FROM training 
WHERE has_research_group is not NULL and college not in ('Agriculture', 'Health', 'Medical Sciences', 'Education', 'Language')  AND has_research_group != -1
GROUP BY name, has_research_group, college
ORDER BY name
```

### Coauthor age

Same for coauthors. Since coauthors are numerous, we do nothing to fix them right now. If they are above 50, we impute with NA in the model so that age_diff between author and coauthor is NA. This might not be the greatest solution because this mean we artificially make a cutoff of age diff of 50 years old. 

```sql
SELECT coauth_name, MAX(coauth_age) as coauth_age 
FROM coauthor 
WHERE coauth_age > 50 
GROUP BY coauth_name
ORDER BY coauth_age DESC
```

<!-- ```sql id=uniq_name 
SELECT name, has_research_group, college
FROM coauthor 
WHERE has_research_group is not NULL and college not in ('Agriculture', 'Health', 'Medical Sciences', 'Education', 'Language')  AND has_research_group != -1
GROUP BY name, has_research_group, college
ORDER BY name
``` -->

---


## Proportion of each college by author age

```js
const tog_age = view(Inputs.toggle({label: "normalize"}))
```

<div>${resize((width) => 
Plot.plot({
  title: "by author age by field",
  width,
  color: {legend:true},
  y: {percent:tog_age?true:false},
  fx: {ticksRotation: 90},
  marks: [
    Plot.barY(training_all, Plot.groupX({ y: tog_age ? "proportion-facet" : "count" }, {
      x: "author_age", fill: "college", 
      sort: {x: "x"}, 
      offset: tog_age ? "normalize" : null,
      tip:true,
      })),
    Plot.gridY(),
    Plot.ruleY([0])
  ]
})
)}
</div>

```sql id=[...training_all] 
  SELECT DISTINCT name, changing_rate, college, author_age, has_research_group::CHAR as has_research_group
  FROM training 
  WHERE 
    changing_rate < 40 AND 
    college in ('Humanities', 'Social Sciences', 'Physical Science', 'Computer Science', 'Biological Sciences', 'Mathematical Sciences', 'Psychological Science') 
  ORDER BY author_age
```
