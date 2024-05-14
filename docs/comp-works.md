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

# What is the computational turn?

It is a turn in that it came fast. Too fast for institution to adapt, but nonetheless expected when you get to grad school. For some fields, this came as a breeze. You just add a few courses here and there. For other, this meant war.

## Why study the computational turn?

Arguably, the following are good enough reasons to study the computational turn:

 - `Diversity in science`: it matters who do the science. If a science is becoming more male-dominated as a result of a computational turn, we should do something about it. There are reasons to believe this is the case.
 - `Reproducibility and transparency in science`: people who are not interested in good software engineering practice won't write code that is reproducible or transparent. 
 - `Reducing the suffering when dabbling with code`: writing dirty code is easy, writing code that your future selves and others will want to engage with is hard. If there is a lack of community when individual engage with computational works, it can have strong negative impact on individuals. Especially when individuals don't have a background in computing and engage reluctantly with ccomputaional works.
 - `Diversity in the tech industry`: it matters who build the tools that impact the scoiety at large. It is not enough to have oversight, we need a diversity of people in the tech industry as well at the level of software engineers. To get there, we need people from different socioeconomic and academic backgrounds that enter in the tech industry.

The computational turn has many benefits, but here we note the other side of the coin from a humanist perspective:

<div class="grid grid-cols-2">
    <div class="card"><h2>Dr Jekyll</h2>
        <li>Computational approach makes maths anb stats easier, sometimes even irrelevant.</li><br>
        <li></li>
    </div>
    <div class="card"><h2>Mr Hyde</h2>
        <li>Fields are can potentially becoming naturalized, which means they are more mathy. This can come with its own issues when the fields care about phenomenology, or the lived experience.</li>
        <li></li>
    </div>
</div>

## What makes the computational turn 'computational'

<figure class="wide">
  <picture>
    <source srcset="./assets/maslow.svg" media="(prefers-color-scheme: dark)">
    <img loading="lazy" src="./assets/maslow.svg" class="wide">
  </picture>
  <figcaption>One potential hierarchy of needs for computational social scientists. By amateur software engineering, we mean testing code, making it shareable and readble, or make it performant. By principled data cleaning, we mean how to clean code in such a way you actually introduce bugs in your cleaning process, and your cleaning process will be reproducible on the long run. To be fair, this is the hierarchy of needs to computational social scientists who work with observational data. The hierarchy ought to differ for experimentalists or theoreticians, but there will be overlap.</figcaption>
</figure>

## A little history of computational X

### Computational Physics

 - [Computational Physics (2013)](https://public.websites.umich.edu/~mejn/cp/)
 - [Python for Astronomers (2014)](http://ugastro.berkeley.edu/pydecal/textbook.pdf)

The computational turn in Physics was barely noticeable. For physicists, it was about using computers to do computation, thus computational physics. It was more about the pitfalls of numerical methods, and how to write efficient code, than promoting F/OSS. That said, in some parts of physics, early on there was also the realization tha computers were more than computations; it was about sharing code, data, analysis, reproducibility, etc. 

### Computational linguistics

<figure class="wide">
  <picture>
    <source srcset="./assets/jurafsky_comp_ling.webp" media="(prefers-color-scheme: dark)">
    <img loading="lazy" src="./assets/jurafsky_comp_ling.webp" class="crop">
  </picture>
  <figcaption>Linguists are talking about computers. What's up with that?</figcaption>
</figure>

The computational turn in linguistics was perhaps one of the most acrimonious divorce.

 - [Computational Linguistics, Volume 19, Number 1, March 1993, Special Issue on Using Large Corpora: I](https://aclanthology.org/J93-1000.pdf)
 - [Computational Linguistics and its Use in Real World:
the Case of Computer Assisted-Language Learning](https://aclanthology.org/C96-2171.pdf)
 - [LINGUISTICS IN A COMPUTATIONAL WORLD](https://www.ideals.illinois.edu/items/11601/bitstreams/42397/data.pdf)

### Computational Thinking

 - [Computational Thinking (2006)](https://www.cs.cmu.edu/~15110-s13/Wing06-ct.pdf)

Surprisingly, this idea of computational thinking at the intersection of computer science and education. It was further realization that computational X is more than computers; it is a way of being. Nothing less. Computers, and communities around them, are cognitive gadgets. Instead of thinking with maths, most people can have an easier time to work with programs. 

### Computational Journalism

 - [11.3: Computational Journalism](https://socialsci.libretexts.org/Bookshelves/Communication/Journalism_and_Mass_Communication/The_American_Journalism_Handbook_-_Concepts_Issues_and_Skills_(Zamith)/11%3A_Future_of_Journalism/11.03%3A_Computational_Journalism)

### Computational Ecology

- [Computational ecology as an emerging science(2012)](https://royalsocietypublishing.org/doi/10.1098/rsfs.2011.0083)

### Computational Finance 

- [https://www.math.cmu.edu/users/bscf/](https://www.math.cmu.edu/users/bscf/whatis.html)

### Computational Statistics

 - [Jake Vanderplas - Statistics for Hackers - PyCon 2016](https://www.youtube.com/watch?v=Iq9DzN6mvYA)

Very related to computational thinking, simulating and bootstrapping is easier than understanding the mathematics behind the p-values.

### Computational Social Science, digital humanities, and Cultural Analytics

<figure class="wide">
  <picture>
    <source srcset="./assets/css_is_sus.webp" media="(prefers-color-scheme: dark)">
    <img loading="lazy" src="./assets/css_is_sus.webp" class="crop">
  </picture>
  <figcaption>Social science + computers?</figcaption>
</figure>

Manifestos

 - [Life in the network: The coming age of computational social science: Science](https://www.semanticscholar.org/paper/Life-in-the-network%3A-The-coming-age-of-social-Lazer-Pentland/eb2269b4fcd83ec96e7f2fca1becd5958ac28c9b)
 - [Computational social science: Obstacles and opportunities (2020)](https://www.semanticscholar.org/paper/Computational-social-science%3A-Obstacles-and-Lazer-Pentland/c1e49d830e67269d4d2053a5f124ea773c79b740)
 - [Text mining for social science - The state and the future of computational text analysis in sociology (2022)](https://www.semanticscholar.org/paper/Text-mining-for-social-science-The-state-and-the-of-Macanovic/f0c6fb5d5f632aed414fa2354fc240685b52783b)
 - [Integrating explanation and prediction in computational social science (2021)](https://www.semanticscholar.org/paper/Integrating-explanation-and-prediction-in-social-Hofman-Watts/16cd0cadc4a757d85da6bd72992f6fb75a685ac7)
 - [Manifesto of computational social science](https://www.semanticscholar.org/paper/Manifesto-of-computational-social-science-Conte-Gilbert/0888bb211901eaac37b19a7e4a5096006349c4d5)
 - [Computational Social Science and Sociology.](https://www.semanticscholar.org/paper/Computational-Social-Science-and-Sociology.-Edelmann-Wolff/be5b11775e2e4a32c1b6dca28c7b24eb158059f6?sort=total-citations)
 - [Text as Data: The Promise and Pitfalls of Automatic Content Analysis Methods for Political Texts](https://www.semanticscholar.org/paper/Text-as-Data%3A-The-Promise-and-Pitfalls-of-Automatic-Grimmer-Stewart/b9921fb4d1448058642897797e77bdaf8f444404)
 - [Large-Scale Computerized Text Analysis in Political Science: Opportunities and Challenges](https://www.semanticscholar.org/paper/Large-Scale-Computerized-Text-Analysis-in-Political-Wilkerson-Casas/0d345c2fb459e6ecc28328917ab37a4707e4a502)
 - [Extracting Policy Positions from Political Texts Using Words as Data](https://www.semanticscholar.org/paper/Extracting-Policy-Positions-from-Political-Texts-as-Laver-Benoit/7d9cc63dfbd34acf271e3a2c922ea1c07fb2f482)

#### The debate 

 - [Teaching Computational Social Science for All (2020)](https://www.cambridge.org/core/journals/ps-political-science-and-politics/article/teaching-computational-social-science-for-all/66EAB886BCF21C647E2387051D6A9BEF)
 - [Computational Analysis of Political Texts: Bridging Research Efforts Across Communities](https://www.semanticscholar.org/paper/Computational-Analysis-of-Political-Texts%3A-Bridging-Glavas-Nanni/4dea8e7bbc8f59b0307879121f5f8eab0848dd06)
 - [For a heterodox computational social science](https://www.semanticscholar.org/paper/For-a-heterodox-computational-social-science-T%C3%B6rnberg-Uitermark/3a45303cf6fb902bbff653e2e1dbb1dcb4ca531c)

## Groups and the computational turn

In the free and open source world, it is understood that many software projects are really about the community. The community is what make a project great or burn it to the ground. F/OSS is in large part responsible for the development of new collaborative tools that sustain the digital economy. It is about project management and having people working together on shared projects. F/OSS requires a whole new understanding of being a good citizen of the free and open source world. For example, by understanding the faux-pas of confusing open-source with free software. It more than just learning about the skills. 

Nowhere it is as obvious that, actually, science is a very individualistic enterprise than by comparing it with F/OSS. What do I mean by that? Isn't it science the most collaborative activity there is? Yes and no, but mostly no. Of course science is about collaboration. But when you thinking about it, so much of _academia_ is about personal feats, what we can call the 'heroic vision of science'. This is why we have laws named after individuals, even though most of the time they weren't really the ones who invented ([Stigler's law](https://en.wikipedia.org/wiki/Stigler%27s_law_of_eponymy)). Most awards and metrics are about individuals. In many domains, people are genuinly scared to be scooped because being the first one to make a discovery is what make you publish in prestigious journals, in turn making it possible to land a faculty position. 

All of this rise the following question; do the computational turn could significantly alter the individualistic tradition such that individuals who work as groups are favored, evolutionarily speaking? By that, can we test for the _multilevel selection hypothesis_, where people who work together outcompete groups who are less collaborative, either by differential reproduction, prestige-biased selection, or even migration across the border of science. 

The same argument can be made at institutional level. Do institutions who are able to adapt to this new reality will be favored, thereby spreading their practices to other, more conservative institutions. This strand of research is about the organizational contexts in which researchers and their groups evolve, either by providing labor advantage or having early start by having stronger digital instructure. 

All of that depend on how we define groups, collaboration, and institutions, which we do next.









