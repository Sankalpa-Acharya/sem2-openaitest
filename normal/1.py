 in csv

import csv

with open('output.csv', 'w') as csvfile:

writer = csv.writer(csvfile, delimiter=',')

writer.writerow(['column 1', 'column 2', 'column 3'])