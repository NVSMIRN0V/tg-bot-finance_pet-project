'''Файл для работы с расходами'''
import sql
from datetime import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class Message:
    '''Структура обработанного сообщения'''
    amount: str
    category: str
    description: str | None


@dataclass(frozen=True)
class Expense:
    '''Структура расхода'''
    index: int | None
    date: datetime
    amount: str
    category: str
    

def add(message: str) -> Expense:
    '''Функция добавления нового расхода'''
    parsed_message = parse(message)
    date = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    expense = Expense(index=None, amount=parsed_message.amount, date=date, category=parsed_message.category)
    sql.insert('expense', {'amount': expense.amount, 'date': expense.date, 'category': expense.category,}) # !
    return expense 


def parse(message: str) -> Message:
    '''Функция парсинга сообщения от пользователя'''
    # Пока реализую в примитивном виде, потом переделаю через регулярки
    message = message.split(' ')
    return Message(amount=message[0], category=message[1], description=None)
