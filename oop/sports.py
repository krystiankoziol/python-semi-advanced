from oop.exeptions import NameTooShortException


class Arena:
    def __init__(self):
        self.games = []
        # self.standing = []

    def add_game(self, game):
        self.games.append(game)

    def standing(self):
        players = []
        scores = []
        for game in self.games:
            white = game.white
            black = game.black
            if white not in players:
                players.append(white)
                scores.append(0)
            if black not in players:
                players.append(black)
                scores.append(0)
            if game.withe_won():
                index = players.index(white)
            if game.black_won():
                index = players.index(black)
            scores[index] += 1
        player_score_list = list(zip(players, scores))
        player_score_list.sort(reverse=True, key=lambda x: x[1])
        return ([pair[0] for pair in player_score_list])


'''
1 lista
2 słaownik zawodnik -liczba zwyciestw
'''


# Zawodnik imię i ranking
class Player:
    def __init__(self, name, ranking):
        if len(name) < 3:
            raise NameTooShortException()
        self._name: str = name
        self.ranking: int = ranking

    def __eq__(self, other):
        if not isinstance(other, Player):
            return False
        return self.name == other.name

    def __hash__(self):
        _result = 0
        for letter in self.name:
            _result += ord(letter)
            _result *= 31
        return _result

    @property
    def name(self):
        return self._name

    def description(self):
        return f'My name is {self.name} and my ranking is {self.ranking}.'


# białe czarne wynik
class Game:
    def __init__(self, white, black, result):
        if result not in (1, 2):
            raise ResultNotInRange

        self.white = white
        self.black = black
        self.result = result

    def withe_won(self):
        return self.result == 1

    def black_won(self):
        return self.result == 2
