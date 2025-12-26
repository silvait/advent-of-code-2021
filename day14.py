import sys
from collections import Counter

from utils import get_input_filename

type Rules = dict[str, str]

RULE_SEPARATOR = " -> "
PART1_STEPS = 10
PART2_STEPS = 40


def parse_rules(rule_lines: list[str]) -> Rules:
    return dict(line.split(RULE_SEPARATOR) for line in rule_lines)


def parse_input(data: str) -> tuple[str, Rules]:
    template, _, *rule_lines = data.splitlines()

    return template, parse_rules(rule_lines)


def adjacent_pairs(template: str) -> list[str]:
    return [a + b for a, b in zip(template, template[1:])]


def apply_rules(template: str, rules: Rules, steps: int) -> int:
    current_pairs = Counter(adjacent_pairs(template))
    element_totals = Counter(template)

    for _ in range(steps):
        next_pairs = Counter()

        for pair, pair_count in current_pairs.items():
            insertion = rules[pair]
            first, second = pair

            next_pairs[first + insertion] += pair_count
            next_pairs[insertion + second] += pair_count

            element_totals[insertion] += pair_count

        current_pairs = next_pairs

    totals = element_totals.values()
    most_common = max(totals)
    least_common = min(totals)

    return most_common - least_common


def part1(template: str, rules: Rules) -> int:
    return apply_rules(template, rules, PART1_STEPS)


def part2(template: str, rules: Rules) -> int:
    return apply_rules(template, rules, PART2_STEPS)


if __name__ == "__main__":
    filename = get_input_filename(sys.argv)

    with open(filename, "r", encoding="utf-8") as f:
        parsed_data = parse_input(f.read())

        for solve in [part1, part2]:
            print(solve(*parsed_data))
