# Multiverse literature review

## Groups are real.

We review the study of groups in the multiverse of scientific research. There are an infinite number of ways to talk about groups. We could simply talk about the grouping of stuff, or how the structure of living systems are determined by that of social organizations. To review the literature, we ask ourselves the following questions:

<div class="callout-box">
  <ul>
      <li>Who argued for the reality of groups?</li>
      <li>What was their underlying ontology, or motives? Did they believe that group interactions were somehow irreducible to individuals.</li>
      <li>What was their modeling approach?</li>
  </ul>
</div>

<div class="grid grid-cols-2">
  <div>

  **Groups in the social sciences**. By the social sciences, we mean those fields interested in humans that are theory-driven, claiming the legacy of their forefathers. They traditionally relied on verbal models and experiments. We put in this bucket conformity studies and group psychology (Asch et al), sociologists drawing from Georg Simmel, and evolutionary minded sociologist and philosophers such as Donald Campbell, David Hull, Bill Wimsatt, etc. We also include sociologists and anthropologists who got into social network analysis. 


  **Group selection in Biology**: That was controversial. In the 1960s, the idea of groups as legitimate level of selection was put forth by Wynne-Edwards. That traits can evolve not in the service of individuals, but because they are benefitial to the groups (early on, it was in terms of population regulation). Biologists went to war with that idea. For many, the collective response was disproportionate (it feels it has something to do with the era). It came back later on, but mostly in terms of multilevel selection theory.
  
  **Firms  as groups**: Organizational scientists, especially those interested in firms ([Richard Scott](https://www.taylorfrancis.com/books/mono/10.4324/9781315663371/organizations-organizing-richard-scott-gerald-davis), ...). They can be evolutionary minded people, speaking of firm selection. They could be classified as a social science; they trace back their origins to some forefathers (Schumpeter, Ronald Coase) and often rely on elaborate concepts. But I feel this community like to be on their own.
  
  **Public Good Games**: It all started with Eleanor Ostrom arguing that small social groups can self-organize to maintain common-pool ressources, thereby avoiding the infamous tragedy of the commons. They even do so better than some centralized governments or the free markets. But N-persons games, with repeated interactions, is also tied to evolutionary game theory. Folks from cultural group selection and statistical physics used extensively dieas of public good games in the context of altruism and cooperation. Truth be told, they could be separated from Ostrom's stuff, and Ostrom's lore is big enough that it could live on its own.

  **Team science**: Starting in the 80-90s, folks from management science and business slowly understood that efficient teams can be more productive. Since then, this idea has been applied to many domains; businesses, but also sport teams, research groups, [software developpers](https://books.google.ca/books/about/Beautiful_Teams.html?id=Na3-vt2ZiPEC&source=kp_book_description&redir_esc=y), and so on. It also became more complex system sciency (with [Scott Page](https://press.princeton.edu/books/paperback/9780691191539/the-diversity-bonus?srsltid=AfmBOop_GYlMKlnwG6cBj9WV8DxAWslY77RTreJR9IfyjrjKMywyv8pT), and other SFI folks). All teams are groups but not all groups are team. Teams are more synergestic, they say.
  
  **Cultural group selection**: This is still controversial, but hasn't been shut down completely by biologist (it partly lives as a social science). It is population biology applied to cultural groups, with the idea that cultural groups could be a legitimate level of selection. That said, defend themselves by arguing for multilevel selection theory; you can take a dual view and have it both ways. 

  **The Ontology of Groups**: Philosophers of collective action theory, social ontology, and collective intentionality. We include Tomasello's work on shared intentionality into the mix. 
  
  **Groups as higher-order networks**: This is antipode of the social sciences. You start from the methods in complex systems, then you just applied to any domain you deem fit. This is our niche. This is a category that is model-first, then concepts come after. As such, groups has been mapped onto models of higher-order itneractions, without much philosophy involved.

  In the theoretical work of this thesis, we seek to inform contemporary group-based models based on higher-order networks with the following facets of groups that cut across these communities:
 - `isolation`: do groups communicate? What is the influence of inter-group interactions.
 - `persistence`: many-body interactions are group momentarily in time. They fundamentally differ from groups that persist in time in that persistent groups can exhibit institutional reality. One might think that repeated many-body interactions is entangled with the evolution of stronger institutions.
 - `irreducibility`: what kinds of group interactions cannot be reduced to the sum of individual, or pairwise, interactions.
 - `alignment`: given group-interactions are irreducible, what does it says about the alignment of individual intentionalities with that of the group minds. How does governance and institutionalization play into that?
 - `differentiation`: with persistent, irreducible, and misaligned groups, we find that individuals are often differentiated in the groups. One key aspect of differentiation is hierearchy and the role of leadership.

  Based on evidence from historical, experimental, and modern thinking about groups, we argue that group-based model should take more space in the toolbox of complex scientists. On the other hand, by formalizing verbal models from the social science with our theoretical works, we hope to help clarify conceptual confusion about the ontology of groups. 
  
  How exactly is what we want to review next. 

  </div>
  <div>
    <center>
    <h4>Timelines</h4>
    <br>
    <div>${selectInput}</div>
    <div>${resize((width) => Plot.legend({marginLeft:width/4, color: {
      domain: ["CGS", "φ", "S", "B", "PS", "P"], 
      range: ["#32cd32", "#dc143c", "#1e90ff", "#32cd32", "#9370db", "#ff7f50"]
      }}))
    }</div>
    <div>${resize((width) => lit_review(width))}
    </div>
    <br>
    <div class="ridge">
    <small>${summaries[select]}</small>
    </div>
  </div>
  </center>
</div>


---

<div class="caution">🚧 Everything that follows is WIP 🚧</div>


## The social sciences of groups

The temptation to perceive social groups as having some independence from its constituents has been around for a long time. Already in 1898, George Simmel was arguing that with emerging national identities, "the society, the unified group, is a structure of independent reality, wich leads its life after peculiar laws and by virtue of peculiar forces, independent of all its individual components" (Simmel 1898). According to Simmel, we could argue that corporations have independence from its constituents, because the laws governing groups are qualitatively different from that of individual psychology.

Similarly, Herbert Spencer was proposing around the same year that individuals, through their individual lives, contribute to the life of the "social organism" that is society. Spencer suggested that we tend to think of societies as organism-like due to the "general persistence of the arrangements among their units throughout the area occupied." In both cases, social aggregates are "things," but unlike any others. These "things" possess a certain kind of independence from their constituents under specific conditions. 
  
The organism-like analogy is furthered explored by Donald Campbell (1956). Campbell makes the point that perceiving groups as entities is far from being crazy when we accept that reality is not given, but socially constructed. When a collection of individuals share a common fate, and tend to fly together like a flock of bird, it is natural to perceive this group as having some organism-like properties. 

Textbook definition in sociology, cultural anthropology or social psychology of groups might include different perspectives, types of social groups, and recurrent notions deemed important to the study of groups: 
  - [functionalist, critical, feminist, symbolic interactionist](https://opentextbc.ca/introductiontosociology/chapter/chapter6-groups-and-organization/)
  - notions of in- and out-groups
  - group leadership
  - group size
  - norms and formal organizations: at some points groups, adopt norms and rules that make it less fun for the original members. This is often where we shift from social groups to voluntary organizations and institutions.
  - Specialization: some people have specific roles in the groups, which can be formal or not.

<div class="tip">In sociology and anthropology, an important distinction is made between primary groups, which is characterized by intimate, lifelong relationships (think of kins, close friends, romantic partners), and secondary groups, which are characterized by goal-oriented and more temporary relationships. In network science, we would associate secondary groups with long ties, which can be essential to shorter longest paths in a social network.</div>

What you won't find in those textbooks is usually a formal notion of networks. Even though they go all the way back, networks were reserved for a small club of people until the 1990s. Post-1990s era, networks was popularized by  [Faust and Wasserman](https://www.cambridge.org/core/books/social-network-analysis/90030086891EB3491D096034684EFFB8) and the rise of computer programming. Conferences (The Sunbelt) and journals (of the same name) came to be. More departments in the social sciences and humanities started to teach on the topic.

<div class="note">Well known methods in social science using networks to study groups: stochastic actor oriented models (SOAM; Snijders 2010), exponential random graph models (ERGM), etc. They are usually looked down by people from the natural sciences. This doesn't help</div>


## Do groups can be a level of selection

In the 1960s, biologists went to war with the idea that groups can be a key level of selection. In his _Animal Dispersion in Relation to Social Behaviour_ (1962), Wynne-Edwards infamously hypothesized that if groups had mechanisms to prevent overexploitation of local resources, such as limiting the number of occupants in the area, they should be able to outcompete groups with more selfish individuals. In evolutionary terms, this idea was translate to having genes that, even though decrease individual fitness, could be selected anyway if they favor group survival.

The idea of groups having a particular ontological status is one that cut deeply across the sciences. In all of them, it remains more or less controversial. A key aspect of the discussion is whether group minds are *reducible* to individual components. Different groups have thought about it in different ways, focusing on different aspect of the questions.

## Firm selection

Interesting enough, the idea that groups as firms can be subject to selection hasn't been as controversial in management and organizational science than it has been in biology.

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
const summaries = {
  'pinned': 'todo 🚧',
  'CGS': 'Drawing from population bioglogy, cultural group selection theory uses a mix of covariance genetics and game theory to demonstrate the conditions under which group-benefitial traits could evolve under group selection proces. The theory emerge from debates in the 1960s about altruism, and how reciprocity is thought to not be sufficient to explain observed large-scale cooperation among unrelated individuals. The key result motivating group selection is the Price equation, applied to groups of individuals having norms that maintain between group-variance, while reducing within-group cultural variations.',
  'φ': 'Collective intentionality is about explaining our feeling that there is something more about collective than the sum of individual intentionalities; it is the idea that friends walking together is more than the individual intending to walk together. There is a "we", as Searly puts it, that feels like is not explainable in terms of individual actions. Another way to put it is that feeling of impersonal "we" that members of societies can have, one in which that nobody knows exactly what it is but nonetheless play an active role in motivating people; such as going to war, or feeling pride when local sport teams win the championship.',
  'S': 'This collection is a frankeinstein of different social sciences talking about the role of groups, each from their own research tradition (e.g. organizational science, sociology, psychology, anthropology). They share the common feature of traditional social sciences; no strong mathematical models to quantify the mechanisms underlying their verbal models, or theories. As such, we end up with an infinity of concepts that describe what are groups and institutions, but no common ground to investigate if each of the social science speaks about the same thing or not.',
  'B': 'todo 🚧',
  'PS': html`<span class="highlight-purple">Collective action theory</span> is derived from Elinor Ostrom's views of social dilemmas, and is typically characterized by its used of public good games. Although it informed by the social sciences, we find that they state a disting set of questions that is important to the study of groups and unique to that literature. The key idea of that literature is how groups can self-govern themselves in the face of a social dilemmas, under particular conditions. Groups can evolve set of rules to prevent the tragedy of the commons, they are not as 'mindless' as once thought. That being said, this literature is often characterized by smaller groups, in which there is a sense of joint commitment toward the common-pool resources.`,
  'P': 'todo 🚧'
}
```

```js
const data_f = d3.sort(select === 'pinned' ? 
            data.filter(d => pinned_title.includes(d.short_title)) : 
            data.filter(d => d.subfield == select), (a,b) => d3.ascending(a.year, b.year))
```

```js
const selectInput = Inputs.radio(["pinned", "S", "B", "φ", "CGS", "PS", "P"], {value: "pinned", format: x => fos2cat[x] })
const select = Generators.input(selectInput)
```

```js
const fos2cat = {
"pinned": "Sacred timeline", "S":"Classical social sciences", "B":"Biological group selection", "φ": "Philosophy", "CGS": "Cultural group selection", "P": "HONs", "PS": "Collective action theory"}

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
          color: {domain: ["CGS", "φ", "S", "B", "PS", "P", "O", "Ψ"], range: ["#32cd32", "#dc143c", "#1e90ff", "#32cd32", "#9370db", "#ff7f50", "#ff7f50", "#ff7f50"]},
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

