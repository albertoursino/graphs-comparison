import json
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import networkx as nx
import wdutil

from pathlib import Path

cities = {}
sisters = set()
query = Path('big-sister-cities.sparql').absolute().read_text()
prefixes = ['city', 'sister']


def add_city(record, cid, prefix):
    if cid in cities:
        cities[cid]['degree'] += 1
    else:
        lon, lat = wdutil.coord(record[f'{prefix}_coordinate_location']['value'])
        cities[cid] = {
            # How many times we encounter this city
            'degree': 1,
            # This is the the name of the city or its sister depending on prefix
            'label': record[f'{prefix}Label']['value'],
            'lon': lon,
            'lat': lat,
            'pop': int(record[f'{prefix}_population']['value'])
        }


resp = wdutil.request(query)

for record in resp['results']['bindings']:

    # in general we get something like http://www.wikidata.org/entity/Q84 (London)
    # we retain only the code Q84

    city_id = record['city']['value'].split('/')[-1]
    sister_id = record['sister']['value'].split('/')[-1]

    relation_id = tuple(sorted([city_id, sister_id]))
    sisters.add(relation_id)

    add_city(record, city_id, prefix='city')
    add_city(record, sister_id, prefix='sister')

with open('big-sister-cities.json', 'w') as f:
    json.dump({'cities': cities, 'sisters': list(sisters)}, f)


G = nx.Graph()
for cid, attr in cities.items():
    # attr is a dictionary with information about the city
    G.add_node(cid, **attr)
for sister in sisters:
    G.add_edge(sister[0], sister[1])
nx.write_gexf(G, 'big-sister-cities.gexf')


if __name__ == "__main__":
    G=nx.readwrite.read_gexf('big-sister-cities.gexf')
    positions = {}
    for node, d in G.nodes(data=True):
        positions[node] = (d['lon'],d['lat'])
    print(positions)
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1], projection=ccrs.PlateCarree())
    #ax.background_img(name='BM', resolution='high')
    ax.background_img()

    nx.draw_networkx_nodes(G, positions, node_size=0, nodelist=cities)
    nx.draw_networkx_edges(G, positions, edgelist=G.edges, width=0.5, edge_color="red")
    plt.show()
