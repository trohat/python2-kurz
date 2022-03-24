import requests
import json
from pprint import pprint

response = requests.get("https://swapi.dev/api/")

#result = json.loads(response.text)

#vysledek = response.json()

#pprint(vysledek["planets"])

#response2 = requests.get("https://swaxpi.dev/api/planets")
#vysledek2 = response2.json()
#pprint(vysledek2)
print(response.status_code)


