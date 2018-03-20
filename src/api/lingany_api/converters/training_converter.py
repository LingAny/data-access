from lingany_api.models.category import Category
from lingany_api.models.training import Training
from lingany_api.persistance.dto.training_dto import TrainingDTO
from sqlutils import Converter


class TrainingConverter(Converter[Training, TrainingDTO]):

    def convert(self, entity: TrainingDTO) -> Training:
        return Training(uid=entity.uid).fill(category=Category(entity.category_id),
                                             native_word=entity.native_word,
                                             foreign_word=entity.foreign_word
                                             )
