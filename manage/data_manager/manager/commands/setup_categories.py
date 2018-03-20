import csv
import logging
from typing import List, Dict, Set
from uuid import uuid4

from manager.conf.configure import Configure
from manager.conf.env_yandex_translator_cong_factory import EnvYandexTranslatorConfFactory
from manager.models.category import Category

from manager.models.external_category import ExternalCategory
from manager.models.language import Language
from manager.models.reflection import Reflection
from manager.services.category_service import CategoryService
from manager.services.traslator import Translator

logging.getLogger().setLevel(logging.INFO)
yandex_translator_conf = EnvYandexTranslatorConfFactory.create()
translator = Translator(yandex_translator_conf)


def setup(conf: Configure, languages: List[Language], reflections: List[Reflection]) -> List[Category]:
    logging.info(f"setup categories...")
    ext_categories = CategoryService.get_supported_categories(conf.list_path + 'categories/')
    categories = convert_external_categories(ext_categories, languages, reflections)
    save_categories(conf=conf, categories=categories)
    return categories


def convert_external_categories(external: List[ExternalCategory], languages: List[Language],
                                reflections: List[Reflection]) -> List[Category]:
    categories: List[Category] = []

    for ext in external:

        logging.info(f'[convert_external_categories] convert category: {ext.title}')
        titles = translate_title(title=ext.title, languages=languages)
        items = translate_items(items=ext.items, languages=languages)

        for ref in reflections:
            title = titles.get(ref.native_lang.code)
            category = Category(uid=uuid4(), title=title, reflection=ref, items=items.get(ref.foreign_lang.code))
            categories.append(category)

    return categories


def translate_title(title: str, languages: List[Language]) -> Dict[str, str]:
    titles: Dict[str, str] = dict()

    for lang in languages:
        if lang.code == 'ru':
            titles.update({
                lang.code: title
            })

        else:
            logging.info(f"translating category name to {lang.title}")
            translated_title = translator.translate_text(title, 'ru', lang.code)
            titles.update({
                lang.code: translated_title
            })
    return titles


def translate_items(items: Set[str], languages: List[Language]) -> Dict[str, Set[str]]:
    data: Dict[str, Set[str]] = dict()

    for lang in languages:
        if lang.code == 'ru':
            data.update({
                lang.code: items
            })

        else:
            logging.info(f"translating category values to {lang.title}")
            translated_items = set()
            for item in items:
                word = translator.translate_word(item, 'ru', lang.code)
                translated_items.add(word)

            data.update({
                lang.code: translated_items
            })
    return data


def save_categories(conf: Configure, categories: List[Category]):
    filename = f'{conf.output_categories_path}/all_categories.csv'
    file = open(filename, 'w')
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['uid:uuid', 'title:text', 'reflection_id:uuid'])

    for category in categories:
        writer.writerow([category.uid.hex, category.title, category.reflection.uid.hex])

    file.close()
