import csv
import os
import pathlib

wd_path = os.path.abspath(os.path.join(os.path.join(pathlib.Path().resolve(), '..'), '..'))


# TODO: Function which creates routes_complete.csv from airport.dat and routes.dat

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
