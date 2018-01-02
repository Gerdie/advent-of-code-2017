
with open('input.txt') as input_file:
    input_str = input_file.read()

    inside_garbage = False
    ignore_char = False
    current_score = 0
    total_score = 0
    garbage_count = 0

    for i, char in enumerate(input_str):
        if ignore_char:
            ignore_char = False
        elif char == '!':
            ignore_char = True
        elif char == '<' and not inside_garbage:
            inside_garbage = True
        elif char == '>':
            inside_garbage = False
        elif char == '{' and not inside_garbage:
            current_score += 1
            total_score += current_score
        elif char == '}' and not inside_garbage:
            current_score -= 1
        elif inside_garbage:
            garbage_count += 1

    print('Part One: {}'.format(total_score))
    print('Part Two: {}'.format(garbage_count))
