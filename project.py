import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card():

    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck():

    def __init__(self):
        self.all_cards=[]
        for everysuit in suits:
            for everyrank in ranks:
                self.all_cards.append(Card(everysuit,everyrank))
    def shuffle(self):
        random.shuffle(self.all_cards)
    def takeone(self):
        return self.all_cards.pop()

class Player():
    def __init__(self,name):

        self.name=name
        self.all_cards=[]
    def removecard(self):

        return self.all_cards.pop(0)
    def addcards(self,newcard):
        if type(newcard)==type([]):
            self.all_cards.extend(newcard)
        else:
            self.all_cards.append(newcard)
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
player1=Player('One')
player2=Player('Two')


new_deck=Deck()
new_deck.shuffle()
mycard=new_deck.takeone()

for i in range(26):
    player1.addcards(mycard)
    player2.addcards(mycard)


gameon=True
roundnumber = 0

while gameon:

    roundnumber+=1
    print(f'Round {roundnumber}'.upper())
    if len(player1.all_cards)==0:
        print('Player one out of cards!!!! Player 2 winnnnnns!!!')
        gameon=False
        break

    if len(player2.all_cards) == 0:
        print('Player two out of cards!!!! Player 1 winnnnnns!!!')
        gameon=False
        break
    card1 =[]
    card1.append(player1.removecard())

    card2 =[]
    card2.append(player2.removecard())
    war =True
    while war:
        if card1[-1].value>card2[-1].value:
            player1.addcards(card2)
            player1.addcards(card1)
            war=False
        elif card1[-1].value<card2[-1].value:
            player2.addcards(card2)
            player2.addcards(card1)
            war=False
        else:
            print('WAR!')
            if len(player1.all_cards)<5:
                print('player 1 has no more carddddd!!\nplayer2 wins')
                gameon=False
                war=False
            elif len(player2.all_cards)<5:
                print('player 2 has no more carddddd!!\nplayer1 wins')
                gameon=False
                war=False
            else:
                for num in range(5):
                    card1.append(player1.removecard())
                    card2.append(player2.removecard())


































