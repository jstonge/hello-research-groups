---
sql:
  embeddings: ../data/embeddings.csv
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


# Overthinking fields of studies

<div class="grid grid-cols-2">
<div>
<figure class="wide">
  <img src="https://i.imgflip.com/8q167g.jpg" alt="" width=300>
  <figcaption>Triple spider-man meme representing how field of study can take different forms.</figcaption>
</figure>

  Do all researchers in a computer science department are doing computer science? Do researchers need to publish in a established sociology venue to be doing sociology? In a computational and complex system world, the relationship between authors' department, venues, and the article content are becoming increasingly fuzzy. This is unfortunate as one of our main goals is to show how field of studies are becoming computational. If a field of study (FoS) changes label as it becomes computational, this makes our problem harder.
  
  Physicists are well-known for applying their toolbox to other disciplines, such as the social sciences and epidemiology. Researchers in computer science departments might end up doing social media studies, even though the subject matter is very much the social sciences. Arguably, the mapping between one researcher's background and its host department is not as consistent as it used to be. 

  Journals evolve over time. Disciplines evolve over time. They can evolve in different ways. First, there is the <em>multiscale</em> nature of displines. Disciplines can branch out to become more or less fine-grained. What used to be the natural sciences is now a collection of subfields, related by a common ancestor that was naturalism (or even philosophy if you go back far enough). Statistics is now machine learning. Machine learning is now many things, as measured by conferences and venues.

  Topics can fall out of fashion, but the ideas stay alive under different forms. Eugenics used to have their own journal. Albeit the eugenism as a field was rejected, we can still see some of the underlying ideas floating around in different field of studies. 

  We will introduce the main taxonomies out there used to classify papers: OpenAlex, semantic scholar, web of science, and google scholar. Each of them have different heritage, openess, and play different roles in the research ecosystem.

  We distinguish between **bottom-up** and **top-down** approaches. The top-up approach use known labels from the top—authors' department or venues' labels—to classify works at the bottom. It used to be the most common way to classify papers. A paper is sociology when it is publish in a known sociology journal. The bottom-up approach is data-driven; it is about clustering fields using the content and metadata of papers.

<div class="tip", label="Overthinking">
   To quantify the computational turn, we want to classify works more in terms topics than methods. If a paper is about the history of the House of Habsburg, or the Republic of Letters, in such a way that this is identfiable as 'History', we want to say this is history works regardless of how it has been studied. Needless to say that this is tricky. FoS are tied to their methodology; anthropologists do interview and field works, historians do archival works, sociologists do big surveys, etc. In some ways, there is no work that is 'pure history works', albeit there are seminal works. This is why we seek to combine multiple perspectives.
</div>

  ## [OpenAlex taxonomy](https://help.openalex.org/how-it-works/topics)
  
  <div class="card">
  <b>tldr;</b> Each paper has a topic, which is then mapped onto Scopus' taxonomy. Topics are clusters on co-citation graph, which has been labeled using GPT3.5 Turbo (they provided top papers based on representative sample of papers). 
  </div>

  OpenAlex worked with people at the Leiden university to have a list of topics to classify papers. That draws from years of experimentation in bibliometry, and perhaps more importantly that is open and transparent. By open, we mean that we know what is the algorithm underlying the classification (as opposed to Web of Science and Google Scholar). Their taxonomy borrows from Scopus's ASJC structure, but works at the leve of papers instead of being derived at the journal level. OpenAlex contribution in that regard was to connect topics to the ASJC structure.
  
  By virtue of being open, they allow us to tinker with their ideas; we know, for instance, that their topics is really link clustering of the co-citation graph. We know that they do not use content to derive their classication. This matters. If we define a field in terms of who cite who, then two researchers using completely different methods might end in different disciplines, even though they work on the same topic. This is most likely the case of linguistics. In open alex, linguistics is found both in the subcategory of Arts and Humanities and in the Social sciences. But if you take a venue-first approach (where the venues dictate the classification), as with Google scholar, we find that computational linguistics is also a field in Engineering & Computer Science.

  - [OpenAlex_topic_mapping_table](https://docs.google.com/spreadsheets/d/1v-MAq64x4YjhO7RWcB-yrKV5D_2vOOsxl4u6GBKEXY8/edit?usp=sharing)
  - [An open approach for classifying research publications](https://www.leidenmadtrics.nl/articles/an-open-approach-for-classifying-research-publications)


</div>
    <div>${resize((width) => plot_tree(oa_taxonomy, {width, height: 2400}))}</div>
</div>

   
</div>

---


```js
const s2orc_taxonomy = FileAttachment("../data/taxonomy/s2orc-fos.json").json();
```

<div class="grid grid-cols-2">
<div>

  ## [Semantic Scholar fields of study](https://blog.allenai.org/announcing-s2fos-an-open-source-academic-field-of-study-classifier-9d2f641949e5)
  
  <div class="card">
  <b>tldr;</b> Each paper has up to three FoS. The model use paper's title and abstract as input. Folks at semantic scholar annotated 500 papers to validate their classification scheme. They favor recall, but still achieve 0.9  prevision with papers+abstracts, and 0.8 for title only papers.
  </div>

  S2ORC build on [Microsoft Academic Graph](https://www.microsoft.com/en-us/research/project/microsoft-academic-graph/) original taxonomy, but they build a machine learning model (linear SVM running on character n-gram TF-IDF representations) to keep classifying papers on their end. Their model use paper's title and abstract as input. They favored a flat hierarchy, but each paper can be composed of up to three field of study. They added in their taxonomy the fields of Linguistics, Law, Education, and Agriculture and Food Sciences.

  
  - [semantic scholar publishing partners](https://www.semanticscholar.org/about/publishers)
  
</div>
<div>${resize((width) => plot_tree(s2orc_taxonomy, {width, height: 400}))}</div>
</div>

---


```sql id=embeddings
SELECT * FROM embeddings  
```

<div class="grid grid-cols-2">
<div>

## Embeddings

<div class="card">
  <b>tldr;</b> Embeddings are magical. We can cluster papers that to create bottom-up field of studies.
</div>

Embeddings are magical, but hard to work with in a principled way. They are magical because they seem to work. Each point in the figure on the left correspond to a paper, or more precisely a combination of the papers' title, abstract, and citation. If you hoover the point, you can look at the title and abstract and see that they are kind of related. They are hard to work with because what says that we are not just reading tea-leaves.

We can aggregate researchers' contributions to better understand their field of study. Because this space is mostly topical, we could in principle find researchers who are doing, say, sociology even if they do not tend to publish in sociological journal. I say mostly, because if computational social scientists keep talking about how they use computational methods, they might end up closer together than to researchers' in their 'true field of study'.

One nice feature with embedding space is that when we use density-based methods to cluster papers, we end up with some proptoypical coordinates of a given field of study... 

</div>
<div>${
    resize((width) =>
        Plot.plot({
            style: "overflow: visible;",
            axis: null,
            height: 600,
            margin: 30,
            r: {range: [1,7]},
            marks: [
                Plot.density(embeddings, {x:"x", y:"y", stroke: "blue", strokeWidth: 0.1}),
                Plot.density(embeddings, {x:"x", y:"y", stroke: "blue", thresholds: 10, strokeWidth: 0.5}),
                Plot.dot(embeddings, {x:"x", y:"y", tip: true, title:d=>`Title: ${d.title}\n\nAbstract: ${d.abstract}`, r: "citationCount"} )
            ],
            caption: "Embeddings are all about constructing a continous space with some notion of distance. With that in hand, it becomes possible to optimize similarity between documents in term of some training objective. In this case, the objective sought to put closer together papers with similar titles and abstract, but also in terms of citations. Understanding how embeddings are constructed is key to understand what assumptions are baked in, as with any other non-supervised methods."
            })
)}
</div>
</div>

<!-- Plot.tip(['sociology of health (hiv)', 'suicide'], {x:[10.3, 10.6], y: [7.9, 10]} ), -->

---

## [Web of Science](https://images.webofknowledge.com/images/help/WOS/hp_research_areas_easca.html)


```js
const wos_taxonomy = FileAttachment("../data/taxonomy/WOS-fields2domain.json").json();
```

<div class="grid grid-cols-2">
<div>
  Talking about FoS
</div>
<div>${resize((width) => plot_tree(wos_taxonomy, {width, height: 1700}))}</div>
</div>

---

## [Google scholar (FoS → Venues)](https://scholar.google.ca/citations?view_op=top_venues&hl=en)

```js
const gscholar_taxonomy = FileAttachment("../data/taxonomy/gscholar-taxonomy.json").json();
```

<div class="grid grid-cols-2">
  <div>
    Here we look at a different approach; papers inheritate the categories of the venues. The rationale is that if a paper is published in well-know venues in, say, linguistics, then it is a linguistic paper. It is unclear where Google Scholar categories are coming from. 

  </div>
  <div>${resize((width) => 
        plot_tree(gscholar_taxonomy, {width, height: 1500}))
    }</div>
</div>

## [Google scholar Full Blown (FoS → Venues)](https://scholar.google.ca/citations?view_op=top_venues&hl=en)

```js
const gscholar_taxonomy2 = FileAttachment("../data/taxonomy/gscholar_full_taxonomy.json").json();

const abbrev2full = {
  "soc": "Social Sciences", 
  "bus": "Business, Economics & Management", 
  "hum": "Humanities, Literature & Arts", 
  "chm": "Chemical & Material Sciences", 
  "med": "Health & Medical Sciences", 
  "bio": "Life Sciences & Earth Sciences", 
  "phy": "Physics & Mathematics", 
  "eng": "Engineering & Computer Science"
}
```
```js
const gscholar = view(Inputs.radio(['soc', 'bus', 'hum', 'chm', 'med', 'bio', 'phy', 'eng'], {
    value: 'soc', 
    format: x => abbrev2full[x],
  }))
```


<div>${resize((width) => plot_tree(
  gscholar_taxonomy2.filter(d => d.name.split(".")[0] == gscholar), 
  { width, height: 10000 }))}</div>


---

## Summary

Best seen if the collapsible table of content closed and wide enough screen. 

#### Level 0

<div class="grid grid-cols-4">
  <div>OpenAlex${ 
    medium_tree(
      d3.flatRollup(oa_taxonomy, v => v.length, d => d.name.split(".")[0])
        .map(([name, count]) => ({name, count}))
        .sort((a,b) => d3.ascending(a.name, b.name)), {width:100, height: 100})
  }
  </div>
  <div>Semantic Scholar${ 
    medium_tree(
      d3.flatRollup(s2orc_taxonomy, v => v.length, d => d.name.split(".")[0])
        .map(([name, count]) => ({name, count}))
        .sort((a,b) => d3.ascending(a.name, b.name)), {width:100, height: 400})
  }
  </div>
  <div>WoS${ 
    medium_tree(
      d3.flatRollup(wos_taxonomy, v => v.length, d => d.name.split(".")[0])
        .map(([name, count]) => ({name, count}))
        .sort((a,b) => d3.ascending(a.name, b.name)), {width:100, height: 100})
  }
  </div>
  <div>GoogleScholar${ 
    medium_tree(
      d3.flatRollup(gscholar_taxonomy2, v => v.length, d => abbrev2full[d.name.split(".")[0]])
        .map(([name, count]) => ({name, count}))
        .sort((a,b) => d3.ascending(a.name, b.name)), {width:100, height: 200})
  }
  </div>
</div>

---


#### Level 1
<div class="grid grid-cols-4">
    <div>OpenAlex${resize((width) => 
      medium_tree(
        d3.flatRollup(oa_taxonomy, v => v.length, d => d.name.split(".")[1])
          .map(([name, count]) => ({name, count}))
          .sort((a,b) => d3.ascending(a.name, b.name)), {width:100, height: 400})
    )}
      <div>
        <br>
        <hr>
        <b>Level2</b> ${resize((width) => 
        medium_tree(
          d3.flatRollup(oa_taxonomy, v => v.length, d => d.name.split(".")[2])
            .map(([name, count]) => ({name, count}))
            .sort((a,b) => d3.ascending(a.name, b.name)), {width:100, height: 3300})
        )}
      </div>
    </div>
  <div>
  Semantic Scholar
  </div>
  <div>WoS${resize((width) => 
    medium_tree(
      d3.flatRollup(wos_taxonomy, v => v.length, d => d.name.split(".")[1])
        .map(([name, count]) => ({name, count}))
        .sort((a,b) => d3.ascending(a.name, b.name)), {width:100, height: 1800})
  )}
  </div>
  <div>GoogleScholar${resize((width) => 
    medium_tree(
      d3.flatRollup(gscholar_taxonomy2, v => v.length, d => d.name.split(".")[1])
        .map(([name, count]) => ({name, count}))
        .sort((a,b) => d3.ascending(a.name, b.name)), {width: 100, height: 3000})
  )}
  </div>
</div>

---

## Final taxonomy

<div class="grid grid-cols-2">
  <div>
  
  With all that, we construct our own taxonomy that seek to bring forth parts of sciences who might be transitioning from the qualitative science to quantitative science. We proceed as follow:

  ```
  ◆ Start from openAlex level 1's hierarchy
  ◆ Break down large categories, use s2orc as replacement
    ◆ Split arts and humanities and social sciences
    ◆ Replace agricultural and biological sciences with Agricultural and Food Sciences
    ◆ Split environmental science into `ecology` and `Pharmacology, Toxicology and Pharmaceutics`
    ◆ Add `Earth and Planetary Sciences`
    ◆ Split Statistics, Probability and Uncertainty from mathematics
  ◆ Aggregate some categories that are not the focused of this study
    ◆ health professions and medicine into health and medical sciences
    ◆ Aggregate Veterinary and dentistry into health and medical science
    ◆ Aggregate energy into physics and astronomy or material science
  ◆ Add Literature and Literary Theory, Information Systems and Management
  ```
  </div>
  <div>${ resize((width) => plot_tree(my_taxonomy, {width, height: 500})) }
  </div>
</div>

```js
const oa_taxonomy = FileAttachment("../data/taxonomy/oa-fields2domain.json").json();
```

```js
function plot_tree(data, {width, height} = {}) {
  return Plot.plot({
    axis: null,
    margin: 10,
    marginLeft: 80,
    marginRight: 160,
    width,
    height,
    marks: [
      Plot.cluster(data, {path: "name", delimiter: "." })
    ]
  })
}
```


```js
function medium_tree(data, {width, height}= {}) {
  return Plot.plot({
    axis: null,
    height,
    margin: 10,
    marginLeft:20,
    width,
    marginRight: 0,
    marks: [
      Plot.tree(
        data,
        { path: "name" }
      )
    ]
  })
}
```

```js
const my_taxonomy = [
  // APPLIED MONEY PEOPLE
  {"name": "Business, Management and Accounting"},
  // SMALL STUFF
  {"name": "Pharmacology, Toxicology and Pharmaceutics"},
  {"name": "Biochemistry, Genetics and Molecular Biology"},
  // INFORMATION STUFF
  {"name": "Computer Science"},
  {"name": "Information Systems and Management"},
  // EDUCATION
  {"name": "Education"},
  // HEALTH
  {"name": "Health & Medical Sciences"},
  // APPLIED
  {"name": "Agricultural and Food Sciences"},
  {"name": "Engineering"},
  {"name": "Materials Science"},
  // "NATURAL SCIENCES"
  {"name": "Chemistry"},
  {"name": "Earth and Planetary Sciences"},
  {"name": "Ecology"},
  {"name": "Neuroscience"},
  {"name": "Physics and Astronomy"},
  // MATHS
  {"name": "Mathematics"},
  {"name": "Statistics, Probability and Uncertainty"},
  // ARTS
  {"name": "Arts"},
  // HUMANITIES
  {"name": "Humanities.History"},
  {"name": "Humanities.Literature and Literary Theory"},
  {"name": "Humanities.Philosophy"},
  {"name": "Humanities.Law"},
  // SOCIAL SCIENCES (FROM LESS TO MORE QUANTS)
  {"name": "Social Sciences.Anthropology"},
  {"name": "Social Sciences.Linguistics"},
  {"name": "Social Sciences.Psychology"},
  {"name": "Social Sciences.Geography"},
  {"name": "Social Sciences.Economics, Econometrics and Finance"},
  {"name": "Social Sciences.Sociology"},
]
```

