library(dagitty)
library(rethinking)

pdf(file="etc/dag1.pdf", width=4, height=5)
dag1 <- dagitty("dag { 
    Gender -> CompWork  
    Gender -> Dept
    Dept -> CompWork  
    Dept -> GroupSize
    Dept -> CollabNorms
    CompWork -> GroupSize
    CompWork -> CollabNorms
    GroupSize -> CollabNorms
}")
coordinates(dag1) <- list( x=c(CollabNorms=1,GroupSize=1,Gender=1,Dept=0,CompWork=2) , y=c(CollabNorms=3,GroupSize=2,Gender=0,Dept=1,CompWork =1) ) 
drawdag( dag1)
dev.off()



pdf(file="etc/dag2.pdf", width=4, height=5)
dag2 <- dagitty("dag { 
    Gender -> CompTheoryWork  
    Gender -> CompDataWork  
    Gender -> Dept
    Dept -> CompTheoryWork  
    Dept -> CompDataWork  
    Dept -> GroupSize
    Dept -> CollabNorms
    CompTheoryWork -> GroupSize
    CompDataWork -> GroupSize
    CompTheoryWork -> CollabNorms
    CompDataWork -> CollabNorms
    GroupSize -> CollabNorms
}")
coordinates(dag2) <- list( x=c(CollabNorms=1,GroupSize=1,Gender=1,Dept=0,CompTheoryWork=2,CompDataWork=2) , y=c(CollabNorms=3,GroupSize=2,Gender=0,Dept=1,CompTheoryWork =1.5, CompDataWork=0.5) ) 
drawdag( dag2)
dev.off()