import sys
import pandas as pd
from googletrans import Translator
from pprint import pprint
from scripts.settings import (
    FIXTURE_PATH,
    CSV_FILE_LOCATION
)
from scripts.utils import (
    get_csv_file_paths,
    create_ordered_alpha_txt_files
)

'''
This file translates words, then writes translated words
into their own text files.
Saves text file of cleaned translated words in /tests/fixtures/*.txt.
'''


# import pdb; pdb.set_trace()
def translate_csv():
    '''
        Translates existing english word lists from ens.vision
        into spanish. 

        Place csv files in /collections/*.csv. Reads all csv files at
        location.

        Creates one text file for every csv file found at location.
        Text files will have file name of parent csv file. Change name
        to new language.

        https://github.com/Zimtente/ens-collections/tree/main/collections.

        CMD EX: $ run-csv
    '''
    translator = Translator()
    csv_files = get_csv_file_paths(csv_files=CSV_FILE_LOCATION)
    total_translated_lists = {}

    # Read csv, create text file of cleaned words from csv file.
    for file in csv_files:
        # Create a file for cleaned translated words.
        f = open(f"{FIXTURE_PATH}/{file.split('/')[-1]}.txt", 'w')
        print(f"Working on translating {file.split('/')[-1]} into spanish...")
        
        # Read existing ens.vision csv file.
        df = pd.read_csv(file)
        shape = df.shape
        spanish_translations = []

        # Iterate down column 0. Translate & clean words. Save in list.
        for index in range(shape[0]):
            eng_word = df.values[index, 0]
            translation = translator.translate(eng_word, src='en', dest='es')
            spanish_translations.append((((translation.text).lower()).strip()).replace(" ", ""))
            # print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

        # Remove dups translated words list.
        spanish_translations = list(dict.fromkeys(spanish_translations))

        # Copy cleaned, dedupped translated words into file.
        for word in spanish_translations:
            f.write(word)
            f.writelines('\n')
        f.close()


def translate_txt():
    '''
        Reads a cleaned english text file, translates to spanish,
        and produces a hash ready text file of translations.

        CMD EX: $ run-txt english-animals.txt spanish-animals.txt
    '''
    try:
        CLEAN_WORDS_FILE = f"{FIXTURE_PATH}/{sys.argv[1]}"
        TRANSLATED_CLEAN_WORDS_FILE = f"{FIXTURE_PATH}/{sys.argv[2]}"
    except IndexError as ie:
        print(f"CMD: $ run-txt file1.txt file2.txt")
        sys.exit(f"Invalid run command. {ie}")

    translator = Translator()
    lines = []

    import pdb; pdb.set_trace()

    # Read from clean words file.
    with open(CLEAN_WORDS_FILE, 'r') as f:
        lines = f.readlines()
    import pdb; pdb.set_trace()
    with open(CLEAN_WORDS_FILE, 'r') as f:
        lines1 = f.readlines()
    import pdb; pdb.set_trace()

    # Translation clean words & create a clean translated words file.
    f = open(TRANSLATED_CLEAN_WORDS_FILE, 'w')
    for line in lines:
        line = line.strip('\n')
        translation = translator.translate(line, src='en', dest='es')
        print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
        f.write(((translation.text).lower()).strip())
        f.writelines('\n')
    f.close()

    # Read from cleaned transated words file.
    with open(TRANSLATED_CLEAN_WORDS_FILE, 'r') as f:
        lines = f.readlines()

    # Feed cleaned file, creates alphabetical + no spaces text files.
    create_ordered_alpha_txt_files(TRANSLATED_CLEAN_WORDS_FILE)