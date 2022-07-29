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


def create_ordered_alpha_txt_files(file = None):
    '''
        Takes a clean text file as input.
        Clean = lower cased & stripped of white spaces on both sides.

        Creates an ordered (alphabetical) text file & a hash ready
        no spaces file. 
    '''
    # Read from cleaned transated words file.
    with open(f"{FIXTURE_PATH}/{file}.txt", 'r') as f:
        lines = f.readlines()

    clean = []
    for line in lines:
        clean.append(line.replace('\n', ""))
    clean.sort()
    
    # Create alphabetical ordered text file.
    f = open(f"{FIXTURE_PATH}/{file}-ordered.txt", 'w')
    for word in clean:
        f.write(word)
        f.writelines('\n')
    f.close()

    # Create no spaces files from alphabetical file.
    f = open(f"{FIXTURE_PATH}/{file}-ordered-nospaces.txt", 'w')
    for word in clean:
        f.write(word.replace(' ', ''))
        f.writelines('\n')
    f.close()
