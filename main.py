from picker import validate_input_or_exit, print_readable_color_picks


if __name__ == '__main__':
    num_colors = int(input('How many colors? (default: 1)\t') or 1)
    validate_input_or_exit(num_colors)
    print('\nYou should use: ')
    print_readable_color_picks(num_colors)
