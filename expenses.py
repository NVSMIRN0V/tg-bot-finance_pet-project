'''Файл для работы с расходами'''
from unittest import result
from categories import Categories, Category
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
    date: datetime | str
    amount: str
    category: str
    

def add(message: str) -> Expense:
    '''Функция добавления нового расхода'''
    parsed_message = parse(message)
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    category = Categories().get_category(parsed_message.category)
    expense = Expense(index=None, amount=parsed_message.amount, date=date, category=category.altname)
    sql.insert('expense', {'amount': expense.amount, 'date': expense.date, 'category': expense.category,}) # !
    return expense 


def parse(message: str) -> Message:
    '''Функция парсинга сообщения от пользователя'''
    # Пока реализую в примитивном виде, потом переделаю через регулярки
    message = message.split(' ')
    return Message(amount=message[0], category=message[1], description=None)


def get_statistics_today() -> dict:
    '''Функция получения статистики расходов за сегодня'''
    # Запрос в бд
    cursor = sql.get_cursor()
    cursor.execute(f'select amount from expense where date(date)=date("now")')
    expenses = cursor.fetchall()
    print(expenses)
    # Формирование ответа
    if not expenses:
        answer = 'Расходов за сегодня нет.'
    else:
        result = 0
        for exp in expenses:
            amount = float(exp[0])
            result += amount
        answer = f'За сегодня Вы потратили {result}р.'    
    return answer
