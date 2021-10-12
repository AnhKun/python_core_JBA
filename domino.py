# Write your code here
import random


# the function that shuffles the domino and assigns them to the user
def shuffle_pieces():
    domino = []
    for i in range(7):
        for j in range(i, 7):
            domino.append([i, j])
    random.shuffle(domino)  # random the domino
    stock = domino[:14]
    computer = domino[14:21]
    player = domino[21:]
    return stock, computer, player


domino_snake = []
highest_double = [[6, 6], [5, 5]]
need_reshuffle = True
while need_reshuffle:
    stock, computer, player = shuffle_pieces()  # shuffle the domino
    for value in highest_double:  # loop through the highest_double to find the domino_snake' snake
        if value in computer:
            domino_snake.append(value)
            computer.remove(value)
            status = "player"
            need_reshuffle = False
            break
        elif value in player:
            domino_snake.append(value)
            player.remove(value)
            status = "computer"
            need_reshuffle = False
            break


def switch_turn(user, num):
    global status
    if num > 0:
        domino_snake.insert(len(domino_snake), user[num - 1])
        user.remove(user[num - 1])
    elif num < 0:
        domino_snake.insert(0, user[abs(num) - 1])
        user.remove(user[abs(num) - 1])
    else:
        user.insert(len(user), stock[0])
        stock.remove(stock[0])
    if status == "computer":
        status = "player"
    else:
        status = "computer"


while True:
    print("=" * 70)
    print("Stock size:", len(stock))
    print("Computer pieces:", len(computer), "\n")


    if len(domino_snake) <= 6:
        for i in range(len(domino_snake)):
            print(domino_snake[i], end="")
    else:
        for i in range(3):
            print(domino_snake[i], end="")
        print("...", end="")
        for i in [-3, -2, -1]:
            print(domino_snake[i], end="")


    print("\nYour pieces:")
    for i in range(len(player)):
        print("{}:{}".format(i + 1, player[i]))

    if status == "computer":
        print("\nStatus: Computer is about to make a move. Press Enter to continue...")
        choice = input()
        random_index = random.randint(-len(computer), len(computer))
        switch_turn(computer, random_index)
    else:
        print("\nStatus: It's your turn to make a move. Enter your command.")
        choice = int(input())
        switch_turn(player, choice)
    if len(computer) == 0 or len(player) == 0:
        break

if len(computer) == 0:
    print("\nStatus: The game is over. Computer won!")
else:
    print("\nStatus: The game is over. You won!")
