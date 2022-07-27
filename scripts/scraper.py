import requests
from bs4 import BeautifulSoup

# import pdb; pdb.set_trace()
def run_scraper():
    URL = "https://a-z-animals.com/animals/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    html = soup.prettify("utf-8")

    with open("tests/fixtures/english-animals-2.html", "wb") as file:
        file.write(html)


    import pdb; pdb.set_trace()

