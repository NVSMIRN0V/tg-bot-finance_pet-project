'''Файл для работы с категориями расходов'''
from dataclasses import dataclass


@dataclass(frozen=True)
class Category:
    '''Структура категории'''
    name: str
    altname: str
    aliases: list[str]


class Categories:
    def __init__(self) -> None:
        self._categories = self._load_categories()

    def _load_categories(self) -> list[Category]:
        '''Загрузить все категории из бд'''
        pass

    def get_category(self) -> Category:
        '''Получить категорию по ее имени или алиасу'''
        pass