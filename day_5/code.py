# hard code number of columns and create list for each column
# for each line, use regex to get character
# add character to collumn based on location int
# for number of moves, pop from list and append to other list

import re

# INITIALISE EVERYTHING
stack1 = []
stack2 = []
stack3 = []
stack4 = []
stack5 = []
stack6 = []
stack7 = []
stack8 = []
stack9 = []

stack_dict = {1:stack1, 
              2:stack2,
              3:stack3,
              4:stack4,
              5:stack5,
              6:stack6,
              7:stack7,
              8:stack8,
              9:stack9
              }

letter_pattern = '[A-Z]'
number_pattern = '\d+'

def get_stack(_span):
    if (_span == 1):
        return stack1
    elif (_span == 5):
        return stack2
    elif (_span == 9):
        return stack3
    elif (_span == 13):
        return stack4
    elif (_span == 17):
        return stack5
    elif (_span == 21):
        return stack6
    elif (_span == 25):
        return stack7
    elif (_span == 29):
        return stack8
    elif (_span == 33):
        return stack9



# SET UP THE STACK/CRATES STRUCTURE

with open('image.txt') as file:
    for line in file:
        for match in re.finditer(letter_pattern, line):
            # print(f'Stack: {match.start()}')
            # print(match.group())
            stack = get_stack(match.start())
            stack.insert(0, match.group())

# print(stack1)
# print(stack2)
# print(stack3)
# print(stack4)
# print(stack5)
# print(stack6)
# print(stack7)
# print(stack8)
# print(stack9)


with open('instructions.txt') as file:
    for line in file:
        inst = re.findall(number_pattern, line)
        # print(inst)
        for i in range(int(inst[0])):
            crate = stack_dict.get(int(inst[1])).pop()
            stack_dict.get(int(inst[2])).append(crate)



final_list = ''
for i in [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]:
    final_list += i.pop()

print(final_list)

############
# PART 1
# 09/12/2022
# ANSWER: ZSQVCCJLL
# TOTAL TIME: 1HR 43M


