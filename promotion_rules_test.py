"""
Testing discount methods
"""

import unittest
from promotion_rules import Rules


class TestRules(unittest.TestCase):

    def test_get_discount_for_type_a(self):
        self.assertEqual(Rules(items_counter={'A': 6, 'B': 4, 'C': 1, 'D': 1})
                         .get_discounted_price_for_type_a(), 150)

    def test_get_discount_for_type_b(self):
        self.assertEqual(Rules(items_counter={'A': 3, 'B': 4, 'C': 1, 'D': 1})
                         .get_discounted_price_for_type_b(), 70)

    def test_get_discount_for_type_c(self):
        self.assertEqual(Rules(items_counter={'A': 3, 'B': 4, 'C': 1, 'D': 1})
                         .get_discounted_price_for_type_c(), 50)

    def test_get_discount_for_type_d(self):
        self.assertEqual(Rules(items_counter={'A': 3, 'B': 4, 'C': 1, 'D': 1})
                         .get_discounted_price_for_type_d(), 15)

    def test_get_discount_for_type_bonus(self):
        rules = Rules(items_counter={'A': 3, 'B': 4, 'C': 1, 'D': 1})
        rules.new_cost = 200
        self.assertEqual(rules.get_discounted_price_for_type_bonus(), 180)

    def get_all_discounts_to_items(self):
        self.assertEqual(Rules(items_counter={'A': 3, 'B': 2, 'C': 1, 'D': 1})
                         .get_discount_to_items(), 155)
