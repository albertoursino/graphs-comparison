import SisterCities
import AirlineRoutes
import Utility
import networkx as nx

s_citiesG = None
routesG = None

try:
    s_citiesG = nx.readwrite.read_gexf('../data/sister_cities_data/big-sister-cities.gexf')
except FileNotFoundError:
    s_citiesG = SisterCities.build_graph()

try:
    routesG = nx.readwrite.read_gexf('../data/airline_routes_data/routes.gexf')
except FileNotFoundError:
    routesG = AirlineRoutes.build_graph()

#node = s_citiesG.nodes['Q84']
#print(node['country'])


#Removing nodes not in common between the two graphs
to_remove = []
for i in s_citiesG.nodes:
    sc = s_citiesG.nodes[i]
    correspondance = False
    for j in routesG.nodes:
        rc = routesG.nodes[j]
        if (Utility.remove_diacritics(sc['label']) == Utility.remove_diacritics(rc['label'])) and\
           (sc['country'] == rc['country']):
            correspondance = True
    if not correspondance:
        to_remove.append(i)
s_citiesG.remove_nodes_from(to_remove)
nx.write_gexf(s_citiesG, '../data/sister_cities_data/big-sister-cities.gexf')


to_remove = []
for i in routesG.nodes:
    rc = routesG.nodes[i]
    correspondance = False
    for j in s_citiesG.nodes:
        sc = s_citiesG.nodes[j]
        if (Utility.remove_diacritics(rc['label']) == Utility.remove_diacritics(sc['label'])) and\
           (rc['country'] == sc['country']):
            correspondance = True
    if not correspondance:
        to_remove.append(i)
routesG.remove_nodes_from(to_remove)
nx.write_gexf(routesG, '../data/airline_routes_data/routes.gexf')
