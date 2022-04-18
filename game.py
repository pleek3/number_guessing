import random
import highscore
import rounddata

highScore = highscore.HighScore()


def clear_console():
    for i in range(100):
        print(" ")


def start_round():
    round_data = rounddata.RoundData()
    round_data.start()

    guesses = 0
    random_number = random.randint(1, 100)

    while True:
        guess = input("Was denkst du, ist die Zahl? ")
        guess = int(guess)
        guesses += 1

        if guess == random_number:
            clear_console()
            print("Du hast richtig geraten!")
            print("Deine Versuche: {}".format(guesses))
            highScore.add_score(guesses)
            round_data.stop()

            print(" ")
            print("HighScore:")
            highScore.print_high_score()
            print(" ")

            print("Tippe 'y' für eine weitere Runde oder 'n' zum verlassen:")
            rematch()

            break
        elif guess > random_number:
            print("Deine Zahl war zu groß!")
        else:
            print("Deine Zahl war zu klein!")


def rematch():
    if input() == "y":
        clear_console()
        start_round()
    else:
        exit()


print("Willkommen bei Number Guess!")
print("Das Ziel ist es, die zufällig generierte Zahl zwsichen 1 und 100 zu erraten.")
print(" ")
start_round()
