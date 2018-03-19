import logging
from typing import List, Dict
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


def setup(conf: Configure, languages: List[Language], reflections: List[Reflection]) -> None:
    logging.info(f"setup categories...")
    ext_categories = CategoryService.get_supported_categories(conf.list_path + 'categories/')
    categories = convert_external_categories(ext_categories, languages, reflections)


def convert_external_categories(external: List[ExternalCategory], languages: List[Language],
                                reflections: List[Reflection]) -> List[Category]:

    categories: List[Category] = []

    for ext in external:

        titles = translate_title(ext.title, languages)

        for ref in reflections:
            title = titles.get(ref.native_lang.code)
            logging.info(f"language: {ref.native_lang.code} title: {title}")
            category = Category(uid=uuid4(), title=title, reflection=ref)
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
            translated_title = translator.translate_text(title, 'ru', lang.code)
            titles.update({
                lang.code: translated_title
            })
    return titles


def save_categories(categories: List[ExternalCategory], reflections: List[Reflection]):
    pass