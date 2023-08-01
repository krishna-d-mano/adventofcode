day1 = open("day1.txt", "r")

total_cal = 0

elf_id = 1

elf_map = {}

while True:
  line = day1.readline()
  if not line:
    break
  if line == "\n":
    elf_map[elf_id] = total_cal
    elf_id += 1
    total_cal = 0
    continue
  total_cal += int(line)

day1.close()

first = max(elf_map.values())

second = sorted(elf_map.values())[-2]

third = sorted(elf_map.values())[-3]

# sum = int(first) + int(second) + int(third)

# print(sum)

print(first)