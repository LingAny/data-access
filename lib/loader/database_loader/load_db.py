import csv
import logging
import os
from uuid import UUID, uuid4

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


path = os.environ.get('DATABASE')
context = EnvDataContextFactory().create_data_context()
logging.getLogger().setLevel(logging.INFO)


def main():
    logging.info('load database...')

    load_languages()
    load_reflections()

    logging.info('completed')


def load_languages():
    logging.info("load languages...")

    languages = CSVReader.read(path + "/structure/dict/languages.csv")

    for i in range(1, len(languages)):
        row = languages[i]
        msg = 'load ' + row[1] + ' language'
        logging.info(msg)
        context.callproc('add_language', [UUID(row[0]), row[1]])

    logging.info("completed load languages")


def load_reflections():
    logging.info('load reflections')
    files = get_files(path + "/structure/dict/reflections")

    for filename in files:
        msg = 'load reflections from ' + filename
        logging.info(msg)
        data = CSVReader.read(filename)
        # load_data(data)


def load_data(data: List[List[Any]]):
    logging.info("load data..")


def get_files(path):
    return [join(path, f) for f in os.listdir(path) if isfile(join(path, f))]


if __name__ == '__main__':
    main()
