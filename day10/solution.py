with open('input.txt') as input_file:
    input_list = input_file.read().split(',')
    input_list = map(int, input_list)
    print(input_list)
