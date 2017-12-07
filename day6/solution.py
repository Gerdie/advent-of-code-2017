# PART ONE

past_configurations = set()
total_loops = 0

with open('input.txt') as input_file:
	memory_banks = map(int, input_file.read().split())
	# memory_banks = [0, 2,7,0]
	num_banks = len(memory_banks)
	past_configurations.add(','.join([str(x) for x in memory_banks]))

	while True:
		max_amt = max(memory_banks)
		max_bank_index = memory_banks.index(max_amt)
		memory_banks[max_bank_index] = 0

		for i in range(max_amt):
			next_index = (max_bank_index + 1 + i) % num_banks
			memory_banks[next_index] = memory_banks[next_index] + 1

		total_loops += 1
		bank_string = ','.join([str(x) for x in memory_banks])
		if bank_string in past_configurations:
			break
		else:
			past_configurations.add(bank_string)

print('Part One: {}'.format(total_loops))
