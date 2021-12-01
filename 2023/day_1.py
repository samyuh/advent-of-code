import re

word_to_number = {
        'one': 'on1ne',
        'two': 'tw2wo',
        'three': 'thr3ree',
        'four': 'fou4our',
        'five': 'fiv5ive',
        'six': 'si6ix',
        'seven': 'sev7ven',
        'eight': 'eig8ght',
        'nine': 'nin9ine'
    }

def sanitize_string(text):
    for word, number in word_to_number.items():
        text = text.replace(word, number)
    
    return text

def calculate_sum_of_numbers(text):
    numbers = re.findall(r'\d+', text)
    return int(numbers[0][0] + numbers[-1][-1])

def part_1(text):
    return calculate_sum_of_numbers(text)

def part_2(text):
    return calculate_sum_of_numbers(sanitize_string(text))

with open('./input.txt', 'r') as file:
    lines = file.readlines()
    values = [part_2(line) for line in lines]
    
    print(f"Result: {sum(values)}")
