// See https://observablehq.com/framework/config for documentation.
export default {
  root: "docs", // path to the source root for preview
  output: "dist", // path to the output root for build
  title: "The Story of US",
  pages: [
    { name: "The Computational Turn", path: "/comp-works" },
    { name: "Epistemic Inequality", path: "/epistemic-inequality" },
    { name: "Computational hysteresis", path: "/hysteresis" },
    { name: "Multiverse Literature Review", path: "/lit-review" },
    { name: "Primer group ontology", path: "/grontology" },
    {
      name: "Models",
      pager: "models",
      pages: [
        { name: "Group-based models", path: "models/gbms" },
      ]
    },
    {
      name: "Methods",
      pager: "methods",
      pages: [
        { name: "Classify computational works", path: "methods/classify-comp-works" },
      ]
    },
    {
      name: "Results",
      pager: "results",
      pages: [
        { name: "Researchers timeline", path: "results/timeline" },
        { name: "Patterns of collaboration", path: "results/summary-groups" },
      ]
    },
    {
      name: "Explore",
      pager: "explore",
      pages: [
        { name: "Summarize DB", path: "explore/summary-db" },
        { name: "Explore NSF awards", path: "explore/nsf-awards" },
        { name: "Explore NEH awards", path: "explore/neh-awards" },
        { name: "Embeddings Playground", path: "explore/embeddings-playground" },
        { name: "Hysteresis modeling", path: "explore/hysteresis-extra" },
      ]
    },
    {
      name: "Appendix",
      pager: "appendix",
      pages: [
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
  style: "style.css"
};
