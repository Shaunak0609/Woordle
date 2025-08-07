import random 
from datetime import datetime

start_date = datetime(2025, 8, 1)
today = datetime.now()
delta_days = (today - start_date).days

def load_words(filename):
    with open(filename) as f:
        words = [line.strip().lower() for line in f]
    return words

word_list = load_words("words.txt")
MAX_TRIES = 6

chosen_word = word_list[delta_days % len(word_list)]

GREEN = '\033[1;42m'
YELLOW = '\033[1;43m'
GRAY = '\033[1;40m'
RESET = '\033[0m'

def get_feedback(guess, target):
    feedback = [""] * 5
    target_chars = list(target)

    for i in range(5):
        if guess[i] == target[i]:
            feedback[i] = GREEN + guess[i].upper() + RESET
            target_chars[i] = None

    for i in range(5):
        if feedback[i] == "":
            if guess[i] in target_chars:
                feedback[i] = YELLOW + guess[i].upper() + RESET
                target_chars[target_chars.index(guess[i])] = None
            else:
                feedback[i] = GRAY + guess[i].upper() + RESET
    
    return "".join(feedback)

print("Welcome to Wordle Clone Wordoo!")

for attempt in range(1, MAX_TRIES + 1):
    while True:
        guess = input(f"\nAttempt {attempt}/6 - Enter a 5-letter word: ").lower()
        if len(guess) != 5:
            print("Please enter exactly 5 letters.")
        elif guess not in word_list:
            print("Word not in list.")
        else:
            break

    feedback = get_feedback(guess, chosen_word)
    print(f"Your guess: {guess.upper()}")
    print(f"Feedback : {feedback}")

    if guess == chosen_word:
        print("You guessed it")
        break
else:   
    print(f"❌ Out of tries. The word was: {chosen_word.upper()}")