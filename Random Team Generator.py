import random

players = input("Enter player names: ").split()

random.shuffle(players)

team1 = players[:len(players)//2]
team2 = players[len(players)//2:]

print("Team 1:", team1)
print("Team 2:", team2)