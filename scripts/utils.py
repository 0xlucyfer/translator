import os
import json
import glob
import sys
from typing import List, Dict
from scripts.settings import (
    FIXTURE_PATH
)

def load_fixture(file_name='ES-nouns-verbs.json'):
    '''
        Loads Fixtures to mock objects
    '''
    full_fixture_path = f'{os.getcwd()}{FIXTURE_PATH}/{file_name}'
    if 'json' in file_name:
        with open(full_fixture_path) as json_file:
            fixture = json.load(json_file)
    elif 'html' in file_name:
        with open(full_fixture_path, "r", encoding='utf-8') as f:
            fixture= f.read()
    return fixture


def get_csv_file_paths(csv_files: str = None) -> List[str]:
    '''
        Load CSV files at location.
    '''
    path = os.getcwd()
    path = path + csv_files
    return glob.glob(os.path.join(path, "*.csv"))


def alpha_order_list():
    # Read from cleaned transated words file.
    with open(f"{FIXTURE_PATH}/spanish-verbs.txt", 'r') as f:
        lines = f.readlines()

    clean = []
    for line in lines:
        clean.append(line.replace('\n', ""))
    clean.sort()
    # import pdb; pdb.set_trace()

    
    f = open(f"{FIXTURE_PATH}/spanish-verbs-ordered.txt", 'w')
    for word in clean:
        f.write(word)
        f.writelines('\n')
    f.close()

    f = open(f"{FIXTURE_PATH}/spanish-verbs-ordered-nospaces.txt", 'w')
    for word in clean:
        f.write(word.replace(' ', ''))
        f.writelines('\n')
    f.close()



alpha_order_list()