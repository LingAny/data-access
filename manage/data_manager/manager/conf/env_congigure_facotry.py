import os

from manager.conf.configure import Configure


class EnvConfigureFactory(object):

    @staticmethod
    def create() -> Configure:
        dict_path = os.environ.get('DICT_PATH')
        list_path = os.environ.get('LIST_PATH')
        output_reflections_path = os.environ.get('OUTPUT_REFLECTIONS_PATH')
        output_categories_path = os.environ.get('OUTPUT_CATEGORIES_PATH')
        return Configure(list_path=list_path, dict_path=dict_path,
                         output_reflections_path=output_reflections_path, output_categories_path=output_categories_path)
