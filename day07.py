import sys
from functools import cache

from utils import get_input_filename


def parse_input(data: str) -> list[int]:
    return list(map(int, data.split(",")))


def calculate_fuel(positions: list[int], target: int, constant: bool) -> int:
    total = 0

    for p in positions:
        steps = abs(p - target)
        total += steps if constant else calculate_cost(steps)

    return total


@cache
def calculate_cost(steps: int) -> int:
    return sum(range(1, steps + 1))


def find_alignment(positions, constant=False):
    highest = max(positions)
    return min(calculate_fuel(positions, i, constant) for i in range(highest + 1))


def part1(positions: list[int]) -> int:
    return find_alignment(positions, True)


def part2(positions: list[int]) -> int:
    return find_alignment(positions)


if __name__ == "__main__":
    filename = get_input_filename(sys.argv)

    with open(filename, "r", encoding="utf-8") as f:
        parsed_data = parse_input(f.read())

        for solve in [part1, part2]:
            print(solve(parsed_data))
