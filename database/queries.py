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
