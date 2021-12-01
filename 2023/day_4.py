import re

with open('./input.txt', 'r') as file:
    lines = file.readlines()

    pattern = re.compile(r'Card\s+(\d+):\s+([\d\s]+)\s*\|\s*([\d\s]+)')
    pile_points = 0
    cards_instances = [1] * len(lines)
    for entry in lines:
        match = pattern.search(entry)
        
        card_num = int(match.group(1))
        group1_numbers = list(map(int, match.group(2).split()))
        group2_numbers = list(map(int, match.group(3).split()))

        common_elements_count = len(set(group1_numbers) & set(group2_numbers))
        pile_points += 2 ** (common_elements_count - 1) if common_elements_count >= 1 else 0

        for idx in range(common_elements_count):
            cards_instances[card_num + idx] += cards_instances[card_num - 1] 
    
    print(f"Part 1: {pile_points}")
    print(f"Part 2: {sum(cards_instances)}")


