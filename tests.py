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

    def test_with_10_and_001(self):
        out = format_price('10.001')
        self.assertEqual(out, '10')

    def test_with_10_and_01(self):
        out = format_price('10.01')
        self.assertEqual(out, '10.01')

    def test_with_error_whole_1(self):
        out = format_price('10s.01')
        self.assertEqual(out, 'Error')

    def test_with_error_whole_1(self):
        out = format_price('s10.01')
        self.assertEqual(out, 'Error')

    def test_with_error_whole_2(self):
        out = format_price('s1s0.0001')
        self.assertEqual(out, 'Error')

    def test_with_error_whole_3(self):
        out = format_price('sasd')
        self.assertEqual(out, 'Error')

    def test_with_error_frac_1(self):
        out = format_price('1000.s')
        self.assertEqual(out, 'Error')

    def test_with_error_frac_1(self):
        out = format_price('1000.s')
        self.assertEqual(out, 'Error')

    def test_with_error_frac_2(self):
        out = format_price('1000.000s')
        self.assertEqual(out, 'Error')

    def test_with_error_frac_3(self):
        out = format_price('0.axs')
        self.assertEqual(out, 'Error')

    def test_with_error_whole_and_frac(self):
        out = format_price('x.s')
        self.assertEqual(out, 'Error')

    def test_with_error_empty_field(self):
        out = format_price('   ')
        self.assertEqual(out, 'Error')

    def test_with_error_double_dot(self):
        out = format_price('12.33.2')
        self.assertEqual(out, 'Error')

    def test_with_error_dash(self):
        out = format_price('12-15-')
        self.assertEqual(out, 'Error')

    def test_with_1_and_many_zeros(self):
        out = format_price('1.00000')
        self.assertEqual(out, '1')

    def test_with_2_and_many_nines(self):
        out = format_price('1.999999')
        self.assertEqual(out, '2')

if __name__ == '__main__':
    unittest.main()
