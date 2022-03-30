import requests
from bs4 import BeautifulSoup

url = "https://www.expats.cz/jobs/offers/it-itc"
#url = "https://api.github.com/user"
#url = "https://twitter.com/search?q=python"


response = requests.get(url)

# jen kontrola jestli nevznikla chyba
response.raise_for_status()

#with open("soubor.html", "wb") as input:
#    input.write(response.content)

soup = BeautifulSoup(response.content)


