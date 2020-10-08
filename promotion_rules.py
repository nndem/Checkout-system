"""
Module describe discount-rules.
Can be run singly.
"""

from mapper import initial_costs


class Rules:
    def __init__(self, items_counter):
        self.items_counter = items_counter
        self.new_cost = 0
        self.condition_type_a = {
            'type': 'A',
            'condition': {
                'count': 3,
                'cost': 75,
            },
            'action': self.get_discounted_price_for_type_a
        }

        self.condition_type_b = {
            'type': 'B',
            'condition': {
                'count': 2,
                'cost': 35
            },
            'action': self.get_discounted_price_for_type_b
        }

        self.condition_type_c = {
            'type': 'C',
            'action': self.get_discounted_price_for_type_c
        }

        self.condition_type_d = {
            'type': 'D',
            'action': self.get_discounted_price_for_type_d
        }

        self.condition_type_bonus = {
            'type': 'bonus',
            'action': self.get_discounted_price_for_type_bonus
            }

    def get_discounted_price_for_type_a(self):
        try:
            self.items_counter['A']
        except KeyError:
            pass
        else:
            amount_to_be_discount = self.items_counter['A'] // self.condition_type_a['condition']['count']
            amount_without_discount = (self.items_counter['A'] - amount_to_be_discount *
                                       self.condition_type_a['condition']['count'])
            self.new_cost = (self.new_cost + amount_to_be_discount *
                             self.condition_type_a['condition']['cost'] +
                             amount_without_discount * initial_costs['A'])
        return self.new_cost

    def get_discounted_price_for_type_b(self):
        try:
            self.items_counter['B']
        except KeyError:
            pass
        else:
            amount_to_be_discount = self.items_counter['B'] // self.condition_type_b['condition']['count']
            amount_without_discount = (self.items_counter['B'] - amount_to_be_discount *
                                       self.condition_type_b['condition']['count'])
            self.new_cost = (self.new_cost + amount_to_be_discount *
                             self.condition_type_b['condition']['cost'] +
                             amount_without_discount * initial_costs['B'])
        return self.new_cost

    def get_discounted_price_for_type_c(self):
        try:
            self.items_counter['C']
        except KeyError:
            pass
        else:
            self.new_cost = (self.new_cost + self.items_counter['C'] *
                             initial_costs['C'])
        return self.new_cost

    def get_discounted_price_for_type_d(self):
        try:
            self.items_counter['D']
        except KeyError:
            pass
        else:
            self.new_cost = self.new_cost + self.items_counter['D'] \
                            * initial_costs['D']
        return self.new_cost

    def get_discounted_price_for_type_bonus(self):
        print('price before bonus ', self.new_cost)
        self.new_cost = self.new_cost if self.new_cost < 150 else self.new_cost - 20
        return self.new_cost

    def get_discount_to_items(self):
        self.condition_type_a['action']()
        self.condition_type_b['action']()
        self.condition_type_c['action']()
        self.condition_type_d['action']()
        self.condition_type_bonus['action']()


def accept_discount():
    rules = Rules(items_counter={'A': 3, 'B': 2, 'C': 0, 'D': 0})
    return rules


if __name__ == '__main__':
    rules = accept_discount()
    rules.get_discount_to_items()
    print(rules.new_cost)
