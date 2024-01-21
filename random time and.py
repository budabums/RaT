import random
import time

def generate_random_number():
    return random.randint(1, 100)

while True:
    random_number = generate_random_number()
    print(f"Random Number: {random_number}")
    time.sleep(10)

import random

phrases = [
    "Hello, world!",
    "Coding is fun!",
    "Keep calm and code on.",
    "The early bird catches the worm.",
    "Life is an adventure.",
    "Learn something new every day.",
    "Be the change you wish to see in the world.",
    "Dream big, work hard.",
    "Success is a journey, not a destination.",
    "Stay positive and keep smiling."
]

while True:
    random_phrase = random.choice(phrases)
    print(f"Random Phrase: {random_phrase}")
    input("Press Enter for another random phrase...")
