import sys


def parse_input(data):
    return [int(line) for line in data.splitlines()]


def count_increasing(numbers):
    return sum(prev < cur for prev, cur in windowed(numbers, 2))


def windowed(arr, window_size):
    return (arr[i : i + window_size] for i in range(len(arr) - window_size + 1))


def sliding_window_sum(numbers, window_size):
    return [sum(w) for w in windowed(numbers, window_size)]


def part1(numbers):
    return count_increasing(numbers)


def part2(numbers):
    new_numbers = sliding_window_sum(numbers, 3)
    return count_increasing(new_numbers)


if __name__ == "__main__":
    filename = "./sample.txt" if len(sys.argv) < 2 else sys.argv[1]

    with open(filename) as f:
        parsed_data = parse_input(f.read())
        print(part1(parsed_data))
        print(part2(parsed_data))
