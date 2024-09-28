from random import randint

words = (
    "Apple",
    "Tiger",
    "Chair",
    "Pizza",
    "Beach",
    "Medium",
    "Garden",
    "Rocket",
    "Bridge",
    "Dragon",
    "Pencil",
)


class Hangman:
    def __init__(self, words, max_attempts=6) -> None:
        self.words = words
        self.max_attempts = max_attempts
        self.word_to_guess = list(
            map(str.lower, list(words[randint(0, len(words) - 1)]))
        )
        self.current_state = list("_" * len(self.word_to_guess))
        self.guessed_letters = set()
        self.used_letters = set()
        self.attempts_left = max_attempts

    def display_current_state(self):
        print(f"\nWord: {' '.join(self.current_state)}")
        print(
            f"Used letters: {', '.join(sorted(self.used_letters)) if self.used_letters else ''}"
        )
        print(f"Remaining attempts: {self.attempts_left}")

    def check_win(self):
        return all(letter in self.guessed_letters for letter in self.word_to_guess)

    def get_valid_guess(self):
        guess = input("\nEnter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabetical character.")
            return

        if guess in self.used_letters:
            print(f"You've already guessed '{guess}'. Try a different letter.")
            return

        self.used_letters.add(guess)
        return guess

    def update_word_progress(self, guess):
        if guess not in self.word_to_guess:
            return False

        for i, letter in enumerate(self.word_to_guess):
            if letter == guess:
                self.guessed_letters.add(guess)
                self.current_state[i] = guess

        return True

    def play(self):
        print("Welcome to Hangman!")
        print(
            f"The word you have to guess consists of {len(self.word_to_guess)} character."
        )

        while self.attempts_left > 0:
            self.display_current_state()

            guess = self.get_valid_guess()

            if self.update_word_progress(guess):
                print(f"Good job! '{guess}' is in the word.")
            else:
                self.attempts_left -= 1
                print(f"Sorry, '{guess}' is not in the word.")

            if self.check_win():
                print(
                    f"\nCongratulations! You've guessed the word: {self.word_to_guess}"
                )
                break
        else:
            print(
                f"\nOut of attempts! The word was: {self.word_to_guess}. Better luck next time."
            )


if __name__ == "__main__":
    WORDS = [
        "apple",
        "tiger",
        "chair",
        "pizza",
        "beach",
        "medium",
        "garden",
        "rocket",
        "bridge",
        "dragon",
        "pencil",
    ]

    game = Hangman(WORDS)
    game.play()


# word_to_guess = list(map(str.lower, list(words[randint(0, len(words) - 1)])))
# word_to_guess_copy = word_to_guess[:]
# print(f"The word you have to guess consists of {len(word_to_guess)} character.")
# print(word_to_guess_copy)
# try_number, num_of_guesses = 1, 10

# guessed_charecters = list("_" * len(word_to_guess))

# while try_number <= num_of_guesses:
#     print(f"Try number {try_number}")

#     guessed_char = input("Enter one charecter: ")

#     while len(guessed_char) != 1:
#         print("Enter only one charecter")
#         guessed_char = input("Enter one charecter: ")

#     guessed_char = guessed_char.lower()
#     print(word_to_guess)

#     indices = [i for i, x in enumerate(word_to_guess) if x == guessed_char]

#     for index in indices:
#         del guessed_charecters[index]
#         guessed_charecters.insert(index, guessed_char)
#         (
#             word_to_guess_copy.remove(guessed_char)
#             if guessed_char.lower() in word_to_guess_copy
#             else ""
#         )

#     print("".join(guessed_charecters))
#     try_number += 1

#     if not word_to_guess_copy:
#         print("You Won :)")
#         break

# if word_to_guess_copy:
#     print("You lose :(")
