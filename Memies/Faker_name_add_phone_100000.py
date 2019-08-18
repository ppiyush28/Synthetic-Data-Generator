import csv
import random
from time import time
from decimal import Decimal
from faker import Faker
from mimesis import Person
from mimesis import Address
from mimesis.schema import Field, Schema
from mimesis.enums import Gender
from mimesis import Generic


person = Person('en')
address = Address('en')
generic = Generic('en')
_ = Field('en')

RECORD_COUNT = 100000
fake = Faker()


def create_csv_file():
    with open('C:/Users/piyush/Desktop/Synetics Data gen/Memies/Memesis_data.csv', 'w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name', 'email', 'product_Num', 'qty',
                      'amount', 'description', 'address', 'city','postal code', 'state',
                      'country']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    'first_name': person.full_name(gender=None),
                    'last_name': _('surname', gender=None),
                    'email': person.email(),
                    'product_Num': _('uuid'),
                    'qty': fake.random_int(min=1, max=9),
                    'amount': float(Decimal(random.randrange(500, 10000))/100),
                    'description': generic.text.word(),
                    'address': address.address(),
                    'city': _('city'),
                    'postal code' : _('zip_code'),
                    'state': _('state'),
                    'country': _('country')
                }
            )


def get_totals():
    qty_total = 0
    amount_total = 0
    with open('C:/Users/piyush/Desktop/Synetics Data gen/Memies/Memesis_data.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if row[4] != 'qty':
                qty = int(row[4])
                qty_total += qty

                amount = float(row[5])
                amount_total += amount
    return qty_total, amount_total


if __name__ == '__main__':
    start = time()
    create_csv_file()
    elapsed = time() - start
    print('created csv file time: {}'.format(elapsed))

    start = time()
    qty_total, amount_total = get_totals()
    elapsed = time() - start
    print('got totals time: {}'.format(elapsed))

    #print('qty: {}'.format(qty_total))
    #print('amount: {}'.format(amount_total))