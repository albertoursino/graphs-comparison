import os
from pathlib import Path
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import networkx as nx
from tqdm import tqdm

import Utility

cities = {}
sisters = set()
prefixes = ['city', 'sister']


def add_city(record, cid, prefix):
    if cid in cities:
        cities[cid]['degree'] += 1
    else:
        lon, lat = Utility.coord(record[f'{prefix}_coordinate_location']['value'])
        cities[cid] = {
            # How many times we encounter this city
            'degree': 1,
            # This is the the name of the city or its sister depending on prefix
            'label': record[f'{prefix}Label']['value'],
            'lon': lon,
            'lat': lat,
            'pop': int(record[f'{prefix}_population']['value'])
        }


def parse_response(resp):
    for record in tqdm(resp['results']['bindings'], desc="Parsing"):
        # in general we get something like http://www.wikidata.org/entity/Q84 (London)
        # we retain only the code Q84
        city_id = record['city']['value'].split('/')[-1]
        sister_id = record['sister']['value'].split('/')[-1]

        relation_id = tuple(sorted([city_id, sister_id]))
        sisters.add(relation_id)

        add_city(record, city_id, prefix='city')
        add_city(record, sister_id, prefix='sister')

    # with open('../data/sister_cities_data/big-sister-cities.json', 'w') as f:
    #    json.dump({'cities': cities, 'sisters': list(sisters)}, f)


def build_graph():
    """
    Build the sister cities graph inserting nodes (cities) and edges (sister bond)
    """
    query = Path('../data/sister_cities_data/big-sister-cities.sparql').absolute().read_text()
    resp = Utility.request(query)
    parse_response(resp)
    G = nx.Graph()
    for cid, attr in tqdm(cities.items(), desc="Creating graph"):
        # attr is a dictionary with information about the city
        G.add_node(cid, **attr)
    for sister in sisters:
        G.add_edge(sister[0], sister[1])
    nx.write_gexf(G, '../data/sister_cities_data/big-sister-cities.gexf')
    return G


def plot(G):
    positions = {}
    for node, d in G.nodes(data=True):
        positions[node] = (d['lon'], d['lat'])

    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1], projection=ccrs.PlateCarree())

    wd_path = os.path.abspath(os.path.join(Path().resolve(), '..'))
    os.environ["CARTOPY_USER_BACKGROUNDS"] = wd_path + r"\data\sister_cities_data"
    ax.background_img(name='ETOPO', resolution='high')

    nx.draw_networkx_nodes(G, positions, node_size=0.03, nodelist=cities, node_shape="o", linewidths=0,
                           node_color="black", alpha=0.9)
    nx.draw_networkx_edges(G, positions, edgelist=G.edges, width=0.06, edge_color="red")

    plt.savefig(wd_path + r'/data/sister_cities_data/plotted_graph.png', format='png', dpi=1200)
    plt.show()


# if __name__ == "__main__":
#    main(False, True)
