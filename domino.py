# Write your code here
import random


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
    stock, computer, player = shuffle_pieces()
    for value in highest_double:
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

print("=" * 70)
print("Stock size:", len(stock))
print("Computer pieces:", len(computer), "\n")
print(domino_snake[0])
print("\nYour pieces:")
for i in range(len(player)):
    print("{}:{}".format(i + 1, player[i]))
if status == "computer":
    print("\nStatus: Computer is about to make a move. Press Enter to continue...")
else:
    print("\nStatus: It's your turn to make a move. Enter your command.")
