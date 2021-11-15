import csv
import os
import pathlib
import networkx as nx
from tqdm import tqdm
import matplotlib.pyplot as plt

wd_path = os.path.abspath(os.path.join(os.path.join(pathlib.Path().resolve(), '..'), '..'))
G = nx.Graph()


def main():
    airports_set = read_airports()
    routes = read_routes()

    print(airports_set[0])
    print(read_routes()[0])
    # print(wd_path)

    # range(100) because I need to test the method fast (can't wait to plot more then 5k airports).
    for i in tqdm(range(6)):
        # Take an airport from the "airport.dat" dataset
        source_airport = airports_set[i]
        # Extrapolate its city (the source city)
        city = source_airport[2]
        # Extrapolate its ID
        source_airport_ID = source_airport[8]
        print(city, source_airport_ID)
        if city != "":
            for route in routes:
                # From all the routes I need to find the destination airports from the initial airport
                if route[3] == source_airport_ID:
                    # I have found one!
                    destination_airport_ID = route[5]
                    # Now I need to find the city of this "destination airport" (destination city)
                    for dest_airport in airports_set:
                        if dest_airport[8] == destination_airport_ID:
                            if dest_airport[2] != "":
                                dest_city = dest_airport[2]
                                # Let's create an edge between the "source city" and the "destination city"
                                G.add_edge(city, dest_city)
    nx.drawing.draw(G, node_size=10)
    # TODO: show the graph on a planisphere
    # TODO: Give the name only to nodes which have more than x neighbours
    # TODO: Weight edges
    plt.show()


def read_airports():
    """
    Reads the data from the file "airports.dat"
    :return:
    """
    rows = []
    file = open(wd_path + "/data/airline_routes_data/airports.dat", encoding="utf-8")
    csv_reader = csv.reader(file)
    for row in csv_reader:
        rows.append(row)
    return rows


def read_routes():
    """
    Reads the data from the file "routes.dat"
    :return:
    """
    rows = []
    file = open(wd_path + "/data/airline_routes_data/routes.dat", encoding="utf-8")
    csv_reader = csv.reader(file)
    for row in csv_reader:
        rows.append(row)
    return rows


if __name__ == "__main__":
    main()
