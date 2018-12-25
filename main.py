import itertools
import copy
import random

class Card(object):
	def __init__(self, value, suite):
		self. value = value
		self.suite = suite

	def __str__(self):
		return "{} of {}".format(self.value, self.suite)

class Deck(object):
	def __init__(self):
		self.create_all_cards()
		self.get_shuffled_deck()

	def create_all_cards(self):
		nums = ["7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
		suites = ["Hearts", "Clubs", "Spades", "Diamonds"]
		
		cards = []
		for i in nums:
			 for j in suites:
			 	cards.append(Card(i, j))

		self.cards = cards

	def get_shuffled_deck(self):
		shuffled_cards = copy.deepcopy(self.cards)
		random.shuffle(shuffled_cards)
		self.cards = shuffled_cards

	def remove_cards(self, n):
		for i in range(n):
			if len(self.cards) != 0:
				self.cards.pop(0)

	def get_cards(self):
		return copy.deepcopy(self.cards)

	def __str__(self):
		return str([str(card) for card in self.cards])

	def __len__(self):
		return len(self.cards)

class Player(object):
	#player object
	def __init__(self, hand):
		self.hand = hand
		self.name = input("What is your name?")

	def __str__(self):
		x = "-"*20 + "\nPlayer {}'s Hand:".format(self.name)
		y = ""
		j = 0
		for i in self.hand:
			j += 1
			y += "{}.".format(j) + " " + str(i) +'\n'
		z = "-" * 20
		return x + "\n" + y + z + "\n"

	def prompt_action(self):
		valid = ["Bez Koz", "Vsichko Koz", "Pika", "Spatiya", "Kypa", "Karo"]

		while True:
			user = input("What is your action? Type 'h' for the list of actions\n")

			if user == "h":
				print("Type either: 'Vsichko Koz', 'Bez Koz', 'Pika', 'Kypa', 'Karo', or 'Spatiya'")
			elif user in valid:
				return user
			else:
				print("Invalid action.")

	def prompt_card(self):
		print(self)

		while True:
			user = input("Using the cooresponding number, select a card: ")

			if int(user) in range(1, 8):
				return self.hand[int(user) - 1]
			else:
				print("Invalid selection.")

	def update_hand(self, new_hand):
		self.hand = new_hand

class AIPlayer(Player):
	def __init__(self):
		pass


class Game(object):
	def __init__(self, player_list):
		self.player_list = player_list
		self.deck = Deck()
		self.suites = {"Vsichko Koz": 5, "Bez Koz": 4, "Pika": 3, "Kypa": 2, "Karo": 1, "Spatiya": 0, "":-1}
		self.card_power = {"Vsichko": {'J':20, '9':14, 'A':11, '10':10, 'K':4, 'D':3}, 
			"Bez": {'A': 11, '10':10, 'K':4, 'D':3, 'J':2}}
		#self.start_round()

	def determine_round_mode(self):
		current_max = ""
		for i in self.player_list:
			response = i.prompt_action()
			if self.suites[response] > self.suites[current_max]:
				current_max = response
		return current_max

	def start_round(self):
		for i in self.player_list:
			i.update_hand(self.get_hand(5))
			print(i)

		mode = self.determine_round_mode()

	def play_round(self):
		mode = self.start_round()

		if mode == "Vsichko Koz":
			pass
		elif mode == "Bez Koz":
			pass
		elif mode == "Kypa":
			pass
		elif mode == "Karo":
			pass
		elif mode == "Pika":
			pass
		elif mode == "Spatiya":
			pass
		else:
			print("Error! Something Went Wrong!")
			quit()

		while len(self.deck) > 0:
			self.play_one_hand(card_powers)

	def play_one_hand(self, card_powers, mode):
		if mode == "Vsichko Koz":
			relevant = card_powers["Vsichko"]

		elif mode == "Bez Koz":
			relevant = card_powers
	def VsichkoKoz(self):
		pass

	def get_hand(self, n):
		hand = self.deck.get_cards()[0:n]

		self.deck.remove_cards(n)

		return hand

	def distribute_cards(self, n):
		#deck is deck object
		#player list is a list of four players
		for i in self.player_list:
			i.update_hand(self.get_hand(n))

if __name__ == "__main__":
	p = []
	for i in range(4):
		p.append(Player([]))

	g = Game(p)
	g.distribute_cards(5)

	for i in g.player_list:
		print(i)

	print(p[0].prompt_card())
	print(p[1].prompt_action())