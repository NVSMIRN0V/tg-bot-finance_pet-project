'''Файл для работы с категориями расходов'''
import sql
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
        dbrequest = sql.fetchall('categories', ['name', 'altname', 'aliases'])
        categories = []
        for data in dbrequest:
            category = Category(name=data['name'], altname=data['altname'], aliases=data['aliases'].split(', '))
            categories.append(category)
        return categories

    def get_all_categories(self) -> list[Category]:
        '''Получить список всех категорий'''
        return self._categories 

    def get_category(self, alias: str) -> Category:
        '''Получить категорию по алиасу'''
        other, finded = None, None
        for category in self._categories:
            if alias in category.aliases:
                finded = category; break 
            elif category.name == 'other':
                other = category
        return finded if finded else other
