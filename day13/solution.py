ALL_LAYERS = []
velocities = []


def add_layer(layer_index, layer_range):
    layer = [1] + [0] * (layer_range - 1)
    if len(ALL_LAYERS) <= layer_index:
        extension = layer_index - len(ALL_LAYERS) + 1
        for x in xrange(extension):
            ALL_LAYERS.extend([[0]])
    ALL_LAYERS[layer_index] = layer


def move_cameras(player_position):
    damage = 0
    # get damage
    if ALL_LAYERS[player_position][0]:
        damage = player_position * len(ALL_LAYERS[player_position])
    # move cameras
    for layer_index, layer in enumerate(ALL_LAYERS):
        if len(layer) > 1:
            for i, indicator in enumerate(layer):
                # if going forward...
                if indicator == 1 and velocities[layer_index]:
                    layer[i] = 0
                    try:
                        layer[i + 1] = 1
                    # go backward
                    except IndexError:
                        layer[i - 1] = 1
                        velocities[layer_index] = 0
                    break
                # if going backward...
                elif indicator == 1 and not velocities[layer_index]:
                    layer[i] = 0
                    if i == 0:
                        layer[i + 1] = 1
                        velocities[layer_index] = 1
                    else:
                        layer[i - 1] = 1
                    break
    return damage

with open('input.txt') as in_file:
    for line in in_file:
        line = line.strip()
        line = map(int, line.split(': '))
        layer, layer_range = line
        add_layer(layer, layer_range)

velocities = [1] * len(ALL_LAYERS)
player_position = 0
damage = 0

while player_position < len(ALL_LAYERS):
    damage += move_cameras(player_position)
    print(ALL_LAYERS)
    player_position += 1

print('Part One: {}'.format(damage))
