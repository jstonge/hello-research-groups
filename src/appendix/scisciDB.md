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


# scsciDB: a science of science database

[scisciDB](https://github.com/jstonge/scisciDB) is a database that seek to facilitate the study of the science of science. The database distinguish itself from others by integrating two complementary, open-source databases, namely AllenAI's Semantic Scholar and OpenAlex, as well as manually collected data. 

The **Semantic scholar** database is awesome because it offers parsed scientific texts; they parse texts to make easily accessible the content of articles at the section-level and have fine-grained reoslution of the whole citation graph.They also open-source their own model for classifying field of studies, as well as the [SPECTER2 embedding model](https://blog.allenai.org/specter2-adapting-scientific-document-embeddings-to-multiple-fields-and-task-formats-c95686c06567), which is a state-of-the-art model of a scientific embedding space.

The **OpenAlex database** has the benefit of having richer metadata; institutions, funders, authors, works, topics are well integrated. We can easily ask questions such as, for instance, how much papers from a particular institution are open-access. Or what is the proportion of public/private funding for all authors across institutions.

On top of the OpenAlex and Semantic Scholar databases, we add some of our own data collected in other ways. A shared weakness by both databases is their poor coverage of the social sciences and humanities. This is because they both use the same indexed database to construct their own database; pubmed, arxiv, DBLP, etc. Most of their indexed database show a bias towards STEMs, computer science, and biomed. We supplement some of the data on our database with available social science and humanities data out there, which we then parse using semantic scholar's software stack.

To facilitate data collection, we like to upload articles by journals. This is helping to stay consistent for the dark-data project. We have a collection in our database dubbed `extra-journals`. We adopt `openAlex` schema as key identifiers for journals and papers.

Lastly, we also supplement information about key **funding agencies** in science; namely the NSF (US), NEH (US), SSHRC (CAN), NSERC (CAN), and ERC (EU). Albeit openAlex have metadata about papers being funded by one of those funding agencies, we wanted to know what projects are being funded at large. 

As part of the thesis, we maintain this database for various projects. For instance, in one project we are interested in knowing the proportion of papers with data availability statements across time and field of studies. To answer this question, we need (i) a way to delineate what constitute a representative sample of science at large and (ii) full content of papers to identify the data availability statements. To delineate the field of studies, this project use all available papers from top venues by field from Google Scolar, as it is widely utilized scheme to determine field of studies. This is a good example where we need to use information from both databases via `scisciDB`, as we first need to know what the venues of the papers (openAlex), then match that to get the content of the papers (semantic scholar).

In the current context, we need to have full content of papers to determine whether the work is computational or not. Similarly, to know if authors are professors and have research groups, we need metadata about them and their coauthors.

## Staying relevant

The DB strives to be useful on the long run, which is a non-trivial goal. Most small-scale projects tend to have short-term vision, which is favoring good enough code over more complex infrastructure. There are good reason for that, as we are scientists and not software engineers. But in reality, any code we envision begin used on longer term must adhere to good software engineering practices to stay relevant. Good software engineering practices are the results of years of painful realizations about how to make code useful on the long run. 

Here is our guideline to make our database useful and even reproducible on the long run; 

 1. `Knowing why we need this database in a first place`: This database is higher-level, meaning that the strength of this database is to _facilitate interoperability between databases of larger institutions_, such as semantic scholar, JSTOR, and openAlex. As such, it is less about scraping data (as openAlex and semantic scholar do) than streamlining our data schema to facilitate interoperability. 
 1. `Our database must remain in sync with its data sources`: If our database is unable to keep up with new works, it'll become obsolete. We take advantage of recent developments from openAlex and Semantic scholar, who are both offering ways to take `diff` between snapshots, i.e. the difference between a previous snapshot and newest one. JSTOR is more difficult to work with, as they neither offer a snapshot of their data, or a easy way to stay update with new works.
 1. `Satisficing best software practices`: To satisfice means to do something that is good enough. Here we want the code to be as much extensible and transparent as possible, but no more. If we do not have pleasure coming back to the codebase, we won't maintain the database for very long.