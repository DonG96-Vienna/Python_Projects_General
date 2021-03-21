'''

Ratespiel

'''

from random import randint

lim = int(input("Enter a upper limit for number guess: "))

while True:
    guess_number = randint(1, lim)

    #print(guess_number)

    lives = 3

    # Initialisieren, damit while einen Vergleich machen kann
    guess = 0

    while guess != guess_number and lives > 0:

        guess = int(input(f"Enter a guess between 1 and {lim}: \n"))

        if guess > guess_number:
            print(f"{guess} is too large! Try again!")
            lives -= 1
            print(f"{lives} lives left!\n")

        elif guess < guess_number:
            print(f"{guess} is too small! Try again!")
            lives -= 1
            print(f"{lives} lives left!\n")

    if guess == guess_number:
        print(f"\n{guess_number} was correct! Congratulations!")

    elif lives == 0:
        print("Out of lives. You lose!\n")

    key = input("Continue playing? (y/n): ")
    if key == 'n':
        break

print("\n\nThanks for playing!")