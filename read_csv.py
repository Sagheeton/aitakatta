import csv

with open(r'username.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)