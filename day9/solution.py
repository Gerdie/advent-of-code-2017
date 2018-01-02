# PART ONE

total_score = 0

def clean_up_garbage(input_str):
    inside_garbage = False
    
    for i, char in enumerate(input_str):
        if not inside_garbage and char == '<':
            inside_garbage = True


with open('input.txt') as input_file:
    input_str = input_file.read()
