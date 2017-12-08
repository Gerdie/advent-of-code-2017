from collections import namedtuple
import re

PROGRAM_PATTERN = '(?P<name>\w+)\s\((?P<weight>\d+)\)((\s->\s)(?P<above>[\w\s,]+))?'
Stack = namedtuple('Stack', ['bottom_program', 'weight'])

class Program_Set(object):
	def __init__(self):
		self.programs = {}

	def get_program(self, program_name):
		return self.programs.get(program_name, None)

	def add_program(self, program):
		existing_program = self.programs.get(program.name, None)
		if existing_program:
			existing_program.update_with(program)
		else:
			self.programs[program.name] = program

	def bottom_program(self):
		return [x for x in self.programs if not self.programs[x].below]

	def get_stack_weight(self, program_name):
		program = self.get_program(program_name)
		if not program.above:
			return program.weight
		return program.weight + sum([self.get_stack_weight(substack_name) for substack_name in program.above])

	def get_unbalanced_program(self, bottom_program=None):
		stack_weights = []
		weights = []
		for stack in bottom_program.above:
			weight = self.get_stack_weight(stack)
			new_stack = Stack('bottom_program'=stack, 'weight'=weight)
			stack_weights.append(new_stack)
			weights.append(weight)
		if max(weights) == min(weights):
			return True
		else:
			uneven_weights = [w for w in weights if weights.count(w) == 1]
			uneven_stacks = [st.name for st in stack_weights if st.weight in uneven_weights]
			if len(uneven_stacks) > 1:
				for st in uneven_stacks:
					if not self.get_unbalanced_program(bottom_program=st.bottom_program):
						for ab_st in st.bottom_program.above:
							if not get_unbalanced_program(ab_st.bottom_program):
								return get_unbalanced_program(ab_st.bottom_program)
						return st.bottom_program

	def is_balanced_stack(self, bottom_program=None):
		if not bottom_program:
			bottom_program = self.bottom_program
		uneven = True
		# 1. find node containing uneven stack
		while uneven:
			stack_weights = []
			weights = []
			for stack in bottom_program.above:
				weight = self.get_stack_weight(stack)
				new_stack = Stack('bottom_program'=stack, 'weight'=weight)
				stack_weights.append(new_stack)
				weights.append(weight)
			if max(weights) == min(weights):
				uneven = False
			else:
				uneven_weights = [w for w in weights if weights.count(w) == 1]
				uneven_stacks = [st.name for st in stack_weights if st.weight in uneven_weights]
				if len(uneven_stacks) > 1:
					for st in uneven_stacks:

						if not self.is_balanced_stack(bottom_program=st.bottom_program):

				else:
					bottom_program = uneven_stacks[0].bottom_program

		# 2. repeat


class Program(object):
	def __init__(self, name, weight, programs_above, programs_below):
		self.name = name
		self.weight = weight
		self.above = programs_above
		self.below = programs_below

	def update_with(self, program_two):
		if program_two.name:
			self.name = program_two.name
		if program_two.weight:
			self.weight = program_two.weight
		if program_two.above:
			self.above = program_two.above
		if program_two.below:
			self.below = program_two.below


all_programs = Program_Set()

with open('test.txt') as input_file:
	for line in input_file:
		match = re.match(PROGRAM_PATTERN, line)
		name, weight, programs_above = match.group('name'), match.group('weight'), match.group('above')
		if programs_above:
			programs_above = programs_above.strip().split(', ')
			for each_program in programs_above:
				above = Program(each_program, 0, None, name)
				all_programs.add_program(above)
		new_program = Program(name, int(weight), programs_above, None)
		all_programs.add_program(new_program)

print('Part One: {}'.format(all_programs.bottom_program()))
print('Part Two: {}'.format(all_programs.get_stack_weight('ugml')))
