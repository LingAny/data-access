import csv
import logging
import os

from os.path import isfile, join
from typing import List, Any

from sqlutils import EnvDataContextFactory


class CSVReader(object):
    @staticmethod
    def read(filename: str) -> List[List[Any]]:
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            data = []
            for row in reader:
                data.append(row)
            return data


class LanguagesReader(object):

    @staticmethod
    def read(filename) -> List[str]:
        with open(filename, 'r') as file:
            data = []
            for line in file:
                if line == '':
                    continue
                data.append(line.strip())
            return data


path = os.environ.get('DATABASE')
context = EnvDataContextFactory().create_data_context()
logging.getLogger().setLevel(logging.INFO)


def main():
    print('MAIN')

    languages = LanguagesReader.read(path + "/structure/list/language_list.txt")
    load_languages(languages=languages)

    files = get_files(path + "/structure/dict")
    print("files: ", files)

    for filename in files:
        data = CSVReader.read(filename)
        load_data(data)


def load_languages(languages: List[str]):
    logging.info("load languages...")
    for lang in languages:
        # print(lang)
        logging.info(lang)


def load_data(data: List[List[Any]]):
    pass


def get_files(path):
    return [f for f in os.listdir(path) if isfile(join(path, f))]


if __name__ == '__main__':
    main()
