import glob
import os
import json
import pandas as pd

from googletrans import Translator
from pprint import pprint
from typing import List, Dict


# import pdb; pdb.set_trace()
def translate():
    '''
        Loads, reads, translates, QAs, & prints english words to spanish.
        Saves new csv file for each file in collections.
    '''
    translator = Translator()
    translation = translator.translate('dragon', src='en', dest='es')
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
    # csv_files = get_csv_file_paths()
    # total_translated_lists = {}

    # for file in csv_files:
    #     f = open(f"tests/fixtures/{file.split('/')[-1]}.txt", 'w')
    #     print(f"Working on translating {file.split('/')[-1]} into spanish...")
        
    #     # Read csv file
    #     df = pd.read_csv(file)
    #     shape = df.shape
    #     spanish_translations = []

    #     # Iterate down column 0, translate + clean word.
    #     for index in range(shape[0]):
    #         eng_word = df.values[index, 0]
    #         translation = translator.translate(eng_word, src='en', dest='es')
    #         spanish_translations.append((((translation.text).lower()).strip()).replace(" ", ""))
    #         # print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

    #     # Remove dups
    #     spanish_translations = list(dict.fromkeys(spanish_translations))
    #     for word in spanish_translations:
    #         f.write(word)
    #         f.writelines('\n')
    #     f.close()


def get_csv_file_paths(csv_files: str = '/collections') -> List[str]:
    '''
        Load CSV files.
        csv_files (str): Location of csv files
    '''
    path = os.getcwd()
    path = path + csv_files
    return glob.glob(os.path.join(path, "*.csv"))


def load_fixture(file_path='/tests/fixtures', fix_name=None):
    '''
        Inject fixtures so we dont need to 
        run calculations each time.
    '''
    # Set fixture vars
    FIX_BASE = path = os.getcwd()
    SWAGGER_FIX = 'example_ingestion_manager_swagger.json'

    fixture_path = f'{ os.getcwd()}{file_path}'
    with open(fixture_path) as json_file:
        fixture = json.load(json_file)
    return fixture
