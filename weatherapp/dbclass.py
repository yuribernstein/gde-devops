import mysql.connector
from mysql.connector import Error

class MySQLDatabase:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        """Establish a database connection."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print('Database connection successful.')
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
    
    def execute_query(self, query, params=None):
        """Execute a SQL query and return the cursor."""
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            self.connection.commit()
            return cursor
        except Error as e:
            print(f"Failed to execute query: {e}")
        finally:
            cursor.close()

    def fetch_one(self, query, params=None):
        """Fetch a single row from a SQL query."""
        cursor = self.execute_query(query, params)
        result = cursor.fetchone()
        cursor.close()
        return result

    def fetch_all(self, query, params=None):
        """Fetch all rows from a SQL query."""
        cursor = self.execute_query(query, params)
        results = cursor.fetchall()
        cursor.close()
        return results

    def close(self):
        """Close the database connection."""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed.")


# usage example
from lesson13.ref_weatherapp.dbclass import MySQLslDatabase

db = MySQLDatabase('localhost', 'root', 'P@ssw0rd', 'WeatherApp')
db.connect()
query = "INSERT INTO Users(username, password, email, birth_date, state) VALUES (%s, %s, %s, %s, %s)"
db.execute_query(query, (username, password, email, birth_date, state))
db.close()
