import requests
from pprint import pprint
from bs4 import BeautifulSoup
from scripts.settings import FIXTURE_PATH


URL = "https://en.wikipedia.org/wiki/List_of_goddesses"
html = requests.get(URL).content
data = BeautifulSoup(html, "html.parser")

pay_load = data.find("div", {"class": "mw-parser-output"})
pay_load.find('div', class_='toclimit-3').decompose()
assets = pay_load.select('ul')

goddesses = []
remove = ['lists of deities', 'cpu', 'oh my goddess!',
    'cautious hero', 'the three shaman queens[3]',
    'holy spirit is feminine for some christians[2][better\xa0source\xa0needed]',
    'aka "the goddess"', 'turquoise woman); yoołgai asdzą́ą́ ',
    'loviatar / louhi'

    ]
add = ['aka', 'loviatar', 'louhi']
new_lines_correction = []
multi_name_correction = []
slash_correction = []
hyphen_correction = []
zerox_correction = []
coma_correction = []
clean = []

for asset in assets:
    word = ((asset.text).lower()).strip()
    goddesses.append(word)

'''
    Think of the following code as smaller and smaller
    shifters of powder. Goddesses are in a rough html
    structure.
'''
for goddess in goddesses:
    if '\n' in goddess:
        new_lines_correction.extend(goddess.split('\n'))
    else:
        new_lines_correction.append(goddess)

for goddess in new_lines_correction:
    if '(' in goddess:
        goddess = goddess.split('(')
        goddess[-1] = goddess[-1].replace(')', '')
        multi_name_correction.extend(goddess)
    else:
        multi_name_correction.append(goddess)

for goddess in multi_name_correction:
    if '/' in goddess:
        goddess = goddess.split('/')
        slash_correction.extend(goddess)
    else:
        slash_correction.append(goddess)

for goddess in multi_name_correction:
    if ' - ' in goddess:
        goddess = goddess.split('-')
        hyphen_correction.append(goddess[0])
    else:
        hyphen_correction.append(goddess)

for goddess in hyphen_correction:
    if '\xa0:' in goddess:
        goddess = goddess.split('\xa0: ')
        zerox_correction.append(goddess[-1])
    elif '\xa0[zh]' in goddess:
        goddess = goddess.replace('\xa0[zh]', '')
        zerox_correction.append(goddess[-1])
    else:
        zerox_correction.append(goddess)

for goddess in zerox_correction:
    if ', ' in goddess:
        goddess = goddess.split(', ')
        coma_correction.extend(goddess)
    else:
        coma_correction.append(goddess)

for goddess in zerox_correction:
    if goddess not in remove: 
        goddess = goddess.strip()
        clean.append(goddess)
clean.extend(add)

# Sort & dedup.
coma_correction.sort()
clean = list(dict.fromkeys(coma_correction))

f = open(f"{FIXTURE_PATH}/english-goddesses.txt", 'w')
for word in clean:
    if len(word) >= 3:
        f.write(word)
        f.writelines('\n')
f.close()


