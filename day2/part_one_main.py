from collections import Counter


INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as fh:
        counters = (Counter(line) for line in fh)
        count_sets = (set(c.values()) for c in counters)
        twos_and_threes = ({v for v in s if v >= 2} for s in count_sets)
        counts = [(bool(2 in s), bool(3 in s)) for s in twos_and_threes]

        number_of_twos = sum(x[0] for x in counts)
        number_of_threes = sum(x[1] for x in counts)

        print(f'Answer is {number_of_twos} * {number_of_threes} = {number_of_twos * number_of_threes}')


if __name__ == '__main__':
    main()
