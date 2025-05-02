import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("test_user")
        # Reset account if it already exists
        self.cursor = self.account.conn.cursor()
        self.cursor.execute("DELETE FROM accounts WHERE user_id = ?", ("test_user",))
        self.cursor.execute("DELETE FROM transactions WHERE user_id = ?", ("test_user",))
        self.account.conn.commit()
        self.account.create_account()

    def test_deposit(self):
        self.account.deposit(100)
        self.assertEqual(self.account.get_balance(), 100)

    def test_withdraw(self):
        self.account.deposit(100)
        self.account.withdraw(40)
        self.assertEqual(self.account.get_balance(), 60)

    def test_insufficient_funds(self):
        self.account.withdraw(200)  # assuming balance starts at 0
        self.assertEqual(self.account.get_balance(), 0)

if __name__ == '__main__':
    unittest.main()
