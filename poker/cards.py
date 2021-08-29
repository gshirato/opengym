import itertools
import random


class Board():
    def __init__(self, sb=10, bb=20):
        self.sb = sb
        self.bb = bb
        self.pod = 0
        self.cards = []

    def flop(self, deck):
        self.cards.extend(deck.deal_n(3))

    def turn(self, deck):
        self.cards.extend(deck.deal_n(1))

    def river(self, deck):
        self.cards.extend(deck.deal_n(1))


def get_action(index):
    return [
        'check',
        'bet',
        'call',
        'raise',
        'fold'
    ][index]


class Player():
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.playable = True

    def draw(self, deck, n_cards):
        self.cards.extend(deck.deal_n(n_cards))

    def action(self, action_index):
        return get_action(action_index)

    @property
    def n_cards(self):
        return len(self.cards)


class Deck():
    def __init__(self):
        self.suits = ['s', 'h', 'd', 'c']
        self.numbers = ['A'] + list(range(2, 11)) + ['J', 'Q', 'K']
        self.cards = list(itertools.product(self.suits, self.numbers))
        self.shuffle()

    def deal(self):
        card_i = random.randint(0, self.n_cards - 1)
        return self.cards.pop(card_i)

    def deal_n(self, n):
        return [self.deal() for _ in range(n)]

    def shuffle(self):
        random.shuffle(self.cards)

    @property
    def n_cards(self):
        return len(self.cards)


def main():
    deck = Deck()
    player_1 = Player('Gota')
    player_2 = Player('Kondo')
    board = Board()

    player_1.draw(deck, 2)
    player_2.draw(deck, 2)

    # プリフロ

    print(player_1.cards)
    print(player_2.cards)

    # アクション

    # フロップ
    board.flop(deck)
    print('----フロップ----')
    print(board.cards, deck.n_cards)

    # アクション

    # ターン
    board.turn(deck)
    print('----ターン----')
    print(board.cards, deck.n_cards)

    # アクション

    # リバー
    board.river(deck)
    print('----リバー----')
    print(board.cards, deck.n_cards)


if __name__ == '__main__':
    main()
