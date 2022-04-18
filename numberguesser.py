import random
from datetime import datetime


class HighScore:
    high_score_list = []

    def add(self, current_guesses: int):
        tmp_min = 0

        if len(self.high_score_list) > 0:
            tmp_min = min(self.high_score_list)
            if len(self.high_score_list) >= 5:
                self.high_score_list.remove(0)

        self.high_score_list.append(current_guesses)

        if tmp_min > current_guesses:
            print("Du hast einen neuen Highscore: {}".format(current_guesses))


def print_high_score(self):
    self.high_score_list.sort()

    for i in range(0, len(self.high_score_list)):
        print('{}. {} {}'.format(i + 1, self.high_score_list[i],
                                 ("Versuche" if self.high_score_list[0] > 1 else "Versuch")))


class Data:
    duration = 0
    start_time = datetime

    def start(self):
        self.start_time = datetime.now()

    def stop(self):
        now = datetime.now()
        self.duration = now - self.start_time
        print(
            "Du hast insgesamt {} Sekunden gebraucht, um die Nummer zu erraten.".format(self.duration.total_seconds()))


def clear_console():
    for i in range(100):
        print(" ")


def start_round():
    data = Data()
    data.start()
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
            highScore.add(guesses)
            data.stop()

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


highScore = HighScore()

print("Willkommen bei Number Guess!")
print("Das Ziel ist es, die zufällig generierte Zahl zwsichen 1 und 100 zu erraten.")
print(" ")
start_round()
