def day7(file):
  def parsing(segments):
    rootDir = {}
    rootDir[".."] = rootDir
    dir = rootDir
    for i in range(len(segments)):
      line = segments[i]
      if line[0] == '$':
        if line[1] == "cd":
          if line[2] == '/':
            dir = rootDir
            continue
          dir = dir[line[2]]
        elif line[1] == "ls":
          for j in range(i+1, len(segments)):
            leadingLine = segments[j]
            if leadingLine[0] == '$':
              break
            elif leadingLine[0][0] in "1234567890":
              dir[leadingLine[1]] = leadingLine[0]
            elif leadingLine[0] == "dir":
              dir[leadingLine[1]] = {}
              dir[leadingLine[1]][".."] = dir
    return rootDir

  def recursion(dir, list):
    size = 0
    for element in dir:
      if element == "..":
        continue
      elif type(dir[element]) == dict:
        dirSize = 0
        dirSize += recursion(dir[element], list)
        if dirSize:
          list.append(dirSize)
        size += dirSize
      else:
        size += int(dir[element])
    return size
    
  def part1(file):
    lines = file.read().splitlines()
    segments = []
    for element in lines:
      line = element.split(' ')
      segments.append(line)
    dir = parsing(segments)
    list = []
    size = recursion(dir, list)
    if size < 100_000:
      print(size)
    yo = 0
    for hi in list:
      if hi < 100_000:
        yo += hi
    print(yo)
      

  def part2(file):
    lines = file.read().splitlines()
    segments = []
    for element in lines:
      line = element.split(' ')
      segments.append(line)
    dir = parsing(segments)
    list = []
    size = recursion(dir, list)
    sizeLimit = 70_000_000
    sizeNeeded = 30_000_000 - (sizeLimit - size)
    requirementMet = []
    for shit in list:
      if shit >= sizeNeeded:
        requirementMet.append(shit)
    lowest = requirementMet[0]
    for poop in requirementMet:
      if poop < lowest:
        lowest = poop
    print(lowest)
    

  part1(file)
  file.seek(0)
  part2(file)

file = open("day7.txt", "r")
day7(file)
