import random
from enum import Enum

class Suit(Enum):
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    CLUBS = "Clubs"
    SPADES = "Spades"

class Card:
    def __init__(self, s, r):
        self.suit = s
        self.rank = r

    def value(self):
        if self.rank in ["Jack", "Queen", "King"]:
            return 10
        if self.rank == "Ace":
            return 11
        return int(self.rank)

    def __str__(self):
        return f"{self.rank} of {self.suit.value}"

class Deck:
    def __init__(self):
        r = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        self.cards = [Card(s, v) for s in Suit for v in r]
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop() if self.cards else None

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, c):
        self.hand.append(c)

    def total(self):
        t = sum(c.value() for c in self.hand)
        aces = sum(1 for c in self.hand if c.rank == "Ace")
        while t > 21 and aces:
            t -= 10
            aces -= 1
        return t

    def is_bust(self):
        return self.total() > 21

    def __str__(self):
        return f"{self.name}: {', '.join(str(c) for c in self.hand)} (Total: {self.total()})"

class Blackjack:
    def __init__(self, players):
        self.deck = Deck()
        self.players = [Player(p) for p in players]
        self.dealer = Player("Dealer")

    def deal(self):
        for _ in range(2):
            for p in self.players + [self.dealer]:
                p.add_card(self.deck.draw())

    def play(self):
        self.deal()
        for p in self.players:
            while not p.is_bust():
                print(p)
                if input(f"{p.name}, hit or stand? (h/s): ").lower() == "h":
                    p.add_card(self.deck.draw())
                else:
                    break
        print(self.dealer)
        while self.dealer.total() < 17:
            self.dealer.add_card(self.deck.draw())
            print(self.dealer)
        self.results()

    def results(self):
        d_total = self.dealer.total()
        print("\nFinal Results:")
        for p in self.players:
            if p.is_bust():
                print(f"{p.name} busts!")
            elif d_total > 21 or p.total() > d_total:
                print(f"{p.name} wins!")
            elif p.total() == d_total:
                print(f"{p.name} ties with Dealer!")
            else:
                print(f"{p.name} loses!")

if __name__ == "__main__":
    names = input("Enter player names (comma-separated): ").split(",")
    game = Blackjack([n.strip() for n in names])
    game.play()
