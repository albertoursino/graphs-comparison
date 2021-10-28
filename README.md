
# Comparison between the graphs "sister cities" and "airline routes"

This is the presentation paper of a *Learning From Network* course's project.
In the following sections we will present the project idea, the results we are hoping to obtain and finally the material we currently have and some details of our way to procede.

## Motivation
Town-twinning is a particular relationship stipulated between two localities, whose goal is to promote a mutual enrichment of cultural, diplomatic, social and/or economic nature. The fact that such agreement is not exclusive allows city administrations to negotiate more relations of this kind, more likely on an international level. All these links build a dense and capillary network between cities across the world.

A “sister city” bond often materializes in trading opportunities and cultural exchanges, encouraging travels that put in contact citizens and companies from different localities. For example, Boston University fosters study abroad programs for college students in the twinned city of Padua. At this point, a question rises: do these partnerships have any influence on the intensity of air traffic between sister cities (taking into account the fact that generally some destinations have to be reached through one or more stopovers)?

The purpose of the project is to analyze **two graphs**:

1.  The first of them is representative of the network of **twinning relations** around the globe, where each vertex stands for a city. All the necessary data for its implementation will be extracted by executing a SPARQL query using the Wikidata’s Query Service, since no raw dataset concerning this topic has been found.
    
2.  The second graph depicts a global mapping of all the **airline routes** connecting different cities, weighted with the amount of flights during a certain time lapse. We will probably use the [Tyler Woebkenberg's dataset](https://data.world/tylerudite/airports-airlines-and-routes).
    

From the comparison of the features computed on both these two graphs, the aim is to observe if there is any similarity between them.

## Method

## Intended experiments

From the previous sections you may have understood this is an **application project**: we are going to do some experiments on the two graphs we have presented above, in particular, we're aiming to discover their similarities.

Below we will present some important experiments we decided to do, and their goals:

- *Clustering*: the goal of this experiment is to define/calculate clusters on both graphs and compare them in order to find some similar clusters.
- *Centralities of cities*: the goal is to calculate various types of centralities of all the nodes on both graphs and compare them for the purpose of finding an eventual correlation.
- *Graphs feature*: the goal here is to calculate the feature of the graphs and compare them in order to observe the differences and maybe extract some interesting results.
- *Distances between nodes*: the goal is to do some experiments on the graphs paths. For example, calculate the shortest path from two cities in both graphs and try to find interesting comparing results. 
- [*in progress...*]

We have to say that these points may change during the project development: some of them could be crucial in order to obtain interesenting results, some of them, instead, could be useless and to be left out. 

To approach all these experiments with the right tools, we will use our knowledge acquired by the *Learning From Network* course itself and obviously we will probably use some sort of pre-implemented libraries for the purpose of facilitating the development of the project.
<!--stackedit_data:
eyJoaXN0b3J5IjpbNTAzNjUxNzU4LC0yMTE5ODUyMzM1LDEyNT
U5MjA2NzIsLTIwODUwODAxMDMsMzUyNTUzMzMxXX0=
-->