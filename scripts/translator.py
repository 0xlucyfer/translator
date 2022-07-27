
import pandas as pd

from googletrans import Translator
from pprint import pprint
from scripts.utils import (
    load_fixture,
    get_csv_file_paths
)

# import pdb; pdb.set_trace()
def translate():
    '''
        Loads, reads, translates, QAs, & prints english words to spanish.
        Saves new csv file for each file in collections.
    '''
    translator = Translator()
    csv_files = get_csv_file_paths()
    total_translated_lists = {}

    for file in csv_files:
        f = open(f"tests/fixtures/{file.split('/')[-1]}.txt", 'w')
        print(f"Working on translating {file.split('/')[-1]} into spanish...")
        
        # Read csv file
        df = pd.read_csv(file)
        shape = df.shape
        spanish_translations = []

        # Iterate down column 0, translate + clean word.
        for index in range(shape[0]):
            eng_word = df.values[index, 0]
            translation = translator.translate(eng_word, src='en', dest='es')
            spanish_translations.append((((translation.text).lower()).strip()).replace(" ", ""))
            # print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

        # Remove dups
        spanish_translations = list(dict.fromkeys(spanish_translations))
        for word in spanish_translations:
            f.write(word)
            f.writelines('\n')
        f.close()
