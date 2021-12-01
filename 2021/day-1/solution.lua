-- Check if a file exists
function file_exists(file)
    local f = io.open(file, "rb")
    if f then f:close() end
    return f ~= nil
end
  
-- Read lines from file
function lines_from(file)
    if not file_exists(file) then return {} end
    lines = {}
    for line in io.lines(file) do 
        lines[#lines + 1] = line
    end
    return lines
end

-- Count if current value is higher than previous
function count_bigger(table)
    local solution = 0
    local prev_value = -1

    for k, puzzle_value in pairs(table) do
        if k ~= 1 then
            if tonumber(puzzle_value) > tonumber(prev_value) then
                solution = solution + 1
            end
        end
        prev_value = puzzle_value
    end
    return solution
end

local file = 'input.txt'
local lines = lines_from(file)

-- Part 1
local solution_part1 = count_bigger(lines)
print(string.format("Part 1: %d", solution_part1))

-- Part 2
function setContains(set, key)
    return set[key] ~= nil
end

local window_values = {}
for k, puzzle_value in pairs(lines) do
    if setContains(lines, k+2) then
        window_values[#window_values + 1] = lines[k] + lines[k+1] + lines[k+2]
    end
end

local solution_part2 = count_bigger(window_values)
print(string.format("Part 2: %d", solution_part2))