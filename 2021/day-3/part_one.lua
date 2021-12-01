-- Check if a file exists
function file_exists(file)
    local f = io.open(file, "rb")
    if f then f:close() end
    return f ~= nil
end
  
function lines_from(file)
    if not file_exists(file) then return {} end
    lines = {}
    for line in io.lines(file) do 
        lines[#lines + 1] = line
    end
    return lines
end

-- Part 1
local instructions = lines_from('input.txt')

local count = {}
local gamma = ""
local epsilon = ""

for _, binary in ipairs(instructions) do
    for i = 1, #binary do
        local bit = binary:sub(i,i)
        if bit == '1' then
            count[i] = #count >= i and count[i] + 1 or 0
        end
    end
end

for i = 1, #count do
    if count[i] >= 500 then
        gamma = gamma .. "1"
        epsilon = epsilon .. "0"
    else
        gamma = gamma .. "0"
        epsilon = epsilon .. "1"
    end
end

local part_1_solution = tonumber(gamma, 2) * tonumber(epsilon, 2)
print("Solution: " .. part_1_solution)