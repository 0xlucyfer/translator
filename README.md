# translator

I should have unit tests for this but I dont.
I do test everything manually from my terminal using import pdb; pdb.set_trace().

#### Definitions of text file states
- `Clean`: Lower cased, stripped of white spaces on both sides.
- `Normalize`: `Clean` + no white spaces + Spanish words with special characters such as `['á', 'é', 'í', 'ó', 'ú', 'ü', 'ñ']` will include a copy of the word without special characters. 

#### Instructions
- Clone
- Run `python3 -m venv venv`.
- Run `. venv/bin/activate`.
- Run `npm i`
- Run `python install -e .`.

### Commands
- Files should be in `/tests/fixtures/`.
- Run `clean spanish-animals`.
    - Creates a `clean` text file at `/tests/fixtures/*-ordered.txt`.
    - Creates a `normalized` text file at `/tests/fixtures/*.txt`.
    - Normalized words with special characters get a copy of the word without special characters.
    - ![Alt text](public/CMD-$-clean-file1.png?raw=true "Example of files produced.")
- Run `run-csv`.
    - Translates existing English ens.vision csv files into Spanish.
    - CSV files must be in `/collections/*.csv`.
    - Translated file will be in `/tests/fixtures/.*txt`.
    - Language values hardcoded but can be easily changed to be automated.
- Run `run-txt english-animals-file1 spanish-animals-file2`.
    - Input: File1 must exist at `/tests/fixtures/*.txt.`
    - Output: Cleaned translated file2 in `/tests/fixtures/*.txt`. 
- Run `animals cleaned-animals`.
    - Scraper for animals list.
- Run `node scripts/normalize.js`
    - Update the location of a normalized text file on line 8.
    - Prints to console, csv formatted, requirements ready data.
    - Copy text on console into your local copy of ens-collections. Copy into `ens-collections/collections/*.csv`.


#### working on starwars characters
- https://en.wikipedia.org/wiki/List_of_Star_Wars:_Knights_of_the_Old_Republic_characters
- https://en.wikipedia.org/wiki/List_of_Star_Wars_Legends_characters
- https://en.wikipedia.org/wiki/Droid_(Star_Wars)#List_of_droid_characters
- https://en.wikipedia.org/wiki/List_of_Star_Wars_characters