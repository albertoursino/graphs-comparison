from pathlib import Path
import networkx as nx
from tqdm import tqdm
import Utility

cities = {}
sisters = set()
prefixes = ['city', 'sister']


def add_city(record, cid, prefix):
    """
    # TODO
    :param record:
    :param cid:
    :param prefix:
    :return:
    """
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
            'pop': int(record[f'{prefix}_population']['value']),
            'country': record[f'{prefix}_countryLabel']['value']
        }


def parse_response(resp):
    """
    # TODO
    :param resp:
    :return:
    """
    for record in tqdm(resp['results']['bindings'], desc="Parsing"):
        # in general we get something like http://www.wikidata.org/entity/Q84 (London)
        # we retain only the code Q84
        city_id = record['city']['value'].split('/')[-1]
        sister_id = record['sister']['value'].split('/')[-1]

        relation_id = tuple(sorted([city_id, sister_id]))
        sisters.add(relation_id)

        add_city(record, city_id, prefix='city')
        add_city(record, sister_id, prefix='sister')


def build_graph():
    """
    Builds the sister cities graph inserting nodes (cities) and edges (sister bond)
    :return: an instance of the graph
    """
    query = Path('../data/sister_cities_data/big-sister-cities.sparql').absolute().read_text()
    resp = Utility.request(query)
    parse_response(resp)
    G = nx.Graph()
    for cid, attr in tqdm(cities.items(), desc="Adding nodes"):
        # attr is a dictionary with information about the city
        G.add_node(cid, **attr)
    for sister in tqdm(sisters, desc="Adding edges"):
        G.add_edge(sister[0], sister[1])
    nx.write_gexf(G, '../data/sister_cities_data/sister_cities.gexf')
    return G


def main():
    G = build_graph()
    Utility.save_plot(G, 'sister_cities_data/complete_sister_cities_plot.png')


if __name__ == "__main__":
    main()
