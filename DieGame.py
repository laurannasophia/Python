import random

def findMax(x, y):
    return max(x, y)

def rollDie():
    print("Rolling")
    return random.randint(1,6)

def main():
    rounds = int(input("How many rounds do you want to play? "))
    i = int(1)
    points1 = int(0)
    points2 = int(0)
    
    while i <= rounds:
        player1DieValue = rollDie()
        player2DieValue = rollDie()

        print("Player 1 rolled " + str(player1DieValue))
        print("Player 2 rolled " + str(player2DieValue))

        if player1DieValue == player2DieValue:
            print(f"Round {i} is a tie.")
            i+=1
        
        elif player1DieValue == findMax(player1DieValue, player2DieValue):
            print(f"Player 1 wins round number {i}")
            points1+=1
            i+=1
        elif player2DieValue == findMax(player1DieValue, player2DieValue):
            print(f"Player 2 wins round number {i}")
            points2+=1
            i+=1
    
    print(f"Rounds played: {rounds}")
    if points1 > points2:
        print(f"Player 1 won with {points1} points! Player 2 got {points2} points.")
    elif points2 > points1:
        print(f"Player 2 won with {points2} points! Player 1 got {points1} points.")
    else:
        print(f"It is a tie with {points1} points for both.")

main()