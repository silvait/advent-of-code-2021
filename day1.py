import sys


def parse_input(data):
    return [int(line) for line in data.splitlines()]


def count_increasing(numbers):
    prev = numbers[0]
    total = 0

    for cur in numbers[1:]:
        total += prev < cur
        prev = cur

    return total

def sliding_window_iter(arr, window_size):
    return (arr[i : i + window_size] for i in range(len(arr) - window_size + 1))


def sliding_window_sum(numbers, window_size):
    return [sum(w) for w in sliding_window_iter(numbers, window_size)]


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
