import os
import csv
import pathlib
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import networkx as nx

wd_path = os.path.abspath(os.path.join(os.path.join(pathlib.Path().resolve(), '..'), '..'))
def read_routes():
    rows = []
    file = open(wd_path + "/data/airline_routes_data/routes_complete.csv", encoding="utf-8")
    csv_reader = csv.reader(file)
    first = 0
    for row in csv_reader:
        if first == 0:
            first += 1
            continue
        rows.append(row)
    return rows

#All the nodes will be stored in "cities", all the edges in "edges" and in positions the coordinates
#associated to each city.
cities = []
edges = []
positions = {}
routes = read_routes()
#It iterates only the first 150 routes in order to avoid entries with "N/D" values
for entry in routes[0:150]:
    cities.append(entry[4])
    cities.append(entry[9])
    edges.append((entry[4],entry[9]))
    positions[entry[4]] = (float(entry[6]),float(entry[5]))
    positions[entry[9]] = (float(entry[11]),float(entry[10]))

G = nx.Graph()
G.add_nodes_from(cities)
for edge in edges:
    #Each edge will be weighted based on how many times the edge shows up.
    if G.has_edge(edge[0], edge[1]):
        G[edge[0]][edge[1]]['weight'] += 1
    else:
        G.add_edge(edge[0], edge[1], weight=1)

ax = plt.axes(projection=ccrs.PlateCarree())
ax.stock_img()
nx.draw_networkx_nodes(G, positions, node_size=2, nodelist=cities)
nx.draw_networkx_edges(G, positions, edgelist=edges)
plt.show()

#TODO: the graph needs to be restyled, because now it's painful to watch
#TODO: we need to decide how to manage the pathological entries of routes_complete.csv