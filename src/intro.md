# Introduction {#chapter:intro}

## Overview

Humans' unique ability to solve collective action problems arises from
the interplay between complex institutions and our cultural psychology
[@boyd_culture_1988; @ostrom_governing_1990; @north_institutions_1990; @henrich_weirdest_2020].
Consider, for instance, our ancestors on the Great Plains of North
America. For at least the last 10,000 years, hundreds of people have
gathered to hunt bison---animals weighing nearly a metric ton and known
for their agility and strength, as well as their poor eyesight
[@boyd_largescale_2022]. These communal hunts are of particular interest
to anthropologists because they involved high-risk and high-reward
strategies in which diverse sets of individuals had to cooperate and
play specific roles to succeed. As the scale and complexity of
collective challenges expanded---from communal hunts to stateless
warfare to managing contagion in industrial societies---humans innovated
more elaborate sets of rules, norms, and conventions, collectively
referred to as institutions [@north_institutions_1990]. Institutions
structure every aspect of human communal life: maintaining peace,
providing care, enforcing justice, and managing intergroup relations.
Critically, these institutional frameworks co-evolved alongside human
cultural psychology, producing minds finely tuned to group cooperation
and fairness---traits observable even in young children. Remarkably,
even 3- or 4-year-old children demonstrate a deep concern for fairness
in group-based problem-solving tasks [@engelmann_childrens_2019].

Complex systems studies have advanced our understanding of social
phenomena like contagion, innovation, and cooperation
[@newman_networks_2010]. By employing mathematical models that reveal
mechanisms behind emergent behaviors such as tipping points, scaling
laws, and community formation
[@newman_structure_2003; @pastor-satorras_epidemic_2001; @barabasi_emergence_1999].
However, despite their insights, traditional network models often
inherit a physics-based view of individuals as mindless entities
interacting in different spaces. While useful, this approach falls short
of capturing the uniquely human, co-evolutionary dynamics between
individuals and institutions. Institutions are inherently collective
phenomena---group-level features that emerge from our unique capacity
for sophisticated, non-trivial social interactions. Recent work on
higher-order networks (HONs) partially addresses this by modeling group
interactions as involving three or more agents, distinct from the
independent influence of pairwise ties
[@benson_higher-order_2016; @battiston_physics_2021]. Still, this
approach often centers on nonlinear effects within groups, overlooking
the broader institutional contexts in which such interactions unfold.
That is, there are group states beyond higher-order interactions, which
are themselves the product of their own dynamics. More generally, before
effectively modeling institutions, we must refine our understanding of
group interactions themselves. Only then can we better represent the
interaction between individual psychology and different aspects of group
interactions.

##### Networked, group interactions: {#networked-group-interactions .unnumbered}

The study of higher-order interactions has exploded in recent years to
explore different types of group interactions and their impact on system
dynamics [@majhi_dynamics_2022; @ferraz_de_arruda_contagion_2024]. While
many models focus on the nonlinearity of within-group dynamics---e.g.,
quorum effects or threshold contagion---they often overlook other
aspects essential to collective action problems. For example, in the
bison hunts of the Great Plains, coordination among hunting parties
required not only internal role differentiation but also intergroup
cooperation and alignment. Thus, group-level behavior is shaped by
interactions between groups; group dynamics do not operate in isolation.
Theories of collective action make clear that what happens within one
group can strongly depend on what happens in others. Capturing such
dependencies requires not just higher-order structure but mechanisms
that treat groups themselves---not just their members---as coupled,
interacting entities.

##### Institutions co-evolve with individuals: {#institutions-co-evolve-with-individuals .unnumbered}

HONs models often overlook the normative contexts in which group
dynamics unfold. For example, while they capture how co-authorship
patterns of varying orders differ from independent pairwise
collaborations, they rarely consider where and how such group
interactions originate
[@benson_higher-order_2016; @patania_shape_2017; @benson_simplicial_2018; @alvarez-rodriguez_evolutionary_2020; @st-onge_influential_2022].
By bringing institutions into focus---as group-level features that
persist beyond transient multi-way interactions---we open the door to
new questions: for instance, how have co-authorship norms evolved in
response to external pressures to publish more
[@smaldino_natural_2016; @tiokhin_shifting_2024]? By distinguishing
between group states (e.g., publishing norms adopted by research groups)
and individual behaviors, we can better examine how individuals respond
to emerging institutional expectations---recognizing variation in those
responses. To be clear, we do not suggest that modeling co-authorships
as group interactions is incorrect. Rather, we argue that these
interactions are embedded in broader institutional dynamics, which
deserve greater attention through the lens of complex systems modeling.

## Theory and methodological frameworks

The theoretical framing of this thesis sits at the intersection of three
disciplines, namely cultural evolution theory, the philosophy of social
ontology, and complex systems. In doing so, we seek to integrate
insights from different perspectives on groups. Cultural evolution
provides an answer to why and where institutions come from, and why it
makes sense that they persist over generations, while social ontology
explains why the phenomenology of groups goes beyond what is typically
assumed by traditional physics-based models. Taken together, these
dimensions provide a nuanced view of the multi-scale co-evolution of
individuals and groups, without reducing one level to the other.

**Cultural evolution theory:** Cultural evolution is essential in
explaining how shifting our view from simple networks to a group-based
perspective can allow institutions to be perceived as having a degree of
independence from their constituents. Cultural evolution theory studies
culture as a distinct system of inheritance and selection, capable of
producing group-level behaviors and adaptations
[@boyd_culture_1988; @cavalli-sforza_cultural_1981]. It emphasizes the
human capacity for cumulative cultural evolution, also known as the
ratchet effect, through which knowledge builds over generations,
enhancing group fitness in local environments
[@tomasello_why_2009; @tomasello_cultural_1999; @tennie_ratcheting_2009].
In humans, cultural traits have co-evolved with biology over at least
two million years in a process known as gene--culture coevolution. This
has embedded culture into both our environment (i.e., the cultural
niche) and our biological makeup
[@laland_darwins_2018; @tomasello_natural_2014; @laland_how_2010]. As
such, cultural evolutionists are interested in modeling the mechanisms
that explain group-level cultural diversity, typically in traditional
societies [@mcelreath_shared_2001].

A key aspect of cultural psychology is how we coordinate with group
members, teach, and learn from each other
[@reader_social_2002; @henrich_secret_2016]. We use social learning
strategies to decide when and from whom to learn [@laland_social_2004].
When individual learning is costly or outcomes are uncertain, it may be
more effective to copy the majority or those who have succeeded in a
task. Conversely, in rapidly changing environments, it can be wiser to
learn by trial and error, since others' knowledge may be outdated.
Furthermore, beyond social learning strategies, we are characterized by
*over-imitation*, i.e. the tendency to copy both relevant and irrelevant
actions when learning from others
[@henrich_evolution_1998; @henrich_evolution_2001]. In various context,
humans---especially children---have been shown to replicate an adult
demonstrator's exact actions, even when a more efficient method exists
or when imitation leads to failure [@nielsen_overimitation_2010]. By
acquiring an individual psychology that is overly reliant on learning
from each other, we have become a species unique in our ability to trump
our own awareness of failure
[@schmidt_young_2016; @tomasello_differences_2023]. This tendency to
adopt and enforce rules based on others' behaviors, even though it might
be individually costly, is the hallmark of scaffolding institutions at
the group level.

**Social ontology of groups:** This thesis also draws from social
ontology to explore the role of collective intentionality in shaping
group behaviors
[@wittgenstein_philosophical_1953; @searle_construction_1995; @gilbert_walking_1990; @jankovic_routledge_2017].
In phenomenology, intentionality refers to the "about-ness" of human
experience---our capacity to direct thoughts toward objects or
concepts---distinguishing purposeful action from mere stimulus-response
behavior
[@zahavi_phenomenology_2018; @gallagher_phenomenological_2013; @merleau-ponty_phenomenology_1945].
Collective intentionality, then, refers to the shared "we" that
underlies the emotional and cognitive responses individuals make on
behalf of their group. Children, once again, excel at passionately
enforcing made-up rules, even those created moments earlier during an
experiment [@tomasello_differences_2023]. In experimental games, they
begin enforcing social norms as early as age 3 or 4---not because the
rules matter for task success, but because of their shared sense of "you
have to play it this way" [@engelmann_childrens_2019]. As with
over-imitation, they might protest against infringed socially
constructed rules, even though the infringement does not affect them at
all [@schmidt_young_2012]. It is the foundation of culture, where later
on people will likewise express moral outrage or indignation when, say,
other ethnic groups might exhibit different norms than those that are
local customs.

We draw one key insight from the study of intentionality relevant to our
work; there is something essential about how individuals experience the
'we-ness' of groups that defines group membership itself. Prominent
philosophers of social ontology---and many cultural evolutionists---have
argued that humans derive meaning through their participation in groups,
not just through individual reasoning. **In the thesis conclusion, we
refer to this foundational challenge---namely, that group interactions
may depend on the mutual recognition of group membership---as the hard
problem of intentionality.**

##### Methodological Framing: {#methodological-framing .unnumbered}

Our methods draw primarily from the physics of HONs, cultural evolution
theory (i.e., population biology applied to cultural systems), and
evolutionary game theory--particularly models of cultural diffusion in
N-player games
[@boyd_origin_2005; @mcelreath_mathematical_2007; @smaldino_modeling_2023; @bowles_cooperative_2011].
More specifically, we use mean-field theory, which plays a central role
and recurs throughout the thesis
[@kadanoff_more_2009; @guerra_annealed_2010]. Game theory and concepts
of bounded rationality are incorporated when integrating group-level
models, including institutional dynamics, with individual preferences
[@von_neumann_simple_1944; @smith_evolution_1982]. We adopt evolutionary
group dynamics as a framework for studying institutions, applying the
concept of fitness from evolutionary game theory at the group level
(e.g., replicator dynamics). Finally, we use a group-based formalism
that builds on recent work with approximate master equations--a
description of complex networks that captures detailed within-group
dynamics while approximating between-group interactions via mean-field
methods
[@hebert-dufresne_propagation_2010; @osullivan_mathematical_2015; @st-onge_master_2021].

Our ability to cooperate in large-scale collective action problems is
only as complex as the problems we create ourselves. HONs models improve
our understanding of group-based phenomena in all sorts of
contagion---technological innovations, gossip, cultural norms, and
viruses. But each of those contagion processes is equally shaped by our
collective, institutional abilities to act together to influence the
direction they will take. Thus, this thesis explores the importance of
the co-evolution between institutions and individuals. By integrating
insights from different disciplines, we arrive at a novel group-based
formalism in complex systems that is informed by both cultural evolution
and the social ontology of groups. Through modeling group states, we aim
to better capture the unique intricacies of human cultural psychology
and the role of institutions as evolving group-level features.


