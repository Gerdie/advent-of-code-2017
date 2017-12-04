# PART ONE
total_valid = 0

with open('input.txt') as input_file:
	for line in input_file:
		line_list = line.split()
		if len(line_list) == len(set(line_list)):
			total_valid += 1

print('Part One: {}'.format(total_valid))

# PART TWO
total_valid = 0

with open('input.txt') as input_file:
	for line in input_file:
		line_list = map(sorted, line.split())
		line_list = [''.join(x) for x in line_list]
		if len(line_list) == len(set(line_list)):
			total_valid += 1

print('Part Two: {}'.format(total_valid))
