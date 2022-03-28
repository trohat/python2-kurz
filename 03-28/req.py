import requests
import json

base_url = "https://the-dune-api.herokuapp.com/"
endpoint = "quotes/10"

url = base_url + endpoint

response = requests.get(url)

if response.status_code == 200:
    result = response.json()
    for quote in result:
        pass
        #print(f'Quote n.{quote["id"]}')
        #print("Quote text: ", end="")
        #print(quote["quote"])

else:
    print("There was an error while getting data from an API!")


response = requests.post("https://jsonplaceholder.typicode.com/todos",
         data=json.dumps({"klic":"hodnota"}))
response = requests.post("https://jsonplaceholder.typicode.com/todos",
         json={"klic":"hodnota"})
