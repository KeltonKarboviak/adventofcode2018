INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as fh:
        total_frequency = sum(int(line) for line in fh)

    print(f'Answer is {total_frequency} frequency.')


if __name__ == '__main__':
    main()
