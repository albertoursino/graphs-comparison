# Midterm Project Report
In this short paper we are going to present what we have done up to now.
In order to clarify the context for the reader, we give some useful links:

 -  [Project presentation paper](https://github.com/albertoursino/GraphsComparison/blob/main/README.md);
 - [GitHub project repository](https://github.com/albertoursino/GraphsComparison).

## Updates

**Graphs structure**:

Here's a detailed description of the current graphs we are working on:
1) The airline routes graph: each node represents an airport in the world: it includes the city name, the geographic coordinates of the airport and the country. Two nodes are linked if there exists a route between the airports.
2) The twinning-relationships graph: each node represents a city in the world: it includes the city name, the geographic coordinates, the population and the country. Two nodes are linked if they are twinned.
3) A reduced version for each graph 1) and 2): only nodes appearing on both graphs are kept, the others are discarded (i.e. each twinned city must have an airport and viceversa)
4) Countries graphs: in addition to the previously described graphs, we decided to integrate an alternative graph structure in our analysis. For both the twinning-relationships graph and the airline routes graph we built a corresponding one as follows:
   - the vertices are representative of the countries around the world
   - every edge between two countries is weighted with the number of occurrencies of edges between the two locations in the original graph  

   The reason behind this choice is the will to better capture eventual relationships between twinning relationships and air traffic, adopting a more macroscopic perspective.
  

**Numerical results**:

[...]

## **Notes**
The main objective of this project has not changed: we're aiming to find similarities between the "sister cities" graph and the "airline routes" graph.

During the start of the project we encountered some small issues with the datasets: 
the first dataset is the result of a query to Wikidata Query Service, and consists of cities all over the world along with their sister cities (we filtered this set by selecting cities with population > 10000); each city is an entity identified by a code in Wikidata, which can be used to retrieve information about the city, such as its label (i.e. its real name in English, for instance London), its country, its population, etc. The other dataset comes from Openflights (https://github.com/jpatokal/openflights), and represents some common airline routes among cities in the world, which are identified by their names (while airports by their airpoirt codes). Since this dataset does not use the same scheme as the previous one, there were a series of issues, which in part have not been solved yet: we cannot compare cities using Wikidata id, so we relied just on names, which however sometimes are not always equal, due to different encodings, like `Tel Aviv` and `Tel-Aviv` or `San José` and `San Jose`. When we retained common cities, in order to compare the two graphs, we took into account these different encodings, by lower casing the strings and stripping the weird accents. Another problem of these two datasets is that common nodes are very few (~ 800) with respect to the total number of cities (~ 4500) or airports (~ 3000) (due to the fact that cities with airports do not appear very often in the first dataset). 

TODO: EXPLAIN WHY WE SHOULD CONSIDER A DIFFERENT GRAPH, WHICH TAKES INTO ACCOUNT MOVEMENTS (city close to airport X which is bonded to city close to airport Y and there exists a route between X and Y)

Some nice pictures of the two datasets on a world map can be found on the repository (link above).


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTAxOTU3NDUwOSwtOTk2MDMwMTA2LDIxMD
I2NzQ3OTQsLTIwNzA0NzQzMjQsMTUxODEwMTc3NCwtMTc0NTI1
ODk1MywxNjY1NjYyNjA0XX0=
-->
