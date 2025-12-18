import sys
from collections import defaultdict
from collections.abc import Iterable

from utils import (
    Coordinate,
    Segment,
    get_input_filename,
    get_line_points,
    parse_segment,
)


def parse_input(data: str) -> list[Segment]:
    return list(map(parse_segment, data.splitlines()))


def is_horizontal_or_vertical(segment: Segment) -> bool:
    start, end = segment
    (x1, y1), (x2, y2) = start, end
    return x1 == x2 or y1 == y2


def plot_segments(segments: Iterable[Segment]) -> dict[Coordinate, int]:
    counts = defaultdict(int)

    for p1, p2 in segments:
        for x, y in get_line_points(p1, p2):
            counts[(x, y)] += 1

    return counts


def count_overlapping_points(segments: Iterable[Segment]) -> int:
    grid = plot_segments(segments)
    return sum(count > 1 for count in grid.values())


def part1(segments: list[Segment]) -> int:
    vertical_or_horizontal_segments = filter(is_horizontal_or_vertical, segments)
    return count_overlapping_points(vertical_or_horizontal_segments)


def part2(segments: list[Segment]) -> int:
    return count_overlapping_points(segments)


if __name__ == "__main__":
    filename = get_input_filename(sys.argv)

    with open(filename, "r", encoding="utf-8") as f:
        parsed_data = parse_input(f.read())

        for solve in [part1, part2]:
            print(solve(parsed_data))
