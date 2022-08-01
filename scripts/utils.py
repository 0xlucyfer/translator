import os
import json
import glob
import sys
import unicodedata
from typing import List, Dict
from scripts.settings import (
    FIXTURE_PATH,
    SPANISH_TILDES,
    NORMALIZE_WORD,
    CLEAN_WORD
)
from unittest.mock import mock_open


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

def get_text_file_paths(txt_files: str = None) -> List[str]:
    '''
        Load CSV files at location.
    '''
    path = os.getcwd()
    path = path + txt_files
    return glob.glob(os.path.join(path, "*.txt"))


def create_ordered_alpha_txt_files(file = None):
    '''
        Takes an uncleaned file and produces a cleaned &
        normalized file.
    '''
    # import pdb; pdb.set_trace()
    if file == None:
        file = sys.argv[1]

    # Read from uncleaned file.
    with open(f"{FIXTURE_PATH}/{file}.txt", 'r') as f:
        lines = f.readlines()

    clean = []
    for line in lines:
        clean.append(line.replace('\n', ""))
    clean.sort()
    
    # Produces cleaned file.
    f = open(f"{FIXTURE_PATH}/{file}-{CLEAN_WORD}.txt", 'w')
    for word in clean:
        f.write(word)
        f.writelines('\n')
    f.close()

    # Produced normalized file.
    f = open(f"{FIXTURE_PATH}/{file}-{NORMALIZE_WORD}.txt", 'w')
    for word in clean:
        word = word.replace(' ', '')
        f.write(word)
        f.writelines('\n')
        
        # If word is special, create non-special copy.
        if tilde_identifier(word) == True:
            non_tilde_copy = remove_accents(word)
            f.write(non_tilde_copy)
            f.writelines('\n')
    f.close()


# tilde_identifier('drügonñátest')
def tilde_identifier(word : str = None):
    '''
        Answers, does word contain any special characters.
    '''
    if any(tilde in word for tilde in SPANISH_TILDES):
        print(f"Tilde found in {word}.")
        return True
    return False


def remove_accents(word):
    '''
        Return word without special characters.
    '''
    only_ascii = (unicodedata.normalize('NFKD', word).encode('ASCII', 'ignore')).decode("utf-8")
    print(f"Copied {word} into {only_ascii}")
    return only_ascii


def multi_mock_open(*file_contents):
    """
        Create a mock "open" that will mock open multiple files in sequence
        Args:
            *file_contents ([str]): a list of file contents to be returned by open
        Returns:
            (MagicMock) a mock opener that will return the contents of the first
                file when opened the first time, the second file when opened the
                second time, etc.
    """
    mock_files = [mock_open(read_data=content).return_value for content in file_contents]
    mock_opener = mock_open()
    mock_opener.side_effect = mock_files
    
    return mock_opener
