import csv

with open("data.csv") as infile:
    csv_file = csv.reader(infile, delimiter=",")
    muj_list = []
    for row in csv_file:
        print(row)
        print(f"Jméno: {row[0]}, Firma: {row[1]}, Plat: {row[3]}")
        muj_list.append(row)

print(muj_list)

        