import re
import math

class Leaf:
    def __init__(self, l, r):
        self.left = l
        self.right = r

    def __repr__(self) -> str:
        return f"({self.left}, {self.right})"

def part_1(instructions, tree):
    current_match = "AAA"
    total_iteration = 0
    iteration = 0
    while current_match != "ZZZ":
        if instructions[iteration] == "R":
            current_match = tree[current_match].right
        if instructions[iteration] == "L":
            current_match = tree[current_match].left

        total_iteration += 1
        iteration = (iteration + 1) % len(instructions)
        
    print(f"Part 1: {total_iteration}")

def part_2(instructions, tree):
    current_match_list = [key for key in tree.keys() if key.endswith('A')]

    total_iteration = 0
    iteration = 0
    while not all(isinstance(element, int) for element in current_match_list):
        for idx in range(len(current_match_list)):
            element = current_match_list[idx]
            if isinstance(element, int): continue
            if element.endswith('Z'):
                current_match_list[idx] = int(total_iteration)
                continue

            if instructions[iteration] == "R":
                element = tree[element].right
            if instructions[iteration] == "L":
                element = tree[element].left

            current_match_list[idx] = element

        total_iteration += 1
        iteration = (iteration + 1) % len(instructions)

    result = math.lcm(*current_match_list)
    print(f"Part 2: {result}")

with open("input.txt") as data:
    lines = data.readlines()
    
    instructions = lines[0][0:-1]
    tree_lines = lines[2:]

    tree = {}
    pattern = re.compile(r'(\w+)\s*=\s*\((\w+),\s*(\w+)\)')
    for entry in tree_lines:
        match = pattern.match(entry)
        tree[match.group(1)] = Leaf(match.group(2), match.group(3))
    
    # Algorithm
    part_1(instructions, tree)
    part_2(instructions, tree)