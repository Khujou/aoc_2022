def part1(file):
  lines = file.readlines()
  count = 0
  for line in lines:
    segments = line.split(',')
    segmentNumbers = []
    for segment in segments:
      numbers = segment.split('-')
      segmentNumbers += [int(x) for x in numbers]
    if segmentNumbers[0] <= segmentNumbers[2] and segmentNumbers[1] >= segmentNumbers[3]:
      count += 1
    elif segmentNumbers[2] <= segmentNumbers[0] and segmentNumbers[3] >= segmentNumbers[1]:
      count += 1
  print("Part 1 is : " + str(count))

def part2(file):
  lines = file.read().splitlines()
  count = 0
  for line in lines:
    segments = line.split(',')
    sn = []
    for segment in segments:
      numbers = segment.split('-')
      sn += [int(x) for x in numbers]
    if sn[0] >= sn[2] and sn[0] <= sn[3]:
      count += 1
    elif sn[1] >= sn[2] and sn[1] <= sn[3]:
      count += 1
    elif sn[2] >= sn[0] and sn[2] <= sn[1]:
      count += 1
    elif sn[3] >= sn[0] and sn[3] <= sn[1]:
      count += 1
  print("Part 2 is : " + str(count))

file = open("day4.txt", "r")
part1(file)
file.seek(0)
part2(file)
