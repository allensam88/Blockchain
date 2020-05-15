"""
Allow the user to enter, save, or change the `id` used for the program
Display the current balance for that user
Display a list of all transactions for this user, including sender and recipient
"""

import requests

user_id = input('Enter user id: ')


def transactions():
    data = requests.get('http://localhost:5000/chain').json()
    chain = data['chain']

    balance = 0
    sent = []
    received = []

    for block in chain:
        for transaction in block['transactions']:
            if transaction['sender'] == user_id:
                balance -= transaction['amount']
                sent.append((transaction['amount'], transaction['recipient']))
            if transaction['recipient'] == user_id:
                balance += transaction['amount']
                received.append((transaction['amount'], transaction['sender']))
    return balance, sent, received


transaction_data = transactions()
balance = transaction_data[0]
debits = transaction_data[1]
credits = transaction_data[2]

print(f'Your current balance is: {balance}')

if debits:
    print('\nDebit Activity')
    for debit_activity in debits:
        print(f'Sent {debit_activity[0]} coins to {debit_activity[1]}')

if credits:
    print('\nCredit Activity')
    for credit_activity in credits:
        print(f'Received {credit_activity[0]} coins from {credit_activity[1]}')
