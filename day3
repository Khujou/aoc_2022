def part1(file):
  lines = file.readlines()
  itemPriority = {}
  alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  for i in range(52):
    itemPriority[alpha[i]] = i + 1
  priorityItem = ""
  for line in lines:
    str1 = line[:int(len(line) / 2)]
    str2 = line[int(len(line) / 2):]
    alreadyCalled = ""
    for char in str1:
      if char not in alreadyCalled:
        if char in str2:
          priorityItem += char
        alreadyCalled += char
  score = 0
  for char in priorityItem:
    score += itemPriority.get(char)
  print("Part 1 is: " + str(score))


def part2(file):
  lines = file.readlines()
  itemPriority = {}
  alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  for i in range(52):
    itemPriority[alpha[i]] = i + 1
  priorityItem = ""
  str1 = ""
  str2 = ""
  str3 = ""
  for line in lines:
    if str1 == "":
      str1 = line
      continue
    elif str2 == "":
      str2 = line
      continue
    elif str3 == "":
      str3 = line
    for char in str1:
      if char in str2:
        if char in str3:
          priorityItem += char
          str1 = ""
          str2 = ""
          str3 = ""
          continue
  #print(priorityItem)
  score = 0
  for char in priorityItem:
    score += itemPriority.get(char)
  print("Part 2 is: " + str(score))


file = open("day3.txt", "r")
part1(file)
file.seek(0)
part2(file)
