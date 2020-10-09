"""Python 3.7. Launch all tests."""
import unittest

test_modules = ['main_test', 'promotion_rules_test']

if __name__ == '__main__':
    suite = unittest.TestSuite()
    for tm in test_modules:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(tm))
    unittest.TextTestRunner().run(suite)
