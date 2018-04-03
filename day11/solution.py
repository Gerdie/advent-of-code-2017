x = 0
y = 0
z = 0

distances = set([])

with open('input.txt') as in_file:
    directions = in_file.read().split(',')
    for d in directions:
        if d == 'n':
            y += 1
            z -= 1
        elif d == 's':
            y -= 1
            z += 1
        elif d == 'ne':
            x += 1
            z -= 1
        elif d == 'sw':
            x -= 1
            z += 1
        elif d == 'nw':
            y += 1
            x -= 1
        elif d == 'se':
            x += 1
            y -= 1
        distance = (abs(x) + abs(y) + abs(z)) / 2
        distances.add(distance)


print('Part One: {}'.format(distance))
print('Part Two: {}'.format(max(distances)))
