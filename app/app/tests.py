from django.test import TestCase

from app.calc import add

class CalcTest(TestCase):

    def test_add_numbers(self):

        self.assertEqual(add(5,4),7)