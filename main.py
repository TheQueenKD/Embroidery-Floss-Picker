import random
import sys


COLORS = [
    '001',
    '002',
    '003',
]


def validate_input_or_exit(num_colors):
    if num_colors <= 0 or num_colors > len(COLORS):
        print(f'Sorry... expected a value between 1 and {len(COLORS)}!')
        sys.exit(1)


def print_readable_color_picks(num_colors):
    picks = color_picker(num_colors)
    for pick in picks:
        print(pick)


def color_picker(number):
    return random.sample(COLORS, number)


if __name__ == '__main__':
    num_colors = int(input('How many colors? ') or 1)
    validate_input_or_exit(num_colors)
    print()
    print('You should use: ')
    print_readable_color_picks(num_colors)
