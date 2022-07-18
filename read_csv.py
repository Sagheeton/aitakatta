import csv

def test_some_value(file):
    with open(file) as f:
        csvreader = csv.DictReader(f, delimiter=';')
        list_f = list(csvreader)
        assert list_f[0]['First name'] == 'Rachel', 'First name is not Rachel'
