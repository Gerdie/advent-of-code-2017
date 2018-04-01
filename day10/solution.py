testing = False

if testing:
    circ_list = range(5)
    in_file = 'test.txt'
else:
    circ_list = range(256)
    in_file = 'input.txt'

circ_len = len(circ_list)


def get_valid_index(num):
    return num % circ_len


def reverse_subset(array, start, end):
    start_i, end_i = get_valid_index(start), get_valid_index(end)
    if start_i < end_i:
        return array[:start_i] + array[start_i:end_i][::-1] + array[end_i:]
    else:
        last_len = len(array[start_i:])
        selected_bit = array[start_i:] + array[:end_i]
        reversed_bit = selected_bit[::-1]
        return reversed_bit[last_len:] + array[end_i:start_i] + reversed_bit[:last_len]

with open(in_file) as input_file:
    input_list = input_file.read().split(',')
    input_list = map(int, input_list)

    current_position = 0
    skip_length = 0

    for num in input_list:
        if num > 0:
            circ_list = reverse_subset(circ_list, current_position, current_position + num)
        current_position += num + skip_length
        skip_length += 1

print(circ_list)
print('Part One: {}'.format(circ_list[0] * circ_list[1]))
