import csv

muj_list = [ ['Anna', 'Google,a.s.', '23', '50000'], ['Pavel', 'Microsoft', '39', '40000'], ['Petr', 'Microsoft', '65', '100000'], ['Monika', 'Github', '43', '60000']]

with open("nova_data.csv", "w", newline="") as outfile:
    zapisovac = csv.writer(outfile, delimiter=",", quotechar="|")
    for rada in muj_list:
        zapisovac.writerow(rada)

