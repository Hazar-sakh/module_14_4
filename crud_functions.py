import sqlite3


def initiate_db():
    connect = sqlite3.connect('teleBot.db')
    curs = connect.cursor()
    curs.execute(
        '''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
        )
        '''
    )
    connect.commit()
    connect.close()


def get_all_products():
    connect = sqlite3.connect('teleBot.db')
    curs = connect.cursor()
    curs.execute(
        '''
        SELECT * FROM Products
        '''
    )
    data = curs.fetchall()
    connect.commit()
    connect.close()
    return data


initiate_db()

# con = sqlite3.connect('teleBot.db')
# curs = con.cursor()
# for i in range(1, 5):
#     curs.execute(
#         '''
#         INSERT INTO Products (id, title, description, price)
#         VALUES (?, ?, ?, ?)
#         ''', (f'{i}', f'Продукт {i}', f'Описание {i}', f'{i * 100}',)
#     )
# con.commit()
# con.close()
