"""
Make:
(should I make it remember players? give them a password too?),
surrender
insurance
hidden count cards feature
"""

from random import shuffle

class CustomError(Exception):
    pass


class Game:
    def __init__(self):
        empty_hand = []
        player_wallet = 500
        dealer_wallet = 1000000
        name_player = input("player name: ")
        name_dealer = "The dealer"
        self.deck = Deck()
        self.p1 = Player(name_player, empty_hand, player_wallet)
        self.p2 = Player(name_dealer, empty_hand, dealer_wallet)

    def check_value(self, ph):
        player_value = 0
        aces = 0
        for card in ph:
            if card.value in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                player_value += int(card.value)
            elif card.value in ["Jack", "Queen", "King"]:
                player_value += 10
            elif card.value == "Ace":
                    aces += 1
        for _ in range(aces):
            if player_value + 11 <= 21:
                player_value += 11
            else:
                player_value += 1
        return player_value

    def check_blackjack(self, ph):
        if len(ph) == 2 and self.check_value(ph) == 21:
            return True
        return False

    def check_winner_during_play(self, p1h, p2h):
        p1v = self.check_value(p1h)
        p2v = self.check_value(p2h)

        if p1v == 21 and p2v == 21:
            return "Tie"
        elif p2v > 21 or ("Ace" in [card.value for card in p1h] and any(
            face_card in [card.value for card in p1h] for face_card in
            ["King", "Queen", "Jack"]) and len(p1h) == 2):
            return "player 1"
        elif p1v > 21 or ("Ace" in [card.value for card in p2h] and any(
            face_card in [card.value for card in p2h] for face_card in
            ["King", "Queen", "Jack"]) and len(p2h) == 2):
            return "Dealer"
        else:
            return "No winner"

        """first check player blackjack
            then check dealer blackjack
            if both blackjack its a tie
            then check player bust 
            (both hands separately(if more than one hand))
            then check dealer bust
            then check who has higher"""

    def check_winner_after_play(self, p1h, p2h):
        p1v = self.check_value(p1h)
        p2v = self.check_value(p2h)
        if p1v == p2v and p1v <= 21:
            return "Tie"
        elif p1v == 21 or p2v > 21 or p2v < p1v <= 21:
            return "player 1"
        elif p2v == 21 or p1v > 21 or p1v < p2v <= 21:
            return "Dealer"


        """first check player blackjack
            then check dealer blackjack
            if both blackjack its a tie
            then check player bust 
            (both hands separately(if more than one hand))
            then check dealer bust
            then check who has higher"""

    def wins(self, winner):
        w = "{} wins this round"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c):
        d = "{} received {}"
        d = d.format(p1n, p1c)
        print(d)

    def hand(self, ph):
        counter = 1
        for card in ph:
            h = "{}: {}"
            h = h.format(counter, card)
            counter +=1
            print(h)

    def play_game(self):
        cards = self.deck.cards
        print("Welcome to Blackjack!")
        p1h, p2h = [], []
        while len(cards) >= 8:
        # check if player wants to leave
            m = "q to quit. Any " + \
                "key to play:"
            response = input(m)
            if response == 'q':
                break
        # check if player wants to change bet
            print("wallet:", self.p1.wallet)
            print("Current Bet: ", self.p1.bet)
            while True:
                try:
                    ask = "Do you want to change your bet? (y/n)"
                    ask_response = input(ask).lower()
                    if ask_response == "y":
                        bet = "Player 1 set a bet line:  "
                        self.p1.bet = int(input(bet))
                # check if player has money to make bet (whether changed or not)
                    if self.p1.bet > self.p1.wallet:
                        raise CustomError
                    self.p1.wallet -= self.p1.bet
                    break
                except ValueError:
                    print("Pick an amount to bet please.")
                except CustomError:
                    print("Pick a bet you can afford.")

            for _ in range(2):
                p1h.append(self.deck.rm_card())
                p2h.append(self.deck.rm_card())
            p1n = self.p1.name
            p2n = self.p2.name
            print(p1n, "'s hand:")
            self.hand(p1h)

            #player moves
            while True:
                check_winner = self.check_winner_during_play(p1h, p2h)
                if check_winner == "Dealer":
                    self.wins(self.p2.name)
                    break
                elif check_winner == "player 1":
                    self.wins(self.p1.name)
                    winnings = round(self.p1.bet * 2)
                    self.p1.wallet += winnings
                    break
                elif check_winner == "Tie":
                    print("Push")
                    break
                try:

                    #if dealer has an ace
                    if "Ace" in [card.value for card in p2h]:
                        print("Dealer has an ace.")
                        options = ["stay", "hit", "double", "insurance"]
                    # if player has the same card values

                    else:
                        options = ["stay", "hit", "double"]
                    print("These are your options: ", options)
                    r1 = "Player 1 choose an option: "
                    response1 = input(r1).lower()
                    if response1 not in options:
                        raise CustomError
                    if response1 == "stay":
                        break
                    elif response1 == "hit":
                        p1h.append(self.deck.rm_card())
                    elif response1 == "double":
                        print("Wager doubled!")
                        p1h.append(self.deck.rm_card())
                        self.p1.bet *= 2
                    elif response1 == "surrender":
                        refund = self.p1.bet // 3
                        self.p1.wallet += refund
                        print(f"Player 1 surrendered and received ${refund:.2f} back.")
                    elif response1 == "insurance":
                        if self.check_blackjack(p2h):
                            insurance = self.p1.bet // 2
                            self.p1.wallet += insurance
                    self.hand(p1h)
                except CustomError:
                    print("Pick an option spelled correctly please.")

            if response1 == "surrender" or self.check_value(p1h) > 21:
                continue
            #dealer hits until over or equal to 21 or
            #over user or equal user given user is 15 or higher
            while self.check_value(p2h) < 16:
                p2h.append(self.deck.rm_card())
                print("Dealer hits.")

                if self.check_value(p2h) >= 21:
                    break

            #check dealer black jack
            if self.check_blackjack(p2h):
                print("Dealer has Blackjack!")
                self.hand(p2h)
                self.wins(self.p2.name)
                continue

            #end turn pay winning if there are
            final_winner = self.check_winner_after_play(p1h, p2h)
            if final_winner == "Dealer":
                self.wins(self.p2.name)
            elif final_winner == "player 1":
                self.wins(self.p1.name)
                winnings = round(self.p1.bet * 2)
                self.p1.wallet += winnings
            elif final_winner == "Tie":
                print("Push")
            print(p1n, "'s hand:")
            self.hand(p1h)
            print(p2n, "'s hand:")
            self.hand(p2h)
            #reset hands for next round
            p1h.clear()
            p2h.clear()

class Player:
    def __init__(self, name, hand, wallet):
        self.bet = 10
        self.card = None
        self.wallet = wallet
        self.name = name
        self.hand = hand
        self.splitHand = None


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards \
                    .append(Card(i,j))
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
    values = (
        None, None, "2", "3", "4",
        "5", "6", "7", "8","9", "10",
        "Jack", "Queen", "King", "Ace"
        )

    def __init__(self, v, s):
        self.value = self.values[v]
        self.suit = self.suits[s]

    def __repr__(self):
        v = self.value + " of " + self.suit
        return v

game = Game()
game.play_game()