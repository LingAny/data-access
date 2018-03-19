import logging
from typing import List

from manager.conf.configure import Configure

from manager.models.external_category import ExternalCategory
from manager.models.language import Language
from manager.models.reflection import Reflection
from manager.services.category_service import CategoryService

logging.getLogger().setLevel(logging.INFO)


def setup(conf: Configure, languages: List[Language], reflections: List[Reflection]) -> None:
    logging.info(f"setup categories...")
    ext_categories = CategoryService.get_supported_categories(conf.list_path + 'categories/')


def save_categories(categories: List[ExternalCategory], reflections: List[Reflection]):
    for ref in reflections:

        if ref.native_lang.title == 'Russian':
            logging.log('[save_categories] native lang in Russian')


        else:
            pass
