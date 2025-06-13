import random
import datetime
import json
import os
from dateutil.relativedelta import relativedelta

DATA_FILE = 'cards.json'

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump({}, f)

with open(DATA_FILE, 'r') as f:
    data = json.load(f)

def generate_numbers():
    return random.randint(9999999999, 999999999999)

def pin_generator():
    return random.randint(1000, 9999)

class Card:
    def __init__(self, type="Visa", name="", pin=None, id=None, value=0, address="", country=""):
        self.type = type
        self.name = name
        if id is None:
            self.id = generate_numbers()
            while str(self.id) in data.keys():
                self.id = generate_numbers()
        self.pin = pin_generator()
        self.value = value
        self.valid = (datetime.date.today() + relativedelta(years=2)).isoformat()
        self.cvc = f"{random.randint(0, 999):03}"
        self.address = address
        self.country = country

    def to_dict(self):
        return {
            "name": self.name,
            "type": self.type,
            "pin": str(self.pin),
            "value": self.value,
            "valid_until": self.valid,
            "cvc": self.cvc
        }

    def save_to_file(self):
        data[str(self.id)] = self.to_dict()
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)

if __name__ == "__main__":
    full_name = input("Enter your full name: ")
    card = Card(name=full_name)
    card.save_to_file()
    print("Card generated and saved!")
    print("Card:", card.name, card.type, card.id, card.value, card.valid, card.cvc)
