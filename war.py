from random import shuffle, randint

class CustomError(Exception):
   pass

class Game:
    def __init__(self):
        empty_hand = []
        global player_count
        player_count = int(input("Are there 1 or 2 players?"))
        if player_count == 1:
            name1 = input("p1 name ")
            name2 = "Bot"
        else:
            name1 = input("p1 name ")
            name2 = input("p2 name ")
        self.deck = Deck()
        self.p1 = Player(name1,empty_hand)
        self.p2 = Player(name2,empty_hand)

    def wins(self, winner):
        w = "{} wins this round"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} chose {}, {} chose {}"
        d = d.format(p1n,
                     p1c,
                     p2n,
                     p2c)
        print(d)

    def hand(self, ph):
        counter = 1
        for card in ph:
            h = "{}: {}"
            h = h.format(counter, card)
            counter+=1

            print(h)
        pass

    def play_game(self):
        cards = self.deck.cards
        print("beginning War!")
        p1h, p2h = [], []
        for card in range(0, 4):
            p1h.append(self.deck.rm_card())
            p2h.append(self.deck.rm_card())

        while len(cards) >= 2:
            m = "q to quit. Any " + \
                "key to play:"
            response = input(m)
            if response == 'q':
                break
            p1h.append(self.deck.rm_card())
            p2h.append(self.deck.rm_card())
            p1n = self.p1.name
            p2n = self.p2.name
            print("Player 1 hand:")
            self.hand(p1h)
            while True:
                try:
                    r1 = "Player 1 choose a card 1 - 5:"
                    response1 = int(input(r1))
                    if response1 not in range(1,6):
                        raise CustomError
                    break
                except ValueError:
                    print("Pick a number please.")
                except CustomError:
                    print("Pick a number 1 through 5 please.")

            p1c = p1h[response1 - 1]
            p1h.pop(response1 - 1)
            if player_count == 1:
                response2 = randint(1, 5)
            else:
                print("Player 2 hand:")
                self.hand(p2h)
                while True:
                    try:
                        r2 = "Player 2 choose a card 1 - 5:"
                        response2 = int(input(r2))
                        if response2 not in range(1, 6):
                            raise CustomError
                        break
                    except ValueError:
                        print("Pick a number please.")
                    except CustomError:
                        print("Pick a number 1 through 5 please.")
            p2c = p2h[response2 - 1]
            p2h.pop(response2 - 1)
            self.draw(p1n,
                      p1c,
                      p2n,
                      p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1,
                          self.p2)
        print("War is over. {}"
              .format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name + " wins"
        if p1.wins < p2.wins:
            return p2.name + " wins"
        return "It was a tie!"

class Player:
    def __init__(self, name, hand):
        self.wins = 0
        self.card = None
        self.name = name
        self.hand = hand

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards \
                    .append(Card(i,
                                 j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Card:
    suits = ("spades",
             "hearts",
             "diamonds",
             "clubs")

    values = (None, None, "2", "3",
              "4", "5", "6", "7",
              "8", "9", "10",
              "Jack", "Queen",
              "King", "Ace")

    def __init__(self, v, s):
        """suit + value are ints"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + \
            " of " + \
            self.suits[self.suit]
        return v

game = Game()
game.play_game()

