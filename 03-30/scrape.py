import requests
from bs4 import BeautifulSoup

url = "https://www.expats.cz/jobs/offers/it-itc"

response = requests.get(url)

#1.)
soup = BeautifulSoup(response.content, "html.parser")
"""
main_content = soup.find(id="jobs-index")

print(type(main_content))

#print(main_content.prettify())
header = main_content.find(class_="list-header")

print(type(header))
print(header.prettify())

anchor = header.find("a")

print(anchor.text)
"""
#2.)
jobs = soup.find(class_="job-list")

all_jobs = jobs.find_all("article")

print(type(all_jobs))

for job in all_jobs:
    anchor = job.find("h3").find("a")
    print(anchor.text)
    print(anchor["href"])


soup.select("div .list-header")