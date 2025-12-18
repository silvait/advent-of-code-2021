import sys
from collections import defaultdict

from utils import get_input_filename, get_line_points

type Coordinate = tuple[int, int]
type Segment = tuple[Coordinate, Coordinate]

COORDINATE_SEPARATOR = ","
SEGMENT_SEPARATOR = " -> "


def parse_coordinate(text: str) -> Coordinate:
    x, y = map(int, text.split(COORDINATE_SEPARATOR))
    return (x, y)


def parse_segment(text: str) -> Segment:
    start, end = text.split(SEGMENT_SEPARATOR)
    return (parse_coordinate(start), parse_coordinate(end))


def parse_input(data: str) -> list[Segment]:
    return list(map(parse_segment, data.splitlines()))


def is_horizontal_or_vertical(segment: Segment) -> bool:
    start, end = segment
    (x1, y1), (x2, y2) = start, end
    return x1 == x2 or y1 == y2


def plot_segments(segments: list[Segment]) -> dict[Coordinate, int]:
    counts = defaultdict(int)

    for p1, p2 in segments:
        for x, y in get_line_points(p1, p2):
            counts[(x, y)] += 1

    return counts


def count_overlapping_points(segments: list[Segment]) -> int:
    grid = plot_segments(segments)
    return sum(count > 1 for count in grid.values())


def part1(segments: list[Segment]) -> int:
    filtered_ranges = list(filter(is_horizontal_or_vertical, segments))
    return count_overlapping_points(filtered_ranges)


def part2(segments: list[Segment]) -> int:
    return count_overlapping_points(segments)


if __name__ == "__main__":
    filename = get_input_filename(sys.argv)

    with open(filename, "r", encoding="utf-8") as f:
        parsed_data = parse_input(f.read())

        for solve in [part1, part2]:
            print(solve(parsed_data))
