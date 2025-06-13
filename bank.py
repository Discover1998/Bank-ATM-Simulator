import card_generator
import json
import os

DATA_FILE = "cards.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump({}, f)

with open(DATA_FILE) as f:
    data = json.load(f)

def update():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

class Bank:
    def __init__(self, name, address, country):
        self.name = name
        self.country = country
        self.address = address
        self.users = len(data)

    def add_user(self, name, address, country):
        user_card = card_generator.Card(name=name, address=address, country=country)
        user_card.save_to_file()
        self.users += 1
        return f"Card created for {name} with card number {user_card.id}, expiration {user_card.valid}, and CVV {user_card.cvc}"

    def remove_user(self, name, card_number):
        if card_number in data:
            del data[card_number]
            update()
            self.users -= 1
            return f"Card removed for {name} with card number {card_number}"
        return "User not found."

    def get_user(self, card_number):
        return data.get(card_number, "User not found.")

    def add_balance(self, card_number, amount):
        if card_number in data:
            data[card_number]['value'] += amount
            update()
            return f"Balance added for {card_number}, new balance: {data[card_number]['value']}"
        return "Card not found."

    def remove_balance(self, card_number, amount):
        if card_number in data and data[card_number]['value'] >= amount:
            data[card_number]['value'] -= amount
            update()
            return f"Balance removed for {card_number}, new balance: {data[card_number]['value']}"
        return "Insufficient balance or card not found."

if __name__ == "__main__":
    bank = Bank("Test Bank", "123 Main St", "USA")
    print(bank.add_user("John Doe", "123 Main St", "USA"))
