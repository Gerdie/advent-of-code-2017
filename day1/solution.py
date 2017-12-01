# PART ONE
total = 0
with open('input.txt') as input_file:
	input_string = input_file.read()
	for i, char in enumerate(input_string):
		if char == input_string[i - 1]:
			total += int(char)
print("Part 1: {}".format(total))

# PART TWO
total = 0
with open('input.txt') as input_file:
	input_string = input_file.read()
	half_length = len(input_string) / 2
	for i, char in enumerate(input_string):
		if char == input_string[i - half_length]:
			total += int(char)
print("Part 2: {}".format(total))