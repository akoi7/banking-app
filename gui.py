import tkinter as tk
from tkinter import messagebox
from bank_account import BankAccount

def handle_create_account():
    user_id = entry_user_id.get()
    if not user_id:
        messagebox.showwarning("Input Error", "Please enter a User ID.")
        return
    account = BankAccount(user_id)
    account.create_account()
    messagebox.showinfo("Success", f"Account for '{user_id}' created.")

def handle_deposit():
    try:
        user_id = entry_user_id.get()
        amount = float(entry_amount.get())
        account = BankAccount(user_id)
        account.deposit(amount)
        messagebox.showinfo("Success", f"${amount:.2f} deposited.")
    except ValueError:
        messagebox.showerror("Input Error", "Enter a valid amount.")

def handle_withdraw():
    try:
        user_id = entry_user_id.get()
        amount = float(entry_amount.get())
        account = BankAccount(user_id)
        account.withdraw(amount)
        messagebox.showinfo("Success", f"${amount:.2f} withdrawn.")
    except ValueError:
        messagebox.showerror("Input Error", "Enter a valid amount.")

def handle_balance():
    user_id = entry_user_id.get()
    if not user_id:
        messagebox.showwarning("Input Error", "Please enter a User ID.")
        return
    account = BankAccount(user_id)
    balance = account.get_balance()
    messagebox.showinfo("Balance", f"Balance: ${balance:.2f}")

# GUI Setup
root = tk.Tk()
root.title("MySQL Banking App")

tk.Label(root, text="User ID").pack(pady=5)
entry_user_id = tk.Entry(root)
entry_user_id.pack()

tk.Label(root, text="Amount").pack(pady=5)
entry_amount = tk.Entry(root)
entry_amount.pack()

tk.Button(root, text="Create Account", command=handle_create_account).pack(pady=2)
tk.Button(root, text="Deposit", command=handle_deposit).pack(pady=2)
tk.Button(root, text="Withdraw", command=handle_withdraw).pack(pady=2)
tk.Button(root, text="Check Balance", command=handle_balance).pack(pady=2)

root.mainloop()
