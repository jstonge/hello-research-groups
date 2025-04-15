# Multiverse literature review

## Groups are real. A synthesis.

We review the study of groups across the multiverse of scientific research. The topic is vast, with countless ways to discuss groups. We could explore the grouping of objects, or how the structure of living systems is shaped by social organizations. We could focus on how human societies are influenced by the rise of formal institutions and firm selection. To navigate this multiverse, we ask how key fields of study have addressed the following questions:

<div class="tldr">
  <ul>
      <li>Who has argued for the reality of groups?</li>
      <li>What was their underlying ontology or motives? Did they believe that group interactions were in some way irreducible to the actions of individuals?.</li>
      <li>What was their modeling approach?</li>
      <li>How do classical notions of groups align with modern higher-order representations of group structure and dynamics?</li>
  </ul>
</div>

<div class="grid grid-cols-2">
  <div>

  **Groups in the Social Sciences**: By social sciences, we refer to fields focused on the study of humans and driven by theoretical frameworks, often building on the legacy of their intellectual forebears. Traditionally, these fields have relied on verbal models and experiments. This category includes conformity studies and group psychology (e.g., Asch et al.), sociologists influenced by Georg Simmel, and evolutionary-minded scholars like Donald Campbell, David Hull, and Bill Wimsatt. We also include sociologists and anthropologists who have developed social network analysis.

  **Group Selection in Biology**: In the 1960s, Wynne-Edwards proposed that groups could serve as a legitimate level of selection. His idea suggested that traits could evolve not for the benefit of individuals but because they are advantageous to groups, initially framed in terms of population regulation. This concept faced strong opposition from biologists. Models of kin selection and evolutionary game theory were central to the ensuing debate.

  **Firms as Groups**: TODO

  **Public Good Games**: Derived from Elinor Ostrom's work on social dilemmas, this body of literature utilizes public good games to study group dynamics. The central idea is how groups can self-govern in the face of social dilemmas under specific conditions. Groups can develop sets of rules to avoid the tragedy of the commons, demonstrating that they are not as 'mindless' as once thought. Notably, this literature often focuses on smaller groups, where a strong sense of joint commitment to common-pool resources is evident.

  **Team Science**: Beginning in the 1980s and 90s, management and business sciences recognized that efficient teams can be more productive. Since then, this idea has been applied across various domains—business, sports teams, research groups, software development, and more. Over time, this concept has integrated with complex systems thinking. While all teams are groups, not all groups function as teams; teams are often described as more synergistic.

  **Cultural Group Selection**: Emerging from population biology, cultural group selection theory integrates covariance genetics and game theory to explore the conditions under which group-beneficial traits can evolve through group selection processes. The theory arose from 1960s debates about altruism and the notion that reciprocity alone may not sufficiently explain large-scale cooperation among unrelated individuals. A key result driving group selection is the Price equation, applied to groups of individuals whose norms maintain between-group variance while reducing within-group cultural variation.

  **The Ontology of Groups**: Collective intentionality seeks to explain the sense that a collective is more than just the sum of individual intentions. As Searle puts it, there is a 'we' that transcends individual actions, like friends walking together—an experience that goes beyond each person merely intending to walk. This concept also manifests in the impersonal 'we' that members of a society feel, motivating collective actions such as going to war or experiencing pride when a local sports team wins a championship.

  **Groups as Higher-Order Networks**: Social scientists are interested in higher-order structures such as triangles, cliques, and clubs. However, here we refer to the community of network scientists who draw from a toolbox rooted in physics, most notably statistical physics and information theory. In contrast to social scientists, the focus of their work often lies in the analytical results and modeling details.
  
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
</div>





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
          height: 1400,
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

