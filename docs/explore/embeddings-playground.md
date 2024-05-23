---
sql:
  embeddings: ../data/embeddings.csv
  emb_lookup: ../data/emb_lookup.csv
---
<style type="text/css">

.focus {
  color: var(--theme-foreground-focus);
}

.invert {
  background-color: var(--theme-foreground-alt);
  color: var(--theme-background);
}

.crop {
  border-radius: 8px;
  margin: 1rem;
  max-width: calc(50% - 2rem);
  box-shadow: 0 0 0 0.75px rgba(128, 128, 128, 0.2), 0 6px 12px 6px rgba(0, 0, 0, 0.4);
  aspect-ratio: 3024 / 1888;
  object-fit: cover;
  object-position: 0 100%;
}

.wbr::before {
  content: "\200b";
}

.wide {
  max-width: 960px;
}

figcaption code {
  font-size: 90%; /* TODO move to global.css */
}

</style>

# Embeddings playground

In this notebook, we do a case study of different embeddings.

## Locating digital humanities

Q: How do embeddings separate 'classical' works from the humanities from the digital humanities?

```sql id=[...lookup]
SELECT * FROM emb_lookup  
```

```js
const form = view(Inputs.form({
    fos: Inputs.select(lookup.map(d=>d.fos)),
    year: Inputs.select(lookup.map(d=>d.year))
    })
)
```

```sql id=[...embeddings]
SELECT * FROM embeddings WHERE fos = ${form.fos} AND year = ${form.year}
```

```js
const sel_pap = view(Inputs.search(embeddings, {label: "search anything"}))
```

```js
const sel_pap2 = view(Inputs.search(sel_pap, {label: "double searchhhh"}))
```

<div>${
     resize((width) =>
         Plot.plot({
             style: "overflow: visible;",
             axis: null,
             width,
             height: 600,
             margin: 30,
             marginLeft: 200,
             r: {range: [1,7]},
             marks: [
                 Plot.density(embeddings, {x:"x", y:"y", stroke: "blue", strokeWidth: 0.1}),
                 Plot.density(embeddings, {x:"x", y:"y", stroke: "blue", thresholds: 10, strokeWidth: 0.3}),
                 Plot.dot(embeddings, {
                    x:"x", y:"y", strokeOpacity: 0.9, stroke: "venue",
                    title:d=>`Title: ${d.title}\n\nvenue: ${d.venue}\n\nfos: ${d.external_fos}`, 
                    tip: sel_pap.length === embeddings.length ? true : false,
                    r: "citationCount"} 
                ),
                 Plot.dot(
                    sel_pap.length === embeddings.length ? "" : sel_pap, {
                    x:"x", y:"y", stroke: "red", fill: "red", tip: true, 
                    title:d=>`Title: ${d.title}\n\nAbstract: ${d.abstract}\n\nfos: ${d.external_fos}`, 
                    r: "citationCount"
                    } 
                ),
                 Plot.dot(
                    sel_pap2.length === sel_pap.length ? "" : sel_pap2, {
                    x:"x", y:"y", stroke: "green", fill: "lightgreen",
                    r: 5, symbol: "cross"
                    } 
                )
             ],
             })
 )}
</div>

```js
Inputs.table(sel_pap)
```

#### Journal counts

```js
Inputs.table(d3.flatRollup(embeddings, v => v.length, d => d.venue)
        .map(([venue, count]) => ({venue, count}))
        .sort((a,b) => d3.descending(a.count, b.count)))
```
