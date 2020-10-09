"""
Testing script
"""

import unittest
from main import Checkout
from entity import Entity


class TestRules(unittest.TestCase):

    def test1_total_price(self):
        co = Checkout()
        co.scan(Entity('A'))
        co.scan(Entity('B'))
        co.scan(Entity('C'))
        self.assertEqual(co.total, 100)

    def test2_total_price(self):
        co = Checkout()
        co.scan(Entity('B'))
        co.scan(Entity('A'))
        co.scan(Entity('B'))
        co.scan(Entity('A'))
        co.scan(Entity('A'))
        self.assertEqual(co.total, 110)

    def test3_total_price(self):
        co = Checkout()
        co.scan(Entity('C'))
        co.scan(Entity('B'))
        co.scan(Entity('A'))
        co.scan(Entity('A'))
        co.scan(Entity('D'))
        co.scan(Entity('A'))
        co.scan(Entity('B'))
        self.assertEqual(co.total, 155)

    def test4_total_price(self):
        co = Checkout()
        co.scan(Entity('C'))
        co.scan(Entity('A'))
        co.scan(Entity('D'))
        co.scan(Entity('A'))
        co.scan(Entity('A'))
        self.assertEqual(co.total, 140)


if __name__ == '__main__':
    unittest.main()
