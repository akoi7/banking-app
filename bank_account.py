import sqlite3

class BankAccount:
    def __init__(self, user_id):
        self.user_id = user_id
        self.conn = sqlite3.connect('bank.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
         # Create the accounts table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                user_id TEXT PRIMARY KEY,
                balance REAL DEFAULT 0.0
            )
        ''')

        # Create the transactions table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                amount REAL,
                type TEXT,  -- 'deposit' or 'withdraw'
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()

    def create_account(self):
        self.cursor.execute('INSERT OR IGNORE INTO accounts (user_id, balance) VALUES (?, ?)', (self.user_id, 0.0))
        self.conn.commit()

    def deposit(self, amount):
        # Step 1: Update balance in the accounts table
        self.cursor.execute(
            'UPDATE accounts SET balance = balance + ? WHERE user_id = ?',
            (amount, self.user_id)
        )

        # Step 2: Insert a transaction record
        self.cursor.execute(
            'INSERT INTO transactions (user_id, amount, type) VALUES (?, ?, ?)',
            (self.user_id, amount, 'deposit')
        )

        self.conn.commit()


    def withdraw(self, amount):
        current_balance = self.get_balance()
        if amount <= current_balance:
            # Step 1: Subtract from balance
            self.cursor.execute(
                'UPDATE accounts SET balance = balance - ? WHERE user_id = ?',
                (amount, self.user_id)
            )

            # Step 2: Record the withdrawal
            self.cursor.execute(
                'INSERT INTO transactions (user_id, amount, type) VALUES (?, ?, ?)',
                (self.user_id, amount, 'withdraw')
            )

            self.conn.commit()
        else:
            print("Insufficient funds.")


    def get_balance(self):
        self.cursor.execute('SELECT balance FROM accounts WHERE user_id = ?', (self.user_id,))
        result = self.cursor.fetchone()
        return result[0] if result else 0.0
