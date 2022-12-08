with open('day_4_input.txt') as file:
    assignment_pairs = 0
    for line in file:
        first_elf = []
        second_elf = []
        line = line.rstrip()

        # for i in range(line[0], line[2]+1):
        #     first_elf.append(i)
        # for i in range(line[4])
        separated_pairs = line.split(',')
        first = separated_pairs[0].split('-')
        second = separated_pairs[1].split('-')
        for i in range(int(first[0]), int(first[1])+1):
            first_elf.append(i)
        for i in range(int(second[0]), int(second[1])+1):
            second_elf.append(i)

        #print(first_elf)
        #print(second_elf)
        # if (set(first_elf).intersection(set(second_elf))):
        #     print('first is in second')
        # elif(set(second_elf).intersection(set(first_elf))):
        #     print('second is in first')
        # else:
        #     print('no overlap')
        first_in_second = True
        for i in first_elf:
            if i not in second_elf:
                first_in_second = False
                #print('first element not in second list')
                break
            # else:
            #     print('first in second')
        
        second_in_first = True
        for i in second_elf:
            if i not in first_elf:
                second_in_first = False
                #print('second element not in first list')
                break
            # else:
            #     print('second in first')

        if (first_in_second and second_in_first):
            assignment_pairs += 1
        elif (first_in_second or second_in_first):
            assignment_pairs += 1
            
    print(assignment_pairs)

#########
# PART 1
# 623 too high
# 07/12/2022
# ANSWER: 584
# TOTAL TIME: 1HR 5M

###############
