'''Файл для работы с бд на уровне запросов sql'''
import sqlite3 as sql


connection =  sql.connect('f.db')
cursor = connection.cursor()


def insert(table: str, data: dict) -> None:
    '''Запись в таблицу новых данных'''

    # Парсинг data
    values = tuple(data.values())
    columns = ', '.join(data.keys())

    # Запись в бд
    cursor.execute(
        f'insert into {table} ({columns})'
        f'values {values}'
    )
    connection.commit()


def fetchall(table: str, cols: list[str], conditions: str = None) -> list[dict]:
    '''Получение результата запроса в бд'''

    # Чтение записей из бд
    cols_joined = ', '.join(cols)
    cursor.execute(
        f'select {cols_joined} from {table} {conditions}'
    )
    objects = cursor.fetchall()

    # Распаковка записей в нужный формат
    unpacked_objects = []
    for obj in objects:
        dict_obj = {}
        for index, col in enumerate(cols):
            dict_obj[col] = obj[index] 
        unpacked_objects.append(dict_obj)        
    return unpacked_objects


def get_cursor() -> sql.Cursor:
    '''Получение курсора'''
    return cursor
