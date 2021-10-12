# write your code here
import random

print("Enter the number of friends joining (including you): ")
num = int(input())

team = {}
if num <= 0:
    print("\nNo one is joining for the party")
else:
    print("\nEnter the name of every fried (including you), each on a new line: ")
    for _ in range(num):
        name = input()
        team[name] = 0

    print("\nEnter the total bill value: ")
    bill = int(input())
    print('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:')
    team_member = [key for key in team.keys()]
    if input() == "Yes":
        lucky_member = random.choice(team_member)
        print("\n{} is the lucky one!\n".format(lucky_member))
        for key in team_member:
            if key == lucky_member:
                continue
            else:
                team[key] = round(bill / (num - 1), 2)
        print(team)
    else:
        print("\nNo one is going to be lucky\n")
        for key in team_member:
            team[key] = round(bill / num, 2)
        print(team)
