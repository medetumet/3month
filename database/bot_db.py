import random
import sqlite3


# СУБД - Система управления базой данных
# SQL = Structured Query Language


def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print("База данных подключена!")

    db.execute("CREATE TABLE IF NOT EXISTS mentor "
               "(id INTEGER PRIMARY KEY, name TEXT, "
               "direction TEXT, age INTEGER, gruppa TEXT)")
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO mentor VALUES "
                       "(?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()


async def sql_command_random(message):
    result = cursor.execute("SELECT * FROM mentor").fetchall()
    random_user = random.choice(result)
    await message.answer(
        f"id:{random_user[0]} name:{random_user[1]} direction{random_user[2]} "
        f"age:{random_user[3]} group:{random_user[4]}"
    )


async def sql_command_all():
    return cursor.execute("SELECT * FROM mentor").fetchall()


async def sql_command_delete(mentor_id):
    cursor.execute("DELETE FROM mentor WHERE id = ?", (mentor_id,))
    db.commit()
