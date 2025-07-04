#database.py

import mysql.connector

class Database:
    _instance = None

    def __init__(self):
        # Real constructor
        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  
            database="recycling_system"
        )
        self.db_cursor = self.db_connection.cursor()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def execute(self, query, params=None):
        if params:
            self.db_cursor.execute(query, params)
        else:
            self.db_cursor.execute(query)
        self.db_connection.commit()

    def fetch_all(self, query, params=None):
        if params:
            self.db_cursor.execute(query, params)
        else:
            self.db_cursor.execute(query)
        return self.db_cursor.fetchall()

    def fetch_one(self, query, params=None):
        if params:
            self.db_cursor.execute(query, params)
        else:
            self.db_cursor.execute(query)
        return self.db_cursor.fetchone()
    
    def execute_query(self, query, params=None):
        """
        This method executes an insert, update, or delete query.
        """
        self.db_cursor.execute(query, params)
        self.db_connection.commit()