# read file line by line
# find length of list and divide by 2
# list 1 = first half
# list 2 = second half
# compare lists and find common value
# get priority of common value (ASCII?)


priority = 0

with open('day_3_input.txt') as file:
    for line in file:
        half_items = int((len(line)-1)/2)
        #print(f'{line[:-1]} length: {len(line)-1}')
        comp1 = line[:half_items] 
        comp2 = line[half_items:half_items*2]
        for i in comp1:
            if i in comp2:
                #print(f'match found: {i} ASCII value: {ord(i)}')
                if i.islower():
                    #print(f'amended value: {ord(i)-96}')
                    priority += ord(i)-96
                else:
                    #print(f'amended value: {ord(i)-38}')
                    priority += ord(i)-38
                break

print(f'Total: {priority}')

##############################
# PART 1
# 06/12/2022
# ANSWER: 7597
# TOTAL TIME: 39M 04S