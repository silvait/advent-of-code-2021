import sys
from collections import defaultdict

from utils import get_input_filename, get_line_points


def parse_input(data):
    ranges = []

    for line in data.splitlines():
        p1_str, p2_str = line.split(" -> ")
        ranges.append([parse_coordinate(p1_str), parse_coordinate(p2_str)])

    return ranges


def is_horizontal_or_vertical(coordinates):
    p1, p2 = coordinates
    (x1, y1), (x2, y2) = p1, p2
    return x1 == x2 or y1 == y2


def parse_coordinate(text: str) -> tuple[int, ...]:
    return tuple(int(c) for c in text.split(","))


def plot_lines(ranges):
    counts = defaultdict(int)

    for p1, p2 in ranges:
        for x, y in get_line_points(p1, p2):
            counts[(x, y)] += 1

    return counts


def count_overlaps(ranges):
    counts = plot_lines(ranges)
    return sum(v > 1 for v in counts.values())


def part1(ranges):
    filtered_ranges = filter(is_horizontal_or_vertical, ranges)
    return count_overlaps(filtered_ranges)


def part2(ranges):
    return count_overlaps(ranges)


if __name__ == "__main__":
    filename = get_input_filename(sys.argv)

    with open(filename, "r", encoding="utf-8") as f:
        parsed_data = parse_input(f.read())

        for solve in [part1, part2]:
            print(solve(parsed_data))
