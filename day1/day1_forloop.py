# read file
day1 = open("day1.txt", "r")

calories = 0

elf_id = 1

elf_map = {}

# read line
lines = day1.readlines()

for line in lines:
  if line == "\n":
    elf_map[elf_id] = calories
    calories = 0
    elf_id += 1
  else:
    calories += int(line)
    # print(calories)

elf_map[elf_id] = calories

largest = max(elf_map.values())

day1.close()

sorted_values = sorted(elf_map.values())

print(sum(sorted_values[-3:]))