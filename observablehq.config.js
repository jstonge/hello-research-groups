// See https://observablehq.com/framework/config for documentation.
export default {
  root: "docs", // path to the source root for preview
  output: "dist", // path to the output root for build
  title: "Hello Research Groups",
  pages: [
    { name: "💡 The rise of computational works", path: "/comp-works" },
    { name: "🗺️ Computational hysteresis", path: "/hysteresis" },
    { name: "💡 Grontology", path: "/grontology" },
    { name: "💡 Epistemic Inequality", path: "/epistemic-inequality" },
    { name: "📊 Researchers timeline", path: "/timeline" },
    { name: "📊 Classify computational works", path: "/classify-comp-works" },
    { name: "💡 Overthinking FoS", path: "/overthinking-fos" },
    { name: "📊 Patterns of collaboration", path: "/summary-groups" },
    { name: "📊 Summarize DB", path: "/summary-db" },
    { name: "📊 Explore NSF awards", path: "/nsf-awards" },
    { name: "📊 Explore NEH awards", path: "/neh-awards" },
    { name: "📊 Embeddings Playground", path: "/embeddings-playground" },
  ],

  // Content to add to the head of the page, e.g. for a favicon:
  head: '<link rel="icon" href="observable.png" type="image/png" sizes="32x32">',
  footer: "Built with Observable.", // what to show in the footer (HTML)
  style: "style.css"
};
