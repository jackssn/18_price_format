import argparse
import textwrap


PRICE_FORMATTING_FAIL = 'Error'


def format_price(price):
    price_str = str(price).replace(' ', '')
    price_without_fraction = get_whole_part(price_str)
    if price_without_fraction:
        return price_without_fraction
    else:
        separators = [',', '.']
        for separator in separators:
            price_parts = price_str.split(separator)
            if is_split_on_two_part(price_parts):
                whole_part, frac_part = price_parts
                return create_pretty_price(whole_part, frac_part)
        return PRICE_FORMATTING_FAIL


def create_pretty_price(integer_str, fraction_str):
    whole_adding, fraction_part = get_frac_part(fraction_str)
    whole_part = get_whole_part(integer_str, whole_adding)
    out = ''
    if not whole_part or not fraction_part:
        return PRICE_FORMATTING_FAIL
    if whole_part:
        out += whole_part
    if fraction_part != '0':
        out += '.%s' % fraction_part
    return out


def get_spaces(integer):
    if integer:
        transversed_number_string = str(integer)[::-1]
        return ' '.join(textwrap.wrap(transversed_number_string, 3))[::-1]
    return None


def get_whole_part(number, adding_from_frac_part=0):
    try:
        return get_spaces(int(number)+int(adding_from_frac_part))
    except ValueError:
        return None


def get_frac_part(number):
    try:
        fraction = float('0.%s' % number)
        fraction_rounded_str = str(round(fraction, 2))
        return fraction_rounded_str[0], fraction_rounded_str[2:]
    except ValueError:
        return 0, None


def is_split_on_two_part(sample):
    return len(sample) == 2


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Format price_str')
    parser.add_argument('price_str', type=str, help='a digit for the change')
    args = parser.parse_args()
    print(format_price(args.price_str))
