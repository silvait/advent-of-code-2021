import sys

from utils import get_input_filename


def parse_input(data: str):
    return []


def part1(*args) -> int:
    total = 0
    return total


def part2(*args) -> int:
    total = 0
    return total


if __name__ == "__main__":
    filename = get_input_filename(sys.argv)

    with open(filename, "r", encoding="utf-8") as f:
        parsed_data = parse_input(f.read())

        for solve in [part1, part2]:
            print(solve(parsed_data))
