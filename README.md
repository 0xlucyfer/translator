# translator

I should have unit tests for this but I dont.
I do test everything manually from my terminal using import pdb; pdb.set_trace().

Clean list = lower-cased, striped of white space on R/L, & alphabetical (a-z) desc.

- Clone
- Run `python3 -m venv venv`.
- Run `. venv/bin/activate`.
- Run `npm i`
- Run `python install -e .`.
- Run `run` to execute script.

### Commands
- Run `clean spanish-animals.txt ` creates a clean list - and creates a no spaces list based off cleaned list. Location is /tests/fixtures/*.txt.
- Run `run-csv` to translate existing ens.vision csv files into another language.
- Rub `run-txt english-animals.txt spanish-animals.txt spanish-animals-nospaces.txt` to translate a cleaned text file into another language, and produce a hash ready file.
- Run `animals cleaned-animals.txt cleaned-animals-nospaces.txt`  to scrape animals & produce a hash ready file.


#### working on starwars characters
https://en.wikipedia.org/wiki/List_of_Star_Wars:_Knights_of_the_Old_Republic_characters
https://en.wikipedia.org/wiki/List_of_Star_Wars_Legends_characters
https://en.wikipedia.org/wiki/Droid_(Star_Wars)#List_of_droid_characters
https://en.wikipedia.org/wiki/List_of_Star_Wars_characters