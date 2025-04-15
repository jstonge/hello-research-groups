// See https://observablehq.com/framework/config for documentation.
export default {
  root: "src", // path to the source root for preview
  output: "dist", // path to the output root for build
  title: "The Story of US",
  pages: [
    { name: "Short history of group minds", path: "/grontology" },
    { name: "Laboratory of group mind", path: "/theory-primer" },
    {
      name: "Models",
      pages: [
        { name: "Defining and classifying models of groups", path: "models/interface" },
        { name: "Computational hysteresis", path: "models/groupSkills"},
        { name: "Paradoxes in the co-evolution of contagions and institutions", path: "models/coevo" },
      ]
    },
    {
      name: "Results",
      pages: [
        { name: "Researchers timeline", path: "results/timeline" },
        { name: "Patterns of collaboration", path: "results/summary-groups" },
      ]
    },
    {
      name: "Methods",
      open: false,
      pages: [
        { name: "Classify computational works", path: "methods/classify-comp-works" },
      ]
    },
    {
      name: "Explore",
      open: false,
      pages: [
        { name: "Summarize DB", path: "explore/summary-db" },
        { name: "Explore NSF awards", path: "explore/nsf-awards" },
        { name: "Explore NEH awards", path: "explore/neh-awards" },
        { name: "Embeddings Playground", path: "explore/embeddings-playground" },
      ]
    },
    {
      name: "Appendix",
      open: false,
      pages: [
        { name: "Multiverse Literature Review", path: "appendix/lit-review" },
        { name: "Overthinking FoS", path: "appendix/overthinking-fos" },
        { name: "Computational + X", path: "appendix/a-comp-story" },
        { name: "SciSciDB", path: "appendix/scisciDB" },
        { name: "Finetuning LLMs", path: "appendix/finetuning-llms" },
        { name: "Accelerating annotations", path: "appendix/accelerating-annots" },
      ]
    }
  ],

  // Content to add to the head of the page, e.g. for a favicon:
  head: '<link rel="icon" href="observable.png" type="image/png" sizes="32x32">',
  footer: "Built with Observable.", // what to show in the footer (HTML)
  style: "styles.css"
};
