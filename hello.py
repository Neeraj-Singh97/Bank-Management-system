import json
from numbers import Number
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    
    @classmethod
    def load_data(cls):
        if Path(cls.database).exists():
            with open(cls.database, 'r') as fs:
                return json.load(fs)
        return []

    @classmethod
    def save_data(cls, data):
        with open(cls.database, 'w') as fs:
            json.dump(data, fs, indent=4)

    @classmethod
    def generate_account_number(cls):
        chars = random.choices("0123456789", k=10)
        random.shuffle(chars)
        return ''.join(chars)

    @classmethod
    def create_account(cls, name, age, email, pin, phone_number, address, aadhaar):
        data = cls.load_data()
        if age < 18 or len(str(pin)) != 4 or len(str(aadhaar)) != 12:
            return None, "Age must be 18+, PIN should be 4 digits, Aadhaar should be 12 digits"
        acc_no = cls.generate_account_number()
        user = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "Phone Number": phone_number,
            "address": address,
            "aadhaar": aadhaar,
            "accountNo.": acc_no,
            "balance": 0,
            "transactions": [] 

        }
        data.append(user)
        cls.save_data(data)
        return user, "Account created successfully"

    @classmethod
    def find_user(cls, acc_no, pin):
        data = cls.load_data()
        for user in data:
            if user['accountNo.'] == acc_no and user['pin'] == pin:
                return user
        return None

    @classmethod
    def deposit(cls, acc_no, pin, amount):
        data = cls.load_data()
        for user in data:
            if user['accountNo.'] == acc_no and user['pin'] == pin:
                if 0 < amount <= 90000:
                    user['balance'] += amount
                    user.setdefault('transactions', []).append({
                        "type": "Deposit",
                        "amount": amount,
                        "balance": user['balance']
                    })
                    cls.save_data(data)
                    return True, "Deposit successful"
                return False, "Amount must be between 1 and 90000"
        return False, "Invalid account or PIN"


    @classmethod
    def withdraw(cls, acc_no, pin, amount):
        data = cls.load_data()
        for user in data:
            if user['accountNo.'] == acc_no and user['pin'] == pin:
                if user['balance'] >= amount:
                    user['balance'] -= amount
                    user.setdefault('transactions', []).append({
                        "type": "Withdraw",
                        "amount": amount,
                        "balance": user['balance']
                    })
                    cls.save_data(data)
                    return True, "Withdrawal successful"
                return False, "Insufficient balance"
        return False, "Invalid account or PIN"

    @classmethod
    def update_user(cls, acc_no, pin, name=None, email=None, new_pin=None):
        data = cls.load_data()
        for user in data:
            if user['accountNo.'] == acc_no and user['pin'] == pin:
                user['name'] = name or user['name']
                user['email'] = email or user['email']
                user['pin'] = int(new_pin) if new_pin else user['pin']
                cls.save_data(data)
                return True, "User details updated"
        return False, "User not found"

    @classmethod
    def delete_user(cls, acc_no, pin):
        data = cls.load_data()
        for i, user in enumerate(data):
            if user['accountNo.'] == acc_no and user['pin'] == pin:
                data.pop(i)
                cls.save_data(data)
                return True, "Account deleted"
        return False, "Account not found"
    @classmethod
    def list_account_numbers(cls):
        data = cls.load_data()
        return [user['accountNo.'] for user in data]
