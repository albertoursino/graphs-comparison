# Midterm Project Report
In this short paper we are going to present what we have done since now.
In order to clarify the context for the reader, we give some useful links:

 -  [Project presentation paper](https://github.com/albertoursino/GraphsComparison/blob/main/README.md);
 - [GitHub project repository](https://github.com/albertoursino/GraphsComparison).

## Updates

**Graphs structure**:

[...]

**Countries graphs**:

[...]

**Numerical results**:

[...]

## **Notes**
The main objective of this project has not changed: we're aiming to find similarities between the "sister cities" graph and the "airline routes" graph.

During the start of the project we encountered some small issues with the datasets: 
the first dataset is the result of a query to Wikidata Query Service, and consists of cities all over the world along with their sister cities (we filtered this set by selecting cities with population > 10000); each city is an entity identified by a code in Wikidata, which can be used to retrieve information about the city, such as its label (i.e. its real name in English, for instance London), its country, its population, etc. The other dataset comes from Openflights (https://github.com/jpatokal/openflights), and represents some common airline routes among cities in the world, which are identified by their names (while airports by their airpoirt codes). Since this dataset does not use the same scheme as the previous one, there were a series of issues, which in part have not been solved yet: we cannot compare cities using Wikidata id, so we relied just on names, which however sometimes are not always equal, due to different encodings, like `Tel Aviv` and `Tel-Aviv` or `San José` and `San Jose`. When we retained common cities, in order to compare the two graphs, we took into account these different encodings, by lower casing the strings and stripping the weird accents. Another problem of these two datasets is that common nodes are very few (~ 800) with respect to the total number of cities (~ 4500) or airports (~ 3000) (due to the fact that cities with airports do not appear very often in the first dataset).

Some nice pictures of the two datasets on a world map can be found on the repository (link above).


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTAxOTU3NDUwOSwtOTk2MDMwMTA2LDIxMD
I2NzQ3OTQsLTIwNzA0NzQzMjQsMTUxODEwMTc3NCwtMTc0NTI1
ODk1MywxNjY1NjYyNjA0XX0=
-->
