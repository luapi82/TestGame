#The goal is to double the money you borrowed and make as much as possible within 5 days. Every action will take away hours left until you're forced to sleep.
import sys
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
from random import randint

playerHP = 100
moneyInBank = 0
moneyInPocket = 0
borrowedAmount = 0
moneyOwed = 0
hoursLeft = 18
daysLeft = 5
workedToday = False
enemyHP = 0

def moneyStolen():
	global moneyInPocket
	nL()
	print('While you were sleeping, a burglar stole all the money from your pockets...')
	moneyInPocket = 0
	
def flipACoin():
	coin = randint(0,1)
	return coin	
	
def pressEnterToContinue():
	nL()
	str(input('Press Enter to continue...'))

def nL():
	print()

def showStats():
	nL()
	print("-----------------------------------------------------------------------------------------------------\n[ Your HP:",playerHP,"] [ Money in pocket:",moneyInPocket,"] [ Money in Bank:",moneyInBank,"] [ Money Owed:",moneyOwed,"] [ Days Left:",daysLeft,"]\n-----------------------------------------------------------------------------------------------------")

def youWon():
	nL()
	print('You won!')
	nL()
	str(input('Press enter to exit game...'))
	return

def youLost():
	nL()
	print('You lost... :(')
	pressEnterToContinue()
	return
	
def fight():
#Can only fight as long as you have HP
	global moneyInPocket
	global moneyOwed
	global playerHP
	global enemyHP
	enemyHP = randint(20,80)
	moneyOnTheTable = int((enemyHP/2))
	def getPower():
		power = randint(1,20)
		return power
	def reportHP():
		print('Your HP: [',playerHP,'] VS Enemy HP: [',enemyHP,']')
	def hitEnemy():
		global enemyHP
		hit = getPower()
		reportHP()
		print('You hit your enemy for [',hit,'] damage!')
		enemyHP -= hit
		pressEnterToContinue()
	def hitPlayer():
		global playerHP
		hit = getPower()
		reportHP()
		print('You got hit for [',hit,'] damage!')
		playerHP -= hit
		pressEnterToContinue()
	showStats()
	nL()
	print('This fight will be worth [$',moneyOnTheTable,'] You currently have [$',moneyInPocket,'].')
	if moneyOnTheTable <= moneyInPocket:
		userChoice=str(input('Are you sure you want to bet that amount? [Y,N]: '))
		nL()
		if (userChoice == 'y' or userChoice == 'Y'):
			while True:
				if flipACoin() == 0:hitEnemy()
				else:hitPlayer()
				if enemyHP <= 0:
					enemyHP = 0
					nL()
					reportHP()
					print('Enemy defeated. You won the battle!')
					moneyInPocket += moneyOnTheTable
					break
				elif playerHP <=0:
					playerHP = 0
					nL()
					reportHP()
					print('You have been defeated. You must rest to regain your HP...')
					moneyInPocket -= moneyOnTheTable
					break
				nL()
				
	else:
		print("Sorry bud, you don't have enough money for this fight. Go get a job!")
		pressEnterToContinue()
	mainGameChoice()
	
def gamble():
#Can gamble as much as you want
	nL()
	print('gamble')
	pressEnterToContinue()
	mainGameChoice()
	
def workPartTime():
#Can only work once a day
	global moneyInPocket
	global workedToday
	from random import randint
	hours = randint(2,7)
	wage = 6
	if workedToday == False:
		nL()
		gained = (hours * wage)
		moneyInPocket += gained
		print('You take a [',hours,'] hour shift at McDonalds and gained $[',gained,']')
		workedToday = True
		pressEnterToContinue()
		mainGameChoice()
	else:
		nL()
		print('You don\'t have any shifts left for today. Come back tomorrow!')
		mainGameChoice()
	
def sleep():
#Sleep replenishes all HP
	global playerHP
	global workedToday
	global daysLeft
	global moneyInBank
	global moneyInPocket
	global moneyOwed
	if (daysLeft > 0):
		workedToday	= False
		nL()
		print('You go to sleep... You wake up the next day feeling replenished.')
		playerHP = 100
		daysLeft -= 1
		if flipACoin() == 1:
			moneyStolen()
		pressEnterToContinue()
		mainGameChoice()
	elif (daysLeft == 0):
		if (moneyInBank + moneyInPocket >= moneyOwed):
			youWon()
		else: 
			nL()
			userChoice=str(input('You don\'t have enough money to win the game. Are you sure you want to finish the game now? [Y,N]: '))
			if (userChoice == 'y' or userChoice == 'Y' or userChoice == 'yes' or userChoice == 'Yes' or userChoice == 'YES'):youLost()
			else:mainGameChoice()
	
def banking():
#Can deposit for a 20% fee
#Can Withdraw
	global moneyInPocket
	global moneyInBank
	costToDeposit = 0.20
	showStats()
	nL()
	print("What would you like to do?")
	while True:
		userChoice=int(input('[1]Deposit, [2]Withdraw, [3]Return to main menu [1-3]:'))
		if (userChoice == 1 or userChoice == 2 or userChoice == 3):
			break
	if (userChoice == 1):
		nL()
		while True:
			toDeposit=int(input('How much would you like to deposit?: '))
			if (toDeposit >= 0 and toDeposit <= moneyInPocket):
				break
		nL()
		cost = int(toDeposit * costToDeposit)
		print('This will cost you $[',cost,']')
		userChoice=str(input('Are you sure you sure? [Y,N]: '))
		if (userChoice == 'y' or userChoice == 'Y' or userChoice == 'yes' or userChoice == 'Yes' or userChoice == 'YES'):
			moneyInBank = toDeposit - cost + moneyInBank
			moneyInPocket -= toDeposit

	elif (userChoice == 2):
		nL()
		while True:
			userChoice=int(input('How much would you like to withdraw?: '))
			if (userChoice >= 0 and userChoice <= moneyInBank):
				moneyInPocket = userChoice + moneyInPocket
				moneyInBank -= userChoice
				break
	pressEnterToContinue()
	mainGameChoice()
	
def exitGame():
	nL()
	userChoice=str(input('Are you sure you want to exit? [Y,N]: '))
	if (userChoice == 'y' or userChoice == 'Y' or userChoice == 'yes' or userChoice == 'Yes' or userChoice == 'YES'):sys.exit()
	else:mainGameChoice()

def mainGameChoice():
	showStats()
	nL()
	print("What would you like to do?")
	while True:
		userChoice=int(input('[1]Fight, [2]Gamble, [3]Work part time, [4]Sleep, [5]Banking, [6]Exit Game [1-6]:'))
		if (userChoice == 1 or userChoice == 2 or userChoice == 3 or userChoice == 4 or userChoice == 5 or userChoice == 6):
			break
	if (userChoice == 1):
		fight()
	elif (userChoice == 2):gamble()
	elif (userChoice == 3):workPartTime()
	elif (userChoice == 4):sleep()
	elif (userChoice == 5):banking()
	elif (userChoice == 6):exitGame()

def startGame():
	global moneyInPocket
	global moneyOwed
	nL()
	message = "You left home. If you can call it that... You have no money. Desperate you borrowed money from someone who was willing to lend it but the catch is to return twice the amount of money within 5 days."
	print (message)
	#speak.Speak(message)
	nL()
	while True:
		userChoice=int(input('How much money would you like to borrow? $[500-1000]: '))
		if (userChoice <= 1000 and userChoice >= 500):
			break
	moneyOwed = userChoice * 2
	moneyInPocket = userChoice
	mainGameChoice()

startGame()