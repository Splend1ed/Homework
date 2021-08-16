import sqlite3

db = sqlite3.connect('SQLite_Lesson_1.db')
sql = db.cursor()

sql.execute('''CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT,
    cash BIGINT
)''')

db.commit()

user_login = input('Login: ')
user_password = input('Password: ')

sql.execute('SELECT login FROM users')
if sql.fetchone() is None:
    sql.execute(f'INSERT INTO users VALUES (?, ?, ?)', (user_login, user_password, 0))
    db.commit()
    print('Done!')
else:
    print('Такая запись уже имееться!')

    for value in sql.execute('SELECT * FROM users'):
        print(value)

# CREATE jobs(id INTEGER ORIMARY KEY NOT NULL AUTOINCREMENT, title VARCHAR(255), salary NUMERIC(10, 2), user_id INTEGER NOT NULL, FOREIGN KEYD^Z) )
