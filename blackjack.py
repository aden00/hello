from random import shuffle


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':1}
playing=True
class Card():
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    def __str__(self):
        return f'{self.rank} of {self.suit}'
class Deck():
    def __init__(self):
        self.allcards=[]
        for suit in suits:
            for rank in ranks:
                self.allcards.append(Card(suit,rank))
    def shuffle(self):
        shuffle(self.allcards)
    def takeone(self):
        return self.allcards.pop()
class Hand:
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0
    def addcard(self,card):
        self.cards.append(card)
        self.value+=values[card.rank]


class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total+=self.bet

    def lose_bet(self):
        self.total-=self.bet

def take_bet(chips):

    while True:
        try:
            chips.bet=int(input('please enter the amount you would like to bet: '))
        except ValueError:
            print('not a number!!!')
            continue
        else:
            if chips.bet>chips.total:
                print('You can not bet more than you have')
            else:
                break

def hit(deck,hand):
    hand.addcard(deck.takeone())

def hit_or_stand(deck,hand):
    global playing
    while True:
        ans=input('do you want to hit or stand? enter h or s: ')
        if ans=="h":
            hit(deck,hand)
        elif ans=="s":
            print("player stands. Dealer is playing.")
            playing=False
        else:
            print('please enter again.')
            continue
        break

def show_some(player, dealer):
    print("\nDealer's card:")
    print("<cardhidden>\n", dealer.cards[1])
    print("\n\nPlayer's card:",*player.cards,sep="\n")
    print("player's value: ", player.value)

def show_all(player, dealer):
    print("Player's card:", *player.cards, sep="\n")
    print("player's value: ",player.value)
    print("Dealer's card:", *dealer.cards, sep="\n")
    print("Dealer's value: ",dealer.value)


def player_busts(player,dealer,chips):
    print('player busts!!!')
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('player wins!!!')
    chips.win_bet()


def dealer_busts(player,dealer,chips):
    print('dealer busts!!')
    chips.win_bet()


def dealer_wins(player,dealer,chips):
    print('dealer wins!')
    chips.lose_bet()


def push(player,dealer):
    print("Dealer and Player tie! It's a push.")

while True:
    print("This is blackjack game.")

    alldeck=Deck()
    shuffle(alldeck.allcards)
    player=Hand()
    dealer=Hand()
    for i in range(2):
        player.addcard(alldeck.takeone())
        dealer.addcard(alldeck.takeone())

    playerchip=Chips()
    print(f"You have ${playerchip.total} in your account.")
    take_bet(playerchip)
    show_some(player,dealer)
    while playing:
        hit_or_stand(alldeck,player)
        show_some(player,dealer)
        if player.value>21:
            player_busts(player,dealer,playerchip)
            break
    if player.value<=21:
        while dealer.value<=17:
            hit(alldeck,dealer)
            show_all(player,dealer)
            if player.value>dealer.value:
                player_wins(player,dealer,playerchip)
            elif dealer.value>21:
                dealer_busts(player,dealer,playerchip)
            elif dealer.value>player.value:
                dealer_wins(player,dealer,playerchip)
            else:
                push(player,dealer)
    print(f'your total amount now:{playerchip.total}')
    ans=input("Want to play again? Enter y or n:")
    if ans=="y":
        playing=True
        continue
    if ans=="n":
        print("thanks for playing")
        break






