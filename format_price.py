import argparse
import textwrap
import math

def format_price(price):
    price = str(price).replace(' ', '')
    if get_whole_part(price):
        return get_whole_part(price)
    else:
        separators = [',', '.']
        for separator in separators:
            if is_split_on_two_part(price.split(separator)):
                whole_part, frac_part = price.split(separator)
                return create_pretty_price(whole_part, frac_part)
        return 'Error'


def create_pretty_price(integer, fraction):
    fraction_part = get_frac_part(fraction)
    whole_part = get_whole_part(integer)
    out = ''
    if not whole_part or not fraction_part:
        return 'Error'
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


def get_whole_part(number):
    try:
        return get_spaces(int(number))
    except ValueError:
        return None


def get_frac_part(number):
    try:
        fraction = float('0.%s' % number)
        fraction_rounded_str = str(round(fraction, 2))
        return fraction_rounded_str[2:]
    except ValueError:
        return None


def is_split_on_two_part(sample):
    return len(sample) == 2


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Format price')
    parser.add_argument('price', type=str, help='a digit for the change')
    args = parser.parse_args()
    print(format_price(args.price))
