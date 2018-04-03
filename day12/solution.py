import re

pattern = '(?P<prog>\d+)\s<->\s(?P<progs>.+)'


class Program(object):

    def __init__(self, num):
        self.num = num

    def add_children(self, children_list):
        self.children = children_list or []


class ProgramLookup(object):

    def __init__(self):
        self.programs = {}

    def add_program(self, program):
        self.programs[program.num] = program

    def count_related_programs(self, program_num, related_programs=None):
        related_programs = related_programs or set([])

        program = self.programs[program_num]
        for child in program.children:
            if child in related_programs:
                continue
            related_programs.add(child)
            self.count_related_programs(child, related_programs=related_programs)

        return len(related_programs)


all_programs = ProgramLookup()

with open('input.txt') as in_file:
    for line in in_file:
        # parse data from line
        match_result = re.match(pattern, line)
        program_num = int(match_result.group('prog'))
        related_programs = match_result.group('progs').split(', ')
        related_programs = map(int, related_programs)
        # create new program
        new_program = Program(program_num)
        new_program.add_children(related_programs)
        all_programs.add_program(new_program)

print('Part One: {}'.format(all_programs.count_related_programs(0)))
