import csv
import logging
from typing import List
from uuid import uuid4

from manager.conf.configure import Configure
from manager.models.language import Language
from manager.models.reflection import Reflection
from manager.services.language_service import LanguageService
from manager.services.reflection_service import ReflectionService

logging.getLogger().setLevel(logging.INFO)


def setup(conf: Configure, languages: List[Language]) -> List[Reflection]:
    reflections = ReflectionService.get_supported_reflections(conf.dict_path + 'reflections/', languages)
    new_supported_reflections = create_new_supported_reflections(languages=languages, reflections=reflections)
    save_new_supported_reflection(languages=languages, reflections=new_supported_reflections, conf=conf)
    return new_supported_reflections


def save_new_supported_reflection(languages: List[Language], reflections: List[Reflection], conf: Configure):
    for native_lang in languages:
        native_to_many_ref = ReflectionService.get_reflections_for_native_lang(native_lang_id=native_lang.uid,
                                                                               supported_reflections=reflections)

        filename = f'{conf.output_reflections_path}/reflection_{native_lang.title}_to_many.csv'
        file = open(filename, 'w')
        writer = csv.writer(file, delimiter=',')
        writer.writerow(['uid:uuid', 'title:text', 'native_language_id:uuid', 'foreign_language_id:uuid'])

        for foreign_lang in languages:
            if native_lang.uid == foreign_lang.uid:
                continue

            native_to_foreign_ref = ReflectionService.get_reflection_for_foreign_lang(foreign_lang.uid,
                                                                                      native_to_many_ref)

            logging.debug(f'save {native_to_foreign_ref.title} into {conf.output_reflections_path}/{filename} ...')
            writer.writerow([native_to_foreign_ref.uid.hex,
                             native_to_foreign_ref.title,
                             native_to_foreign_ref.native_lang.uid.hex,
                             native_to_foreign_ref.foreign_lang.uid.hex])

        file.close()


def create_new_supported_reflections(languages: List[Language], reflections: List[Reflection]) -> List[Reflection]:
    new_supported_reflection = []
    for native_lang in languages:
        logging.info(f'get supported reflections for {native_lang.title} native language')
        native_to_many_ref = ReflectionService.get_reflections_for_native_lang(native_lang_id=native_lang.uid,
                                                                               supported_reflections=reflections)
        if len(native_to_many_ref) == 0:
            logging.info(f"No reflections for {native_lang.title} native language")
        else:
            logging.info(f"Has {len(native_to_many_ref)} reflections for {native_lang.title} native language")

        for foreign_lang in languages:

            if native_lang.uid == foreign_lang.uid:
                continue

            native_to_foreign_ref = ReflectionService.get_reflection_for_foreign_lang(foreign_lang.uid,
                                                                                      native_to_many_ref)

            if not native_to_foreign_ref:
                title = f'reflection {native_lang.title} to {foreign_lang.title}'
                logging.info(f'create: {title}')
                new_reflection = Reflection(uid=uuid4(), title=title,
                                            native_lang=native_lang, foreign_lang=foreign_lang)
                new_supported_reflection.append(new_reflection)

            else:
                logging.info(f'reflection {native_lang.title} to {foreign_lang.title} is exists')
                new_supported_reflection.append(native_to_foreign_ref)
    return new_supported_reflection
