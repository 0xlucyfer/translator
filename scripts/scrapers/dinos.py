import requests
from pprint import pprint
from bs4 import BeautifulSoup
from scripts.settings import FIXTURE_PATH


URL = "https://www.thoughtco.com/dinosaurs-a-to-z-1093748"
html = requests.get(URL).content
data = BeautifulSoup(html, "html.parser")

pay_load = data.find("div", {"class": "comp structured-content expert-content mntl-sc-page mntl-block"})
dinos = pay_load.select('p')
dinos =  dinos[4:]
clean = []

add = []
counter = 0

for dino in dinos:
    inside_anchor = dino.select('a')
    # - r REMOVE
    if counter == 696 or counter == 392 or counter == 391 or \
       counter == 311 or counter == 206 or counter == 205 or counter == 310:
        counter += 1
        continue

    if inside_anchor != []:
        clean.append((inside_anchor[0].text).lower().strip())
    else:
        word = (dino.text).split('-')
        word = word[0].replace('\n', '').strip().lower()
        clean.append(word)
    counter += 1

# Sort & dedup.
clean.sort()
clean = list(dict.fromkeys(clean))

f = open(f"{FIXTURE_PATH}/english-dinosaurs.txt", 'w')
for word in clean:
    if len(word) >= 3:
        f.write(word)
        f.writelines('\n')
f.close()