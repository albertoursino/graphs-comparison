import SisterCities
import AirlineRoutes
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

node = s_citiesG.nodes['Q84']
print(node['country'])