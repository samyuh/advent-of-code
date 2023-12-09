from functools import reduce

def solver(time, minimum_distance):
    pass

def solver_brute_force(time, minimum_distance):
    result = 0
    for pressing_time in range(time):
        travel_time = time - pressing_time
        total_distance = pressing_time * travel_time
        
        result += 1 if total_distance > minimum_distance else 0
    return result

with open("input_6.txt") as file:
    time_list = list(map(int, file.readline().split()[1:]))
    distance_list = list(map(int, file.readline().split()[1: ]))
    
    time_concat = int(''.join(map(str, time_list)))
    distance_concat = int(''.join(map(str, distance_list)))

    number_ways = []
    for time, minimum_distance in zip(time_list, distance_list):
        result = solver_brute_force(time, minimum_distance)
        number_ways.append(result)
    
    result_part_1 = reduce(lambda x, y: x * y, number_ways)
    result_part_2 = solver_brute_force(time_concat, distance_concat)

    print(f"Part 1: {result_part_1}")
    print(f"Part 2: {result_part_2}")
