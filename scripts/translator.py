
import pandas as pd

from googletrans import Translator
from pprint import pprint
from scripts.utils import (
    load_fixture,
    get_csv_file_paths
)

# # import pdb; pdb.set_trace()
# # Reading from CSV file
# def translate():
#     '''
#         CSV files: Loads, reads, translates, QAs, & prints english
#         words to spanish. Saves new csv file for each file in collections.
#     '''
#     translator = Translator()
#     csv_files = get_csv_file_paths()
#     total_translated_lists = {}

#     for file in csv_files:
#         f = open(f"tests/fixtures/{file.split('/')[-1]}.txt", 'w')
#         print(f"Working on translating {file.split('/')[-1]} into spanish...")
        
#         # Read csv file
#         df = pd.read_csv(file)
#         shape = df.shape
#         spanish_translations = []

#         # Iterate down column 0, translate + clean word.
#         for index in range(shape[0]):
#             eng_word = df.values[index, 0]
#             translation = translator.translate(eng_word, src='en', dest='es')
#             spanish_translations.append((((translation.text).lower()).strip()).replace(" ", ""))
#             # print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

#         # Remove dups
#         spanish_translations = list(dict.fromkeys(spanish_translations))
#         for word in spanish_translations:
#             f.write(word)
#             f.writelines('\n')
#         f.close()

# Reading from text file
def translate():
    '''
        CSV files: Loads, reads, translates, QAs, & prints english
        words to spanish. Saves new csv file for each file in collections.
    '''
    # translator = Translator()
    # lines = []
    # with open('tests/fixtures/english-animals.txt', 'r') as f:
    #     lines = f.readlines()

    # f = open('tests/fixtures/spanish-animals.txt', 'w')
    # for line in lines:
    #     line = line.strip('\n')
    #     translation = translator.translate(line, src='en', dest='es')
    #     print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

    #     f.write(((translation.text).lower()).strip())
    #     f.writelines('\n')
    # f.close()

    with open('tests/fixtures/spanish-animals.txt', 'r') as f:
        lines = f.readlines()

    f = open('tests/fixtures/spanish-animals-nospaces.txt', 'w')
    for line in lines:
        line = line.strip('\n')
        line = line.replace(" ", "")

        f.write(((line).lower()).strip())
        f.writelines('\n')
    f.close()

