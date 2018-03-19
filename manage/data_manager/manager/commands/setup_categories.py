import logging
from typing import List

from manager.conf.configure import Configure
from manager.models.language import Language
from manager.models.reflection import Reflection
from manager.services.category_service import CategoryService

logging.getLogger().setLevel(logging.INFO)


def setup(conf: Configure, languages: List[Language], reflections: List[Reflection]) -> None:
    logging.info(f"setup categories...")
    categories = CategoryService.get_supported_categories(conf.list_path + 'categories/')
