import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        self.connection = self._connect()
        self._initialize_db()

    def _connect(self):
        """Establish MySQL connection"""
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',      # Change to your MySQL username
                password='',      # Change to your MySQL password
                database='banking_db'
            )
            print("✅ Connected to MySQL")
            return conn
        except Error as e:
            print(f"❌ Connection failed: {e}")
            raise

    def _initialize_db(self):
        """Create tables if they don't exist"""
        commands = [
            """CREATE TABLE IF NOT EXISTS accounts (
                account_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                balance DECIMAL(12, 2) NOT NULL DEFAULT 0.0
            )""",
            """CREATE TABLE IF NOT EXISTS transactions (
                id INT AUTO_INCREMENT PRIMARY KEY,
                account_id INT NOT NULL,
                amount DECIMAL(12, 2) NOT NULL,
                type ENUM('DEPOSIT', 'WITHDRAW') NOT NULL,
                FOREIGN KEY (account_id) REFERENCES accounts(account_id)
            )"""
        ]
        
        cursor = self.connection.cursor()
        for cmd in commands:
            cursor.execute(cmd)
        self.connection.commit()
        cursor.close()

    def execute(self, query, params=None, fetch=False):
        """Execute SQL queries safely"""
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, params or ())
            self.connection.commit()
            return cursor.fetchall() if fetch else None
        except Error as e:
            self.connection.rollback()
            raise Exception(f"Database error: {e}")
        finally:
            cursor.close()

    def close(self):
        """Close the connection"""
        if self.connection.is_connected():
            self.connection.close()
            print("🔌 MySQL connection closed")
