# Group-based models

In this notebook, our goal is to bridge the gap between the ontology of social groups and higher-order representations of groups.

<div class="note" label="Interface paper - guideline">
<small>
    <ul>
        <li>Editorial paper for physicists. The main goal here is to get physicists minimally interested in philosophy of groups (and perhaps causation).</li>
        <li>In the process, we explain why people in HONs conflate group structure and group non-reducible interactions (literature on contagion).</li>
        <li>The meta-goal is, actually, why do we want HONs to be informed by philosophy? Do these communities are too far away to have something useful to say to each other? Hopefully not, they are talking about the same 'group stuff' (allegedly). We'll see, for now we seek to map group-based models on Randall's typology. </li>
        <li>We give the minimal picture of philosophy of groups, while showing the maths of the different group-based models.</li>
        <li>Optionally, we leave space to integrate <em>casusation</em> into the mix. It feels that this is a promising way to explain the meaning group existence; groups exist inasmuch that they cause individual to behave in such or such way.</li>
        <li>See <a href="https://jstonge.observablehq.cloud/hello-research-groups/grontology">grontology sister paper</a> and <a href="https://www.overleaf.com/project/65917775b218bbec87f59521">overleaf project (need permissions).</a></li>
    </ul>
</small>
</div>

## I. Introduction

<div class="margin-note">
    <img src="https://raw.githubusercontent.com/jstonge/hello-research-groups/main/docs/assets/HenslinCh5.webp" alt="Trulli" width=400px style="box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
    <center>
    <figcaption>A typical introduction to social groups,<br>from the Essentials of Sociology (13th Ed. by James M. Henslin).</figcaption>
    </center>
</div>


The study of social groups is central to the humanities and social sciences. Introductory texbooks describe how groups have key functional roles in explaining a wide ranging of phenomena such as wars, markets, kinship systems, individual psychology and so on. These textbooks propose a typology of groups, and set of hypotheses, derived from their respective tradition. In this context, philosophers have sought to subsume the wide variability of group typologies under a set of essential dimensions in the study of social ontology of groups (SOGs). However, the social sciences mostly lack network models describing mechanisms by which groups emerge and come to drive human behaviors.

In recent years, the study of the structure and dynamics of pairwise interactions in network science has evolved to include higher-order networks (HONs). As with SOGs, network scientists aim to define emergent group-level phenomena or traits that are considered irreducible to their individual constituents. Yet, both HONs and SOGs rarely, if ever, interact at the ontological level, or in discussions concerning the existence of (social) groups as entities independent from the individuals that constitute them.

In this paper, we aim to better understand the intersection of SOGs and higher-order representations to facilitate interdisciplinary works. We relate key assumptions from the philosophy of groups and the higher-order representations formulated by network scientists. To do so, we map higher-order representations onto essential dimensions of groups as identified by philosophers. We hope that by mapping core assumptions within both perspectives we can facilitate interdiscplinary works of qualitative and quantative researchers interested in group-structured systems. We find that there is still much work to be done to formulate a transciplinary view of group-level behaviors.

<ul class="card task-list">
  Todo<br><br>
  <li><input type="checkbox"><em>Context</em>: Social sciences and philosophy talk a lot about groups, but they don't really model them. Physicists only recently started to model groups via higher-order networks, but they didn't engage seriously with the philosophy of groups.</li>
  <li><input type="checkbox"><em>Goal</em>: Showing why it is useful to relate how different communities (social ontology of groups, physics, cultural evolution) think about group irreducibility.</li>
</ul>


## II. The philosophy of groups

<ul class="task-list">
  <li><input type="checkbox">Simple grouping based on shared features (node or edge)</li>
  <li><input type="checkbox">Intentional groups</li>
  <li><input type="checkbox">Interacting intentional groups</li>
  <li><input type="checkbox">Non-reducibly interacting intentional groups</li>
</ul>

In social ontology of groups (SOGs), philosophers highlight key conditions to talk about group-level properties, such as group beliefs, or rationality. One of they key arguments is about collective intentionality, or how groups can entertain collective propositional beliefs that are not the sum of individual beliefs. In this section, we identify the essential dimensions in SOGs that make groups irreducible to its constituents.


### A typology of groups

<span style="font-variant: small-caps;">Natural kinds</span> represent groupings of entities that reflect the natural state of the world. These entities form groups based on a shared _property_ of interest. These groupings emerge from nature itself, rather than being mere constructs of the mind. This conception of groups underpins the intuitive belief that certain shared properties, for example, bind cetaceans into the category of whales. Natural kinds extends to cultural artifacts, such as 'K-pop' originated from South Korea. Similarly, entities can come together through a shared relations of interests.

We next model a situation where <span style="font-variant: small-caps;">interactions</span> are enough to determine groups. 

After adding interactions, we have <span style="font-variant: small-caps;">intentional groups</span>, where a collection of agents form a group based on the beliefs of some shared relationships or properties of interest.

We distinguish between groups who believe to have some shared properties from groups that maintain individual beliefs about what the groups want. In this case, the interactions between intentional agents lead to something different; groups is interacting based on what is going in the mind of its constituents.

The riot is a case of (spontaenous) collective intentionality, where a crowd emerge from a set of individuals believing that they are in "it" together. Supported by developmental psychology and cultural evolution, humans have been shown to have peculiar abilities of shared intentionality, that make us capable of acting as an impersonal "we". 

From this impersonal shared intentionality, it is possible to have <span style="font-variant: small-caps;">non-reducible interacting groups</span>; one in which group membership, and the emergent collective intentionality, arises from a set of individuals bootstraping their (mutual) beliefs into the idea that they form a social group. The group is the product of a set of interactions, 

### Groups as causation

<ul class="task-list">
  <li><input type="checkbox">A causal view of non-reducible interacting groups</li>
</ul>

Another way to formalize the idea the existence groups exist is by saying that groups _cause_ particular individual behaviors. For instance, we could say that a crowd caused a riot after the Canuck's hockey team lost the 2012 Stanley Cup final. WEIRD people ought to dislike, or reject, the idea of a crowd causing individuals riot, as individual agency is one of the cornerstone of Western societies. Yet, in a documentary on the topic, people were asked what happened that day. In many cases, they will answer that they didn't have the intention to riot. 

Drawing from structural causal models, we say that groups is a direct cause of a behavior $Y$ if the group appears in the function that assigns $Y$'s value.

When the joint beliefs of belonging lead to group intentionality, this can lead to groups _causing_ individual to behave in all sorts of ways. 

We explored philosophical perspectives on what it means for a group to lie, be rational, and, more broadly, to exist. We provided a typology inspired from SOGs to define what is meant by non-reducible groups. How does key assumptions in the philosophy of groups relate to that of higher-order networks? 

### Group-level traits

<ul class="task-list">
  <li><input type="checkbox">A mutliscale, evolutionary perspective on groups</li>
  <li><input type="checkbox">Explain how can we have group selection while individuals being target of evolution</li>
  <li><input type="checkbox">How can known gruoup structural differences from CGS can be mapped onto Randall's typology</li>
</ul>

Yet another way in which we can talk of groups influencing behavior is to frame the aggregate of particular individual behaviors as group-level traits. This supplement aforementionned perspective in that it is something that has evolved; groups who are best able to coordinate on large-scale, causing unrelated individuals to cooperate can be selected.


## III. The structure and dynamics of higher-order networks

We first provide a whirldwind tour of modeling the structure and dynamics of group-structured systems. We highlight [4] critera under which cliques, and their dynamics, are better represented as higher-order interactions; _reducibility_, _persistence_, _isolation_, and _alignment_. But first, what are higher-order representations?


### Higher-order representations

<div class="margin-note">
    <center>
    <img src="https://raw.githubusercontent.com/jstonge/hello-research-groups/main/docs/assets/McPherson1982.webp" alt="Trulli" width=400px>
    <figcaption>Figure 1. McPherson 1982. The caption reads: <br>"Each row represents an individual. Each column represents an organization.<br>The rowsums are the total number of affiliations for the given individual.<br>The column sums are the organizational sizes."<br>Higher-order structure always reduce to a simple bipartite graph,<br>but not all bipartite graph represent higher-order interactions.</figcaption>
    </center>
</div>

In social network analysis (SNA), groups generally refers to known social structures, such as cliques, clubs, teams, and organizations. These are often represented as two-mode networks where groups as represented as second type of nodes. 

SNA researchers typically focus on the relationships between social networks and groups, e.g. how social connections can predict group memberships (Neal 2022), the impact of cliques on power dynamics (as with the Medici). In many cases, groups are thought to give rise to pairwise social networks, or networks restricted to dyadic interactions, but then social networks are generally studied on their own. This meaning of groups is referred to the **dual view** of social networks.

Let the clubs or else denoted with $m$, which the size 

<ul class="task-list">
  <li><input type="checkbox">Explain why higher-order representations in themselves are not sufficient to give rise to higher order effects.</li>
  <li><input type="checkbox">Explain the relationship between group-based models and bipartite projection using the above features</li>
</ul>

In themselves, this dual view of social networks is not sufficient to give rise to group effects. 

### Irreducibility, persistence, isolation, and alignment

<img src="https://raw.githubusercontent.com/jstonge/hello-research-groups/main/docs/assets/drawing.svg" alt="Trulli" class="margin-note" width=300px>

<ul class="task-list">
  <li><input type="checkbox">Reducibility</li>
  <li><input type="checkbox">Persistency</li>
  <li><input type="checkbox">Isolation</li>
  <li><input type="checkbox">Alignment</li>
</ul>

_Irreducibility_ 

Group-based models formalize the notion of group effects, by definition  _irreducible_ to its pairwise interactions, as higher-order interactions. In this case, we jointly study the effect of groups and individuals within the same system. In contagion studies, for example, we can think of the coevolution of group behaviors, such as groups imposing policies to limit the spread of contagion, and how individuals might react to group interventions. 

_Persistence_ 

Groups are differentiated in terms of persistence; shared interactions with random individuals at the mall is very different than individuals bumping repeatedly into each other in a household.

_Isolation_ 

This is an old idea that the way in which group collide give the tone for in/outgroup dynamics. In biology, demes were defined by the fact that they were isolated from one another. In cultural anthropology, the idea that groups can be unit of adaptation stems from that of maintaining variation within groups. If groups are too similar, you can't have selection.

_Alignment_

Alignment is about groups behaving for their own good, regardless of individual intentionalities.


### Higher-order dynamics on and of networks

<ul class="task-list">
  <li><input type="checkbox">Homogenous mean-field vs approximate master equations</li>
  <li><input type="checkbox">Conflating higher-order networks with nonlinear effects in the dynamics.</li>
</ul>

With both these definition out of the ways, we distinguish different line of works even within the physics of higher-order networks. 

<!-- To keep up with our coauthorship example, say that we are interested in modeling the group-based dynamics of unsound research methods in science that still result in publications. Groups in the above schema represent sets of coauthors that are "susceptible" or "infected" individuals to unsound methods (example borrowed from Smaldino 2016).  -->


#### Homogenous mean-field on HONs

<div class="margin-note">
    <img src="https://raw.githubusercontent.com/jstonge/hello-research-groups/main/docs/assets/battiston2021.webp" alt="Trulli" width=400px>
    <center>
    <figcaption>Schematics of mean-field approximation on higher-order networks.</figcaption>
    </center>
</div>

<ul class="task-list">
  <li><input type="checkbox">Spread across groups with nonlinear effects within groups (bodo_sis_2016; reviewed by arruda_contagion_2024).</li>
  <li><input type="checkbox">How are they reducible, permanent, and isolated. </li>
</ul>

Conflate higher-order networks with the nonlinear effects in the dynamics (aka being able to decompose the dynamics within every clique into a combination of pairwise dependencies, then the network is just a pairwise network with cliques, or fully reducible. Alternatively, clique is better represented as an inseparable entity like a hyperedge)


#### Group-based master equations (GMEs)

<div class="margin-note">
    <img src="https://d3i71xaburhd42.cloudfront.net/78f3dc203b1ef17e35ef0321f85656de69884c48/1-Figure1-1.png" alt="Trulli" width=400px>
    <center>
    <figcaption>Schematics of group-based master equations.</figcaption>
    </center>
</div>

<ul class="task-list">
  <li><input type="checkbox">dufresne_propagation_2010</li>
  <li><input type="checkbox">nonlinear effect spread across groups (osullivan_mathematical_2015)</li>
  <li><input type="checkbox">Distinguishing group-based dynamics (nonlinear, complex and higher-order contagion) from a node-based one (nonlinear, complex and first-order contagion) (burgio_adaptive_2023)</li>
  <li><input type="checkbox">st-onge_master_2021</li>
</ul>

In group-based AMEs (GMEs) which compress networks based on the states of nodes within cliques or groups. In doing so, we break down large systems in subsystems and coarse-grain the systems of a set of master equations. Coarse-graining is based on well-defined groups like fully connected cliques and on the states of nodes they contain. Groups are very loosely defined in that formalism. Since we are talking of contaion in a general sense, individuals sharing a ventilation system within a building counts as groups given that this grouping has an impact on the spread of unwanted pathogen. 

GMEs are group-based models in that higher-order interactions cannot be decomposed into simpler pairwise interactions. Membership distribution gm and group size distribution pn are two quantities from which we take expected values. The average excess group size, i.e., the average number of neighbors this node has in that group, is 〈n(n − 1)〉/〈n〉.


<div class="box-container">
    <div class="box">
        <div class="box-title">Box 1: Mathematical models of ephemeral and persistent groups</div>
        <div class="box-content">
            <p>Many popular models of higher-order networks account for groups in a mean-field manner. Meaning that they consider the average state of all possible groups. Consider the simple case where something is spreading across groups (an epidemic, cooperation, an idea or a meme) such that individuals are either in a susceptible or infectious state. A mean-field description might track the fraction of infectious individuals ${tex`i`} like so
            </p>
            <center>
            ${tex`\frac{d}{dt}i = -\alpha i + \sum_{s=2}^{\infty} \sum_{k=0}^{s} \binom{s}{k} i^k (1 - i)^{s-k} (s-k) \beta(s,k)`}
            </center>
            <p>
            Explain.<br> 
            This description is equivalent to an <em>annealed</em> structure where all possible groups exist and are shuffled infinitely fast. Therefore, models of this kind consider fully ephemeral groups with no persistence as they do not capture structural or dynamical correlations within groups. To account for persistent groups, we must at least account for correlations within groups as the duration of a group interaction induces correlations across the state of its members. We might therefore use master equations that the probability distribution ${tex`G_{s,i}`} that a group of size ${tex`s`} is in a state with any discrete number ${tex`i`} of infectious individuals between 0 and ${tex`s`}. This distribution evolves according to
            </p>
            <center>
            ${tex`\frac{d}{dt}G_{s,i} = -\alpha i G_{s,i} - \beta(s, i)(s - i)G_{s,i} + \alpha(i + 1)G_{s,i+1} + \beta(s, i - 1)(s - i + 1)G_{s,i+1}`}
            </center>
            <p>Explain.</p>
            </div>
        </div>
    </div>
</div>

## IV. Where philosophy meets higher-order networks

<ul class="task-list">
  <li><input type="checkbox">Why is philosophy and the social sciences and physics of HONs should constrain each others?</li>
  <li><input type="checkbox">Physics is too far away to inform philosophy.</li>
  <li><input type="checkbox">Philosophy is too unbounded to inform physics of HONs.</li>
  <li><input type="checkbox">Is collective intentionlity useful for modeling social groups?</li>
</ul>

Now that we have formalize how physicists think of higher-order interactions, we seek bring together a bit closer the philosophy of groups with GMEs. Philosophers argued for the importance of collective intentionality to achieve non-reducible interacting groups. Yet, phycists talk of higher-order interactions that are irreducible to pairwise interactions. 


## V. Discussion

<ul class="task-list">
  <li><input type="checkbox"><em>Big claim I never know where to put</em>: group-based models are useful because we coarse-grained a system into a natural level to explain human behaviors. This runs against our (WEIRD) biases of favoring individuals, or nodes, over groups</li>
</ul>

Famous last words.










## Appendix 

### Scale-free networks

<!-- In this view, **persistence** means that coauthors who keep working together on papers as a group is impacting the probability of adoption of individuals to unsound methods. This is non-reducible to pairwise coauthorships in that there might be non-linear effects of infection _within_ groups. -->

For instance, letting _n_ in the schema above to be group size, we can see transmission rate is controlled by scaling exponent ${tex`\nu`} that changes with respect to group size:

```js
const infection = function(x, nu, beta) {
    return beta*x**(-nu)
}
```

<div>${resize((width) => 
    Plot.legend({width:width/4,
    color: {
        range: ["limegreen", "black", "red",], 
        domain: ["ν=0.5", "ν=1", "ν=2"]
    }}))
}</div>
<div>${
    Plot.plot({
    height: 300,
    width: 450,
    x: {label: "group size"},
    y: {label: "infection rate"},
    grid: true,
    marks: [
        Plot.lineY([...Array(20).keys()].map(x => infection(x, 2, 0.1)), {stroke:"red"}),
        Plot.lineY([...Array(20).keys()].map(x => infection(x, 1, 0.1))),
        Plot.lineY([...Array(20).keys()].map(x => infection(x, 0.5, 0.1)), {stroke: "limegreen"})
    ],
    caption: "β fixed at 0.1"
})
}
</div>


<!-- <ul class="task-list">
  <li><input type="checkbox">Claim 1: Conflate higher-order networks with the nonlinear effects in the dynamics (aka being able to decompose the dynamics within every clique into a combination of pairwise dependencies, then the network is just a pairwise network with cliques, or fully reducible. Alternatively, clique is better represented as an inseparable entity like a hyperedge)</li>
  <li><input type="checkbox">Claim 2: Group does not depend on exact knowledge about the state of non-members (contra Gleeson). The non-linear effects have to be within the group and not spillover to other groups.</li>
</ul> -->



<style type="text/css">
    .margin-note {
        margin: 20px;
        float: right;  /* Align the image to the right */
    }

    p.small {
      font-variant: small-caps;
    }

    ul {
        list-style-type: disc;
        padding-left: 0px;
    }

    .task-list {
        list-style-type: none;
        padding: 10;
    }

    .task-list li {
        margin-bottom: 10px;
        width: 470px;
        padding: 5px 10px;
        background-color:  #F5F5F5;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    .task-list input[type="checkbox"] {
        margin-right: 10px;
    }

    /* MATHEMATICS BOX */

    .box-container {
        padding: 10px; /* Padding around the box */
        max-width: calc(70% - 2rem);
    }

    .box {
        border: 1px solid #333;
        border-radius: 8px;
        padding: 20px;
        background-color: #f9f9f9;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px; /* Added margin around the box */
        width: 100%;
        box-sizing: border-box;
    }

    .box-title {
        background-color: #333;
        color: #fff;
        padding: 10px;
        border-radius: 6px 6px 0 0;
        font-weight: bold;
    }

    .box-content {
        padding: 20px;
    }

</style>
