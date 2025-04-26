import random

def findMax(x, y):
    return max(x, y)

def rollDie():
    print("the die is cast")
    return random.randint(1,6)

def main():
    player1DieValue = rollDie()
    player2DieValue = rollDie()
    findMax(player1DieValue, player2DieValue)

    print("Player 1 rolled " + str(player1DieValue))
    print("Player 2 rolled " + str(player2DieValue))

    if player1DieValue > player2DieValue:
        print("Player 1 wins")
    elif player2DieValue > player1DieValue:
        print("Player 2 wins")
    else:
        print("It's a tie")

main()