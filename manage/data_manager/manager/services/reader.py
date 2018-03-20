import csv
from typing import List, Any

import os

from os.path import isfile, join


class CSVReader(object):
    @staticmethod
    def read(filename: str) -> List[List[Any]]:
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            data = []
            for row in reader:
                data.append(row)
            return data


class LineReader(object):

    @staticmethod
    def read(filename: str) -> List[Any]:
        with open(filename, 'r') as file:
            data = []
            for line in file:
                line = line.strip()
                if line == '':
                    continue
                data.append(line)
            return data


class FolderReader(object):

    @staticmethod
    def get_files(path: str) -> List[str]:
        return [join(path, f) for f in os.listdir(path) if isfile(join(path, f))]

    @staticmethod
    def get_names(path: str) -> List[str]:
        return [f for f in os.listdir(path) if isfile(join(path, f))]
