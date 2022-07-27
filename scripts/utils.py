import os
import json
import glob
from typing import List, Dict
from scripts.settings import (
    FIXTURE_PATH
)

def load_fixture(file_name='ES-nouns-verbs.json'):
    '''
        Fixtures to mock objects.
        - ES-nouns-verbs.json: all English nouns & verbs translated into Spanish.
        - english-animals.html: from https://a-z-animals.com/animals/
    '''
    full_fixture_path = f'{os.getcwd()}{FIXTURE_PATH}/{file_name}'
    with open(full_fixture_path) as json_file:
        fixture = json.load(json_file)
    return fixture


def get_csv_file_paths(csv_files: str = '/collections') -> List[str]:
    '''
        Load CSV files.
        csv_files (str): Location of csv files
    '''
    path = os.getcwd()
    path = path + csv_files
    return glob.glob(os.path.join(path, "*.csv"))
