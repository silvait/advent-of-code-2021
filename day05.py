import sys
from collections import defaultdict

from utils import get_input_filename


def parse_input(data):
    ranges = []

    for line in data.splitlines():
        first, second = line.split(" -> ")
        ranges.append([parse_coordinate(first), parse_coordinate(second)])

    return ranges


def is_straight(c1, c2):
    return c1[0] == c2[0] or c1[1] == c2[1]


def parse_coordinate(text: str) -> tuple[int, ...]:
    return tuple(int(c) for c in text.split(","))


def draw_and_count(ranges):
    counts = defaultdict(int)

    for c1, c2 in ranges:
        for x, y in integer_line_points(c1, c2):
            counts[(x, y)] += 1

    return sum(v > 1 for v in counts.values())


def part1(ranges):
    return draw_and_count([(c1, c2) for c1, c2 in ranges if is_straight(c1, c2)])


def integer_line_points(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        points.append((x1, y1))

        if x1 == x2 and y1 == y2:
            break

        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

    return points


def part2(ranges):
    return draw_and_count(ranges)


if __name__ == "__main__":
    filename = get_input_filename(sys.argv)

    with open(filename, "r", encoding="utf-8") as f:
        parsed_data = parse_input(f.read())

        for solve in [part1, part2]:
            print(solve(parsed_data))
