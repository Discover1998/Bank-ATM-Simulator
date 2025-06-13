import json
import datetime

DATA_FILE = "cards.json"

def load_file():
    with open(DATA_FILE) as f:
        return json.load(f)

def update(data):
    with open(DATA_FILE, 'w', encoding='utf8') as f:
        json.dump(data, f, indent=4)

def withdraw(card_id, take_money, data):
    if card_id in data:
        if data[card_id]["value"] < take_money:
            return "Not enough money"
        data[card_id]["value"] -= take_money
        update(data)
        return f"Withdrawal successful. Remaining balance: {data[card_id]['value']} USD."

def add_money(card_id, amount, data):
    if card_id in data:
        data[card_id]["value"] += amount
        update(data)
        return "Money added successfully to your balance."

def display_balance(card_id, data):
    if card_id in data:
        return f"Your current balance: {data[card_id]['value']} USD."

def main():
    data = load_file()
    while True:
        print("====================================================")
        print("	 Welcome to the ATM 	")
        print(f"	 {datetime.date.today()} : {datetime.datetime.now().strftime('%H:%M')}	")
        print("====================================================")
        card_num = input("Enter your card number: ")
        pin = input("Enter your PIN: ")

        if card_num in data and data[card_num]['pin'] == pin:
            while True:
                print("\n1. Withdraw\n2. Add Money\n3. Display Balance\n4. Exit")
                choice = input("Enter your choice: ")
                if choice == '1':
                    amount = int(input("Amount to withdraw: "))
                    print(withdraw(card_num, amount, data))
                elif choice == '2':
                    amount = int(input("Amount to deposit: "))
                    print(add_money(card_num, amount, data))
                elif choice == '3':
                    print(display_balance(card_num, data))
                elif choice == '4':
                    print("Have a nice day!")
                    break
        else:
            print("Invalid card number or PIN.")
        print("====================================================")

if __name__ == "__main__":
    main()
