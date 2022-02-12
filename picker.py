"""All functions for app"""

import random
import sys
import typing as t

from constants import COLORS


def validate_input_or_exit(num_colors: int) -> None:
    """
    Validate `num_colors` is between 1 and length of `COLORS`, or exit with error code 1
    :param num_colors: integer
    :return: None
    """
    if num_colors <= 0 or num_colors > len(COLORS):
        print(f'Sorry... expected a value between 1 and {len(COLORS)}!')
        sys.exit(1)


def print_readable_color_picks(num_colors: int) -> None:
    """
    Print `num_colors` chosen colors from `COLORS`
    :param num_colors: integer
    :return: None
    """
    picks = color_picker(num_colors)
    for pick in picks:
        print(pick)


def color_picker(num_colors: int) -> t.List[str]:
    """
    Return a randomly chosen list of `num_colors` colors without repeating from `COLORS`
    :param num_colors: integer
    :return: List of chosen colors
    """
    return random.sample(COLORS, num_colors)
