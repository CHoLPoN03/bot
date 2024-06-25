import sqlite3
class Queries:
    CREATE_REVIEW_TABLE = ''' 
    CREATE TABLE IF NOT EXISTS review_results(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        number TEXT,
        date DATE,
        food TEXT,
        cleanliness TEXT,
        comment TEXT
        )
    '''


    DROP_DISHES_TABLE = "DROP TABLE IF EXISTS categories"
    DROP_CATEGORIES_TABLE = "DROP TABLE IF EXISTS dishes"

    CREATE_CATEGORIES_TABLE = """
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );
        """

    CREATE_DISHES_TABLE = """
        CREATE TABLE IF NOT EXISTS dishes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(id)
        );
        """


    POPULATE_CATEGORIES_TABLE = """
        INSERT INTO categories (name) 
        VALUES ("Пицца"),
        ("Десерты"),
        ("Коктейли"),
        ("Напитки")
    """


    POPULATE_DISHES_TABLE = """
    INSERT INTO dishes (name, price, category_id)
    VALUES ("Баварская", 500, 1),
           ("Сырная", 550, 1),
           ("Пончик клубничный", 159, 2),
           ("Чизкейк", 159, 2),
           ("Классический молочный коктейль", 189, 3),
           ("Шоколадный молочный коктейль", 199, 3),
           ("Морс Вишня", 139, 4),
           ("Fuse tea", 139, 4)
    """
