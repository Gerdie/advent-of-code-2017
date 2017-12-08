# PART ONE
import re

INSTRUCTION_PATTERN = '(?P<register>\w+)\s(?P<operation>(inc)|(dec))\s(?P<amt>-?\d+)\sif\s(?P<register2>\w+)\s(?P<cond>[<>=!]+)\s(?P<cond_amt>-?\d+)'

max_val = 0
register_values = {}

def modify_register_and_return_val(register, operation, amt):
	if operation == 'inc':
		new_val = register_values.get(register, 0) + amt
	elif operation == 'dec':
		new_val = register_values.get(register, 0) - amt
	register_values[register] = new_val
	return new_val

with open('input.txt') as input_file:
	for line in input_file:
		line = line.strip()
		matches = re.match(INSTRUCTION_PATTERN, line)
		register, op, amt = matches.group('register'), matches.group('operation'), int(matches.group('amt'))
		register2, cond, cond_amt = matches.group('register2'), matches.group('cond'), int(matches.group('cond_amt'))
		register2_val = register_values.get(register2, 0)
		if cond in ['>', '>='] and register2_val > cond_amt:
			new_val = modify_register_and_return_val(register, op, amt)
			if new_val > max_val:
				max_val = new_val
		elif cond in ['<', '<='] and register2_val < cond_amt:
			new_val = modify_register_and_return_val(register, op, amt)
			if new_val > max_val:
				max_val = new_val
		elif cond in ['==', '<=', '>='] and register2_val == cond_amt:
			new_val = modify_register_and_return_val(register, op, amt)
			if new_val > max_val:
				max_val = new_val
		elif cond == '!=' and register2_val != cond_amt:
			new_val = modify_register_and_return_val(register, op, amt)
			if new_val > max_val:
				max_val = new_val

print('Part One: {}'.format(max(register_values.values())))
print('Part Two: {}'.format(max_val))
