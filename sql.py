'''Файл для работы с бд на уровне запросов sql'''
import sqlite3 as sql


connection = sql.connect('finance.db')
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


def init_db():
    '''Инициализировать бд'''
    with open("db.sql", "r", encoding='utf-8') as f:
        script = f.read()
    cursor.executescript(script)
    connection.commit()


def check_if_exists():
    '''Проверить, инициализирована ли бд'''
    try:
        cursor.execute('select name from sqlite_master where type="table" and name="expenses";')
        result = cursor.fetchone()
        if not result:
            init_db()
        else:
            return
    except sql.Error as e:
        print(f"Ошибка при подключении к базе данных: {e}")
        return False


check_if_exists()