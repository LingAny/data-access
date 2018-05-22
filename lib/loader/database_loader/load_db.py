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
    load_categories()
    load_training()

    logging.info('completed')


def load_languages():
    logging.info("load languages...")

    languages = CSVReader.read(path + "/structure/dict/languages.csv")

    for i in range(1, len(languages)):
        row = languages[i]
        msg = 'load ' + row[1] + ' language'
        logging.info(msg)
        context.callproc('add_language', [UUID(row[0]), row[1], row[2]])

    logging.info("completed load languages")


def load_reflections():
    logging.info('load reflections')
    files = get_files(path + "/structure/dict/reflections")

    for filename in files:
        msg = 'load reflections from ' + filename
        logging.info(msg)
        data = CSVReader.read(filename)
        for i in range(1, len(data)):
            row = data[i]
            logging.info('load ' + row[1])
            context.callproc('add_reflection', [UUID(row[0]), row[1], UUID(row[2]), UUID(row[3])])

    logging.info("completed load reflections")


def load_categories():
    logging.info('load categories')
    files = get_files(path + "/structure/dict/categories")
    for filename in files:
        msg = 'load categories from ' + filename
        logging.info(msg)
        data = CSVReader.read(filename)
        for i in range(1, len(data)):
            row = data[i]
            logging.info('load ' + row[1])
            context.callproc('add_category', [UUID(row[0]), UUID(row[2]), row[1]])

    logging.info("completed load categories")


def load_training():
    logging.info('load categories')
    files = get_files(path + "/structure/dict/training")
    for filename in files:
        msg = 'load training from ' + filename
        logging.info(msg)
        data = CSVReader.read(filename)
        for i in range(1, len(data)):
            row = data[i]
            logging.info('load training ' + row[2] + ':' + row[3])
            context.callproc('add_training', [UUID(row[0]), UUID(row[1]), row[2], row[3]])

    logging.info("completed load training")


def get_files(p_path):
    return [join(p_path, f) for f in os.listdir(p_path) if isfile(join(p_path, f))]


if __name__ == '__main__':
    main()
