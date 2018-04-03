
opposites_map = {
    'n': 's',
    'ne': 'sw',
    'nw': 'se'
}

steps_map = {}

with open('input.txt') as in_file:
    directions = in_file.read().split(',')
    for direction in directions:
        steps_map[direction] = steps_map.get(direction, 0) + 1

# eliminate opposites
for opposite in opposites_map:
    north_dir = steps_map.get(opposite, 0)
    south_dir = steps_map.get(opposites_map[opposite], 0)
    if north_dir == south_dir:
        steps_map[opposite] = 0
        steps_map[opposites_map[opposite]] = 0
    elif north_dir > south_dir:
        steps_map[opposite] = north_dir - south_dir
        steps_map[opposites_map[opposite]] = 0
    elif south_dir > north_dir:
        steps_map[opposites_map[opposite]] = south_dir - north_dir
        steps_map[opposite] = 0

print(steps_map)

# 2 steps 'ne' + 'nw' can be condensed as 1 step 'n'
if steps_map.get('ne', 0) > 0 and steps_map.get('nw', 0) > 0:
    if steps_map['ne'] > steps_map['nw']:
        steps_map['n'] = steps_map['n'] + steps_map['nw']
        steps_map['ne'] = steps_map['ne'] - steps_map['nw']
        steps_map['nw'] = 0
    elif steps_map['nw'] > steps_map['ne']:
        steps_map['n'] = steps_map['n'] + steps_map['ne']
        steps_map['nw'] = steps_map['nw'] - steps_map['ne']
        steps_map['ne'] = 0
if steps_map.get('se', 0) > 0 and steps_map.get('sw', 0) > 0:
    if steps_map['se'] > steps_map['sw']:
        steps_map['s'] = steps_map['s'] + steps_map['sw']
        steps_map['se'] = steps_map['se'] - steps_map['sw']
        steps_map['sw'] = 0
    elif steps_map['sw'] > steps_map['se']:
        steps_map['s'] = steps_map['s'] + steps_map['se']
        steps_map['sw'] = steps_map['sw'] - steps_map['se']
        steps_map['se'] = 0

print('Part One: {}'.format(sum(steps_map.values())))
