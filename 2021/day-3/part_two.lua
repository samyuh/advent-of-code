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

-- Part 2
local function biggest_count(instructions, gt)
    local i = 0
    while #instructions ~= 1 do
        i = i + 1
        
        local ones = {}
        local zeros = {}
        for _, binary in ipairs(instructions) do
            local bit = binary:sub(i,i)
            if bit == '1' then
                ones[#ones + 1] = binary
            else
                zeros[#zeros + 1] = binary
            end
        end
        if gt then
            instructions = #ones >= #zeros and ones or zeros
        else
            instructions = #ones >= #zeros and zeros or ones
        end 
    end
    return instructions[1]
end

local instructions = lines_from('input.txt')
local c02 = biggest_count(instructions, false)
local oxygen = biggest_count(instructions, true)

local part_2_solution = tonumber(oxygen, 2) * tonumber(c02, 2)
print("Solution: " .. part_2_solution)