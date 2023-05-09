

import csv

with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(["Name", "City", "Country"])
    writer.writerow(["Diane Murray", "Seattle", "United States"])
    writer.writerow(["Tom Cruise", "Los Angeles", "United States"])
    writer.writerow(["CcuttingEdge", "New York", "United States"])
    writer.writerow(["Gavin Holmes", "Berlin", "Germany"])