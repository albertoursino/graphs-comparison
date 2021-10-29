
# Comparison between the graphs "sister cities" and "airline routes"

This is the presentation paper of a *Learning From Network* course's project.
In the following sections we will present the project idea, the results we are hoping to obtain and finally the material we currently have and some details of our way to procede.

## Motivation
Town-twinning is a particular relationship stipulated between two localities, whose goal is to promote a mutual enrichment of cultural, diplomatic, social and/or economic nature. The fact that such agreement is not exclusive allows city administrations to negotiate more relations of this kind, more likely on an international level. All these links build a dense and capillary network between cities across the world.

A “sister city” bond often materializes in trading opportunities and cultural exchanges, encouraging travels that put in contact citizens and companies from different localities. For example, Boston University fosters study abroad programs for college students in the twinned city of Padua. At this point, a question rises: do these partnerships have any influence on the intensity of air traffic between sister cities (taking into account the fact that generally some destinations have to be reached through one or more stopovers)?

The purpose of the project is to analyze **two graphs**:

1.  The first of them is representative of the network of **twinning relations** around the globe, where each vertex stands for a city. All the necessary data for its implementation will be extracted by executing a SPARQL query using the Wikidata’s Query Service, since no raw dataset concerning this topic has been found.
    
2.  The second graph depicts a global mapping of all the **airline routes** connecting different cities, weighted with the amount of flights during a certain time lapse. We will probably use the [Tyler Woebkenberg's dataset](https://data.world/tylerudite/airports-airlines-and-routes).
    
## Method

### Problems
We would like to compute:
1. Betweeness centralities and closeness centralities for each node of both networks
2. Compute clusters in order to identify communities, for example, see whether European cities are more likely to establish a "sister city" bond within Europe, as well as for other countries like U.S. between American cities
3. Compute some graph-level features, for instance [TO DO]
### Algorithms
For 1) we will try to use exact algorithms; if, however, the graph is too large or the computation requires time, we will try approximate algorithms, such as Eppstein-Wang or Chechik-Cohen. For 2) there are at least two approaches, like graph embeddings or cluster algorithms specific to graphs. We haven't covered them yet [TO DO]

## Intended experiments

From the previous sections you may have understood this is an **application project**: we are going to do some experiments on the two graphs we have presented above, in particular, we're aiming to discover their similarities.

**Experiments** we have decided to do, and their goals:
- ***Centralities of cities***: calculate various types of centralities of all the nodes on both graphs and compare them for the purpose of finding an eventual correlation.
- ***Graphs feature vector***: extract the feature vector of both graphs and compare them with the intention of looking at the differences and maybe extract some interesting results.
- ***Distances between cities***: analyze some graphs paths (e.g. the shortest path from two cities in both graphs) and try to find similarities. 
- ***Clustering***: compute clusters on both graphs and compare them in order to find some similar clusters.
- [*in progress...*]

**Libraries**: NetworkX, Pandas, Numpy, Matplotlib, [...]
**Machine for experiments**: Ryzen 2600x, RTX 3060, 16GB of RAM, >100GB of disk space. We will probably run the code on the [IntelliJ IDEA](https://www.jetbrains.com/idea/) environment.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTU1NjczNjQ2OCwxODA4NDQ0MTA1LDI2OD
EzMzg3NSwtMTE1MDAxMzA3OSw1MzY2Nzk3NDksLTgwOTQ2MDUx
MSwtMjExOTg1MjMzNSwxMjU1OTIwNjcyLC0yMDg1MDgwMTAzLD
M1MjU1MzMzMV19
-->