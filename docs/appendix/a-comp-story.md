<style type="text/css">
.gallery {
  margin: 2rem -1rem;
  gap: 2rem;
  max-width: calc(840px + 2rem);
}

.gallery a {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
}

.gallery img {
  max-width: 100%;
  border-radius: 8px;
  box-shadow: 0 0 0 0.75px rgba(128, 128, 128, 0.2), 0 6px 12px 0 rgba(0, 0, 0, 0.2);
  aspect-ratio: 2500 / 1900;
}
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
  max-width: calc(100%);
  margin: 1rem;
  display: block;
  margin-left: auto;
  margin-right: auto;
}

figcaption code {
  font-size: 90%; /* TODO move to global.css */
}

</style>


# Appendix A: The history of the computational turn

## The prehistory of the computational turn

- [My Mother Was a Computer (2005)](https://press.uchicago.edu/ucp/books/book/chicago/M/bo3622698.html)
- [When Computers Were Human (Sept 2007)](https://press.princeton.edu/books/paperback/9780691133829/when-computers-were-human)
- [Coding Freedom: The Ethics and Aesthetics of Hacking (2012)](https://press.princeton.edu/books/paperback/9780691144610/coding-freedom)
- [Programmed Inequality (2018)](https://mitpress.mit.edu/9780262535182/programmed-inequality/)
- [The Gendered History of Human Computers (June 2019)](https://www.smithsonianmag.com/science-nature/history-human-computers-180972202/)
- [The Secret History of Women in Coding (June 2019)](https://www.nytimes.com/2019/02/13/magazine/women-coding-computer-programming.html)
- [Coders: Who They Are, What They Think and How They Are Changing Our World (2019)](https://books.google.ca/books/about/Coders.html?id=q72OEAAAQBAJ&source=kp_book_description&redir_esc=y)
- [The Impact of Women in Computer Science History: A Post-War American History (June 2019)](https://www.cs.ubc.ca/~mochetti/files/journal02.pdf)
- [Women in Computing (May 2020)](https://www.sciencemuseum.org.uk/objects-and-stories/women-computing)
- [Changing the Curve: Women in Computing (2021)](https://ischoolonline.berkeley.edu/blog/women-computing-computer-science/)
- [There Are Too Few Women in Computer Science and Engineering (2022)](https://www.scientificamerican.com/article/there-are-too-few-women-in-computer-science-and-engineering/)

## Computational X

We provide a whirlwind tour of computational X and a brief depiction of what it means for each of them.

### Computational Physics

The computational turn in Physics was barely noticeable. For physicists, it was about using computers to do computation, thus computational physics. It was more about the pitfalls of numerical methods, and how to write efficient code, than promoting F/OSS. That said, in some parts of physics, early on there was also the realization tha computers were more than computations; it was about sharing code, data, analysis, reproducibility, etc. 

 - [Computational Physics (2013)](https://public.websites.umich.edu/~mejn/cp/)
 - [Python for Astronomers (2014)](http://ugastro.berkeley.edu/pydecal/textbook.pdf)

### Computational linguistics

As we saw, the computational turn in linguistics was perhaps one of the most acrimonious divorce (the first of the digital humanities).

 - [Computational Linguistics, Volume 19, Number 1, March 1993, Special Issue on Using Large Corpora: I](https://aclanthology.org/J93-1000.pdf)
 - [Computational Linguistics and its Use in Real World:
the Case of Computer Assisted-Language Learning](https://aclanthology.org/C96-2171.pdf)
 - [LINGUISTICS IN A COMPUTATIONAL WORLD](https://www.ideals.illinois.edu/items/11601/bitstreams/42397/data.pdf)

### Computational Journalism

 - [11.3: Computational Journalism](https://socialsci.libretexts.org/Bookshelves/Communication/Journalism_and_Mass_Communication/The_American_Journalism_Handbook_-_Concepts_Issues_and_Skills_(Zamith)/11%3A_Future_of_Journalism/11.03%3A_Computational_Journalism)

### Computational Ecology

- [Computational ecology as an emerging science(2012)](https://royalsocietypublishing.org/doi/10.1098/rsfs.2011.0083)

### Computational Finance 

- [https://www.math.cmu.edu/users/bscf/](https://www.math.cmu.edu/users/bscf/whatis.html)

### Computational Statistics

Very related to computational thinking, simulating and bootstrapping is easier than understanding the mathematics behind the p-values.

 - [Jake Vanderplas - Statistics for Hackers - PyCon 2016](https://www.youtube.com/watch?v=Iq9DzN6mvYA)

### Computational Social Science, digital humanities, and Cultural Analytics

Manifestos

 - [Life in the network: The coming age of computational social science: Science](https://www.semanticscholar.org/paper/Life-in-the-network%3A-The-coming-age-of-social-Lazer-Pentland/eb2269b4fcd83ec96e7f2fca1becd5958ac28c9b)
 - [Computational social science: Obstacles and opportunities (2020)](https://www.semanticscholar.org/paper/Computational-social-science%3A-Obstacles-and-Lazer-Pentland/c1e49d830e67269d4d2053a5f124ea773c79b740)
 - [Text mining for social science - The state and the future of computational text analysis in sociology (2022)](https://www.semanticscholar.org/paper/Text-mining-for-social-science-The-state-and-the-of-Macanovic/f0c6fb5d5f632aed414fa2354fc240685b52783b)
 - [Integrating explanation and prediction in computational social science (2021)](https://www.semanticscholar.org/paper/Integrating-explanation-and-prediction-in-social-Hofman-Watts/16cd0cadc4a757d85da6bd72992f6fb75a685ac7)
 - [Manifesto of computational social science](https://www.semanticscholar.org/paper/Manifesto-of-computational-social-science-Conte-Gilbert/0888bb211901eaac37b19a7e4a5096006349c4d5)
 - [Computational Social Science and Sociology.](https://www.semanticscholar.org/paper/Computational-Social-Science-and-Sociology.-Edelmann-Wolff/be5b11775e2e4a32c1b6dca28c7b24eb158059f6?sort=total-citations)
 - [Text as Data: The Promise and Pitfalls of Automatic Content Analysis Methods for Political Texts](https://www.semanticscholar.org/paper/Text-as-Data%3A-The-Promise-and-Pitfalls-of-Automatic-Grimmer-Stewart/b9921fb4d1448058642897797e77bdaf8f444404)
 - [Large-Scale Computerized Text Analysis in Political Science: Opportunities and Challenges](https://www.semanticscholar.org/paper/Large-Scale-Computerized-Text-Analysis-in-Political-Wilkerson-Casas/0d345c2fb459e6ecc28328917ab37a4707e4a502)
 - [Extracting Policy Positions from Political Texts Using Words as Data](https://www.semanticscholar.org/paper/Extracting-Policy-Positions-from-Political-Texts-as-Laver-Benoit/7d9cc63dfbd34acf271e3a2c922ea1c07fb2f482)

#### The debate 

 - [Teaching Computational Social Science for All (2020)](https://www.cambridge.org/core/journals/ps-political-science-and-politics/article/teaching-computational-social-science-for-all/66EAB886BCF21C647E2387051D6A9BEF)
 - [Computational Analysis of Political Texts: Bridging Research Efforts Across Communities](https://www.semanticscholar.org/paper/Computational-Analysis-of-Political-Texts%3A-Bridging-Glavas-Nanni/4dea8e7bbc8f59b0307879121f5f8eab0848dd06)
 - [For a heterodox computational social science](https://www.semanticscholar.org/paper/For-a-heterodox-computational-social-science-T%C3%B6rnberg-Uitermark/3a45303cf6fb902bbff653e2e1dbb1dcb4ca531c)

## Computational Theories

Sometimes, what we mean by computational is not that we use computers. It is that a process is computational. For instance, the 'computational theory of the mind' (CCTM) says that the mind is something akin to a computer. It is tied to the computational turn in science, but you do not need a computer to do research on CCTM. If anything, it a topic of predilections for armchair philosophers.

Another edge case for our purpose is the philosophy of computational thinking. With the rise of computational works, researchers started to realize that using computers as cognitive aids can benefit more than computer scientists. Computational thinking is learning known mathematical skills---sequences, differential calculus, all kinds of mathematical abstractions---but with computer programs. The original proponents, people like Seymour Papers, Alan Kay, and Jeannette Wing, sit at the intersection of computer science and education. They use programming language, such as the LOGO programming language, or SCRATCH, as medium to teach people of all age a compuatational way of thinking about problems.

Some works on computational thinking definitely are definitely computational works, some others are conceptual. This is a hard one to disambiguate.

- [Computational Thinking (2006)](https://www.cs.cmu.edu/~15110-s13/Wing06-ct.pdf)


