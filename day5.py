def day5():
  
  def parsingCrane(file):
    lines = file.read().splitlines()
    stacks = {}
    for line in lines:
      if line[1] == "1":
        break
      for i in range(len(line)):
        if i%4 == 1:
          if stacks.get(i, 0) == 0:
            stacks[i] = line[i]
          else:
            stacks[i] += line[i]
    for element in stacks:
      stacks[element] = stacks[element].strip()
    i = 1
    newStacks = {}
    for element in stacks:
      newStacks[i] = stacks[element]
      i += 1
    return newStacks

  def parsingCommands(file):
    lines = file.read().splitlines()
    commands = []
    for line in lines:
      numbers = []
      if "move" not in line:
        continue
      segments = line.split(' ')
      for segment in segments:
        if segment.isdigit():
          numbers += [int(segment)]
      commands += numbers
    return commands
    
  
  def part1(file):
    boxes = parsingCrane(file)
    file.seek(0)
    commands = parsingCommands(file)
    for i in range(int(len(commands) / 3)):
      i *= 3
      old = boxes[commands[i+2]][::-1]
      old += boxes[commands[i+1]][:commands[i]]
      boxes[commands[i+2]] = old[::-1]
      boxes[commands[i+1]] = boxes[commands[i+1]][commands[i]:]
    str = ""
    for thing in boxes:
      if len(boxes[thing]) > 0:
        str += boxes[thing][0]
    print(str)
      
      

  def part2(file):
    boxes = parsingCrane(file)
    file.seek(0)
    commands = parsingCommands(file)
    for i in range(int(len(commands) / 3)):
      i *= 3
      old = boxes[commands[i+2]][::-1]
      new = boxes[commands[i+1]][:commands[i]]
      old += new[::-1]
      boxes[commands[i+2]] = old[::-1]
      boxes[commands[i+1]] = boxes[commands[i+1]][commands[i]:]
    str = ""
    for thing in boxes:
      if len(boxes[thing]) > 0:
        str += boxes[thing][0]
    print(str)

  file = open("day5.txt", "r")
  part1(file)
  file.seek(0)
  part2(file)

day5()
