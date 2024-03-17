class Player:
    def init(self, name):
        self.name = name
        self.hand = []

    def draw_card(self, deck):
        self.hand.append(deck.draw())

    def play_card(self):
        return self.hand.pop(0) if self.hand else None