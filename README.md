# flashcard-app
# Flashcard App

A Python-based quiz application for learning through flashcards, featuring multiple decks and persistent score tracking using JSON.

## Code Structure

The app is built with three main classes in `flashcard_app.py`:

- **Flashcard**: Represents a single flashcard.
  - Attributes:
    - `question`: The question text (string).
    - `answer`: The correct answer (string, case-insensitive).
  - Used to store individual question-answer pairs.

- **Deck**: Manages a collection of flashcards with score tracking.
  - Attributes:
    - `name`: Deck name (string, e.g., "Math").
    - `cards`: List of `Flashcard` objects.
    - `correct`: Number of correct answers (integer).
    - `incorrect`: Number of incorrect answers (integer).
  - Methods:
    - `add_card(question, answer)`: Adds a new flashcard.
    - `play()`: Randomly selects a card, prompts the user, and updates scores.

- **FlashcardApp**: Manages multiple decks and saves/loads scores.
  - Attributes:
    - `decks`: Dictionary mapping deck names to `Deck` objects.
    - `save_file`: JSON file for score persistence (`flashcard.json`).
  - Methods:
    - `add_deck(name)`: Creates a new deck.
    - `add_card_to_deck(deck_name, question, answer)`: Adds a card to a deck.
    - `play_deck(deck_name)`: Plays a deck’s quiz.
    - `save()`: Saves scores to `flashcard.json`.
    - `load()`: Loads scores from `flashcard.json`.

- **Data Storage**:
  - Scores are stored in `flashcard.json` as a dictionary (e.g., `{"Math": {"correct": 5, "incorrect": 0}, "science": {"correct": 3, "incorrect": 0}}`).

## Features
- Create and manage multiple decks (e.g., Math, Science).
- Add flashcards with questions and answers.
- Play quizzes with random card selection and score tracking.
- Persistent scores saved in JSON (`flashcard.json`).
- Debug mode for inspecting code flow (not shown in current code).

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Thelegend-biostat/flashcard-app.git


