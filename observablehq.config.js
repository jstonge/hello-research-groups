// See https://observablehq.com/framework/config for documentation.
export default {
  root: "docs", // path to the source root for preview
  output: "dist", // path to the output root for build
  title: "Hello Research Groups",
  pages: [
    { name: "Researcher timeline", path: "/timeline" },
    { name: "Summary Research Groups", path: "/summary-groups" },
    { name: "Summary DB", path: "/summary-db" },
    { name: "NSF awards", path: "/nsf-awards" },
    { name: "NEH awards", path: "/neh-awards" }
  ],

  // Content to add to the head of the page, e.g. for a favicon:
  head: '<link rel="icon" href="observable.png" type="image/png" sizes="32x32">',
  footer: "Built with Observable.", // what to show in the footer (HTML)
  style: "style.css"
};
