import itertools
import re
from collections import defaultdict, namedtuple


INPUT_FILE = 'input.txt'
PATTERN = re.compile(
    r'#\d+ @ (?P<left_gap>\d+),(?P<top_gap>\d+): (?P<width>\d+)x(?P<height>\d+)'
)


Claim = namedtuple('Claim', ['left_gap', 'top_gap', 'width', 'height'])


def generate_pairs_from_claim(claim):
    return [
        (y, x)
        for y in range(claim.top_gap, claim.top_gap+claim.height)
        for x in range(claim.left_gap, claim.left_gap+claim.width)
    ]


def main():
    with open(INPUT_FILE, 'r') as fh:
        data = (line.strip() for line in fh)
        matches = (PATTERN.match(line) for line in data)
        match_groups = (
            map(int, match.group('left_gap', 'top_gap', 'width', 'height'))
            for match in matches
            if match is not None
        )
        claims = [Claim(*group) for group in match_groups]

    pair_occurrences = defaultdict(int)
    pairs = itertools.chain.from_iterable(
        generate_pairs_from_claim(claim) for claim in claims
    )
    for pair in pairs:
        pair_occurrences[pair] += 1

    multiple_claimed_squares = [
        occurrences
        for occurrences in pair_occurrences.values()
        if occurrences >= 2
    ]
    number_of_multiples = len(multiple_claimed_squares)

    print(f'Answer is {number_of_multiples} squares.')


if __name__ == '__main__':
    main()
