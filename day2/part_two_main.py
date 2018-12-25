from collections import Counter
from itertools import zip_longest


INPUT_FILE = 'input.txt'
STRING_LENGTH = 26


def count_positional_diffs(x, y):
    return sum(
        bool(a != b) for a, b in zip_longest(x, y)
    )


def get_common_letters(x, y):
    return [a for a, b in zip_longest(x, y) if a == b]


def main():
    with open(INPUT_FILE, 'r') as fh:
        data = [line.strip() for line in fh]

    answer = []
    for x in data:
        for y in data:
            common_letters = get_common_letters(x, y)
            if len(common_letters) == STRING_LENGTH - 1:
                answer = ''.join(common_letters)

    print(f'Answer is "{answer}".')


if __name__ == '__main__':
    main()
