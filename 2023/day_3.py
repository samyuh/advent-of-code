def convert_matrix(lines):
    matrix = []
    for line in lines:
        matrix_line = [char for char in line if char != '\n']
        matrix.append(matrix_line)
    return matrix

def adjacency_matrix(matrix, row_i, column_i, column_e, row_len, column_len):
    for column_c in range(max(column_i - 1, 0), min(column_e + 2, column_len)):
        for row_c in range(max(row_i - 1, 0), min(row_i + 2, row_len)):
            element = matrix[row_c][column_c]
            if element != '.' and not element.isnumeric(): 
                return int(''.join(matrix[row_i][column_i:column_e+1]))
    return 0

def adjacency_matrix_gear(matrix, row_i, column_i, column_e, row_len, column_len):
    for column_c in range(max(column_i - 1, 0), min(column_e + 2, column_len)):
        for row_c in range(max(row_i - 1, 0), min(row_i + 2, row_len)):
            element = matrix[row_c][column_c]
            if element != '.' and not element.isnumeric(): 
                number = int(''.join(matrix[row_i][column_i:column_e+1]))
                if element == '*':
                    matrix[row_c][column_c] = 'G_1 ' + str(number)
                elif element.startswith('G_1'):
                    matrix[row_c][column_c] = 'G_2 ' + matrix[row_c][column_c] + ' ' + str(number) 
                elif element.startswith('G_2'):
                    matrix[row_c][column_c] = 'G_3'

def find_numeric_sequence(line, start_index):
    end_index = start_index
    while end_index < len(line) and line[end_index].isnumeric():
        end_index += 1
    return end_index - 1

def part_1(file_to_open):
    with open(file_to_open) as file:
        lines = file.readlines()
        matrix = convert_matrix(lines)

        row_len = len(matrix)
        column_len = len(matrix[0])

        sum = 0
        for row_i, line in enumerate(matrix):
            column_i = 0
            while column_i < column_len:
                if line[column_i].isnumeric():
                    column_e = find_numeric_sequence(line, column_i)
                    sum += adjacency_matrix(matrix, row_i, column_i, column_e, row_len, column_len)
                    column_i = column_e
                column_i += 1
        print(sum)

def part_2(file_to_open):
    with open(file_to_open) as file:
        lines = file.readlines()
        matrix = convert_matrix(lines)

        row_len = len(matrix)
        column_len = len(matrix[0])

        for row_i, line in enumerate(matrix):
            column_i = 0
            while column_i < column_len:
                if line[column_i].isnumeric():
                    column_e = find_numeric_sequence(line, column_i)
                    adjacency_matrix_gear(matrix, row_i, column_i, column_e, row_len, column_len)
                    column_i = column_e
                column_i += 1

        sum = 0
        for line in matrix:
            for char in line:
                if char.startswith('G_2'):
                    number_1, number_2 = int(char.split(' ')[2]), int(char.split(' ')[3])
                    sum += number_1 * number_2
        print(sum)

if __name__ == "__main__":
    part_1("input.txt")
    part_2("input.txt")
