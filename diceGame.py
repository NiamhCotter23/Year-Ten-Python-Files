import random
def dice():
    roll =random.randint(1,6)
    #print(roll)
    return roll
    dice()
def dice1():
    roll1 =random.randint(1,6)
    #print(roll)
    return roll1
    dice1()


player1=0
player2=0

for i in range(5):
    score=dice()+dice()
    if score % 2 == 0:
        score=score+10
    else:
        score=score-5
        if score<0:
            score=0
        else:
            score=score
player2=score
print(player2)

for i in range(5):
    score1=dice1()+dice1()
    if score1 % 2 == 0:
        score1=score1+10
    else:
        score1=score1-5
        if score1<0:
            score1=0
        else:
            score1=score1
player1=score1
print(player2)