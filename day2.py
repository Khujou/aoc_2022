class Solution:
  
  def part1(file):
    totalScore = 0
    for lines in file.readlines():
      line = lines.split('\n')
      enemyHand = line[0][0]
      yourHand = line[0][2]
      if enemyHand == 'A':
        if yourHand == 'X':
          totalScore += 4
        elif yourHand == 'Y':
          totalScore += 8
        elif yourHand == 'Z':
          totalScore += 3
          
      elif enemyHand == 'B':
        if yourHand == 'X':
          totalScore += 1
        elif yourHand == 'Y':
          totalScore += 5
        elif yourHand == 'Z':
          totalScore += 9
          
      elif enemyHand == 'C':
        if yourHand == 'X':
          totalScore += 7
        elif yourHand == 'Y':
          totalScore += 2
        elif yourHand == 'Z':
          totalScore += 6
    print(totalScore)

  
  def part2(file):
    totalScore = 0
    for lines in file.readlines():
      line = lines.split('\n')
      enemyHand = line[0][0]
      yourHand = line[0][2]
      if enemyHand == 'A':
        if yourHand == 'X':
          totalScore += 3
        elif yourHand == 'Y':
          totalScore += 4
        elif yourHand == 'Z':
          totalScore += 8
          
      elif enemyHand == 'B':
        if yourHand == 'X':
          totalScore += 1
        elif yourHand == 'Y':
          totalScore += 5
        elif yourHand == 'Z':
          totalScore += 9
          
      elif enemyHand == 'C':
        if yourHand == 'X':
          totalScore += 2
        elif yourHand == 'Y':
          totalScore += 6
        elif yourHand == 'Z':
          totalScore += 7
    print(totalScore)


  
  file = open("day2.txt", "r")
  part1(file)
  file.seek(0)
  part2(file)
