import os

from os.path import isfile, join

from sqlutils import EnvDataContextFactory


def main():
    print('MAIN')
    path = os.environ.get('DATABASE')
    context = EnvDataContextFactory().create_data_context()

    print("path: " + path)
    files = get_files(path + "/structure/dict")
    print("files: ", files)


def get_files(path):
    return [f for f in os.listdir(path) if isfile(join(path, f))]


if __name__ == '__main__':
    main()
