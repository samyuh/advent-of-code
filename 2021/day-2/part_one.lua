local horizontal = 0
local depth = 0

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


local instructions = lines_from('input.txt')
for _, v in ipairs(instructions) do
    words = {}
    for word in v:gmatch("%w+") do table.insert(words, word) end

    if string.find(words[1], "forward") then
        horizontal = horizontal + tonumber(words[2])
    elseif string.find(words[1], "down") then
        depth = depth + tonumber(words[2])
    else
        depth = depth - tonumber(words[2])
    end
end

local part_1 = depth * horizontal
print('Part 1 Solution: ' .. part_1)