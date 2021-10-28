
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

From the previous sections you may have understood this is an **application project**. 
We are going to do some experiments on the two graphs we are presented above in order to achieve some interesting results.
Below I will present some of them and their objectives:

- *Clustering*: the goal of this experiment is to define/calculate clusters on both graphs and compare them for the purpose of find some similar clusters.
- *Centralities of cities*: the goal is to calculate various types of centralities of all cities on both graphs and compare them in order to find a sort of similarity.
- *Graphs feature*: the goal here is to calculate the feature of the graphs and compare them in order too see the differences and maybe extract some interesting results.
- *Distances between nodes*: the goal is to do some experiments on the graphs paths. For example, we want to calculate the shortest path from two cities in both graphs and try to find intereting comparing results. 
- [*in progress...*]

I have to say that these points can change during the project development: some of them can be crucial in order to obtain interesenting results, some of them instead can be useless and so to leave out. 
In order to approach all these experiments with the right tools, we will use our knowledge acquired by the *Learning From Network* course itself and obviously we will probably use some sort of pre-implemented libraries for the purpose of making our life easier.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTI1NTkyMDY3MiwtMjA4NTA4MDEwMywzNT
I1NTMzMzFdfQ==
-->