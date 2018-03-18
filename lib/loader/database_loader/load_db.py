import os

from sqlutils import EnvDataContextFactory


def main():
    print('MAIN')
    path = os.environ.get('DATABASE')
    context = EnvDataContextFactory().create_data_context()


if __name__ == '__main__':
    main()
