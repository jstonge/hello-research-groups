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


```js
const taxonomy = FileAttachment("../data/taxonomy/comp-taxonomy.json").json();
```

<div class="grid grid-cols-2">
<div>

  ## Classifying computational works

  As we saw in the previous section, 'computational' has different meaning for different communities. For some communities, computational is really about numerical works. As in computational physics. In other communities, such as the social sciences, computational as in 'computational methods' refer to a set of practices that require programming in some ways.

  We define computational works with the following heuristics:

  > Did the authors had to run code to produce the paper, aka perform simulations, produce visualization, or run statistical analysis. 

  This is hard to answer. We adopt the following methods, which goes from full blown quantification of how much computation there might have been in papers to a simple binary classification. 

  ### Computational complexity
  
  This is the best answer we can give. Given a set of parsed pdfs, we extract sentences containing mention of practices that might involve computer programming, i.e. simulation, data or code availability statement, computational X, and so on. For each mention, we seek to determine author's intent (same than the [Software Mention Recognition task at NSLP 2024](https://github.com/NFDI4DS/nslp2024/blob/main/accepted_papers/NSLP_2024_paper_28.pdf), related more generally to classifying citation intent in papers). That is, we seek to determine if the author was mentioning simulation/data/code/... such that it involved usage or creation of the mention thing, or it was a simple mention of other's work. To do that, we need to be able to extract all mentions from a papers.
  
  With that in hand, we can create a score on a "computational complexity" scale, where zero is non-computational at all and 9 is very much computational. We understand computational complexity like anthropologists understand technological complexity. We assume that we are able to count bits of the paper that involve computation. A paper with only numerical simulations contain less computation than one involving simulations as well as a full blown data analysis pipeline. Similarly, one where authors had to scrape their own data contains more computation than one where the data was provided and so on. In a very naive way, this notion of computational complexity is literally Kolmogorov complexity, where complexity is measured in terms of the shortest computer programs that could produce the paper in question. The only difference is that we actually seek to measure program lengths underlying ideas.
  </div>
  <div><br><br><br><br><br><br><br>${
  resize((width) => plot_tree(taxonomy, {width, height: 800}))
  }</div>
</div>

### Distilling computational complexity to binary classification

In many cases on our main database (semantic scholar), we have papers' title, abstract, figures. Based on that, we can seek to estimate the probability that a paper is computational, but we cannot fully quantify the computational complexity of a paper.  We play the following question game to label computational papers from abstract, title, and figures alone:
- Do they straight up claim to use computational methods or do computational X?
  - Is there a mention of computational methods, aka topic modeling, BERT, word embeddings, automated text analysis, text mining, etc?
  - Do they cite a F/OSS library in their references?
- Do they have way too much data to do it without programming?
- Do their figures look like they've been generated by a programming language?

Here are some pitfalls when doing so:
- Papers talking _about_ computational social science or digital humanities are not computational. This is why simply matching sentences with keywords is not good enough.
- _Computational_ theory of the mind is mostly conceptual. Philosophers love to talk about it.
- There might be figures in a paper, but they are from someone else and the authors are just _talking_ about it to make a point.
- There might be figures in a paper, but not produced by code. When they are schema, it is obvious. When it is excel or SAS, you need to distinguish between those and figures produced by programminglanguages. Not always easy, but generally doable.


```js
function plot_tree(data, {width, height} = {}) {
  return Plot.plot({
    axis: null,
    marginLeft: 80,
    width,
    height,
    marks: [
      Plot.tree(data, {path: "name", delimiter: ".", tip: true })
    ]
  })
}
```