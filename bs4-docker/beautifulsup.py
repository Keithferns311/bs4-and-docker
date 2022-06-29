from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.bbc.com/')
html=response.text
soup = BeautifulSoup(html, 'html.parser')
title=soup.find_all("a",class_="block-link__overlay-link")
summary=soup.find_all("p", class_="media__summary")
# for link in soup.find_all("a",class_="block-link__overlay-link"):
#     for summary in soup.find_all("p", class_="media__summary"):
#         print(f"Title\tlink.string.strip()\n")
#         print("Summary\t summary")
for index in range(len(summary)):
    print(f"Title {index}:\t{title[index].string.strip()}\nSummary:\t{summary[index].string.strip()}\n")