elf_array = []

with open('day_1_input.txt') as file:
    elf_total = 0
    for line in file:
        if line.strip() == "":
            elf_array.append(elf_total)
            elf_total = 0
        else:
            elf_total += int(line)

elf_array.sort(reverse=True)
print(elf_array)

print(f'Most calories: {elf_array[0]}')

##############################
# PART 1
# 01/12/2022
# ANSWER: 69836
# TOTAL TIME: ~10m

#########################
