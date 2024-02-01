import random
cpu = random.randint(1, 3)

user = input("Choose Rock, Paper, Or Scissors: ")
print(f"you chose {user}")
if user == "rock":
	if cpu == 1: #cpu chose rock
		print("computer chose rock")
		print("Tie game")
	elif cpu == 2: # cpu chose paper
		print("computer chose paper")
		print("you lost")
	else:
		print("computer chose scissors")
		print("you win")

if user == "paper":
	if cpu == 1: #cpu chose rock
		print("computer chose rock")
		print("you win")
	elif cpu == 2: #cpu chose paper
		print("computer chose paper")
		print("tie game")
	else:
		print("compter chose scissors")
		print("you lose")

if user == "scissors":
	if cpu == 1:
		print("computer chose rock")
		print("you lose")
	elif cpu == 2:
		print("computer chose paper")
		print("you win")
	else:
		print("computer chose scissors")
		print("tie game")

