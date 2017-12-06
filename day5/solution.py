# PART ONE

number_steps = 0

def step_with_offset(i):
	step = step_list[i]
	next_i = i + step
	step_list[i] = step + 1
	return next_i

with open('input.txt') as input_file:
	step_list = map(int, input_file.read().split())
	i = 0
	while i < len(step_list):
		i = step_with_offset(i)
		number_steps += 1

print('Part One: {}'.format(number_steps))

# PART TWO	

number_steps = 0

def step_with_offset(i):
	step = step_list[i]
	next_i = i + step
	if step >= 3:
		step_list[i] = step - 1
	else:
		step_list[i] = step + 1
	return next_i

with open('input.txt') as input_file:
	step_list = map(int, input_file.read().split())
	i = 0
	while i < len(step_list):
		i = step_with_offset(i)
		number_steps += 1

print('Part Two: {}'.format(number_steps))
