def day6(file):
  def part1and2(file, num):
    line = file.read()
    for i in range(len(line) - (num-1)):
      str = line[i:i+num]
      dict = {}
      for char in str:
        if dict.get(char, 0) == 0:
          dict[char] = 1
        else:
          dict[char] += 1
      j = 0
      for element in dict:
        if dict[element] == 1:
          j += 1
      if j == num:
        return(i + num)
  
  print(part1and2(file, 4))
  file.seek(0)
  print(part1and2(file, 14))

file = open("day6.txt", "r")
day6(file)
