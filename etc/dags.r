library(dagitty)
library(rethinking)

pdf(file="etc/dagA.pdf", width=4, height=4)
dagA <- dagitty("dag { 
    Gender -> CompWork  
    Gender -> Dept
    Dept -> CompWork 
    CompWork -> AcademicSurvival
    Dept -> AcademicSurvival
}")
coordinates(dagA) <- list( x=c(Gender=1,Dept=0,CompWork=2, AcademicSurvival=1) , y=c(Gender=0,Dept=1,CompWork =1, AcademicSurvival=2) ) 
drawdag( dagA)
dev.off()

pdf(file="etc/dagB.pdf", width=4, height=4)
dagB <- dagitty("dag { 
    Gender -> CompWork  
    Gender -> Dept
    Dept -> CompWork 
    CompWork -> AcademicSurvival
    CompWork -> CollabNorms
    Dept -> CollabNorms
    CollabNorms -> AcademicSurvival
    Dept -> AcademicSurvival
}")
coordinates(dagB) <- list( 
    x=c(Gender=1,Dept=0,CompWork=2, CollabNorms=1, AcademicSurvival=1) , 
    y=c(Gender=0,Dept=1,CompWork =1, AcademicSurvival=2, CollabNorms=1.5) 
) 
drawdag( dagB)
dev.off()

pdf(file="etc/dagC.pdf", width=4, height=4)
dagC <- dagitty("dag { 
    Gender -> CompWork  
    Gender -> Dept
    Dept -> CompWork 
    CompWork -> AcademicSurvival
    CompWork -> GroupSize
    CompWork -> LaborAdv
    Dept -> GroupSize
    GroupSize -> CollabNorms
    LaborAdv -> GroupSize
    LaborAdv -> CollabNorms
    CollabNorms -> AcademicSurvival
    Dept -> AcademicSurvival
}")
coordinates(dagC) <- list( 
    x=c(Gender=1,Dept=0,CompWork=2, GroupSize=1,CollabNorms=1, AcademicSurvival=1,LaborAdv=2) , 
    y=c(Gender=0,Dept=1,CompWork =1, CollabNorms=2, GroupSize=1.5, AcademicSurvival=3,LaborAdv=2.5) 
) 
drawdag( dagC)
dev.off()

pdf(file="etc/dagC1.pdf", width=6, height=3)
dagC1 <- dagitty("dag { 
    u [unobserved]
    Dept -> GroupSize
    Dept -> LaborAdv
    GroupSize -> CollabNorms
    LaborAdv -> GroupSize
    LaborAdv -> CollabNorms
    CollabNorms -> AcademicSurvival
    Prestige -> LaborAdv
    u -> AcademicSurvival
    u -> Prestige
}")
coordinates(dagC1) <- list( 
    x=c(Prestige=-0.5, GroupSize=1,CollabNorms=0.5,LaborAdv=0, Dept=0.5, AcademicSurvival=0, u=-0.5) , 
    y=c(Prestige=1, CollabNorms=2, GroupSize=1,LaborAdv=1, Dept=0, AcademicSurvival=2, u=2) 
) 
drawdag( dagC1 )
dev.off()

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


pdf(file="etc/dag3.pdf", width=4, height=5)
dag3 <- dagitty("dag { 
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
    LaborAdv -> GroupSize
    LaborAdv -> CollabNorms
}")
coordinates(dag3) <- list( x=c(LaborAdv=2, CollabNorms=1,GroupSize=1,Gender=1,Dept=0,CompTheoryWork=2,CompDataWork=2) , y=c(LaborAdv=2.5, CollabNorms=3,GroupSize=2,Gender=0,Dept=1,CompTheoryWork =1.5, CompDataWork=0.5) ) 
drawdag( dag3)
dev.off()
