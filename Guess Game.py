the_word = "justin"
attempt = 5
guess = ""

print("Welcome to the game. You have total 5 attempt to guess the word")

while attempt > 0:
    guess = input("Guess the word: ").lower()
    if guess == the_word:
        print("You won")
        break
    else:
        attempt -= 1
        if attempt > 0:
            print("You lost a chance and now you are left with", attempt, " attempt")
        else:
            print("Game Over! You've used all 5 attempts.")
            print("The correct word was: {the_word}")
