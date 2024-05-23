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

# Computational hysteresis in the social sciences

In the previous sections, we defined the computational turn and reviewed literature on various non-meritocratic factors that shape academia, e.g. institutional prestige and labor advantage, the unequal impact of parenthood, and gendered attrition in faculty careers. Here, we begin to put everything together to show how the computational turn, via _computational hysteresis_, ought to exacerbate some of the observed gendered bias observed in academia, if nothing is done. 

Hysteresis is a well-known idea from physics applied to a plethora of domains. In ecology, this is tied to alternative stable states and critical transition. Empirically, ecologists are interested in how perturbation to an ecosystem force communities  out of their original stable state.

## A group-based master equations model of hysteresis

Group-based master equations (GBMs) in which we track probability distribution over groups instead of tracking populational averages. For instance, think about how researchers learn to model epidemic. Often, they use homgenous mean-field equations, where susceptible individuals might infected in proportion of average number of infected individuals in the population. In this family of models, it is assumed that all individuals can randomly bounce in each other, potentially infecting each other. Instead of assuming random mixing, GBMs track the probability of groups in a certain state, say a group of seven individuals with three infected individuals, to move to a state with four infected individuals. With this structure, researchers can model how groups are doing in managing the epidemic. If individuals are in a group with strong mask policy, the probability to flow from a state of three to four infected individuals might be much more slim than without it. When keeping track of groups, it is easier to thinking of ingroup effects in the context of many other groups.


