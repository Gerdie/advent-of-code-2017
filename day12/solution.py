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

    def get_related_programs(self, program_num, related_programs=None):
        related_programs = related_programs or set([])

        program = self.programs[program_num]
        for child in program.children:
            if child in related_programs:
                continue
            related_programs.add(child)
            self.get_related_programs(child, related_programs=related_programs)

        return related_programs

    def find_all_groups(self):
        programs = set([])
        groups = 0

        for program_num in self.programs:
            # don't process programs in groups we've already counted
            if program_num in programs:
                continue
            group_set = self.get_related_programs(program_num)
            programs = programs | group_set
            groups += 1

        return groups


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

print('Part One: {}'.format(len(all_programs.get_related_programs(0))))
print('Part Two: {}'.format(all_programs.find_all_groups()))
