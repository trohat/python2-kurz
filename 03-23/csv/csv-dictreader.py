import csv

with open("data.csv") as infile:
    csv_file = csv.DictReader(infile, delimiter=",")
    for row in csv_file:
        print(row)
        print(f'Jméno: {row["jmeno"]}, Firma: {row["pracoviste"]}, Plat: {row["plat"]}')

      