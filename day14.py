import sys
from collections import Counter

from utils import get_input_filename

type Rules = dict[str, str]


def parse_rules(lines: list[str]) -> Rules:
    rules = {}

    for current in lines:
        pair, insertion = current.split(" -> ")
        rules[pair] = insertion

    return rules


def parse_input(data: str) -> tuple[str, Rules]:
    lines = data.splitlines()

    template = lines[0]
    rules = parse_rules(lines[2:])

    return template, rules


def adjacent_pairs(template: str) -> list[str]:
    return [template[i : i + 2] for i in range(len(template) - 1)]


def apply_rules(template: str, rules: Rules, count: int) -> int:
    current_pairs = Counter(adjacent_pairs(template))
    element_totals = Counter(template)

    for i in range(count):
        next_pairs = Counter()

        for pair, count in current_pairs.items():
            insertion = rules[pair]
            first, second = pair

            next_pairs[first + insertion] += count
            next_pairs[insertion + second] += count

            element_totals[insertion] += count

        current_pairs = next_pairs

    totals = element_totals.values()
    most_common = max(totals)
    least_common = min(totals)

    return most_common - least_common


def part1(template: str, rules: Rules) -> int:
    return apply_rules(template, rules, 10)


def part2(template: str, rules: Rules) -> int:
    return apply_rules(template, rules, 40)


if __name__ == "__main__":
    filename = get_input_filename(sys.argv)

    with open(filename, "r", encoding="utf-8") as f:
        parsed_data = parse_input(f.read())

        for solve in [part1, part2]:
            print(solve(*parsed_data))
