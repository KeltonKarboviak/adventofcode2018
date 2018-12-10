import itertools


INPUT_FILE = 'input.txt'


def main():
    results = set()
    frequency = 0
    with open(INPUT_FILE, 'r') as fh:
        fh_ints = (int(line) for line in fh)
        cycle = itertools.cycle(fh_ints)
        for i in cycle:
            frequency += i
            if frequency in results:
                break
            else:
                results.add(frequency)

    print(f'First duplicate is {frequency} frequency.')


if __name__ == '__main__':
    main()
