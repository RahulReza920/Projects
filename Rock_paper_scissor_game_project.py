#Rock Paper Scissors game
#class,object,initfunction,function with argument
#list,random number,

from random import randint
print("**************************************************************")
print("Winning Rules of the Rock paper scissor game as follows: \n\n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n") 

class Player:
	def __init__(self):
		self.score = 0
		self.choice = None

human = Player()
computer = Player()

def game(player1, player2):
	choices = ["rock", "paper", "scissors"]

	computerChoice = randint(0, 2)
	player2.choice = choices[computerChoice]

	while (player1.choice == None):
		print("********************************************")
		humanChoice =input("What is your decision: Rock, Paper or Scissors: ").lower()
		if (humanChoice not in choices):
			print("Please spell or enter a correct option.\n")
		else:
			player1.choice = humanChoice
    
	print( "Human chooses: " + player1.choice )
	print( "Computer chooses: " + player2.choice + "\n")

	result = whoWon(player1, player2)
	if (result == 0):
		print("Match Draw")
	elif (result == 1):
		print("Human wins the game")
		player1.score += 1
	elif (result == 2):
		print("Computer wins the game")
		player2.score += 1
	else:
		print("Error: No result applicable to the match")

	print( "Player Scores: " + str(player1.score) + " | Computer scores: " + str(player2.score) + "\n")

	player1.choice = None

# return 0 if draw.
# return 1 if player1 won, 
# return 2 if player2 won, 
def whoWon(player1, player2):
	if (player1.choice == player2.choice):
		return 0
	elif (player1.choice == "rock") and (player2.choice == "scissors"):
		return 1
	elif (player1.choice == "rock") and (player2.choice == "paper"):
		return 2
	elif (player1.choice == "paper") and (player2.choice == "scissors"):
		return 2
	elif (player1.choice == "paper") and (player2.choice == "rock"):
		return 1
	elif (player1.choice == "scissors") and (player2.choice == "rock"):
		return 2
	elif (player1.choice == "scissors") and (player2.choice == "paper"):
		return 1
	else:
		return 3


playAgain = True

while (playAgain == True):
	game(human, computer)

	request =input("Would you like to play again? (Y/N) : ").lower()
	if (request == 'y'):
		playAgain = True
		print("Playing again\n")
	elif (request == 'n'):
		playAgain = False
		print("Let's stop\n")
	else:
		print("Didn't understand either Y or N, playing again by default.\n")
	

