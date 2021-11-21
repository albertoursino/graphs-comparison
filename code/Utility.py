import csv
import os
import pathlib

wd_path = os.path.abspath(os.path.join(pathlib.Path().resolve(), '..'))

# If the files airports.dat and/or routes.dat are updated then we should update also routes_complete.csv
# -> update = True
update = False


def create_routes_complete():
    # TODO: Function which (re)creates routes_complete.csv from airport.dat and routes.dat
    pass


def read_routes():
    """
    Reads the file "routes_complete.csv"
    :return: matrix with all "routes_complete.csv" entries
    """
    # Before reading routes_complete.csv we check if it should be update
    if update:
        create_routes_complete()
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
