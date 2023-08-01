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
    print(calories)

print(elf_map)

largest = max(elf_map.values())

print(largest)

# seperate each elf's inventory by reading new lines
# add up each inventory
# find inventory with most calories