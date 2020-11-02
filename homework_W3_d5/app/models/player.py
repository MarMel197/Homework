class Player:

    def __init__(self, name, selection):
        self.name = name
        self.win_count = 0
        self.selection = selection

    def add_win(self):
        self.win_count += 1

