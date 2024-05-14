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

## Categorizing field of sciences

To say whether a field is becoming computational, we need to classify papers with one or many fields of science. This is a well known task that is still actively worked upon (CITE recent works; [this workshop](https://github.com/NFDI4DS/nslp2024/blob/main/accepted_papers/NSLP_2024_paper_27.pdf)). We start by looking at exclusive labelling--both from top-down and bottom-up approches--we then talk about works multiple labels.

### Top-down approaches

Top-down approaches are ...

Databases like web of science uses venues as marker. If you publish your papers in a venue the 'American Journal of Sociology', then it is sociology. This is not a bad start. Oftentimes, this approach will even get you emerging field such as computational linguistics, as they become mature they will start their own venue. 

But using venues as markers have its pitfalls. [EXPLAIN WHY]. This might take time before an emerging field has its own venue, due to edfitorial resistance. A computational linguistics paper might end up in computer science journals instead of linguistics because of disagreements about linguistics becoming computational. It might be that papers are more or less prototypical of the venues. That some papers in the 'Journal of Sociology' is really more political or anthropological.

Another top-down approach is to look at keywords that authors use to describe their own work, or what the crowd has to say. 

### Bottom-um approaches

Instead of using the labels from the venues, you can adopt a bottom-up approach. Look at the content of a paper using some clustering algorithm.

### A mix of the two

Try both, and see how the findings are aligned.

## Timely issues

The tricky bit is how to  handle time. Any label is subject to the _Theseus's paradox_. That is, if you change all the parts that is the the ship of Theseus, but that those original parts are somehow reused somewhere else to build a new ship, which one Theseus ship. The one that stayed afloat, that maybe Theseus is still on it, or the new on that is built from the original part of Theseus' ship. 

## OA taxonomy

