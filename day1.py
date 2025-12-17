import sys


def parse_input(data: str) -> list[int]:
    return [int(s) for s in data.splitlines()]


def count_increasing(numbers: list[int]) -> int:
    return sum(prev < cur for prev, cur in windowed(numbers, 2))


def windowed(arr: list, window_size: int):
    return (arr[i : i + window_size] for i in range(len(arr) - window_size + 1))


def sliding_window_sum(numbers: list[int], window_size: int) -> list[int]:
    return [sum(w) for w in windowed(numbers, window_size)]


def part1(numbers: list[int]) -> int:
    return count_increasing(numbers)


def part2(numbers: list[int]) -> int:
    new_numbers = sliding_window_sum(numbers, 3)
    return count_increasing(new_numbers)


if __name__ == "__main__":
    filename = "./sample.txt" if len(sys.argv) < 2 else sys.argv[1]

    with open(filename, "r", encoding="utf-8") as f:
        parsed_data = parse_input(f.read())

        for solve in [part1, part2]:
            print(solve(parsed_data))
