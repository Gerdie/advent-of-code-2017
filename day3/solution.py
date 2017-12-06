# PART ONE
starting_val = 361527


def get_grid_size(num):
    nearest_square = int(num ** 0.5)
    return nearest_square + 1 if nearest_square % 2 == 0 else nearest_square + 2


def find_route_to_center(num):
    grid_size = get_grid_size(num)
    distance = grid_size - 1
    highest = grid_size ** 2
    # corners
    number_list = [highest, highest - distance, highest - distance * 2, highest - distance * 3]
    higher = [x + 1 for x in number_list]
    lower = [x - 1 for x in number_list]
    if num in number_list:
        return distance
    for i in range(grid_size / 2):
        distance -= 1
        if num in higher or num in lower:
            return distance
        else:
            higher = [x + 1 for x in higher]
            lower = [x - 1 for x in lower]

print('Part One: {}'.format(find_route_to_center(starting_val)))

# PART TWO

# grid = [[n, n, n],
#         [n, n, n],
#         [n, n, n]]

grid = [[1]]

def calculate_cell_value(grid, x, y):
    total = 0
    try:
        total += grid[y + 1][x]
    except IndexError:
        pass
    try:
        total += grid[y][x + 1]
    except IndexError:
        pass
    try:
        total += grid[y + 1][x + 1]
    except IndexError:
        pass
    if y > 0:
        try:
            total += grid[y - 1][x]
        except IndexError:
            pass
        try:
            total += grid[y - 1][x + 1]
        except IndexError:
            pass
    if x > 0 and y > 0:
        try:
            total += grid[y - 1][x - 1]
        except IndexError:
            pass
    if x > 0:
        try:
            total += grid[y][x - 1]
        except IndexError:
            pass
        try:
            total += grid[y + 1][x - 1]
        except IndexError:
            pass
    return grid, total

def get_new_row(row_size):
    return [0] * row_size

def expand_grid(grid, highest):
    len_y = len(grid)
    # start at bottom and go up
    for val in range(len_y):
        grid, new_cell = calculate_cell_value(grid, len_y, len_y - 1 - val)
        if new_cell > highest:
            return new_cell
        grid[-1 - val].append(new_cell)
    # add to top
    top_row = get_new_row(len_y + 1)
    grid = [top_row] + grid
    # calculate top from right to left
    for val in range(len_y + 1):
        grid, new_cell = calculate_cell_value(grid, len_y - val, 0)
        if new_cell > highest:
            return grid, new_cell
        grid[0][len_y - val] = new_cell
    # go down left side and pre-pend zero vals
    for val in range(len_y + 1):
        grid[val] = [0] + grid[val]
    # calculate left side vals
    for val in range(len_y + 1):
        grid, new_cell = calculate_cell_value(grid, 0, val)
        if new_cell > highest:
            return new_cell
        grid[val][0] = new_cell
    # add to bottom
    bottom_row = get_new_row(len_y + 2)
    grid.append(bottom_row)
    # calculate bottom vals
    for val in range(len_y + 2):
        grid, new_cell = calculate_cell_value(grid, val, len_y + 1)
        if new_cell > highest:
            return new_cell
        grid[-1][val] = new_cell
    return grid, None


while True:
    grid, highest = expand_grid(grid, starting_val)
    if highest is not None:
        break

print('Part Two: {}'.format(highest))
