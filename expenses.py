'''Файл для работы с расходами'''
import sql
from categories import Categories, Category
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
    sql.insert('expenses', {'amount': expense.amount, 'date': expense.date, 'category': expense.category,}) # !
    return expense 


def parse(message: str) -> Message:
    '''Функция парсинга сообщения от пользователя'''
    # Пока реализую в примитивном виде, потом переделаю через регулярки
    message = message.split(' ')
    return Message(amount=message[0], category=message[1], description=None)


def get_statistics_today() -> str:
    '''Функция получения статистики расходов за сегодня'''
    # Запрос в бд
    expenses = sql.fetchall('expenses', ['amount'], 'where date(date)=date("now")')

    # Формирование ответа
    if not expenses:
        answer = 'Расходов за сегодня нет.'
    else:
        result = 0
        for exp in expenses:
            result += float(exp['amount'])
        answer = f'За сегодня Вы потратили {result}р.'    
    return answer


def get_list_expenses_today() -> str:
    '''Функция получения расходов за сегодня списком.'''
    # Запрос в бд
    expenses = sql.fetchall('expenses', ['amount', 'category'], 'where date(date)=date("now")')

    # Формирование ответа
    if not expenses:
        answer = 'Расходов за сегодня нет.'
    else:
        answer = ''
        for ind, exp in zip(range(1, len(expenses) + 1), expenses):
            amount, category = exp.values()
            answer += str(ind) + '. ' + amount + ' ' + category + '.\n'
    return answer
