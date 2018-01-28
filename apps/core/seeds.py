import random
from decimal import Decimal

from . import models


class Seeder:

    def __init__(self):
        self.products = [
            'Orange Ball', 'Chew Toy 1', 'Car Bowl',
            'Dog Bed' 'Cat Food', 'Dog Food'
        ]

    def seed(self):
        for x in range(20):
            title = random.choice(self.products) + f' {random.randint(1, 10000)}'
            price = float(format(Decimal(str(random.random())), '.2f'))
            quantity = random.randint(1, 100)
            customer = models.User.objects.get(pk=random.randint(1, 3))
            product = models.Product(title=title, price=price)
            product.save()
            sale = models.Sale(
                product=product,
                quantity=quantity,
                customer=customer
            )
            sale.save()
