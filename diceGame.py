#rules
print("""Rules:
The points rolled on each player’s dice are added to their score.
If the total is an even number, and additional 10 points are added to their score.
If the total is an odd number, 5 points are subtracted from their score.
The score of a player cannot go below 0 at any point.
The person with the highest score at the end of the 5 rounds wins.
If both players have the same score at the end of the 5 rounds, they each roll 1 die and whoever gets the highest score wins (this repeats until someone wins).
""")

#Dice function
import random
def dice():
    return random.randint(1,6)

player1=0
player2=0

#Player 1's turn
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

#Player 2's turn
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

#Winner
print("And now for the winner!")
if player1>player2:
    winner="Player1"
    playerWin=player1
elif player1==player2
    winner=""
else:
    winner="Player2"
    playerWin=player2
print(f"The winner is {winner} with a score of {playerWin}")

#Play again?
