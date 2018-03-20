class Configure(object):

    def __init__(self, list_path: str, dict_path: str, output_reflections_path: str,
                 output_categories_path: str, output_training_path: str) -> None:
        self._output_training_path = output_training_path
        self._list_path = list_path
        self._dict_path = dict_path
        self._output_reflections_path = output_reflections_path
        self._output_categories_path = output_categories_path

    @property
    def list_path(self) -> str:
        return self._list_path

    @property
    def dict_path(self) -> str:
        return self._dict_path

    @property
    def output_reflections_path(self) -> str:
        return self._output_reflections_path

    @property
    def output_categories_path(self) -> str:
        return self._output_categories_path

    @property
    def output_training_path(self) -> str:
        return self._output_training_path
