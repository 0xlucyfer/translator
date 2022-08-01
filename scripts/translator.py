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
    create_ordered_alpha_txt_files,
    get_text_file_paths
)

'''
Input: Existing csv/txt file with words.
Output: Cleaned & Normalized text files.
'''


# import pdb; pdb.set_trace()
def translate_csv():
    '''
        Translates from a csv file. 

        Place csv files in /collections/*.csv. Reads all csv files at
        location.

        Creates one text file for every csv file found.
        Text files will have file name of parent csv file. Change name
        to new language.

        https://github.com/Zimtente/ens-collections/tree/main/collections.

        CMD EX: $ run-csv
    '''
    translator = Translator()
    csv_files = get_csv_file_paths(csv_files=CSV_FILE_LOCATION)
    total_translated_lists = {}

    # For every file at location.
    for file in csv_files:
        # Create a file for cleaned translated words.
        f = open(f"{FIXTURE_PATH}/{file.split('/')[-1]}.txt", 'w')
        print(f"Working on translating {file.split('/')[-1]} into spanish...\n")
        
        # Get shape of csv object.
        df = pd.read_csv(file)
        shape = df.shape
        spanish_translations = []

        # Iterate down column 0. Translate word, clean word, save in list.
        for index in range(shape[0]):
            eng_word = df.values[index, 0]
            translation = translator.translate(eng_word, src='en', dest='es')
            spanish_translations.append((((translation.text).lower()).strip()).replace(" ", ""))
            print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

        # Remove dups from cleaned list.
        spanish_translations = list(dict.fromkeys(spanish_translations))

        # Copy cleaned list into text file.
        for word in spanish_translations:
            f.write(word)
            f.writelines('\n')
        f.close()


def translate_txt():
    '''
        Reads a cleaned text file, translates to new language,
        and outputs a cleaned & a normalize text file.

        CMD EX: $ run-txt english-animals spanish-animals
    '''
    try:
        CLEAN_WORDS_FILE = f"{FIXTURE_PATH}/{sys.argv[1]}"
        TRANSLATED_CLEAN_WORDS_FILE = f"{FIXTURE_PATH}/{sys.argv[2]}"
    except IndexError as ie:
        print(f"CMD: $ run-txt file1 file2")
        sys.exit(f"Invalid run command. {ie}")

    translator = Translator()
    lines = []

    # Read from clean file.
    with open(CLEAN_WORDS_FILE, 'r') as f:
        lines = f.readlines()

    # Translate words & copy translated word into text file.
    f = open(TRANSLATED_CLEAN_WORDS_FILE, 'w')
    for line in lines:
        line = line.strip('\n')
        translation = translator.translate(line, src='en', dest='es')
        print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
        f.write(translation.text)
        f.writelines('\n')
    f.close()

    # Create a cleaned & a normalized text file.
    create_ordered_alpha_txt_files(TRANSLATED_CLEAN_WORDS_FILE)


# def SS_data_from_1970():
#     '''
#         Rough draft which gets the most popular names according
#         to social security records. 
#     '''
#     MIN_POP = 2000
#     m_names_list = []
#     f_names_list = []
#     txt_files = get_text_file_paths(txt_files='/collections')
#     f = open(f"{FIXTURE_PATH}/all-female-names.txt", 'w')
#     m = open(f"{FIXTURE_PATH}/all-male-names.txt", 'w')

#     for file in txt_files:
#         print(f'working on {file}')
#         df = pd.read_csv(file)
#         shape = df.shape

#         for index in range(shape[0]):
#             popularity = df.values[index, 2]

#             if MIN_POP > popularity:
#                 break

#             geneder = df.values[index, 1]
#             name = df.values[index, 0]

#             if geneder.lower() == 'm':
#                 m_names_list.append(name)
#             else:
#                 f_names_list.append(name)

#     m_names_list = list(dict.fromkeys(m_names_list))
#     f_names_list = list(dict.fromkeys(f_names_list))

#     for name in f_names_list:
#         f.write(name)
#         f.writelines('\n')
#     f.close()

#     for name in m_names_list:
#         m.write(name)
#         m.writelines('\n')
#     m.close()