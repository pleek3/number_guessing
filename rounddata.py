from datetime import datetime


class RoundData:

    def __init__(self) -> object:
        self.duration = 0
        self.start_time = None

    def start(self):
        self.start_time = datetime.now()

    def stop(self):
        now = datetime.now()
        self.duration = now - self.start_time

        print(
            "Du hast insgesamt {} Sekunden gebraucht, um die Nummer zu erraten.".format(self.duration.total_seconds()))
