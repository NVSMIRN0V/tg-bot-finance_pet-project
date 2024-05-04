'''Файл для работы с расходами'''


from dataclasses import dataclass


@dataclass(frozen=True)
class Expense:
    '''Структура расхода'''
    index: int | None
    amount: float
    category: str
    