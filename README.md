
# Find similarities between two particular graphs

![Airline Routes](https://github.com/albertoursino/GraphsComparison/blob/main/data/airline_routes_data/complete_routes_plot.png?raw=true)![Sister Cities](https://github.com/albertoursino/GraphsComparison/blob/main/data/sister_cities_data/complete_sister_cities_plot.png?raw=true)
This is the presentation paper of a *Learning From Network* course's project.
In the following sections we will present the project idea, the results we are hoping to obtain and finally the material we currently have and some details of our way to procede.

## Motivation

Town-twinning is a particular relationship stipulated between two localities, whose goal is to promote a mutual enrichment of cultural, diplomatic, social and/or economic nature. The fact that such agreement is not exclusive allows city administrations to negotiate more relations of this kind, more likely on an international level. All these links build a dense and capillary network between cities across the world.

A “sister city” bond often materializes in trading opportunities and cultural exchanges, encouraging travels that put in contact citizens and companies from different localities. For example, Boston University fosters study abroad programs for college students in the twinned city of Padua. At this point, a question rises: do these partnerships have any influence on the intensity of air traffic between sister cities (taking into account the fact that generally some destinations have to be reached through one or more stopovers)?

The purpose of the project is to analyze **two graphs**:

1.  The first of them is representative of the network of **twinning relations** around the globe, where each vertex stands for a city. All the necessary data for its implementation will be extracted by executing a SPARQL query using the Wikidata’s Query Service, since no raw dataset concerning this topic has been found.
    
2.  The second graph depicts a global mapping of all the **airline routes** connecting different cities, weighted with the amount of flights during a certain time lapse. We will probably use the [Tyler Woebkenberg's dataset](https://data.world/tylerudite/airports-airlines-and-routes).

## Intended Experiments

As you may have understood, this is an **application project**: we are going to do some experiments on the two graphs we have presented above, in particular, we're aiming to discover their similarities.

**Experiments** we have decided to do, and their goals:
- ***Centralities of cities***: calculate various types of centralities of all the nodes on both graphs and compare them for the purpose of finding an eventual correlation.
- ***Graphs feature vector***: extract the feature vector of both graphs and compare them with the intention of looking at the differences and maybe extract some interesting results.
- ***Distances between cities***: analyze some graphs paths (e.g. the shortest path from two cities in both graphs) and try to find similarities. 
- ***Clustering***: compute clusters on both graphs and compare them in order to find some similar clusters.
- [*maybe others...*]

**Libraries**: networkx, matplotlib, cartopy, csv, requests, unicodedata2, re

**Machine for experiments**: We have a computer with the following hardware: Ryzen 2600x, RTX 3060, 16GB of RAM and >100GB of disk space. We will probably run the code on the [IntelliJ IDEA](https://www.jetbrains.com/idea/) environment using Python as a programming language.


## Algorithms

In general, we will try to use exact algorithms; if, however, the graph is too large or the computation requires too much time, we will try approximate algorithms, such as ***Eppstein-Wang*** or ***Chechik-Cohen***. 

For the clustering experiment there are at least two approaches; for example "graph embeddings" or specific cluster algorithms for graphs. 

There are certainly other algorithms that we can come up with but we are going to learn them later during the course.

## Bibliography
- [Not all paths lead to Rome: Analysing the network of sister cities](https://arxiv.org/abs/1301.6900)
- [OpenFlights](https://openflights.org/data.html) + [jpatokal](https://github.com/jpatokal)/**[openflights](https://github.com/jpatokal/openflights)**
- [yaph](https://github.com/yaph)/**[big-sister-cities](https://github.com/yaph/big-sister-cities)**
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTA5NDUzMzMxNiw4NTI3NDYxNjEsMTQ4Mj
c4MTQ2OCwxMTIzNDUwMTQ2LDg3NjQxMzA0NiwtMjkwNjc3MzY4
LC0xOTE5ODA4NzMsNzUwMjQyNDQ2LDE3NDI1NjczOTMsMTU1Nj
czNjQ2OCwxODA4NDQ0MTA1LDI2ODEzMzg3NSwtMTE1MDAxMzA3
OSw1MzY2Nzk3NDksLTgwOTQ2MDUxMSwtMjExOTg1MjMzNSwxMj
U1OTIwNjcyLC0yMDg1MDgwMTAzLDM1MjU1MzMzMV19
-->