
def add_layer(layer_index, layer_range, ALL_LAYERS):
    layer = [1] + [0] * (layer_range - 1)
    if len(ALL_LAYERS) <= layer_index:
        extension = layer_index - len(ALL_LAYERS) + 1
        for x in xrange(extension):
            ALL_LAYERS.extend([[0]])
    ALL_LAYERS[layer_index] = layer


def get_damage(player_position, ALL_LAYERS):
    damage = 0
    caught = False
    # get damage
    if ALL_LAYERS[player_position][0]:
        caught = True
        damage = player_position * len(ALL_LAYERS[player_position])
    return damage, caught


def move_cameras(ALL_LAYERS, velocities):
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


def reset_layers():
    ALL_LAYERS = []
    velocities = []
    with open('input.txt') as in_file:
        for line in in_file:
            line = line.strip()
            line = map(int, line.split(': '))
            layer, layer_range = line
            add_layer(layer, layer_range, ALL_LAYERS)

    velocities = [1] * len(ALL_LAYERS)

    return ALL_LAYERS, velocities


def play_game(delay=False, exit_if_damage=False):
    ALL_LAYERS, velocities = reset_layers()
    player_position = 0
    damage = 0

    while player_position < len(ALL_LAYERS):
        damage += get_damage(player_position, ALL_LAYERS)[0]
        move_cameras(ALL_LAYERS, velocities)
        player_position += 1

    return damage


def play_multiplayer():
    ALL_LAYERS, velocities = reset_layers()
    player_positions = [0]
    player_delays = [0]
    delay = 0
    indices_to_remove = []

    while player_positions[0] < len(ALL_LAYERS):
        for i, player_position in enumerate(player_positions):
            _, caught = get_damage(player_position, ALL_LAYERS)
            if caught:
                indices_to_remove.append(i)
        move_cameras(ALL_LAYERS, velocities)
        # increment positions
        player_positions = map(lambda x: x+1, player_positions)
        delay += 1
        player_positions.append(0)
        player_delays.append(delay)

        if indices_to_remove:
            player_positions = [x for x in player_positions if player_positions.index(x) not in indices_to_remove]
            player_delays = [x for x in player_delays if player_delays.index(x) not in indices_to_remove]
            indices_to_remove = []

    return player_delays[0]


print('Part One: {}'.format(play_game()))
print('Part Two: {}'.format(play_multiplayer()))
