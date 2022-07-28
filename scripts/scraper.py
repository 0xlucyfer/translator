import requests
from pprint import pprint
from bs4 import BeautifulSoup
from scripts.settings import (
    FIXTURE_PATH
)


## As time goes on the community will add/remove/ammend animals on the list.
def run_scraper():
    add = [
        'serpent',
        'black widow',
        'antilope',
        'bass',
        'manturon',
        'himalayan bear',
        'orangutan',
        'sea snake',
        'condor',
        'panda',
        'cacatua',
        'dragon',
        'hydra'
    ]
    remove = [
        'asp',
        'american wirehair traits: what to know before you buy',
        'sphynx traits: what to know before you buy'
    ]
    URL = "https://a-z-animals.com/animals/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    
    # Grab CSS animal container.
    animals_container = soup.select('div[class*="entry-content"]')
    animal_hrefs = []
    extracted = []

    # Iterate entire animals container.
    for animals in animals_container:
        # Container with all li objects.
        pay_load = animals.findAll("div", {"class": "container"})

        # Get hrefs in li
        for animal in pay_load:
            links = animal.select('li a[href]')

            # Extract text from link. Those are the animals.
            for link in links:
                link = link.text.split('(')
                extracted.append((link[0].strip()).lower())

                if len(link) == 2:
                    link = link[1].replace(')', "")
                    link = link.strip()
                    extracted.append(link.lower())

    # Needed for directe english to spanish translation.
    f = open(f"tests/fixtures/english-animals.txt", 'w')
    for element in extracted:
        f.write(element)
        f.writelines('\n')
    for element in add:
        f.write(element)
        f.writelines('\n')
    f.close()

    # Need for ENS hashing.
    f = open(f"tests/fixtures/english-animals-nospaces.txt", 'w')
    for element in extracted:
        f.write(element.replace(" ", ""))
        f.writelines('\n')
    for element in add:
        f.write(element.replace(" ", ""))
        f.writelines('\n')
    f.close()
