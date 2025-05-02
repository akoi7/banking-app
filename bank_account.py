import mysql.connector

class BankAccount:
    def __init__(self, user_id):
        self.user_id = user_id
        self.conn = mysql.connector.connect(
            host="localhost",
            user="your_user",
            password="your_password",
            database="banking"
        )
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        # You can remove this if you already created tables using schema.sql
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                user_id VARCHAR(255) PRIMARY KEY,
                balance DECIMAL(10, 2) DEFAULT 0.00
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id VARCHAR(255),
                amount DECIMAL(10, 2),
                type ENUM('deposit', 'withdraw'),
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES accounts(user_id)
            )
        ''')
        self.conn.commit()

    def create_account(self):
        self.cursor.execute(
            'INSERT IGNORE INTO accounts (user_id, balance) VALUES (%s, %s)',
            (self.user_id, 0.0)
        )
        self.conn.commit()

    def deposit(self, amount):
        self.cursor.execute(
            'UPDATE accounts SET balance = balance + %s WHERE user_id = %s',
            (amount, self.user_id)
        )
        self.cursor.execute(
            'INSERT INTO transactions (user_id, amount, type) VALUES (%s, %s, %s)',
            (self.user_id, amount, 'deposit')
        )
        self.conn.commit()

    def withdraw(self, amount):
        current_balance = self.get_balance()
        if amount <= current_balance:
            self.cursor.execute(
                'UPDATE accounts SET balance = balance - %s WHERE user_id = %s',
                (amount, self.user_id)
            )
            self.cursor.execute(
                'INSERT INTO transactions (user_id, amount, type) VALUES (%s, %s, %s)',
                (self.user_id, amount, 'withdraw')
            )
            self.conn.commit()
        else:
            print("Insufficient funds.")

    def get_balance(self):
        self.cursor.execute(
            'SELECT balance FROM accounts WHERE user_id = %s',
            (self.user_id,)
        )
        result = self.cursor.fetchone()
        return result[0] if result else 0.0
