```js
const selectInput = Inputs.radio(["pinned", "philosophy", "social sciences", "evolutionary biology", "cultural evolution", "policy studies"], {value: "pinned"})
const select = Generators.input(selectInput)
```

<div>${selectInput}</div>
<div>${resize((width) => 
  Plot.plot({
    width,
    height: 630,
    marginLeft: 140, marginBottom: 50, marginRight: 120, marginTop: 10,
    x: { axis: null },
    y: { axis: null, domain: [-200 / 2, 200 / 2] },
    marks: [
      Plot.ruleY([0]),
      Plot.ruleX(
        data.filter(d => select === 'pinned' && d.pinned ? d : d.type == select), 
        { x: "year", y: (d, i) => (i % 2 === 0 ? 25 : -25)  }),
      Plot.dot(
        data.filter(d => select === 'pinned' && d.pinned ? d : d.type == select), 
        { x: "year", fill: "#fff", stroke: "type" }
      ),
      Plot.text(
        data.filter(d => select === 'pinned' && d.pinned ? d : d.type == select), 
        { x: "year", y: (d, i) => (i % 2 === 0 ? -4 : 4 ), text: (d) => d.year.toString()}
      ),
      Plot.image(
        data.filter(d => select === 'pinned' && d.pinned ? d : d.type == select), 
        { x: d => select === "philosophy" ? d.year : d.year === 2006 ? 1998 : d.year, 
          y: (d, i) => i % 2 === 0 ? 54 : -54,
        src: "link",
        width: data.map(d => select === 'pinned' && d.pinned ? 270 : 200)
      })
    ]
  })
)}
</div>

```js
  Plot.plot({
    width,
    height: 630,
    marginLeft: 140, marginBottom: 50, marginRight: 120, marginTop: 10,
    x: { axis: null },
    y: { axis: null, domain: [-200 / 2, 200 / 2] },
    marks: [
      Plot.ruleY([0]),
      Plot.ruleX(
        data2, 
        { x: "year", y: (d, i) => (i % 2 === 0 ? 25 : -25)  }),
      Plot.dot(
        data2, 
        { x: "year", fill: "#fff", stroke: "type" }
      ),
      Plot.text(
        data2, 
        { x: "year", y: (d, i) => (i % 2 === 0 ? -4 : 4 ), text: (d) => d.year.toString()}
      ),
      Plot.image(
        data2, 
        { x: d => d.year, 
          y: (d, i) => i % 2 === 0 ? 54 : -54,
        src: d => "https://raw.githubusercontent.com/jstonge/hello-research-groups/main/docs/assets/"+d.short_title+".webp",
        width: 200
      })
    ]
  })

```



# Grontology

The social ontology of groups is the enterprise of determining the ontological status, or beingness, of social groups and/or group cognition (Epstein 2024). It brings forth questions about the 'meaning' of groups; what we mean when we say groups exist, whether groups can lie, take actions, or if they can be accoutable for their actions. 

At the center of the discussion, there is the notion of **reducibility** of group minds to individual components. For instance, when we say that a corporation such as Volswagen intententionally lied about their diesel engine emissions, do we mean that the company itself lied or that bad actors within the company lied. Common sense tells us that corporations are not individuals, so they cannot lie. Individuals must be held accountable. 

At the same time, there are innumerable cultural references who like to embody corporations as human beings, as if there is something more about evil corporations than the sum of individual intentionalities (CITE). We defend that this is a conundrum, in that we still lack group-based formalism that allow for some degree of emergence without embracing full blown irreducibility of groups to individuals. We provide such formalism by mapping current philosophical stances we review here on our group-based models. 

There are many sciences have something to say about the social ontology of groups, each bringing their own set of questions that is rooted in their intellectual heritage. We reduce the wide variety of perspectives on the topic to the methods they use to study groups. As such, we have the [4] following pairs: philosophy and verbal models, classical social science and simple networks, linear models, and qualitative science, evolutionary sciences and population biology and game theory, and policy studies and game theory _à la Ostrom_. Obviously, this a a bit caricatural. But we find this perspective help tremendously to what each field of study means by 'group', and how they compare to our group-based formalism.

We first lay the philosophical groundwork for our modeling work, which we introduce in the next section. We hint at other sciences and their methods that inform our philosophical work where it is relevant. 

## The social ontology of groups

<ul class="task-list">
  <li><input type="checkbox">Basic grouping that can be node- or edge-first based on shared property (no interactions; no intentionality)</li>
  <li><input type="checkbox">Intentional groups (reducible; adding mental states)</li>
    <li><input type="checkbox">Non-reducible intentional groups.</li>
</ul>

#### Back to the basics

We like to put marbles, books, or cards that share some quality or feature together. This shared property—color, size, and so—allows for ordering. We call this ordered collection a grouping, or cluster, and they sometime serve a functional goal, such as searching for a good hand in card games. Or it can be purely esthetics, such as organizing books based on color. Philosophers call this grouping 'natural kinds'. Similarly, one can cluster  based on relation of interest. For instance, Mars and Jupiter are similar in that they orbit the sun. Otherwise, they couldn't be more different as planet.

A well-known fact social psychology, is how Western Educated Industrialized Rich and Democratic (WEIRD) societies tend to put individuals, or entities, before interactions. When asked to introspect during the 'Who Am I?' test, psychologists found again and again that WEIRD people define themselves in terms of individual attributes (CITE). In many other cultures, such as Japan, they might define themselves with respect to their relationships, e.g. 'I am Sora's professor' instead of 'I am a teacher'. 

Similarly, we can think of how the [distributional hypothesis](https://en.wikipedia.org/wiki/Distributional_semantics) revolutionized our way to represent text in linguistics. That is, we went from representing text as bag-of-words, where the fundamental units are word counts, to representing text in a continous representations where word coordinates encode the _context_ in which we find the words. This shift allowed us to have a less WEIRD representation of text where from coordinates alone, we could extract semantic relationships, e.g. 'the hammer is to the nail as the screwdriver is to the screw'.

We can build networks out of these interactions because we now have a notion of nodes and edges. Until recently, researchers in network science did not realize how useful it is to adopt edge-first view; clustering on links lead naturally to the idea of hierarchy (groups part of groups) and overlapping communities (I am both a teacher and a father) (CITE Bagrow ?). [EXPLAIN].

#### Intentional groups

The components involved in interactions may or may not involve intentionality. Intentional agents possess mental states. The same grouping can be interepreted with or without intentionality. For example, a group of sperm whales can be classified based on shared features without considering whether they are intentional agents. They are groups by virtue of sharing some features, such as feeding and migration behaviors, size, or communicating via echolocation and vocalization. 

However, recent studies have shown that sperm whales have a matrilineally based social organization, meaning that males tend to leave the clans while female offsprings stay with their moms (CITE whitehead). Moreover, groups who are tightly knit might develop accent when vocalizing, distinguishing between in groups and out groups. When groups depend on intentionality and a share identity, there is a sense where individuals have mental states that can tell whether they are part of the group or not. The young males "believe" they are not part of their mothers' group when they come to age, not unlike how traditional matrilineal societies work in humans. 

<div class="note">In sociology and anthropology, an important distinction is made between primary groups, which is characterized by intimate, lifelong relationships (think of kins, close friends, romantic partners), and secondary groups, which are characterized by goal-oriented and more temporary relationships. In network science, we would associate secondary groups with long ties, which can be essential to shorter longest paths in a social network.</div>

<div class="note">Well known methods in social science using networks to study groups: stochastic actor oriented models (SOAM; Snijders 2010), exponential random graph models (ERGM)</div>

#### Non-reducible, intentional groups

A group becomes irreducible to its constituents when group membership is conditional on each other's beliefs.

<!-- #### Intentionality and unit of adaptation

<ul class="task-list">
  <li><input type="checkbox">How does group as unit of adaptation is connected to non-reducible groups</li>
</ul>

Non-reducibility is at the heart of the original debate on the evolution of groups in biology in the 1960s. Wynne-Edwards put forth the idea that groups could be a unit of adaption. That some behaviors could serve for the benefit of the groups such as individual reulating  -->

## The social science and its relationship to evolutionary science


<ul class="task-list">
  <li><input type="checkbox">Sociologists inheriting from Simmel vs evolutionary thinkers</li>
</ul>

Textbook definition in sociology, cultural anthropology or social psychology of groups might include different perspectives, types of social groups, and recurrent notions deemed important to the study of groups: 
 - [functionalist, critical, feminist, symbolic interactionist](https://opentextbc.ca/introductiontosociology/chapter/chapter6-groups-and-organization/)
 - notions of in- and out-groups
 - group leadership
 - group size
 - norms and formal organizations: at some points groups, adopt norms and rules that make it less fun for the original members. This is often where we shift from social groups to voluntary organizations and institutions.
 - Specialization: some people have specific roles in the groups, which can be formal or not.


## Pragmatic approach to the studies of groups

<ul class="task-list">
  <li><input type="checkbox">What is the grontology pragmatic approach</li>
  <li><input type="checkbox">Why do we care?</li>
</ul>

Policy studies can be characterize in terms of tragedy of the commons, governance and the coevolution of institutional policies and group organization, as well as bringing game-theoric notions to the discussion (CITE OSTROM).


## Commented bibliography

 - [Stanford Encyclopedia of Philosophy's entry on Social Ontology (§ Social Groups)](https://plato.stanford.edu/entries/social-ontology/#KeyDomaAddrSociOnto): Great introduction to the philosophical enterprise that is the study of social ontology; what it is and why do we care. 


```js
const data = FileAttachment("./data/grontology.json").json();
```

```js
const data2 = FileAttachment("./data/group_selection_in_biology.csv").csv();
```

```js
data2
```

<!-- STYLE CSS -->


<style type="text/css">

.focus {
  color: var(--theme-foreground-focus);
  border-radius: 8px;
  margin: 1rem;
  box-shadow: 0 0 0 0.75px rgba(128, 128, 128, 0.2), 0 6px 12px 6px rgba(0, 0, 0, 0.4);
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

@import url('https://fonts.googleapis.com/css2?family=Lato&display=swap');

 ul {
        list-style-type: disc;
        padding-left: 20px;
    }

/* Style for the task list */
    .task-list {
        list-style-type: none;
        padding: 0;
    }

 .task-list li {
        margin-bottom: 10px;
        padding: 5px 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

/* Style for the checkbox */
     .task-list input[type="checkbox"] {
        margin-right: 10px;
    }
</style>

