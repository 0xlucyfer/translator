import requests
import re
from pprint import pprint
from bs4 import BeautifulSoup
from scripts.settings import (
    FIXTURE_PATH
)
from scripts.utils import (
    load_fixture
)

ANIMALS_PATTERN = r"<a href=.*</a>"

# import pdb; pdb.set_trace()
def run_scraper():
    URL = "https://a-z-animals.com/animals/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="ResultsContainer")

    # html = soup.prettify("utf-8")
    # with open("tests/fixtures/english-animals-2.html", "wb") as file:
    #     file.write(html)

    regex_pattern = re.compile(ANIMALS_PATTERN)
    # x = '<li class="list-item"><a href="https://a-z-animals.com/animals/aardvark/">Aardvark</a></li><li'

    for pay_load in soup.select('div[class*="entry-content"]'):
        animals = pay_load.findAll("div", {"class": "container"})

        for animal in animals:
            import pdb; pdb.set_trace()
            x = re.findall(regex_pattern, animal.text)

    import pdb; pdb.set_trace()
