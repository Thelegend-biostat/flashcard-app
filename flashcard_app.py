import os 
import random
import json


class Flashcard:
	## Represents a single flashcard.

	def __init__(self, question, answer):
		self.question = question
		self.answer = answer


class Deck:
	## representings a deck of flashcards with tracking.
	def __init__(self, name):
		self.name = name
		self.cards = [] #list of flash cards objects
		self.correct = 0
		self.incorrect = 0

	def add_card(self, question, answer):
		self.cards.append(Flashcard(question, answer))

	def play(self):
		if not self.cards:
			print("No cards in this deck!")
			return
		card = random.choice(self.cards)
		print(f"Question: {card.question}")
		user_answer = input("Your answer: ").lower().strip()
		if user_answer == card.answer:
			print("correct!")
			self.correct += 1
		else:
			print(f"wrong! The answer is: {card.answer}")
			self.incorrect += 1
		print(f"Score for {self.name}: Correct = {self.correct}, incorrect = {self.incorrect}")


class FlashcardApp: 
	## Main App to manage multiple decks......

	def __init__ (self, save_file = "flashcard.json"):
		self.decks = {}  #Dictionary: name --> Deck
		self.save_file = save_file
		self.load()

	def add_deck(self, name):
		if name not in self.decks:
			self.decks[name] = Deck(name)
			print(f"Deck '{name}' created")

	def add_card_to_deck(self, deck_name, question, answer):
		if deck_name in self.decks:
			self.decks[deck_name].add_card(question, answer)
		else:
			print("Deck not found!")

	def play_deck(self, deck_name):
		if deck_name in self.decks:
			self.decks[deck_name].play()
		else:
			print("Deck not found!")

	def save(self):
		data = {name: {"correct": deck.correct, "incorrect": deck.incorrect} for name, deck in self.decks.items()}
		with open(self.save_file, "w") as f:
			json.dump(data, f)
		print("Progress saved.")


	def load(self):
		if os.path.exists(self.save_file):
			with open(self.save_file, "r") as f:
				data = json.load(f)
			for name, scores in data.items():
				self.add_deck(name)
				self.decks[name].correct = scores["correct"]
				self.decks[name].incorrect = scores["incorrect"]
			print("Progress loaded")





app = FlashcardApp()
app.add_deck("Math")
app.add_card_to_deck("Math", "15 - 6", "9")
app.add_card_to_deck("Math", "20 - 6", "14")
app.add_card_to_deck("Math", "24 + 6", "30")

app.add_deck("science")
app.add_card_to_deck("science", "What's force/area?", "pressure")
app.add_card_to_deck("science", "What's the smallest unit of life?", "cell")
app.add_card_to_deck("science", "What gas do plants absorb from the atmosphere for photosynthesis?", "carbon dioxide")


app.play_deck("Math")
app.play_deck("science")

app.save()


app.load()
























