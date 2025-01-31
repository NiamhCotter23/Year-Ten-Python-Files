#Dice function
import random
def dice():
    return random.randint(1,6)

player1=0
player2=0

for i in range(5):
    dice1=dice()
    dice2=dice()
    print(f"Player1 rolled a {dice1} and a {dice2}")
    score=dice1+dice2

    if score % 2 == 0:
        score+=10
    else:
        score-=5
        if score<0:
            score=0
    player1+=score
print(f"Player1's total score for this round is {player1}")

for i in range(5):
    dice3 = dice()
    dice4 = dice()
    print(f"Player2 rolled a {dice3} and a {dice4}")
    score1 = dice3 + dice4
    if score1 % 2 == 0:
        score1+=10
    else:
        score1-=5
        if score1<0:
            score1=0
    player2+=score1
print(f"Player2's total score for this round is {player2}")
