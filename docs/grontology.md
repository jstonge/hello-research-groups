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

</style>

<div>${resize((width) => 
  Plot.plot({
    width,
    height: 600,
    marginLeft: 150, marginBottom: 50, marginRight: 180,
    x: { axis: null },
    y: { axis: null, domain: [-200 / 2, 200 / 2] },
    marks: [
      Plot.ruleY([0]),
      Plot.ruleX(data, {
        x: "year",
        y: (d, i) => (i % 2 === 0 ? 25 : -25)
      }),
      Plot.dot(data, { x: "year", fill: "#fff", stroke: "#000" }),
      Plot.text(data, {
        x: "year", y: (d, i) => (i % 2 === 0 ? -4 : 4 ), text: (d) => d.year.toString()
      }),
      Plot.image(data, {
        x: "year",
        y: (d, i) =>
          i % 2 === 0
            ? 30 + d.numberOfLines * 16 * 0.5
            : -30 - d.numberOfLines * 16 * 0.5,
        src: "link",
        width: 270,
        title: "text"
      })
    ]
  })
)}
</div>

```js
const data = [
  {
    year: 1956,
    numberOfLines: 3,
    link: "https://raw.githubusercontent.com/jstonge/hello-research-groups/main/docs/assets/campbell.webp"
  },
  {
    year: 1990,
    numberOfLines: 3,
    link: "https://raw.githubusercontent.com/jstonge/hello-research-groups/main/docs/assets/boyd_richerson_1989.webp"
  },
  {
    year: 2006,
    numberOfLines: 3,
    link: "https://raw.githubusercontent.com/jstonge/hello-research-groups/main/docs/assets/gilbert.webp"
  },
  {
    year: 2016,
    numberOfLines: 3,
    link: "https://raw.githubusercontent.com/jstonge/hello-research-groups/main/docs/assets/tomlinson.webp"
  }
]
```

# Grontology

In the previous section, we defined the rise of computational works as a shifting ground that might benefit particular research groups. To show that, we need to define what are groups and why they matter.

## Back to the basics

We like to put marbles, books, or cards that share some quality or feature together. This shared property---color, size, and so---allows for ordering. We call this ordered collection a grouping, or cluster, and they sometime serve a functional goal, such as search for a good hand in card games. Or not, putting similar marbles or books together based on color might just be pleasing. Philosophers call this grouping 'nautral kinds'. Similarly, one can cluster  based on relation of interest. For instance, Mars and Jupiter are similar in that they orbit the sun. Otherwise, they couldn't be more different as planet.

A persisting fact in social psychology is how WEIRD people put individuals, or entities, before interactions. When asked to introspect during the 'who am i' test, psychologists found again and again that WEIRD people define themselves in terms of individual attributes. In many other cultures, such as Japan, they might define themselves with respect to their relationships, e.g. 'I am Sora's professor' instead of 'I am a teacher'. Thus, another way to group stuff is based on relationship, e.g. 'the hammer is to the nail as the screwdriver is to the screw'. In linguistics, we can think of pairs of words co-ocuring. In Jane Austin's Pride and Prejudice, 'Elizabeth' is most correlated with words such as 'looked',  'walked', 'sat', 'listened, or 'answered'. 

We can build networks out of these interactions because we now have a notion of nodes and edges. Until recently, researchers in network science did not realize how useful it is to adopt edge-first view; clustering on links lead naturally to the idea of hierarchy (groups part of groups) and overlapping communities (I am both a teacher and a father) [CITE BAGROW]. 

Those parts composing the interactions might or might not entail _intentionality_; intentional agents have mental states. Note the difference here between a grouping with or without intentionality. A group of sperm whales can be classified as such based on some shared features, regardless them being intentional agents. Or they can be called a group based on intentional features, such as males believing they are not part of their family groups. Indeed, most sperm whales have a matrilineally based social organization, meaning that males tend to leave the clans while female offsprings stay with their moms (CITE whitehead). The grouping has some intentionality; there is a sense where individuals have mental states that can tell whether they are part of the group or not. The young males "believe" they are not part of their mothers' group when they come to age, not unlike how traditional matrilineal societies work in humans. 
