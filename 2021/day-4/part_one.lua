-- Check if a file exists
local function file_exists(file)
    local f = io.open(file, "rb")
    if f then f:close() end
    return f ~= nil
end
  
local function lines_from(file)
    if not file_exists(file) then return {} end
    lines = {}
    for line in io.lines(file) do 
        lines[#lines + 1] = line
    end
    return lines
end

local function split(s, delimiter)
    result = {}
    for match in (s..delimiter):gmatch("(.-)"..delimiter) do
        table.insert(result, match)
    end
    return result
end

local function get_input()
    local instructions = lines_from('input.txt')
    local draw = {}
    
    local boards = {}

    local current_board = {}
    for i, line in ipairs(instructions) do
        if i == 1 then
            for match in line:gmatch("[^,]+") do
                draw[#draw + 1] = match
            end
        else
            if line == "" then
                if #current_board ~= 0 then
                    boards[#boards + 1] = current_board
                end
                current_board = {}
            else
                local new_numbers = {}
                -- Remove spaces and trim
                line = line:gsub(" +"," "):gsub("^%s*(.-)%s*$", "%1")
                -- Split by spaces
                line = split(line, ' ')
                for _, number in ipairs(line) do
                    new_numbers[#new_numbers + 1] = {number, false}
                end

                current_board[#current_board + 1] = new_numbers
            end
        end
    end
    boards[#boards + 1] = current_board
    return draw, boards
end

local function count_line(board)
    local value = 0
    
    for _, line in ipairs(board) do
        for _, number in ipairs(line) do
            if not number[2] then
                value = value + tonumber(number[1])
            end
        end     
    end

    return value
end

local function draw(boards, draws)
    for i, value in ipairs(draws) do
        for _, board in ipairs(boards) do
            for _, line in ipairs(board) do
                for _, number in ipairs(line) do
                    if number[1] == value then
                        number[2] = true
                    end
                end
            end
        end

        for _, board in ipairs(boards) do
            for _, line in ipairs(board) do
                local count = 0

                for _, number in ipairs(line) do
                    if number[2] then
                        count = count + 1
                    end
                end

                if count == 5 then 
                    return value * tonumber(count_line(board))
                end
            end

            for i = 1, #board do
                local count = 0

                for _, lines in ipairs(board) do
                    if lines[i][2] == true then
                        count = count + 1
                    end
                end

                if count == 5 then 
                    return value * tonumber(count_line(board))
                end
            end
        end
    end
end

draws, boards = get_input()
print('Solution Part 1: ' .. draw(boards, draws))