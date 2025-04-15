# Defining and classifying models of groups: The social ontology of higher-order networks

>_This chapter presents a series of group-based models, each built on progressively stronger ontological commitments about the nature of social groups. As a standalone paper, it includes a condensed version of the history of groups from the introduction. Readers already familiar with that material may wish to skip the section §[1.2](#interface.section.review){reference-type="ref" reference="interface.section.review"}._

>_We show how the dimensions of coupling, persistence, reducibility, and alignment can be expressed through network modeling assumptions. While higher-order networks (HONs) emphasize multi-way interactions, they often rely on the annealed assumption--where group configurations shift faster than the dynamics--capturing mostly ephemeral, isolated groups. We offer one direction in which group-based models can be broadened to encompass a diversity of ontological commitments. By assuming a fixed or slowly changing (quenched) topology, we can model persistent groups and capture coupling between them. Building on this, we introduce stronger assumptions about group behavior, such as the presence of group-level states that are irreducible to individual states. These allow us to represent institutions and cultural norms as active influences in their own right. Finally, we introduce misalignment to capture cases where group-level outcomes diverge from individual preferences. Together, these modeling choices offer a conceptually grounded typology for HONs that connects network science with broader theories of group behavior._

> _The models here set the stage for the following chapters. Chapter [\[chapter:coevo\]](#chapter:coevo){reference-type="ref" reference="chapter:coevo"} presents an irreducible, coupled model of co-evolving individuals and institutions. Chapter [\[chapter:groupSkills\]](#chapter:groupSkills){reference-type="ref" reference="chapter:groupSkills"} examines the emergence of new skills in persistent but isolated research groups. This work builds on prior research [@hebert-dufresne_propagation_2010; @hebert-dufresne_source-sink_2022]._

## Abstract

In complex systems, the study of higher-order interactions has exploded
in recent years. Researchers have formalized various types of group
interactions, such as public goods games, biological contagion, and
information broadcasting, showing how higher-order networks can capture
these interactions more directly than pairwise models. However, equating
hyperedges--edges involving more than two agents--with groups can be
misleading, as it obscures the polysemous nature of the term "group
interactions". For instance, many models of higher-order interactions
focus on the internal state of the hyperedge, specifying dynamical rules
at the group level. In doing so, these models often neglect how
interactions with external groups can influence behaviors and dynamics
within the group itself. Yet, anthropologists and philosophers remind us
that external norms governing intergroup behavior, in the form of
intergroup competition or cooperation, are essential to defining
within-group dynamics. In this paper, we synthesize concepts from social
ontology relevant to the emerging physics of higher-order networks. We
propose a typology for classifying models of group interactions based on
two key perspectives. The first focuses on individuals within groups
engaging in collective action, where shared agency serves as the binding
force. The second adopts a group-first approach, emphasizing
institutional facts that extend beyond the specific individuals
involved. Building on these perspectives, we introduce four dimensions
to classify models of group interactions: persistence, coupling,
reducibility, and alignment. For the physics of higher-order networks,
we provide a hierarchy of nested mathematical models to explore the
complex properties of social groups. We also highlight social
interactions not yet explored in the literature on higher-order networks
and propose future research avenues to foster collaboration between
social ontology and the physics of complex systems.

## Introduction

Broadly defined, the mathematical modeling of complex systems, and in
particular network science, is the multidisciplinary study of how
interactions in a system shape the emergent properties and functions of
the system [@newman_networks_2010]. In recent years, there has been a
large wave of research on higher-order networks where group interactions
are modeled more directly as hyperedges which can be different entities
based on their *order* (size). With hyperedges, group interactions at a
higher order, such as adolescent cliques, committed minorities,
information broadcasting, or contagion within households, can be shown
to be *different* from the pairwise interactions at a lower order
[@battiston_physics_2021; @ferraz_de_arruda_contagion_2024]. By modeling
group interactions at higher orders, we can analyze them as more than
mere correlated bundles of pairwise interactions. But human group
interactions extend beyond individuals interacting in non-trivial ways.
Group norms and institutions shape group behaviors just as groups
influence individual dynamics, yet they remain irreducible to multi-way
interactions. For instance, mask mandates and other shielding measures
significantly alter contagion dynamics in workplaces, extending beyond
the effects of higher-order interactions alone
[@st-onge_paradoxes_2024]. These public health policies are the end
result of cumulative cultural learning, shaped by thousands of years of
socio-technical innovations and intergroup competition
[@boyd_culture_1988; @tomasello_why_2009; @henrich_weirdest_2020].
Similarly, while an increase in the number of coauthors in papers may
hint at the rise of teams in science
[@wuchty_increasing_2007; @uzzi_scientific_2012], modeling the norms and
practices within teams directly offers a different perspective on the
role of collaboration in shaping scientific productivity.

To model networks beyond higher-order interactions, we propose a
typology of group interactions that is informed by the long-standing
history of group minds in the social sciences and, more broadly, the
social ontology of groups. We establish two key connections. The first
highlights the impact of group interactions on individuals, particularly
as influenced by varying degrees of group persistence and coupling. Just
as the jury's paradox and other anti-aggregation arguments show that
group attitudes can contradict individual preferences, higher-order
interactions display nonlinear behavior as they cannot be reduced to a
simple additive function of independent individual influences.

The second connection focuses on (strong) group non-reducibility,
distinguishing it from groups that are weakly emergent due to the
absence of a simple aggregation scheme. We define strongly non-reducible
groups as norms and institutions that do not directly follow from the
states of members or group-level features. By adopting a group-level
perspective that emphasizes the role of institutional facts, we argue
that we can better investigate the coevolution of individuals and
groups--an aspect that is difficult to capture by focusing on
individuals-based dynamics. We can then show how possible misalignment
between individuals and institutions can emerge by reintroducing
individual preferences within the context of group dynamics based on
group-level fitness. This approach enables us to take a step toward
modeling group epistemology, cognition, and rationality within
higher-order network models, as is necessary for modeling norms and
institutions governing group interactions.

Taken together, we establish a typology of group models with the
following dimensions: persistence, coupling, reducibility, and
alignment. This typology helps address ongoing disagreements about the
underlying ontology of models of groups. Consider this; in reviews of
higher-order dynamics, complex contagion models---where dynamics depend
on a nonlinear function of all network neighbors of a given node--are
often ignored [@centola_complex_2007]. Why is that? Likely because
groups are central to the definition, particularly in terms of group
*persistence*. Why, then, are complex contagion dynamics based on social
reinforcement not considered "higher-order", even when they occur over
groups [@watts_influentials_2007; @osullivan_mathematical_2015]? The key
distinction for a system to be considered a higher-order network model
appears to be whether the dynamical rules are nonlinear and specified at
the group level, such that a group interaction cannot be described as a
collection of pairwise interactions. For example, in our typology, we
distinguish between models assuming isolation and those depending on the
states of agents outside the group, or their *coupling*. If coupled, the
dynamics within a hyperedge are not fully determined by the state of
that hyperedge, and such complex dynamics might not fall under the
purview of the current higher-order network literature
[@arruda_contagion_2024]. Interestingly, this distinction is more rooted
in mathematical convenience than empirical evidence. In many
evolutionary models of groups, the role of other groups is essential to
understanding focal groups
[@boyd_culture_1988; @smaldino_evolution_2018].

The rest of the paper proceeds as follows. We first provide a brief
history of group minds, highlighting the debate surrounding group
realism in the sciences (sec.
[1.2](#interface.section.review){reference-type="ref"
reference="interface.section.review"}). By examining how beliefs about
the existence of groups have fundamentally shaped social science
methodologies, we can better identify blind spots in contemporary models
of group interactions. Next, we develop a hierarchy of nested
mathematical models to explore increasingly complex and detailed
properties of social groups (sec.
[1.3](#typology.intro){reference-type="ref"
reference="typology.intro"}). We begin by presenting models of group
persistence and coupling mapped to group interactions derived from
aggregation-based arguments. We then introduce models of group
irreducibility, incorporating the concept of individual-group
misalignment. In its most detailed form, our framework allows us to
mathematically consider important questions such as collective beliefs,
shared intentions, and emerging institutions.

## A short history of group minds

Understanding how group behavior emerges from individuals--and when it
cannot be reduced to them--has long challenged both social scientists
and modelers. We briefly review key positions in the debate over group
minds, with a focus on ideas relevant to modeling group interactions in
social systems.

##### The early debate

A longstanding question in the social sciences concerns whether groups
are real entities with their own dynamics or just convenient labels for
aggregates of individuals. This debate is best understood as one between
group realism and methodological individualism (MI), shaped by early
theoretical developments in sociology and economics
[@schumpeter_methodological_1907; @weber_categories_1913]. Group
realists like Durkheim emphasized the emergent properties of society,
arguing that social norms and institutions regulate behavior and exist
independently of individual intentions. While this may seem like a
strong ontological commitment in retrospect, consider how professions or
legal codes can hardly be reduced to any single individual
[@durkheim_rules_1895 p.51]. And yet, paradoxically, they are enacted by
individuals all the same. MI, as championed by Weber and Schumpeter,
argued that only individuals have desires and beliefs; thus, social
phenomena must ultimately be explained in terms of individual motives
and actions. Schumpeter coined the term "methodological individualism"
to clarify that treating groups as agents is not merely misleading--it's
a category error [@schumpeter_concept_1909]. Yet, the issue persisted in
different forms throughout the twentieth century
[@popper_open_1945; @homans_bringing_1964; @arrow_methodological_1994][^1].

##### Social network analysis

Emerging in the mid-20th century, social network analysis (SNA) shifted
focus to patterns of interaction among individuals, using sociograms to
map relationships. Inspired by early sociologists such as Georg Simmel,
SNA pioneers developed bipartite graphs with two types of
nodes--individuals and the groups or events to which they belonged--to
capture affiliation patterns
[@simmel_conflict_1908; @feld_focused_1981; @mcpherson_hypernetwork_1982; @breiger_duality_1974].
This duality enabled researchers to study overlapping memberships and
community structure indirectly, through individual-level ties. However,
despite tracking group affiliations, SNA largely retained MI's emphasis
on individuals as the primary units of analysis
[@wellman_structural_1988; @neal_duality_2023]. Groups appeared only as
aggregations of pairwise ties or node attributes, without independent
dynamics of their own.

As a result, bipartite models struggled to represent genuine group-level
phenomena, such as norms, institutional memory, or collective
decision-making processes that exhibit inherently nonlinear dynamics.
The assumption was that all group effects could be derived linearly from
individual interactions, missing essential feedback loops or emergent
group states. In contrast, more recent higher-order network models,
based on hypergraphs or simplicial complexes, allow direct modeling of
group interactions as irreducible entities with nonlinear dynamics,
providing tools that are better aligned with group realist perspectives.

##### Groups are real

In response to MI's growing influence, a number of scholars mounted a
defense of groups as legitimate units of analysis
[@campbell_common_1956; @warriner_groups_1956; @horowitz_concept_1953; @wynne-edwards_animal_1962].
In *Groups Are Real: A Reaffirmation*, sociologist C.K. Warriner
challenges methodological individualism by framing the debate as one
between nominalists--who view groups as mere aggregations of individuals
(with all reality vested in the individual)--and realists, who regard
groups as ontologically distinct entities. He also critiques
interactionists, who try to balance individual and group perspectives
but tend to default to individual-level explanations, since groups lack
the clear boundaries and subjective experiences of individuals. But just
as individuals are not reducible to their biology, he insists that
groups are not reducible to the individuals that compose them. The
question is how.

At this point, scholars sought to ground group realism in observable
mechanisms or formal models. Donald Campbell (1956) argued that groups
are real, but the organism-like analogy is misleading
[@campbell_common_1956]. To make his argument, he drew from the *common
fate principle*--the gestalt idea that elements moving together in
unison share a degree of reality. This principle helps explain why
groups are perceived as real even if they lack physical unity, like a
body. Think of a flock of birds or a marching band; no physical boundary
binds them, but their coordinated movement signals a degree of *we-ness*
(a property Campbell liked to call *entitativity*). Meanwhile, Herbert
Simon (1964) reluctantly made the argument that organizational goals
cannot be simply reduced to individual goals [@simon_concept_1964].
Instead, organizations operate through structured roles that shape
behavior at every level. Simon argued that organizational goals are
emergent; they do not simply reflect the preferences of CEOs, boards, or
stakeholders but instead arise from the constraints imposed by
institutional roles at every level of the organization
[@simon_concept_1964]. He contended that explaining organizational
behaviors in terms of individual motives is fraught with problems since
organizational goals do not simply match those of the CEOs, the board,
or the stakeholders; large organizations are modified in practice by
employees at all levels of the organization. Simon's work bridges
individualist and group-level modeling, showing how organizational goals
arise from constraints on individual roles---not from the aggregation of
preferences alone.

Following up on Simon's work, organizational science further embraced
the idea that small working groups were the building blocks of
organizations, rather than individuals. Building on this insight,
organizational theorists shifted from abstract ontological debates to
empirical studies of how groups function in practice. This view is
discussed at length in H. J. Leavitt's paper *Suppose we took groups
seriously\...* (1976), laying the foundation for a systems-level
approach to small group performance, known today as team science
[@leavitt_suppose_1974; @hackman_design_1987; @katzenbach_wisdom_1992; @mathieu_evolution_2018; @wuchty_increasing_2007; @goodwin_science_2018; @hall_science_2018].
Like Schumpeter before him, Leavitt steered away from metaphysical
debates. Instead, he championed empirical research on how communication
structures shape group outcomes---drawing on the experimental work of
Bavelas and others [@bavelas_communication_1950; @leavitt_effects_1951].

##### The evolutionary dynamics of group-level features

Anthropologists and cultural evolutionists have emphasized the
coevolution of human psychology and group dynamics to explain our unique
capacity for large-scale cooperation
[@boyd_cultural_1982; @richerson_cultural_2016]. Human cognition is
uniquely attuned to social learning---especially through conformity,
prestige bias, and intragroup imitation---while deviant behavior is
regulated through norms and reputational sanctions. These mechanisms
scaffold both individual and group-level cultural knowledge. A striking
feature of human psychology is our tendency to over-imitate: children
across cultures faithfully reproduce unnecessary steps in tasks. From a
modeling perspective, these learning biases promote greater similarity
within groups (low within-group variance) while preserving variation
between them.

Such dynamics lend themselves to formal modeling via multilevel
selection, or cultural group selection. When traits benefit the group
more than the individual, group-level selection can dominate---even if
the trait is individually costly. As Darwin himself proposed, traits
like patriotism or self-sacrifice---especially in the context of
intergroup warfare---may evolve because groups that promote them
outcompete more selfish ones [@darwin_descent_1871; @bowles_did_2009].
Recent studies show that group extinctions due to violent intergroup
competition occur on timescales of 500-1,000 years [@soltis_can_1995].
Crucially, this logic applies not only to tribes or ethnic groups but
also to voluntary organizations such as churches, universities, and
firms---where selection acts more rapidly and competition is often
nonviolent [@henrich_weirdest_2020].

In parallel, institutional theorists such as Nelson and Winter extended
evolutionary models to firms, reframing Schumpeter's notion of "creative
destruction" as a process of organizational selection. Firms compete
through varying strategies, technologies, and routines---some of which
prove more adaptive than others [@nelson_schumpeterian_1982]. Unlike
neoclassical economics, this approach emphasizes *bounded rationality*:
agents operate with limited information and adopt heuristics, leading to
persistent diversity rather than convergence to an optimum. Concepts
like path dependence illustrate how early choices---such as the QWERTY
keyboard---can lock in suboptimal solutions due to institutional
inertia. Once embedded, organizational routines become difficult to
reverse. Douglass North extended this perspective by describing
institutions as emergent systems that persist beyond individual
lifespans through cultural transmission: "learning embodied in
individuals, groups, and societies" that is "cumulative through time"
[@north_rise_1973]. For modelers, these ideas support representing
institutions as evolving entities in their own right, with group-level
traits such as norms, routines, and decision structures that are not
reducible to individual behavior.

Cultural evolution theory and new institutional theory developed
research programs around group-level traits that can evolve, stabilize,
and compete in ways that go beyond individual-level dynamics. With
models, they sought to avoid the earlier "Panglossian
adaptationism"--the assumption that all observed traits are somewhat
optimally selected. For modelers, the group-based approach raises two
central challenges. First, group dynamics often cannot be captured
solely through individual traits or pairwise interactions---even under
assumptions of weak emergence. Second, group-level traits and individual
incentives frequently diverge, especially in the context of intergroup
competition or collective decision-making. This misalignment requires
explicit modeling of cross-level feedback. Understanding both
irreducibility and misalignment is key to modeling collective behavior
in complex social systems.

## Typology of groups and group-based modeling

The literature on group interactions is fragmented across communities,
with ongoing disagreements about the underlying ontology of groups. We
define a typology of models of groups that integrates mathematical
assumptions with the long-standing history of group interactions.

-   **Ephemerality:** Are group interactions fleeting or persistent? Do
    the interaction dynamics wash out any correlation between individual
    states?

-   **Coupling:** How much do you need to know about non-members to
    predict group dynamics?

-   **Irreducibility:** Can you predict a group's behavior based solely
    on its members, or do you need extra information about the group
    itself?

-   **Misalignment:** Do groups behave in ways that reflect the
    preferences of their members?

We use this typology to classify broad families of models based on the
kinds of higher-order interactions they can represent. While this review
focuses on models rather than the empirical aspects of human groups, we
highlight connections to the empirical literature where possible.

### Group persistence and intergroup coupling

When discussing the existence of a group, persistence and coupling
consistently emerge as key features. Early on, Georg Simmel and others
studied how group size and composition influence stability. They
compared smaller, tightly knit groups based on intimate connections
(primary groups) with larger groups that promote formal organizations,
impersonal interactions, and specialized roles (secondary groups), such
as bureaucracies [@cooley_social_1909]. Broadly speaking, the idea of
group persistence is intertwined with that of interactions between
groups, as (ethnic) groups are believed to engage in cooperation or
competition. Strongly competing groups are more tightly bound, as they
may restrict interactions to maintain their advantage. In contrast,
cooperative groups are more open and can facilitate the mixing of people
and ideas, leading to a reduction in group differences. Although
permanence and isolation are key features, their meaning varies
depending on the social groups in question. Both work teams and
ethnolinguistic tribes are, to some extent, permanent or relatively
isolated, but somewhat in different ways.

From a modeling perspective, we distinguish groups formed through
momentary interactions and those persisting in time. We define momentary
group interaction as a set of individuals engaged in some shared
activity within a time window that is short compared to the
characteristic timescale of the dynamics. In the physics of HONs, these
interactions can be modeled as hyperedges within an annealed hypergraph
(see [Box 1](#tcolorbox:modelbox1)). Groups continuously form and
dissolve, so the individuals with whom one interacts continuously
change.

:::: spacing
1.15

::: tcolorbox
[]{#tcolorbox:modelbox1 label="tcolorbox:modelbox1"} The continuous
formation and dissolution of groups implies the absence of dynamic
correlations between the states of individuals. Therefore, knowing the
expected state of a random individual is all we need to describe
ephemeral groups. A simple mean-field equation for the fraction $I$ of
individuals in a state--say--'active' is sufficient:
$$\frac{d}{dt}I = \sum_{n=2}^\infty p_n\sum_{k=0}^n \binom{n}{k} I^{k} (1-I)^{n-k} \left[(n-k)\beta(n,k)- k\alpha(n,k)\right] \; .
\label{eq:ephemeral}$$ Here, $p_n$ is the probability distribution of
group sizes, while $\beta(n,k)$ ($\alpha(n,k)$) is the rate at which
inactive (active) individuals become active (inactive), which is a
generic function of the group size $n$ and the number $k$ of active
individuals in the group. In particular,
$p_n \binom{n}{k} I^{k} (1-I)^{n-k}$ is the probability that a random
group has $n$ members, of which $k$ are active.

The description given by
Eq. ([\[eq:ephemeral\]](#eq:ephemeral){reference-type="ref"
reference="eq:ephemeral"}) is equivalent to a *annealed* structure with
an infinite number of individuals (nodes) and groups (hyperedges), where
every group is possible and all groups are reshuffled on a timescale
much (ideally, infinitely) shorter than the timescale (here defined by
either $1/\beta$ or $1/\alpha$) at which the dynamical process unfolds.
Both structural and dynamical correlations are absent in these models.
:::
::::

In contrast, group permanence generally induces dynamical correlations.
For example, if an individual in a household gets sick, others in the
household are likely to be infected sooner or later. Since the household
persists over time--enforcing repeated interactions--the states of its
members become correlated through the dynamics (here, a contagion
process). We can therefore study how specific group interactions
influence the local and global dynamics. In the limit of never-changing
groups, these define a *quenched* structure, representable as a static
hypergraph, where hyperedges (groups) connect to each other through
shared nodes (e.g. a household and a sports team with a member in
common). In this case, neglecting dynamical correlations may lead to a
poor understanding of the system's behavior. One can define models that,
in addition to accounting for the quenched topology, are able to
preserve dynamical correlations within groups by tracking the state
evolution of each group [@burgio_network_2021]. The large amount of
information used by such models makes them highly accurate but also
computationally costly. Moreover, all that information is often
difficult to access in real-world systems.

An alternative approach is offered by approximate master equations
(AMEs) models
[@hebert-dufresne_propagation_2010; @st-onge_master_2021; @burgio_adaptive_2023].
Although assuming an infinite, annealed structure, such models can work
as satisfactory approximations for large quenched (or slowly varying)
topologies due to the dynamical correlations they account for. Groups
are assumed to be constantly reshuffling, but not uniformly at random;
they rather do so while respecting the current probability distribution
of group states (e.g. proportion of groups with $i$ active and $j$
inactive nodes, for every $i$ and $j$), so that dynamic correlations
within groups are preserved. More sophisticated formulations of AMEs can
also account for some dynamic correlations *between* groups
[@burgio_adaptive_2023] (see [Box 2](#tcolorbox:modelbox2)).

:::: spacing
1.15

::: tcolorbox
[]{#tcolorbox:modelbox2 label="tcolorbox:modelbox2"} To account for
persistence, we must at least preserve correlations within groups, since
the duration of a group interaction induces correlations among the
states of its members. The latter can also change state because of their
membership in other groups. As a minimal model, we might, therefore, use
approximate master equations. These describe the temporal evolution of
the probability distribution $G_{n,i}$ that a group of size $n$ has $i$
active individuals (between 0 and $n$). The description tracks the
processes within a focal group exactly and the processes within external
groups in a mean-field fashion. The distribution $G_{n,i}$ thus evolves
according to $$\begin{aligned}
    \notag \frac{d}{dt}G_{n,i} =&~ (n-i+1)\left[\beta(n,i-1) + \rho\phi\right]G_{n,i-1}
    - (n-i)\left[\beta(n,i) + \rho\phi\right]G_{n,i} \\
    &+ (i+1)\left[\alpha(n,i+1) + \rho'\psi\right]G_{n,i+1} - i\left[\alpha(n,i) + \rho'\psi\right]G_{n,i} \; ,
    \label{eq:box2}
\end{aligned}$$ where
$$\phi = \frac{\sum_{n,i}(n-i)\beta(n,i)G_{n,i}}{\sum_{n,i}(n-i)G_{n,i}} \; ,\ \
   \psi = \frac{\sum_{n,i}i\alpha(n,i)G_{n,i}}{\sum_{n,i}iG_{n,i}} \; ,
   \label{eq:box2_aux}$$\
are the respective probabilities of being activated or deactivated in
random external groups. The factors $\rho$ and $\rho'$ quantify the
coupling between groups for the activation and deactivation mechanisms,
respectively. The case of isolated groups corresponds to
$\rho = \rho' = 0$. In the case of susceptible-infected-susceptible
(SIS) type dynamics, recovery is typically modeled as an intrinsic
process, independent of group composition or external coupling. This
corresponds to setting $\rho'=0$, while allowing $\rho>0$ to model
infection through external contact.
:::
::::

If groups persist over time, it then makes sense to ask if and how they
interact with the outside social world. In [Box
2](#tcolorbox:modelbox2), strongly coupled groups are those in which
out-group states provide information about within-group dynamics. For
example, children playing together can spread infections between
households. Similarly, group coupling affects information flow in social
contagions--polarized groups freely exchange information internally but
not externally. In pairwise networks, modularity captures this, but
perfectly modular networks differ from quenched, coupled ones; in the
former, contagion remains a sum of independent influences. In contrast,
higher-order structures introduce nonlinear reinforcement, where
repeated interactions within persistent groups amplify contagion beyond
independent pairwise transmissions.

The coupling is distinct from adaptive networks, where individuals can
move between groups based on several mechanisms, such as leaving when
dissatisfied
[@gross_adaptive_2007; @marceau_adaptive_2010; @burgio_adaptive_2023] or
ascribed migration [@mcelreath_mathematical_2007 ch.6]. Instead, our
modeling allows for recombination, where a mix of ephemerality with
persistence of group dynamics can result in something new. By modeling
how individuals form, reshuffle, or stay put, we can achieve an adaptive
group-structured system. In some cases, this approach might be better
suited to model group processes such as intergroup competition
[@wilson_intergroup_2003; @henrich_cultural_2004; @richerson_cultural_2013].
In other cases, such as with social systems exhibiting strong
polarization, coupling can instead be extended by adding a polarity to
the coupling parameter. In this case, antagonistic influence could
simply lead groups to adopt the opposite behaviors of what adverse
groups are exhibiting, without requiring people to move
[@smaldino_coupled_2021].

The description of persistent group-based dynamics remains limited in
that the state of a group is fully derived from that of its members.
Group interactions in households impacting contagion dynamics seem
reasonable enough, but what about clans within ethnolinguistic tribes
competing with each other, or tacit organizational knowledge? To account
for persistent cultural behaviors, we propose shifting our view from
groups as sets of individuals engaged in multi-way interactions to a
stronger notion of emergence based on cultural group-level traits
[@smaldino_cultural_2014].

### Irreducible group-level features

In many ways, the vast majority of group interactions are mediated by
cultural group-level traits, as human behaviors are regulated by
institutions. Consider how sports teams consist of players, staff, and
management, all working together to optimize team performance. Teams
succeed or fail not only due to synergistic individual performance but
also due to persistent group-level traits, such as how management
decides to allocate resources among its members
[@turchin_ultrasociety_2016]. Cultural traits are considered to operate
at the group level because they are shaped by the ratio of within-group
and between-group competition, rather than by individual performance
alone [^2]. For example, if management chooses to distribute resources
more evenly, it reduces within-group competition for the best contracts
[@tiokhin_shifting_2024]. In this context, contracts promoting equity
serve as one of many norms that facilitate cooperation among team
members, contributing to the group's overall *organization*. In [Box
3](#tcolorbox:modelbox3), this idea is captured as an abstract
group-level feature, $\ell$, which can be framed as fostering altruistic
states among teams.

:::: spacing
1.15

::: tcolorbox
[]{#tcolorbox:modelbox3 label="tcolorbox:modelbox3"} In irreducible
groups, the dynamics affect both the state of the members of a group as
well as group features $\ell$ that do not directly follow from the state
of the members. We therefore split the dynamics into two sets of
transitions, one governing members and one governing emergent group
features, like this
$$\frac{d}{dt}G_{n,i}^\ell = \frac{d}{dt}M_{n,i}^\ell + \frac{d}{dt}E_{n,i}^\ell \; .$$
[]{#eq:box3 label="eq:box3"}\
The first set of transition rates, $\frac{d}{dt}M_{n,i}^\ell$, governs
transitions related to the members of the group and is equivalent to
Eq. ([\[eq:box2\]](#eq:box2){reference-type="ref" reference="eq:box2"})
but with dynamical parameters $\alpha$ and $\beta$ now being a function
of the group feature $\ell$.

The second set of transition rates, $\frac{d}{dt}E_{n,i}^\ell$, governs
the transitions for the group features $\ell$. We can imagine that the
group mind might want to promote or hinder activation and that $\ell$
might capture the level of group activity dedicated to this function
(e.g., the creation of group norms). We could then assign a perceived
fitness $Z^\ell$ to the levels $\ell$ (potentially also a function of
the state of its members, i.e., $Z^{\ell}_{n,i}$). In a very simple
form, group minds might then perform a biased random walk over the
fitness landscape of group features $\ell$: $$\label{eq:box3_groups}
    \frac{d}{dt}E_{n,i}^\ell = h(n,i,\ell-1) \dfrac{Z^{\ell}_{n,i}}{Z^{\ell-1}_{n,i}} G_{n,i}^{\ell-1} + h(n,i,\ell+1) \dfrac{Z^{\ell}_{n,i}}{Z^{\ell+1}_{n,i}} G_{n,i}^{\ell+1} - h(n,i,\ell) \dfrac{Z^{\ell-1}_{n,i}+Z^{\ell+1}_{n,i}}{Z^{\ell}_{n,i}} G_{n,i}^{\ell} \; ,$$
where the transition rate for group features, $h(n,i,\ell)$, accounts
for potential dependencies on the current state of the group (resources,
costs, etc.).
:::
::::

By assuming group-level independence, we can directly model how groups
adopt a series of discrete levels of institutional strength to enhance
their capacity to promote individually costly behaviors. In the current
form of the model, adopting stronger norms results in a faster adoption
rate of costly behaviors among members, but this can be further
elaborated (as we do in sec.
[1.3.3](#secion:alignment){reference-type="ref"
reference="secion:alignment"}). In our team example, modern teams could
engage in increasingly sophisticated strategies to promote team equity.
Just as coupling involves knowing the state of out-group members to
predict the state of individuals within groups, irreducibility can be
understood as the amount of information about the group required to
predict the state of its members. When group state is perfectly
correlated with that of its members, it is fully reducible.

Without group-level traits, groups are indistinguishable if their
members find themselves sharing the same states. Once we account for
group states, these may vary or remain constant while shaping the
dynamics within groups. For example, a team might change its
communication platform, influencing group dynamics. But practically, we
are interested in how those changes may lead to groups being more or
less successful, exhibiting group-level fitness. In [Box
3](#tcolorbox:modelbox3), group-level fitness influences how groups
decide to scale institutional strength up or down, based on a trade-off
between achieving success and balancing other factors, such as the
potential costs of scaling up group norms. With group-level features, we
can begin to inquire about the impact of perceived success, or perhaps
prestige, of neighboring groups on within-group dynamics
[@richerson_cultural_2016; @hebert-dufresne_source-sink_2022].

We highlight some key findings based on the dynamics of models from [Box
3](#tcolorbox:modelbox3). First, there are critical thresholds in terms
of collective costs, benefits, and the individual adoption rate $\beta$
that determine the widespread adoption of costly behaviors, as expected.
Then, the phenomenon of institutional localization has been
identified--that is, a specific institutional level dominates the
fitness landscape within certain parameter ranges
[@st-onge_paradoxes_2024; @hebert-dufresne_source-sink_2022]. This has
raised questions about the conditions under which groups invest in
scaling up their policies versus relying on other groups to bear the
burden of increased institutional efforts while reaping the benefits
within their own groups--what has been dubbed as "institutional
free-riding" [@st-onge_paradoxes_2024]. Lastly, it was found that when
individual behaviors are perceived as excessively costly (perhaps
adopting equitable contracts by sports players in our running example is
seen as such) institutions may respond by intensifying their efforts to
promote those behaviors [@st-onge_paradoxes_2024]. This "call to action"
suggests that worst-case scenarios can drive institutional change,
whereas more tolerable situations may be accepted, leading to lower
overall adoption rates.

Irreducible features help distinguish between groups as mere containers
of interactions and groups as entities with higher-level traits subject
to selection. The group independence assumption is a useful
simplification in that we can directly model institutional dynamics
without having to explain their emergence. Yet, organized groups rarely
emerge in a mathematical vacuum. Increased institutional strength is
fundamentally correlated with changes in resource management and social
hierarchy, which we both include as components of misalignment.

### Alignment of individuals and groups

We define alignment as the degree to which individual-level states--such
as preferences, beliefs, or actions--are congruent with group-level
dynamics. Alignment arises when group behavior reinforces individual
goals, and vice versa. Misalignment, by contrast, occurs when groups
produce outcomes that persist despite contradicting or neglecting the
goals of their members. Alignment interacts with previous dimensions to
capture a diversity of group phenomena in nature.

In animal behavior, alignment can be as simple as bird flocks or fish
schools emerging from individuals obeying local interaction rules---such
as repulsion, attraction, or predator avoidance
[@reynolds_flocks_1987; @ioannou_predatory_2012]. These decentralized
dynamics generate group-level benefits (e.g., anti-predator shielding)
that align with individual fitness. Similar effects arise in human
systems; for example, the presence of more cyclists on the road improves
safety for all, even without explicit coordination. In such cases,
group-level properties emerge from simple local rules that reinforce
individual goals.

In contrast, misalignment arises when group-level patterns feed back in
ways that contradict individual incentives. A simple example is that of
*Roger's Paradox*, where overreliance on social learning degrades
decision quality in changing environments [@rogers_does_1988]. When
individuals copy others rather than directly engaging with the world,
groups risk becoming unresponsive or locked into outdated norms
[@torney_social_2015]. A similar dynamic appears in Condorcet's jury
paradox, where individually rational votes aggregate into irrational
majorities. In both cases, individuals act sensibly based on local
information, yet the group produces outcomes no one intended. Real-world
examples abound: alarm calls become noisy under excessive imitation
[@brown_social_2003], and speculative bubbles form when investors herd
without reevaluating fundamentals [@lo_wisdom_2022]. In such models,
misalignment arises within *persistent but reducible* groups--structures
where individual behavior correlates over time, but the group exerts no
independent influence.

With irreducible groups---those possessing persistent states like norms
or policies--misalignment takes on a more institutional character. These
group-level structures can persist even when they diverge from the
preferences or goals of individual members. Consider researchers
choosing between slower, reproducible methods and faster, less rigorous
ones. When success metrics reward publication volume, individuals are
incentivized to cut corners---even if the group would benefit from
quality-focused norms [@dawson_role_2022; @tiokhin_shifting_2024]. This
isn't necessarily a case of bad actors engaging in p-hacking; rather,
individuals may continue practices they have learned and seen rewarded,
despite growing evidence of their detrimental effects
[@smaldino_natural_2016]. Groups may attempt to enforce better norms
through institutional policies, but unless those norms are strong,
visible, and valued, individuals may simply defect through apathy. In
this context, misalignment stems not from resistance but from
indifference.

This mismatch between individual incentives and collective structures
isn't just a product of faulty aggregation. Institutions evolve on
different timescales and are often sustained by mechanisms like prestige
[@way_gender_2016], norm entrenchment [@richerson_cultural_2016], or
institutional lock-in [@nelson_search_1993]. They may persist even when
they no longer serve their members, creating structural inertia that
deepens misalignment. Conversely, institutions can promote better
practices---such as transparency or methodological rigor---while
individuals may exhibit inertia on shorter timescales, failing to adapt
even when norms shift in that direction.

We explore this dynamic more formally in [Box 4](#tcolorbox:modelbox4),
which presents a minimal model of institutional misalignment.
Individuals belong to groups (e.g., cliques), each with an institutional
quality level $\ell$, determining the perceived value of public goods
$s(\ell)$. Strategy updates---such as choosing to cooperate or
defect---depend on peer behavior and institutional satisfaction. The
probability of adopting cooperation follows a sigmoid function $f(x)$,
where $f(s(\ell)-1)$ captures responsiveness to institutional strength.
Here, individuals behave more cooperatively when institutions are
perceived as strong, and vice versa.

:::: spacing
1.0

::: tcolorbox
[]{#tcolorbox:modelbox4 label="tcolorbox:modelbox4"}

Alignment in irreducible groups takes the same basic form as in [Box
3](#tcolorbox:modelbox3) but with the additional component that
individuals have opinions about how their institution manages their
public goods. A minimal implementation of the latter amounts to adding
an institution-dependent term of spontaneous transition in the dynamic
equation for the state of the individuals. We thus write
$$\begin{aligned}
\label{eq:box4_ind}
    \notag \frac{d}{dt}M_{i}^\ell =&~ (n-i+1)\left[\gamma f(s(\ell) - 1) + \beta(i-1) + \rho \beta \phi \right]G_{i-1,\ell} \\
                    \notag  &- (n-i)\left[ \gamma f(s(\ell) - 1) + \beta i + \rho \beta \phi \right] G_{i,\ell} \\
                    \notag &+ (i+1) \left[ \gamma f(1-s(\ell)) + \alpha(n-i-1) + \rho \alpha \psi \right] G_{i+1,\ell} \\
                    &- i\left[\gamma f(1-s(\ell)) + \alpha(n-i) + \rho \alpha \psi \right] G_{i,\ell} \; ,
\end{aligned}$$

where, for simplicity, we removed dependence on group size $n$ by
assuming all groups are equally sized (more generally, we would have an
index $n$ to account for distributed size). As in [Box
3](#tcolorbox:modelbox3), after summing over $\ell$, the terms $\phi$
and $\psi$ represent the influence of other groups on individual
transitions. The function $f(x)$ gives the probability that a defecting
individual switches to cooperation (activates), and depends on the
perceived quality $s(\ell)$ of the public good, where
$ds(\ell)/d\ell > 0$. The parameter $\gamma$ governs the rate of
spontaneous behavioral switching. Without loss of generality, we set
$\ell = 1$ to represent the threshold at which individuals are
indifferent to institutional performance, and fix $s(1) = 1$. We choose
$f(x)$ to be symmetric about zero (i.e., $f(x) + f(-x) = 1$), so that
$f(s(1)-1=0)=1/2$ represents indifference, and $f(-x) = 1 - f(x)$ gives
the probability for a cooperator to switch to defection.

The second set of transition rates $\frac{d}{dt} E_{i}^\ell$ is similar
to Eq. [\[eq:box3_groups\]](#eq:box3_groups){reference-type="ref"
reference="eq:box3_groups"}, but--mirroring Eq.
[\[eq:box4_ind\]](#eq:box4_ind){reference-type="ref"
reference="eq:box4_ind"}--we give institutions more agency by including
a term of spontaneous, fitness-independent change ($\propto \mu$). Then,
as in Eq. [\[eq:box3_groups\]](#eq:box3_groups){reference-type="ref"
reference="eq:box3_groups"}, the transition rates be any function of $i$
and $\ell$ (and $n$). Supposing that upgrading and maintaining stronger
institutions entails some cost, we write $$\begin{aligned}
    \notag \frac{d}{dt}E_{i}^\ell =&~ g(bi - c\ell) \left[\mu + \rho \dfrac{Z^{\ell}_{n,i}}{Z^{\ell-1}_{n,i}}\right]G_{n,i}^{\ell-1}
        - g(bi - c(\ell+1)) \left[\mu + \rho \dfrac{Z^{\ell+1}_{n,i}}{Z^{\ell}_{n,i}}\right]G_{n,i}^{\ell} \\
        \notag &+  \left[ \mu g(c(\ell+1) - bi) + \rho  g(bi - c\ell) \dfrac{Z^{\ell}_{n,i}}{Z^{\ell+1}_{n,i}}\right] G_{n,i}^{\ell+1}  \\
        &-
        \left[ \mu g(c\ell - bi) + \rho g(bi - c(\ell-1)) \dfrac{Z^{\ell-1}_{n,i}}{Z^{\ell}_{n,i}} \right] G_{n,i}^{\ell} \; ,
\end{aligned}$$

where the function $g$ accounts for the balance between the available
resources ($\propto bi$) and the cost to sustain ($\propto c\ell$). The
overall dynamics allows us to explore how individual- and group-level
traits coevolve driven by alignment.
:::
::::

Crucially, the model allows institutional misalignment to become
self-reinforcing. If a group underinvests in norms (low $\ell$),
cooperation declines, leading to weaker outcomes and even lower
investment---a "race to the bottom". Conversely, well-maintained
institutions can stabilize cooperation, even under noise or temptation
to defect. This dynamic reflects a feedback loop: individuals are
sensitive to norms only when the group visibly invests in collective
goods. Otherwise, they default to inaction, and group performance
collapses.

The model also incorporates bounded rationality via a sensitivity
parameter $\alpha$. When $\xi$ is low, behavior becomes noisy and less
strategic; when $\xi$ is high, behavioral thresholds sharpen,
approximating rational adaptation. This flexibility allows us to
interpolate between stochastic imitation and goal-oriented
decision-making.

Importantly, the institution itself evolves. Group-level quality $\ell$
rises or falls based on internal dynamics (e.g., number of cooperators)
and comparisons to other groups. Institutions that succeed in managing
public goods attract more cooperation, which in turn reinforces their
strength---linking micro-level behavior to macro-level evolution.

If research groups exist in a cultural context that strongly values
individual achievement (e.g., the myth of the heroic inventor), efforts
to shift the unit of selection from individuals to groups may be
resisted [@henrich_weirdest_2020]. Our model captures this interplay:
cooperation spreads through peer imitation and group identity but is
moderated by the institution's perceived quality. A group may invest
heavily in promoting cooperative norms---such as mentoring, code review,
or rigorous methodology---but if members remain indifferent, these norms
may fail to take hold. Irreducible institutions do not merely shape
strategy---they also define roles, responsibilities, and prestige. In
this way, misalignment interacts with social differentiation:
institutions like academia offer stable roles (e.g., professor, advisor)
that come with behavioral expectations, but if those roles become
disconnected from individuals' lived experiences or values, misalignment
arises not just in behavior, but in identity and purpose.

By treating institutions as persistent group-level states that both
shape and respond to individual behavior, we can model the
coevolutionary feedback between people and structure. Misalignment, in
this view, is not a statistical quirk---it is a dynamic process through
which group norms and individual actions gradually diverge, potentially
undermining collective goals. Conversely, individuals can also diverge
from long-term, sustainable goals promoted by groups. Capturing this
process is essential for understanding real-world systems where
alignment must be earned, not assumed.

## Discussion

We outlined four dimensions of group models, integrating insights from
higher-order interactions and the long-standing history of group
interactions. We found that models of higher-order interactions mainly
address weakly emergent group behaviors, whether ephemeral or
persistent. By incorporating group-level features, we improve our
ability to represent the coevolution of individuals and institutions.
Before concluding, we highlight some challenges and future directions in
applying our framework to empirical research.

##### Measuring group-level features

Measuring co-authorships is easier than measuring the norms and
institutions shared by research groups. Individual interactions often
seem easier to measure than group interactions. Yet, this does not mean
that social networks are more real than group interactions. Individual
interactions are not as easy to measure as they seem; social networks
are subject to assumptions and are often error-prone
[@young_robust_2020]. What we define as nodes and edges depends on the
research question; for example, friendship can be defined reciprocally
or not, leading to different networks [@butts_revisiting_2009]. Then, it
is good to remind ourselves that any kind of social interaction occurs
within specific sociotechnical contexts. Individual productivity is
easier to measure because we have made it easy, and co-authorship is
particularly prominent because Western scientists have long attributed
ideas to individuals [@henrich_weirdest_2020]. Ultimately, the key is to
use the right tools for the work at hand, and researchers studying teams
in science should model changing norms and policies, as the meaning of
co-authorship varies over time and across communities. The availability
of group interactions does not exempt us from clear assumptions about
their meaning.

That being said, how would we start to measure group-level features?
Anthropologists, among other fields, made tremendous efforts to measure
and characterize cultural groups throughout the world. In recent times,
researchers have begun to take on the challenges of coding norms and
policies and making them accessible through open databases
[@slingerland_database_2024; @turchin_seshat_2015; @kirby_d-place_2016].
Another example is the Oxford COVID-19 Government Response Tracker data,
which was a tremendous effort by public health researchers to track
policies adopted by governments in response to the COVID-19 pandemic. A
key part of their effort was ensuring intercoder reliability in how a
team of experts quantified the strength of government responses. In
general, this ability to organize scientific teams on a larger scale to
agree on relevant norms has been shown to be key to modeling group-level
features [@slingerland_coding_2020].

##### Measuring misalignment

Strongly emergent misalignment, perhaps due to being a mouthful, is also
the most challenging dimension to estimate because it involves
variability in individual preferences and group dynamics. How do we know
if sports team management or a research group is misaligned with the
interests of its members? Worse still, what about misalignment in
organizations such as a "Mafia" or a "Church"? We must rely on
evolutionary models; if the group-level feature is assumed to promote
group success, in terms of higher fitness, then misalignment occurs
whenever individual preferences are not aligned with that (functional)
goal. Sometimes, it is obvious, as with suicide bombers willing to die
for their group to prosper. Most of the time, this is more nuanced, as
with religious acts that entail serious risks and significant
investments of time, leading to increased performance of the group
relative to other religious groups [@power_social_2017]. Modeling
functional group behaviors has been controversial, but the combination
of contemporary theoretical modeling and fieldwork can help us identify
the necessary ingredients to determine when group-beneficial traits are
favored, as one of many potential alternative stable states
[@boyd_group_1990; @boyd_culture_1988; @boyd_group_2002; @soltis_can_1995].
Once again, a key aspect of quantifying misalignment is intercoder
reliability among domain experts when identifying latent norms and
policies, as well as individual variability, which can then be used to
make predictions.

##### Group minds redux

When early social scientists discussed the idea of "group minds", they
made logical (verbal) arguments about society exhibiting organism-like
characteristics. This has led to a kind of Panglossian evolutionism,
where group adaptation is everywhere while motivating a Victorian
*laissez-faire* [@campbell_how_1994], which was later dismissed. In our
typology, we are assuming that *group-level features*, such as norms and
institutions, do influence group-level fitness. Importantly, fitness is
defined generally in our model, but it must be empirically specified. In
the case of interfirm competition, for instance, empirical research
continues to specify how exactly organizational breakthroughs in
management and innovation improve overall firm success, whether through
differential survival or proliferation [@richerson_cultural_2016]. It is
related but not reducible to the idea of group minds as collective
intelligence, or weak emergence. In this view, there is a similar
ongoing effort to empirically assess how teams perform better than the
sum of individual performance, most notably through complementary
skills, communication strategies, or diversity of expertise
[@page_diversity_2010]. As such, both the question of whether particular
group-level features and weak emergence entail the existence of group
minds is open and subject to empirical inquiry, though it has now been
influenced by extensive modeling work.

It is worth mentioning that philosophers have argued at length in recent
years about the meaning of groups exhibiting cognitive-like properties
[@french_collective_1984; @pettit_groups_2001]. As with collective
intelligence, some aspects of it are generally accepted, such as ants
exhibiting memory-like properties through pheromone trails
[@gordon_ant_2010]. However, as with the organism-like analogy, what is
meant exactly by a corporation lying about the fuel efficiency of its
vehicles is still an ongoing ontological debate
[@lackey_epistemology_2021]. In its strongest form, philosophers argue
that groups capable of believing, knowing, asserting, or even lying can
be held accountable for their actions, effectively becoming moral
entities--an issue that falls beyond the scope of this review
[@lackey_epistemology_2021].

##### Big groups and networked norms

Our typology is meant to represent group interactions, both small and
large. However, some group interactions are too abstract and
hierarchical to currently fit into our modeling work; for example, a
federal government issuing an executive order like a mask mandate. As
such, the key level of analysis for our typology is the level at which
policies are implemented, for instance, local health departments. At
this level, groups can be thought of as copying and learning from each
other. There is also an additional layer of global top-down influence,
referred to as "higher-level" political-economic institutions, which
interact with both "lower-level" institutions, such as those related to
kinship, marriage, religion, and people's cultural psychology. Only by
developing models that can capture the joint influence of individual
variability along with that of lower-level institutions can we begin
exploring the larger, more diverse "pluralistic" political institutions
[@henrich_big_2015; @acemoglu_why_2013].

Our family of models focused on models with binary states at the
individual level and a single abstract group-level state that influences
those states. Nothing prevents our work from being extended to more
complex states at all levels. One more challenging generalization is to
consider overlapping institutions and identity as part of the connection
between groups. People have overlapping memberships, which are known to
significantly impact the dynamics of systems. Similarly, norms and
institutions often come in bundles, with specific networks of practices.

##### Conclusion

As the modeling of group dynamics and higher-order networks flourishes,
we will continue to see new mathematical approaches to describe groups.
By using our typology to compare models, we hope to not only clarify and
classify existing efforts, but also identify types of groups and group
interactions that are currently ignored by these efforts.

## Appendix

In our short history of group minds, we noted at least one important
feature missing from our typology; social differentiation.
Differentiation refers to the diversity among members in roles,
responsibilities, or rewards---and is key to understanding how
coordination, hierarchy, and inequality arise within groups
[@redhead_social_2022; @smith_leadership_2016]. In biological and social
systems alike, differentiation enables synergy: the performance of a
group can exceed the sum of its parts when members specialize and
coordinate their actions [@araujo_team_2016; @guimera_team_2005]. We
left this category out of the main text because our current typology
does not yet include a group-based model with differentiated
individuals. But here we provide a short overview of how differentiation
is addressed across relevant modeling traditions---from network science
to cultural evolution and higher-order interactions---to draw attention
to novel modeling opportunities in that area.

##### Differentiation as heterogeneity

Differentiation in networks can be as simple as *node metadata*---fixed
attributes like class, gender, or rank. These are often treated as
exogenous labels that may (or may not) correlate with community
structure [@newman_structure_2016]. When such attributes shape
interaction patterns---for instance, assortativity by class or
profession---we enter the realm of *heterogeneous mixing*. This
introduces structure into interaction but still assumes randomness
conditioned on classes (e.g. node features or degree-based). As such, it
cannot capture *dynamical correlations*---state dependencies that build
up over time through repeated interactions. In contrast, persistent
groups preserve local structure, enabling individual states to co-evolve
through reinforcement, norm enforcement, or coordinated roles.
Differentiation in this sense is structuring group interactions---not
just a label but a product of sustained interaction.

##### Differentiation improving group coordination

In evolutionary models, social differentiation enhances group
performance by enabling more sophisticated forms of coordination. In
correlative coordination games, any shared behavior---regardless of
content---yields higher payoffs than uncoordinated actions. These models
explain how arbitrary conventions (e.g., driving on the right) can
emerge and stabilize [@smaldino_modeling_2023]. In asymmetric
coordination games, one strategy leads to better group outcomes but
imposes initial costs on individuals---such as contributing to a public
good that only succeeds if enough others do the same [@boyd_group_2002].
Differentiation means that individuals adopt specialized strategies,
like moralists who both cooperate and punish defectors to help the group
reach and maintain beneficial equilibria [@boyd_group_1990]. A third
form, complementary coordination, involves interlocking roles---"I cook,
you clean" kind of scenarios. These games produce surplus only when
roles are matched. If rewards are balanced, roles can rotate; if not,
differentiation may harden into hierarchy, with some roles becoming
persistently higher status or more burdensome. Over time, such roles may
align with social markers like gender, age, or skill, embedding
stratification within the group structure [@smaldino_modeling_2023]. In
this view, differentiation is not just functional---it is formative,
shaping how groups coordinate, specialize, and reproduce internal
inequalities.

##### Differentiation as synergy in HONs

Whereas differentiation in cultural diffusion and coordination games
emphasizes how roles and strategies contribute to group success,
higher-order network models highlight how group structure
itself---rather than internal role composition---can generate synergy.
In these models, individuals interact through hyperedges: explicit
group-level interactions where the composition and size of each group
shape outcomes. Recent work on order-heterogeneous hypergraphs shows
that even without role differentiation, cooperation can be amplified if
the synergy factor scales super-linearly with group order
($R(g) \propto g^\beta$)---meaning larger groups yield
disproportionately larger payoffs
[@alvarez-rodriguez_evolutionary_2020; @burgio_evolution_2020]. This
structural differentiation---determined by who participates with whom,
and in which group sizes---shifts the critical thresholds for
cooperation and alters relaxation times. Such models complement cultural
diffusion approaches [@boyd_group_2002], but go further by assigning
high-order effects to the topology of participation itself. In this
view, differentiation is not just about roles or strategies, but about
the topology of participation---how group size and overlap encode
evolutionary leverage.

##### Differentiation sustaining group-level features

In all models we've seen so far, groups are reassembled each round, and
synergy arises from transient structure or strategy---not from
persistent group identity or evolving institutions. Irreducible group
structures, such as the churches, ethnicities, or unions, do more: they
create, stabilize, and legitimize roles over time. The moralist, for
example, is not merely a strategic role but can become a codified
identity embedded within a system of beliefs, or a priest. Institutions
interact with differentiation to determine who does what, for whom, and
at what cost. From the perspective of higher-order network models, this
kind of institutional differentiation remains fundamentally
understudied---most work still focuses on ephemeral, isolated groups.
Yet differentiation is more than heterogeneous mixing; it shapes not
only immediate coordination but also collective performance across
evolutionary timescales.

[^1]: See [@udehn_changing_2002] for a review of the changing face of
    methodological individualism. Group realism is entangled with that
    of functionalism, where groups are real because they occupy
    functional roles that promote the common good, as in the
    organism-like analogy of groups.

[^2]: This argument draws on the Price Equation, which shows that the
    ratio of within-group to between-group variance determines the
    conditions under which group selection can outweigh individual
    selection [@richerson_cultural_2016]. Here we avoid introducing yet
    another formalism to the paper and keep the text focused on the
    formalism discussed in the mathematical boxes.
