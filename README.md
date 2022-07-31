# translator

I should have unit tests for this but I dont.
I do test everything manually from my terminal using import pdb; pdb.set_trace().

#### Clean List
Lower cased & stripped of white spaces on both sides.

#### Instructions
- Clone
- Run `python3 -m venv venv`.
- Run `. venv/bin/activate`.
- Run `npm i`
- Run `python install -e .`.
- Run `run` to execute script.

### Commands
- Files should be in `/tests/ficxtures/`.
- Run `clean spanish-animals`.
    - Creates a cleaned ordered list.
    - Then creates a no spaces hash ready list (normalized).
    - Normalized words with special characters get a copy of the word without special characters. Ex: `Tiburon` & `Tiburon` are both included in normalized list.
    - ![Alt text](public/CMD-clean-example.png?raw=true "Example of files produced.")
- Run `run-csv`.
    - Translates existing English ens.vision csv files into Spanish.
    - CSV files must be in `/collections/*.csv`.
    - Translated file will be in `/tests/fixtures.*txt`.
    - Language values hardcoded but can be easily changed to be automated.
- Run `run-txt english-animals-file1 spanish-animals-file2`.
    - File one must exist at `/tests/fixtures/*.txt.`
    - Produces a cleaned translated file2 in `/tests/fixtures/*.txt`. 
- Run `animals cleaned-animals`.
    - Scraper for animals list.


#### working on starwars characters
- https://en.wikipedia.org/wiki/List_of_Star_Wars:_Knights_of_the_Old_Republic_characters
- https://en.wikipedia.org/wiki/List_of_Star_Wars_Legends_characters
- https://en.wikipedia.org/wiki/Droid_(Star_Wars)#List_of_droid_characters
- https://en.wikipedia.org/wiki/List_of_Star_Wars_characters