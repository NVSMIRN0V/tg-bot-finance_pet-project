'''Файл для работы с категориями расходов'''


from dataclasses import dataclass


@dataclass(frozen=True)
class Category:
    '''Структура категории'''
    name: str
    altname: str
    aliases: list[str]