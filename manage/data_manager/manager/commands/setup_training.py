import csv
import logging
from typing import Set, List, Tuple
from uuid import uuid4

from manager.conf.configure import Configure
from manager.conf.env_yandex_translator_cong_factory import EnvYandexTranslatorConfFactory
from manager.models.category import Category
from manager.models.training import Training
from manager.services.traslator import Translator

logging.getLogger().setLevel(logging.INFO)
yandex_translator_conf = EnvYandexTranslatorConfFactory.create()
translator = Translator(yandex_translator_conf)


def setup(conf: Configure, categories: List[Category]) -> None:
    trainings = create_trainings(categories)
    save(conf=conf, trainings=trainings)


def save(conf: Configure, trainings: List[Training]) -> None:
    filename = f'{conf.output_training_path}/all_trainings.csv'
    file = open(filename, 'w')
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['uid:uuid', 'category_id:uuid', 'native_word:text', 'foreign_word:text'])

    for t in trainings:
        writer.writerow([t.uid.hex, t.category.uid.hex, t.native_item, t.foreign_item])

    file.close()


def create_trainings(categories: List[Category]) -> List[Training]:
    training_list: List[Training] = []
    for category in categories:
        items: Set[str] = category.items
        logging.info(f"create trainings for category '{category.title}' of {category.reflection.title}")
        for item in items:
            native_item, foreign_item = translate_item(item=item,
                                                       native_lang_code=category.reflection.native_lang.code,
                                                       foreign_lang_code=category.reflection.foreign_lang.code)

            training = Training(uid=uuid4(), category=category, native_item=native_item, foreign_item=foreign_item)
            training_list.append(training)

    return training_list


def translate_item(item: str, native_lang_code: str, foreign_lang_code: str) -> Tuple[str, str]:
    if native_lang_code == 'ru':
        native_item = item
    else:
        native_item = translator.translate_word(item, 'ru', native_lang_code)

    foreign_item = translator.translate_word(item, 'ru', foreign_lang_code)
    return native_item, foreign_item
