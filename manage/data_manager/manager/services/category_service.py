import logging
from typing import List


from manager.models.external_category import ExternalCategory
from manager.services.reader import FolderReader, LineReader

logging.getLogger().setLevel(logging.INFO)


class CategoryService(object):

    @staticmethod
    def get_supported_categories(path: str) -> List[ExternalCategory]:
        files = FolderReader.get_files(path)
        logging.info(f"[get_supported_categories] files: {files}")
        categories = []
        for filename in files:
            logging.info(f'load category from {filename}')
            data = LineReader.read(filename)
            if len(data) < 2:
                continue
            title = data[0]
            values = set(data[1:])
            categories.append(ExternalCategory(title=title, values=values))

        return categories
