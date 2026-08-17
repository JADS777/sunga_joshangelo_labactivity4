import unittest
from main import Checkout, PL, DL, NoDiscount

class TestCheckout(unittest.TestCase):

    def test_pl_discount(self):
        checkout = Checkout(PL())
        result = checkout.calculate_total(100)
        self.assertEqual(result, 0)

    def test_dl_discount(self):
        checkout = Checkout(DL())
        result = checkout.calculate_total(100)
        self.assertEqual(result, 50)

    def test_no_discount(self):
        checkout = Checkout(NoDiscount())
        result = checkout.calculate_total(100)
        self.assertEqual(result, 100)

if __name__ == '__main__':
    unittest.main()
