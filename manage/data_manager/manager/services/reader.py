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


class FolderReader(object):

    @staticmethod
    def get_files(path: str) -> List[str]:
        return [join(path, f) for f in os.listdir(path) if isfile(join(path, f))]
