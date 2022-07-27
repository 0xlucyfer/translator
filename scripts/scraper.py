import requests
from pprint import pprint
from bs4 import BeautifulSoup
from scripts.settings import (
    FIXTURE_PATH
)
from scripts.utils import (
    load_fixture
)


# ANIMALS_PATTERN = r"<a href=.*>(.*)</a>"

# import pdb; pdb.set_trace()
def run_scraper():
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
                extracted.append(link[0].strip())

                if len(link) == 2:
                    link = link[1].replace(')', "")
                    link = link.strip()
                    extracted.append(link)

    f = open(f"tests/fixtures/english-animals.txt", 'w')
    for element in extracted:
        f.write(element)
        f.writelines('\n')
    f.close()
