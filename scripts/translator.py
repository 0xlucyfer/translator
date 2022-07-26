import glob
import os
import json
import pandas as pd

from googletrans import Translator, constants
from pprint import pprint
from typing import List



def translate():
    translator = Translator()
    csv_files = get_csv_file_paths()

    for file in csv_files:
        # Read csv file
        df = pd.read_csv(file)
        # Get df dimensions - (col, row)
        shape = df.shape
        count = 0
        spanish_translations = []

        # Iterate over all columns
        # shape[0] should equal count
        for index in range(shape[0]):
            eng_word = df.values[index, 0]
            translation = translator.translate(eng_word, src='en', dest='es')
            spanish_translations.append(translation.text)
            count+=1
            print(f"EN: {eng_word} || ES: {translation.text}")
            # print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
        break
    import pdb; pdb.set_trace()


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
