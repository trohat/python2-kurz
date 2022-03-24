import csv

with open("nova_data2.csv", "w", newline="") as outfile:
    zapisovac = csv.DictWriter(outfile, fieldnames=["jmeno", "prijmeni", "vek"])
    zapisovac.writeheader()
    zapisovac.writerow({"jmeno": "Anna", "prijmeni": "Novakova", "vek": 28})
    zapisovac.writerow({"jmeno": "Eva", "prijmeni": "Cerna", "vek": 35})
    zapisovac.writerow({"jmeno": "Jana", "prijmeni": "Bila", "vek": 15})