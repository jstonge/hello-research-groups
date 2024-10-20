# Multiverse literature review

## Groups are real. A synthesis.

We review the study of groups in the multiverse of scientific research. The topic is vast. There are an infinite number of ways to talk about groups. We could simply talk about the grouping of stuff, or how the structure of living systems are determined by that of social organizations. We could focus how human societies are being shaped rise of formal institutions and firm selection. To cut across the multiverse, we ask ourselves how key field of studies answered the following questions:

<div class="callout-box">
  <ul>
      <li>Who argued for the reality of groups?</li>
      <li>What was their underlying ontology, or motives? Did they believe that group interactions were somehow irreducible to individuals.</li>
      <li>What was their modeling approach?</li>
  </ul>
</div>

<div class="grid grid-cols-2">
  <div>

  **Groups in the Social Sciences**: By social sciences, we mean those fields interested in humans and driven by theory, claiming the legacy of their forefathers. Traditionally, these fields relied on verbal models and experiments. In this category, we include conformity studies and group psychology (Asch et al.), sociologists drawing from Georg Simmel, and evolutionary-minded sociologists and philosophers such as Donald Campbell, David Hull, Bill Wimsatt, etc. We also include sociologists and anthropologists who have ventured into social network analysis.

  **Group Selection in Biology**: This was controversial. In the 1960s, Wynne-Edwards proposed the idea of groups as a legitimate level of selection. The idea was that traits could evolve not in the service of individuals but because they are beneficial to groups (initially framed in terms of population regulation). Biologists fiercely opposed this idea. For many, the collective response seemed disproportionate, possibly influenced by the social climate of the era. Group selection theory resurfaced later, mostly in the form of multilevel selection theory.

  **Firms as Groups**: Organizational scientists, especially those interested in firms (Richard Scott, etc.), often approach firms through an evolutionary lens, talking about firm selection. While these scholars could be classified as part of the social sciences, they tend to exist in their own domain, tracing their origins to forefathers like Schumpeter and Ronald Coase, and often relying on complex concepts. However, this community seems to prefer some degree of independence from the broader social sciences.

  **Public Good Games**: This literature, derived from Elinor Ostrom's work on social dilemmas, typically uses public good games to study group dynamics. Though informed by the social sciences, it presents a distinct set of questions important to the study of groups and unique to this literature. The key idea is how groups can self-govern in the face of social dilemmas under specific conditions. Groups can evolve sets of rules to avoid the tragedy of the commons, showing they are not as "mindless" as once thought. Notably, this literature often focuses on smaller groups, where a sense of joint commitment toward common-pool resources is present.

  **Team Science**: Starting in the 1980s and 90s, management and business science began to realize that efficient teams can be more productive. Since then, the idea has been applied across various domains—business, sports teams, research groups, software developers, and so on. Over time, this concept has merged with complex systems thinking (e.g., Scott Page and other SFI scholars). While all teams are groups, not all groups are teams; teams are often described as more synergistic.

  **Cultural Group Selection**: Emerging from population biology, cultural group selection theory combines covariance genetics and game theory to demonstrate the conditions under which group-beneficial traits can evolve through group selection processes. The theory originated from 1960s debates about altruism and how reciprocity alone might not explain large-scale cooperation among unrelated individuals. A key result driving group selection is the Price equation, applied to groups of individuals with norms that maintain between-group variance while reducing within-group cultural variations.

  <div class="note">
  We distinguish between group-level features that map onto kin-based and formal institutions. By kin-based, we mean social institutions that are characteristics of kin-based social systems; they facilitate assortments but are based on the biology of cooperation. Formal institutions are written set of rules that are abstracted to unify voluntary-based  groups (associations), think of firms, church, universities, non-profits, or ministries. Both institution types are characterized by societal facts and collective intentionality specifying behavioral rules for within- and inter-group interactions. A popular definition is how institution reduce ambiguities in navigating social lives. 
  </div>

  **The Ontology of Groups**: Collective intentionality seeks to explain the feeling that a collective is more than the sum of individual intentions. As Searle puts it, there is a "we" that transcends individual actions, like friends walking together, which is more than each person merely intending to walk. This concept can also manifest in the impersonal "we" that members of a society feel, motivating them toward collective actions such as going to war or feeling pride when a local sports team wins a championship. 

  **Groups as Higher-Order Networks**: Social scientists are interested in higher-order structures, such as triangles, cliques, and clubs. But here we refer to the community of network scientists who share a toolbox that is coming from physics, most notably statistical physics and information theory. By contrasts to the social scientists, the devil of their work is often in the analytic results and modeling details.

  In the theoretical work of this thesis, we seek to inform contemporary group-based models based on higher-order networks with the following facets of groups that cut across these communities:
  <div class="def">
    <ul>
    <li><em>Isolation</em>: do groups communicate? What is the influence of inter-group interactions.
    <li><em>Persistence</em>: many-body interactions are group momentarily in time. They fundamentally differ from groups that persist in time in that persistent groups can exhibit institutional reality. One might think that repeated many-body interactions is entangled with the evolution of stronger institutions.
    <li><em>Irreducibility</em>: what kinds of group interactions cannot be reduced to the sum of individual, or pairwise, interactions.
    <li><em>Alignment</em>: given group-interactions are irreducible, what does it says about the alignment of individual intentionalities with that of the group minds. How does governance and institutionalization play into that?
    <li><em>Differentiation</em>: with persistent, irreducible, and misaligned groups, we find that individuals are often differentiated in the groups. One key aspect of differentiation is hierearchy and the role of leadership.
    </ul>
  </div>

  We find that by focusing on key textbook concepts in combination with modeling approach best compress the high-dimensionality of our review. As such, we start by reviewing textbook understanding of groups, before diving into the modern approach to model groups, which can be summarized with networks and agent-based modeling, game theory (evolutionary game theory, common-pool ressource games, public good games), and higher-order networks. We draw from empirical findings, but we don't engage much with them.

  Based on evidence from historical, experimental, and modern thinking about groups, we argue that group-based model should take more space in the toolbox of complex scientists. On the other hand, by formalizing verbal models from the social science with our theoretical works, we hope to help clarify conceptual confusion about the ontology of groups. 
  
  </div>
  <div>
    <center>
    <h4>Timelines</h4>
    <br>
    <div>${selectInput}</div>
    <div>${resize((width) => Plot.legend({marginLeft:width/4, color: {
      domain: ["CGS", "φ", "S", "B", "PS", "P", "O", "IS", "F"], 
      range: ["#001219", "#005F73", "#0A9396", "#94D2BD", "#E9D8A6", "#EE9B00", "#CA6702", "#BB3E03", "#AE2012"]
      }}))
    }</div>
    <div>${resize((width) => lit_review(width))}
    </div>
  </div>
  </center>
</div>


---

<div class="caution">🚧 Everything that follows is WIP 🚧</div>


## Prehistory

In this section, we review classical works on groups in the social sciences. We find that much of early work in sociology works spell out (in words) ideas that are central to the thesis. Similarly, we briefly review work in organizational science on firm selection, which branched out from sociology around the 1940s (Scott & Davis 2007). In the 1950s-1960s, the debate of group selection reveals the challenges and important of models when thinking of "groups" as potential target for natural selection. We also find that work on conformity in social psychology is important to mention. From todays' perspective, we find that the idea of people blindly adhering to the majority and authority was meant to be cautionary tales against communism (CITE). 

### The classical social sciences of groups

- Forefathers in sociology: [Georg Simmel](https://en.wikipedia.org/wiki/Georg_Simmel), [Max Weber](https://en.wikipedia.org/wiki/Max_Weber), [Charles Horton Cooley](https://en.wikipedia.org/wiki/Charles_Horton_Cooley) (1864-1929), [William Graham Sumner](https://en.wikipedia.org/wiki/William_Graham_Sumner), [Herbert Spencer](https://en.wikipedia.org/wiki/Herbert_Spencer) (1820-1903)
- Textbooks: [Introduction to Sociology 3rd edition (Little 2023)](https://opentextbc.ca/introductiontosociology3rdedition/front-matter/about-the-book/), [Cultural Anthropology: The Human Challenge 15th edition(HAVILAND et al. 2015)](https://www.cengage.ca/c/cultural-anthropology-the-human-challenge-15e-haviland-prins-mcbride-walrath/9781305633797/), [How Humans Evolved (Boyd, Silk, Langerbrager 2023)](https://wwnorton.com/books/9781324061748)

The temptation to perceive social groups as having some independence from its constituents has been around for a long time. Already in 1898, George Simmel was arguing that with emerging national identities, "the society, the unified group, is a structure of independent reality, wich leads its life after peculiar laws and by virtue of peculiar forces, independent of all its individual components" (Simmel 1898). According to Simmel, we could argue that corporations have independence from its constituents, because the laws governing groups are qualitatively different from that of individual psychology.

Similarly, Herbert Spencer was proposing around the same year that individuals, through their individual lives, contribute to the life of the "social organism" that is society. Spencer suggested that we tend to think of societies as organism-like due to the "general persistence of the arrangements among their units throughout the area occupied." In both cases, social aggregates are "things," but unlike any others. These "things" possess a certain kind of independence from their constituents under specific conditions. 
  
The organism-like analogy is furthered explored by Donald Campbell (1956). Campbell makes the point that perceiving groups as entities is far from being crazy when we accept that reality is not given, but socially constructed. When a collection of individuals share a common fate, and tend to fly together like a flock of bird, it is natural to perceive this group as having some organism-like properties. 

Textbook definition in sociology, cultural anthropology or social psychology of groups might include different perspectives, types of social groups, and recurrent notions deemed important to the study of groups: 
  - [functionalist, critical, feminist, symbolic interactionist](https://opentextbc.ca/introductiontosociology3rdedition/part/chapter-7-groups-and-organizations/)
  - notions of in- and out-groups
  - group leadership
  - group size
  - norms and formal organizations: at some points groups, adopt norms and rules that make it less fun for the original members. This is often where we shift from social groups to voluntary organizations and institutions.
  - Specialization: some people have specific roles in the groups, which can be formal or not.

<div class="tip">In sociology and anthropology, an important distinction is made between primary groups, which is characterized by intimate, lifelong relationships (think of kins, close friends, romantic partners), and secondary groups, which are characterized by goal-oriented and more temporary relationships. In network science, we would associate secondary groups with long ties, which can be essential to shorter longest paths in a social network.</div>

What you won't find in those textbooks is usually a formal notion of networks. Even though they go all the way back, networks were reserved for a small club of people until the 1990s. Post-1990s era, networks was popularized by  [Faust and Wasserman](https://www.cambridge.org/core/books/social-network-analysis/90030086891EB3491D096034684EFFB8) and the rise of computer programming. Conferences (The Sunbelt) and journals (of the same name) came to be. More departments in the social sciences and humanities started to teach on the topic.

<div class="note">Well known methods in social science using networks to study groups: stochastic actor oriented models (SOAM; Snijders 2010), exponential random graph models (ERGM), etc. They are usually looked down by people from the natural sciences. This doesn't help</div>


## The emerging science of firms and organizations

 - Forefathers in organizational and management science: [Max Weber](https://en.wikipedia.org/wiki/Max_Weber), [Herbert Simon](https://en.wikipedia.org/wiki/Herbert_A._Simon), [R.K. Merton](https://en.wikipedia.org/wiki/Robert_K._Merton), 
 - Forefathers institutional theories: [Ronald Coase](https://en.wikipedia.org/wiki/Ronald_Coase), [Joseph Schumpeter](https://en.wikipedia.org/wiki/Joseph_Schumpeter)
 - Textbooks: [Organizations and Organizing: Rational, Natural, and Open System Perspectives (Scott and Davis, 2007)](https://doi.org/10.4324/9781315663371 ), [Institutions and organizations: ideas, interests, and identities (Scott 2014)](https://uk.sagepub.com/en-gb/eur/institutions-and-organizations/book237665)

Interesting enough, the idea that groups as firms can be subject to selection hasn't been as controversial in management and organizational science than it has been in biology.

Sometimes, sociology and organizational science are hard to distinguish, see [Peter_Blau](https://en.wikipedia.org/wiki/Peter_Blau), [Ronald Stuart Bur](https://en.wikipedia.org/wiki/Ronald_Stuart_Burt) (Burt 2000)[https://www.sciencedirect.com/science/article/abs/pii/S0191308500220091?via%3Dihub], [Paul DiMaggio](https://en.wikipedia.org/wiki/Paul_DiMaggio), [Charles Perrow](https://en.wikipedia.org/wiki/Charles_Perrow), [Oliver E. Williamson](https://en.wikipedia.org/wiki/Oliver_E._Williamson)

## Group selection

In the 1960s, biologists went to war with the idea that groups can be a key level of selection. In his _Animal Dispersion in Relation to Social Behaviour_ (1962), Wynne-Edwards infamously hypothesized that if groups had mechanisms to prevent overexploitation of local resources, such as limiting the number of occupants in the area, they should be able to outcompete groups with more selfish individuals. In evolutionary terms, this idea was translate to having genes that, even though decrease individual fitness, could be selected anyway if they favor group survival.

The idea of groups having a particular ontological status is one that cut deeply across the sciences. In all of them, it remains more or less controversial. A key aspect of the discussion is whether group minds are *reducible* to individual components. Different groups have thought about it in different ways, focusing on different aspect of the questions.

## Do we need a Leviathan or the free market to manage public goods?

Neither, according to Ostrom. Collective action theory is a response to Harding's tragedy of the commons (1960s) that took a live of its own starting in the 1980s. It now cut across many domains. It is about governance and the coevolution of institutional policies and group organization, as well as bringing game-theoric (questions of rationality) notions to the discussion (CITE OSTROM).

## Team science

Better team make more money. Some people say more diverse teams are smarter than homogenous teams. But their definition of teams is kind of sloppy. A set of individuals doesn't make a team (im looking at you bibliometricians). At the same time, it is not nothing.

#### A. Team science in business

Good teams make more money.

#### B. Team science in F/OSS

How do you make teams with people who never met in persons make better softwares than people in companies who are paid to do the same.

#### C. Team science in science

Does more people means better paper?

#### D. Team science in complex systems

Emergence is all around us.

## The return of (cultural) group selection

Hey biologists, maybe groups can be a legitimate level of selection after all. But you need to be enculturated.

## But what are groups?

Do groups can lie? Or have beliefs? What do people mean when they say that groups exist.

## Higher-order networks

Groups redefined.


<div class="note" label="What's coming">
  <small>
      <ul>
        <li>Grontology paper. The main goal here is to get out our philosophy stance on group-based models, informed by network science.</li>
        <li>At the same time, this a synthesis of how different field of studies talk about group stuff.</li>
        <li>The meta-goal is, actually, why do we want philosophy to be informed by HONs? Do these communities are too far away to have something useful to say to each other? Hopefully not, they are talking about the same 'group stuff' (allegedly).</li>
        <li>The paper is geared towards the masses, less math. We offer a whirlwind tour of how physcists and cultural evolutionits think represent groups in their models.</li>
        <li>See <a href="https://jstonge.observablehq.cloud/hello-research-groups/models/gbms">interface sister paper</a> and <a href="https://www.overleaf.com/4292575746rhffnmxxtmmp#9eeb3a">overleaf project.</a></li>
      </ul>
  </small>
</div>


## Appendix

The way we organized our literature review is by putting the field of studies first, then discussing their respective group ontology. There are other ways we could have organized our literature review.

### A story of cooperation and altruism

The main question underlying a few of these fields is that of the evolution of cooperation in human societies. 

 - (1960s) The original group selection sought to explain how altruistic behaviors could best served groups. It was found to be unnecessary, because of kin selection.
 - Ostrom's work (1980s) was a response to Hardin's tragedy of the commons (1960s).
 - Cultural group selection (1980s) is about reversing the idea of selfish individuals, being vehicles for their genes. Humans are hyper-cooperative by nature, leading to different group-based processes by which cooperation among unrelated individuals can emerge in large-scale societies. 
 - Alternative to cultural group selection, altruism can be explained with models of structured populations (Nowak 2005). It wasn't long before the same argument was made on higher-order networks (Perc 2013). 

From this perspective, half of our original categories are about the evolution of cooperation. We are left with:

 - Firms as groups
 - Team science
 - Groups in the social sciences (without evolutionary minded folks)
 - The ontology of groups

<!-- APPENDIX -->



```js
const data = FileAttachment("data/lit_review.csv").csv({typed: true});
```

```js
const data_f = d3.sort(select === 'pinned' ? 
            data.filter(d => pinned_title.includes(d.short_title)) : 
            data.filter(d => d.subfield == select), (a,b) => d3.ascending(a.year, b.year))
```

```js
const selectInput = Inputs.radio(["pinned", "S", "B", "φ", "CGS", "PS", "P", "O", "F"], {value: "pinned", format: x => fos2cat[x] })
const select = Generators.input(selectInput)
```

```js
const fos2cat = {
  "pinned": "Sacred timeline", 
  "S":"Classical social sciences", 
  "B":"Biological group selection", 
  "φ": "Philosophy", 
  "CGS": "Cultural group selection", 
  "P": "HONs", 
  "PS": "Collective action theory",
  "O": "Team science",
  "F": "Organizational science"
}

const pinned_title = ['rice_quantitative_1938', 'warriner_groups_1956', 'campbell_common_1958', 'wynne-edwards_animal_1962', 'neal_duality_2023',   'smith_group_1976', 'okasha_why_2001', 'sterelny_return_1996', 'breiger_duality_1974', 'boyd_culture_1985' , 'ostrom_covenants_1992', 'gilbert_rationality_2006', 'smaldino_cultural_2014' ,'french_collective_1984', 'battiston_physics_2021']
```

```js
function lit_review(width) {
  const linewidth = 20
  return Plot.plot({
          width,
          height: 1200,
          marginBottom: 50, marginTop: 50,marginLeft:20,
          y: { axis: null, reverse: true },
          x: { axis: null, domain: [-200 / 2, 200 / 2] },
          color: {
            domain: ["CGS", "φ", "S", "B", "PS", "P", "O", "F"], 
            range: ["#001219", "#005F73", "#0A9396", "#94D2BD", "#E9D8A6", "#EE9B00", "#CA6702", "#BB3E03"]
            },
          marks: [
            Plot.ruleX([0]),
            Plot.dot(
              data_f, { y: "year", fill: "subfield" }
            ),
            Plot.ruleY(
              data_f,  { 
                filter: (d, i) => (i % 2 === 0), 
                y: "year",   x: 20,  dx: 5,
                }
            ),
            Plot.ruleY(
              data_f,  { 
                filter: (d, i) => (i % 2 !== 0), 
                y: "year",  
                x: -20,  dx: -5,
                }
            ),
            Plot.text(
              data_f,  { 
                y: "year",  x: (d, i) => (i % 2 === 0 ? 6 : -6 ), 
                dy: -5,
                text: (d) => d.year.toString(),
                opacity: (d,i) => data_f[i > 0 ? i-1 : data_f.length-1].year === data_f[i].year ? 0 : 1
              }
            ),
            Plot.text(
              data_f, 
              {
                filter: (d, i) => (i % 2 === 0),
                y: d => d.year, 
                x: 25 , 
                text: d => `${d.title} (${d.short_title}${d.contrib_type})`, 
                textAnchor: "start",
                lineWidth: 23, 
                tip: true,
                title: d => `tldr; ${d.tldr}`
            }),
            Plot.text(
              data_f, 
              {
                filter: (d, i) => (i % 2 !== 0),
                y: d => d.year, 
                x: -25 , 
                text: d => `${d.title} (${d.short_title}${d.contrib_type})`, 
                textAnchor: "end",
                lineWidth: linewidth, 
                tip: true,
                title: d => `tldr; ${d.tldr}`
            }),
          ],
        })
}
```

```js
data
```

<!-- STYLING -->

<style type="text/css">
    
    .margin-note {
        margin: 20px;
        float: right;  /* Align the image to the right */
    }

    p.small {
      font-variant: small-caps;
    }

    div.ridge {
      border-style: groove;
      border-width: 1px;
      padding: 20px;
      width: 75%;
      margin-left: 20px;
    }

    .highlight-red {
        color:  #dc143c;          /* Change the color to red */
        text-decoration: underline; /* Underline the text */
    }
    .highlight-blue {
        color: #1e90ff;          /* Change the color to red */
        text-decoration: underline; /* Underline the text */
    }
    .highlight-green {
        color: #32cd32;          /* Change the color to red */
        text-decoration: underline; /* Underline the text */
    }
    .highlight-purple {
        color: #9370db;          /* Change the color to red */
        text-decoration: underline; /* Underline the text */
    }
    .highlight-coral {
        color: #ff7f50;          /* Change the color to red */
        text-decoration: underline; /* Underline the text */
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

  @import url('https://fonts.googleapis.com/css2?family=Lato&display=swap');

</style>

  <!-- ul {
        list-style-type: disc;
        padding-left: 0px;
    }

  /* Style for the task list */
  .task-list {
        list-style-type: none;
        padding: 10;
    }

  .task-list li {
        margin-bottom: 10px;
        padding: 5px 10px;
        background-color:  #F5F5F5;
        border: 0.01px solid #ccc;
    }

  /* Style for the checkbox */
  .task-list input[type="checkbox"] {
        margin-right: 10px;
    } -->

