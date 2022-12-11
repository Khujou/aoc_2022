class Solution:

  def part1(file):
    list = []
    count = 0
    for lines in file.readlines():
      line = lines.split('\n')
      if line[0] == '':
        list.append(count)
        count = 0
      else:
        count += int(line[0])
    list.append(count)

    count = list[0]
    for i in list:
      if i > count:
        count = i
    
    print("Part 1 is: " + str(count))

  def part2(file):
    list = []
    count = 0
    for lines in file.readlines():
      line = lines.split('\n')
      if line[0] == '':
        list.append(count)
        count = 0
      else:
        count += int(line[0])
    list.append(count)

    a = list[0]
    b = list[0]
    c = list[0]
    for i in list:
      if i > a:
        c = b
        b = a
        a = i
      elif i > b:
        c = b
        b = i
      elif i > c:
        c = i

    countTotal = a + b + c

    print("Part 2 is: " + str(countTotal))
  

  file = open("day1.txt", "r")
  part1(file)
  file.seek(0)
  part2(file)
