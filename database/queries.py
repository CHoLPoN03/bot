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