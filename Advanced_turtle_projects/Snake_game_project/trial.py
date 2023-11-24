
highscore = 1
with open('highscore.txt','w') as f:
    f.write(str(highscore+3))

with open('highscore.txt') as f:
    highscore = int(f.readline().rstrip('\n'))


print(highscore)