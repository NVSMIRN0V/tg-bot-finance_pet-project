import sqlite3 as sql


def create_table_categories() -> None:
    '''Функция для создания таблицы категорий'''    
    connection = sql.connect('f.db')
    cursor = connection.cursor()

    # Создать таблицу 
    cursor.execute(
        '''
            create table if not exists categories (
                name text primary key,
                altname text,
                aliases text
            );
        '''
    )

    # Заполнить таблицу
    categories = [
        ('home', 'дом', 'аренда, счета, счетчики, вывоз мусора, охрана, консьерж, жку'),
        ('pets', 'домашние животные', 'питомец, товары для животных, услуги ветеринара, кот, собака, ветеринар'),
        ('food', 'еда', 'еда, ресторан, кфц, кфс, мак, чикен, магнит, пятерочка, пятерка, кафе, магазин, магаз, доставка'),
        ('transport', 'транспорт', 'автобус, проездной, авиа, метро, такси, электричка, автомобиль, общественный транспорт, повозка, поезд, ласточка, элка, авто, машина, проезд, '),
        ('debts', 'долги', 'кредитные карты, кредитка, долг, кредит, ипотека, банк'),
        ('telecom', 'связь', 'телефон, мтс, связь, интернет, вайфай, вифи, модем'),
        ('education', 'образование', 'учебники, канцтовары, обучение, репетитор'),
        ('entertainment', 'отдых и развлечения', 'игры, фильм, книга, книги, диски, журналы, журнал, кино, фото, театр, выставки, боулинг, чил, отдых, поездка, подписка, музыка, фильмы'),
        ('health', 'здоровье и красота', 'косметика, парфюмерия, салон, спорт, лекарства, парикмахер, врач, анализы, больница, тренировки, бокс, зал'),
        ('clothes', 'одежда и аксессуары', 'одежда, обувь, аксессуары, украшения, химчистка, ателье, ремонт обуви'),
        ('savings', 'сбережения', 'резервный фонд, отпуск, накопления, инвестиции, резерв, сбережения'),
        ('household', 'товары для дома', 'белье, мелкая техника, приборы, посуда, кухонная утварь, товары для ванной, предметы интерьера, интерьер, мебель, ремонт'),
        ('other', 'прочие', 'служебные расходы, карманные расходы, чаевые, взносы, банковские комиссии, нотариус, утеря денег, доставка товара'),
    ]

    for name, altname, aliases in categories:
        cursor.execute('insert into categories (name, altname, aliases) values (?, ?, ?)', (name, altname, aliases))

    connection.commit()
    connection.close()


def create_table_extends() -> None:
    connection = sql.connect('f.db')
    cursor = connection.cursor()

    cursor.execute(
        '''
            create table if not exists extends (
                id integer primary key autoincrement,
                amount text,
                date text,
                category text,
                foreign key (category) references categories(name)
            );
        '''
    )

    connection.commit()
    connection.close()


def insert_into_extends() -> None:
    connection = sql.connect('f.db')
    cursor = connection.cursor()

    cursor.execute(
        '''
            insert into extends (amount, date, category) 
            values ('150', '03/05/24', 'transport');
        '''
    )

    connection.commit()
    connection.close()


def select_from_extends():
    connection = sql.connect('f.db')
    cursor = connection.cursor()

    cursor.execute(
        '''
            select * from extends as E
            join categories as C
            on E.category=C.name
        '''
    )

    result = cursor.fetchall()
    for row in result: 
        print(row) 

    connection.close()
