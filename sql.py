'''Файл для работы с бд на уровне запросов sql'''
import sqlite3 as sql


connection =  sql.connect('f.db')
cursor = connection.cursor()


def insert(table: str, data: dict) -> None:
    # Парсинг data
    values = tuple(data.values())
    columns = ', '.join(data.keys())

    # Запись в бд
    cursor.execute(
        f'insert into {table} ({columns})'
        f'values {values}'
    )
    connection.commit()
