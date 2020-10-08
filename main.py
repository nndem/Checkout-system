""""
Module contains main-function to run the app.
"""

import collections
from entity import Entity
from promotion_rules import Rules


class Checkout:
    """
    Class contains basics methods for checkout system
    """
    def __init__(self):
        self.basket = []
        self.total_cost = 0
        self.analyzed_items = {}

    def scan(self, entity):
        """
        Method adds new item into the basket
        @param entity: obj
        """
        self.basket.append(entity.type)

    @property
    def total(self):
        """"
        Analyzes chosen item and updates their cost in accordance
        with the discounts.
        @returns total cost
        """
        self.analyzed_items = self.basket_analyzer()
        self.update_cost()
        return self.total_cost

    def update_cost(self):
        """"
        Methods provides a Rules object that provides discount-methods to items
        """
        rules = Rules(self.analyzed_items)
        rules.get_discount_to_items()
        self.total_cost = rules.new_cost

    def basket_analyzer(self):
        """
        @return: dict of countered item , e.g. {'A':3, 'B':4,...}
        """
        try:
            iter(self.basket)
        except TypeError:
            print(self.basket, 'is not iterable')
        else:
            return collections.Counter(self.basket)


if __name__ == '__main__':
    co = Checkout()

    co.scan(Entity('A'))
    co.scan(Entity('A'))
    co.scan(Entity('A'))
    co.scan(Entity('B'))
    co.scan(Entity('B'))
    price = co.total
    print("Discounted items new cost", price)
