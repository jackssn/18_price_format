import argparse
import textwrap


def format_price(price):
    price = str(price).replace(' ', '')
    if get_whole_part(price):
        return get_whole_part(price)
    else:
        separators = [',', '.']
        for separator in separators:
            if split_validation(price.split(separator)):
                whole_part, frac_part = price.split(separator)
                return create_pretty_price(whole_part, frac_part)


def create_pretty_price(integer, fraction):
    if int(fraction) == 0:
        return get_whole_part(integer)
    else:
        return "%s.%s" % (get_whole_part(integer), get_frac_part(fraction))


def get_spaces(integer):
    if integer:
        integer = str(integer)[::-1]
        return ' '.join(textwrap.wrap(integer, 3))[::-1]
    return None


def get_whole_part(number):
    try:
        return get_spaces(int(number))
    except:
        return None


def get_frac_part(number):
    try:
        return str(round(float('0.%s' % number), 2))[2:]
    except:
        return None


def split_validation(sample):
    if len(sample) == 2:
        return True
    return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Format price')
    parser.add_argument('price', type=str, help='a digit for the change')
    args = parser.parse_args()
    print(format_price(args.price))
