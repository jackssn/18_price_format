import unittest

from format_price import format_price


class FormatPriceTestCase(unittest.TestCase):

    def test_without_fractional_part(self):
        out = format_price('100.0')
        self.assertEqual(out, '100')

    def test_with_correct_round(self):
        out = format_price('100.039')
        self.assertEqual(out, '100.04')

    def test_with_6_digits_without_fractional_part(self):
        out = format_price('100000')
        self.assertEqual(out, '100 000')

    def test_with_6_digits(self):
        out = format_price('333333.55745567645')
        self.assertEqual(out, '333 333.56')

    def test_with_5_digits(self):
        out = format_price('33333.55745567645')
        self.assertEqual(out, '33 333.56')

    def test_with_4_digits(self):
        out = format_price('1234.01')
        self.assertEqual(out, '1 234.01')

    def test_without_fractional_part_comma(self):
        out = format_price('100,0')
        self.assertEqual(out, '100')

    def test_with_correct_round_comma(self):
        out = format_price('100,039')
        self.assertEqual(out, '100.04')

    def test_with_6_digits_without_fractional_part_comma(self):
        out = format_price('100000')
        self.assertEqual(out, '100 000')

    def test_with_6_digits_comma(self):
        out = format_price('333333,55745567645')
        self.assertEqual(out, '333 333.56')

    def test_with_5_digits_comma(self):
        out = format_price('33333,55745567645')
        self.assertEqual(out, '33 333.56')

    def test_with_4_digits_comma(self):
        out = format_price('1234,01')
        self.assertEqual(out, '1 234.01')

    def test_with_6_digits_without_fractional_part_space(self):
        out = format_price('100 000 ')
        self.assertEqual(out, '100 000')

    def test_with_6_digits_space(self):
        out = format_price('33 333 3.55745567645')
        self.assertEqual(out, '333 333.56')

    def test_with_5_digits_space(self):
        out = format_price('33 333.55745567645')
        self.assertEqual(out, '33 333.56')

if __name__ == '__main__':
    unittest.main()
