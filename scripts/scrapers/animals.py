import requests
import sys
from pprint import pprint
from bs4 import BeautifulSoup
from scripts.settings import FIXTURE_PATH
from scripts.utils import normalize_file

ADD = [
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
    'hydra',
    'leprechauns'
    'cyclops'
    'ogre'
    'goblins'
    'goblin'
    'fairies'
    'fairy'
    'hadas'
    'gorgon'
    'mermaid'
    'minotaur'
    'centaur'
    'centaurs'
    'fauns'
    'faun'
    'werewolf'
    'loch ness monster'
    'griffin'
]

REMOVE = [
    'asp',
    'american wirehair traits: what to know before you buy',
    'sphynx traits: what to know before you buy'
]

## As time goes on the community will add/remove/ammend animals on the list.
def run_scraper():
    '''
        Extracts all animals from "https://a-z-animals.com/animals/".
        
        sys.argv[1]: location to save cleaned animal words.
        Ex.          $ animals 'cleaned-animals.txt`
    '''

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
                    link = ((link[1].replace(')', "")).strip()).lower()
                    extracted.append(link)

    # Have all animals, cleaned.
    extracted.extend(ADD)

    # Save cleaned animals into text file.
    try:
        f = open(f"{FIXTURE_PATH}/{sys.argv[1]}", 'w')
    except IndexError as ie:
        print(f"CMD: `$ animals file1.txt file2-nospaces.txt`")
        sys.exit("Invalid run command.")
        
    for element in extracted:
        f.write(element)
        f.writelines('\n')
    f.close()

    # Feed cleaned file, creates alphabetical + no spaces text files.
    normalize_file(f"{FIXTURE_PATH}/{sys.argv[1]}")
