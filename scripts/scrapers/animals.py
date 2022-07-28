import requests
import sys
from pprint import pprint
from bs4 import BeautifulSoup
from scripts.settings import (
    FIXTURE_PATH
)


## As time goes on the community will add/remove/ammend animals on the list.
def run_scraper():
    '''
        Extracts all animals from "https://a-z-animals.com/animals/".
        Creates/Writes two files. Sys.arg1
        
        sys.argv[1]: location to save cleaned animal words - txt.
        Ex.          $ animals 'cleaned-animals.txt`
        sys.argv[2]: location to save cleaned animal words with
                     no spaces - txt. This makes the words hash ready.
        Ex.          $ animals cleaned-animals.txt cleaned-animals-nospaces.txt
    '''
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
                    link = ((link[1].replace(')', "")).strip()).lower()
                    extracted.append(link)

    # Save animals into text file.
    try:
        f = open(f"{FIXTURE_PATH}/{sys.argv[1]}", 'w')
    except IndexError as ie:
        print(f"CMD: `$ animals file1.txt file2-nospaces.txt`")
        sys.exit("Invalid run command.")
        
    for element in extracted:
        f.write(element)
        f.writelines('\n')
    for element in add: # Add missing animals.
        f.write(element)
        f.writelines('\n')
    f.close()

    try:
        # Save cleaned animals words without spaces for correct ens hashes.
        f = open(f"{FIXTURE_PATH}/{sys.argv[2]}", 'w')
    except IndexError as ie:
        print(f"CMD: `$ animals file1.txt file2-nospaces.txt`")
        sys.exit("Invalid run command.")

    for element in extracted:
        f.write(element.replace(" ", ""))
        f.writelines('\n')
    for element in add:
        f.write(element.replace(" ", ""))
        f.writelines('\n')
    f.close()
