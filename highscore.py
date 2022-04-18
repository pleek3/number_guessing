"""
As far as I know, the private modifier from java can be represented by "__".
Example: __foo or like here in the code: __high_score_list

I read that in Python you probably just don't overwrite variables of the other classes,
nevertheless I added the underlines just to be sure.
"""


class HighScore:

    def __init__(self) -> object:
        self.__high_score_list = []

    def add_score(self, score: int):
        tmp_min_score = 0

        if len(self.__high_score_list) > 0:
            tmp_min_score = min(self.__high_score_list)

            if len(self.__high_score_list) >= 5:
                self.__high_score_list.remove(0)

        self.__high_score_list.append(score)

        if tmp_min_score > score:
            print("Du hast einen neuen Highscore: {}".format(score))

    def print_high_score(self):
        self.__high_score_list.sort()

        for i in range(0, len(self.__high_score_list)):
            print('{}. {} {}'.format(i + 1, self.__high_score_list[i],
                                     ("Versuche" if self.__high_score_list[0] > 1 else "Versuch")))
