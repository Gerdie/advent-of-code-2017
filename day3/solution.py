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

# grid = [[x, x, x],
#         [x, x, x],
#         [x, x, x]]

grid = [[1]]

def expand_grid():
    len_y = len(grid)
    # start at bottom going right
    new_cell = calculate_cell_value(len_y - 1, len_y - 1)
    grid[-1].append(new_cell)
    for x in range(len_y):
        new_cell = calculate_cell_value(len_y - 1, len_y - 1)
        grid[-1].append(new_cell)



def calculate_cell_value(x, y):
    total = 0
    try:
        total += grid[x][y + 1]
    except IndexError:
        pass
    try:
        total += grid[x][y - 1]
    except IndexError:
        pass
    try:
        total += grid[x + 1][y - 1]
    except IndexError:
        pass
    try:
        total += grid[x + 1][y]
    except IndexError:
        pass
    try:
        total += grid[x + 1][y + 1]
    except IndexError:
        pass
    try:
        total += grid[x - 1][y - 1]
    except IndexError:
        pass
    try:
        total += grid[x - 1][y]
    except IndexError:
        pass
    try:
        total += grid[x - 1][y + 1]
    except IndexError:
        pass
    return total


def expand_grid(grid):
    current_size = len(grid[0])
    for row in grid:
        row = [0] + row + [0]
    grid = [[0] * current_size] + grid
    grid.append([0] * current_size)

grid = [[1]]


def part_two():
    highest = 0
    while True:
        expand_grid(grid)
        if highest > starting_val:
            return highest

