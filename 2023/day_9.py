def parse_matrix(line):
    values = [int(x) for x in line.split(' ')]
    matrix = [values, ]

    while not all(x == 0 for x in values):
        values = [second - first for first, second in zip(values, values[1:])]
        matrix.append(values)

    return matrix

def retrieve_history(line):
    matrix = parse_matrix(line)

    to_pass = 0
    for idx in range(len(matrix)-1, -1, -1):
        matrix[idx].append(matrix[idx][-1] + to_pass)
        to_pass = matrix[idx][-1]

    return to_pass

def retrieve_history_backwards(line):
    matrix = parse_matrix(line)

    to_pass = 0
    for idx in range(len(matrix)-1, -1, -1):
        matrix[idx].insert(0, matrix[idx][0] - to_pass)
        to_pass = matrix[idx][0]

    return to_pass

if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()

        history_values = [retrieve_history(line) for line in lines]
        history_values_backwards = [retrieve_history_backwards(line) for line in lines]
        print(f"Part 1: {sum(history_values)}")
        print(f"Part 2: {sum(history_values_backwards)}")