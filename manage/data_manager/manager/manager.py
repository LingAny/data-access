import logging

from manager.commands import setup_reflections, setup_categories
from manager.conf.env_congigure_facotry import EnvConfigureFactory
from manager.services.language_service import LanguageService


def manage():
    conf = EnvConfigureFactory.create()

    logging.info(f'setup')
    languages = LanguageService.get_supported_languages(conf.dict_path + '/languages.csv')
    for lang in languages:
        logging.info(f'Supported language: {lang.title}')

    reflections = setup_reflections.setup(conf=conf, languages=languages)

    setup_categories.setup(conf=conf, languages=languages, reflections=reflections)

if __name__ == '__main__':
    manage()
