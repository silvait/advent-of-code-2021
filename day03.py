import sys
from collections.abc import Callable

from utils import get_input_filename

type Bits = list[bool]
type Report = list[Bits]


def parse_input(data: str) -> Report:
    return [[c == "1" for c in line] for line in data.splitlines()]


def bools_to_int(bools: Bits) -> int:
    binary_str = ["1" if b else "0" for b in bools]
    return int("".join(binary_str), 2)


def part1(report: Report) -> int:
    ones_count = report[0][:]

    for line in report[1:]:
        for i, bit in enumerate(line):
            ones_count[i] += bit

    half = len(report) / 2
    most_common = [zeros > half for zeros in ones_count]
    gamma_rate = bools_to_int(most_common)

    least_common = [not bit for bit in most_common]
    epsilon_rate = bools_to_int(least_common)

    return gamma_rate * epsilon_rate


def calculate_rating(report: Report, selector: Callable[[list, list], int]) -> int:
    current = report[:]

    for i in range(len(current[0])):
        partitions = [[], []]

        for line in current:
            bit = line[i]
            partitions[bit].append(line)

        chosen_partition = selector(partitions[0], partitions[1])
        current = partitions[chosen_partition]

        if len(current) == 1:
            break

    return bools_to_int(current[0])


def calculate_oxygen_rating(report: Report) -> int:
    def pick_most_common(zeros: list, ones: list) -> int:
        return 1 if len(ones) >= len(zeros) else 0

    return calculate_rating(report, pick_most_common)


def calculate_co2_rating(report: Report) -> int:
    def pick_least_common(zeros: list, ones: list) -> int:
        return 0 if len(zeros) <= len(ones) else 1

    return calculate_rating(report, pick_least_common)


def part2(report: Report) -> int:
    o_rating = calculate_oxygen_rating(report)
    co2_rating = calculate_co2_rating(report)

    return o_rating * co2_rating


if __name__ == "__main__":
    filename = get_input_filename(sys.argv)

    with open(filename, "r", encoding="utf-8") as f:
        parsed_data = parse_input(f.read())

        for solve in [part1, part2]:
            print(solve(parsed_data))
