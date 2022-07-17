import csv

with open(r'resources/username.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)