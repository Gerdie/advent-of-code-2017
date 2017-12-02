# PART ONE
total = 0
with open('input.txt') as input_file:
    for row in input_file:
        row = [int(num) for num in row.split()]
        total += max(row) - min(row)
print('Part One: {}'.format(total))

# PART TWO
total = 0
with open('input.txt') as input_file:
    for row in input_file:
        row = [int(num) for num in row.split()]
        for i, num in enumerate(row):
            for next_num in row[i + 1:]:
                if num % next_num == 0:
                    total += num / next_num
                if next_num % num == 0:
                    total += next_num / num
print('Part Two: {}'.format(total))
