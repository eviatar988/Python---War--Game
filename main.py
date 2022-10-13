# In this project I used the udemy website, course:Complete-Python-3-Bootcamp-master
# Enjoy th WAR game !
# Eviatar Cohen

import random

suits=('Hearts','Clubs','Diamonds','Spades')

ranks=('One','Two' ,'Three', 'Four', 'Five', 'Six','Seven','Eight','Nine','Ten','Jack','Qeen','King','Ace')

values={'One':1, 'Two':2 ,'Three':3, 'Four':4, 'Five':5, 'Six':6 ,'Seven':7,
        'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Qeen':12,'King':13,'Ace':14}


class Card:

    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self):
       return self.rank + ' of ' + self.suit

class Deck:

    def __init__(self):

        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                created_card=Card(suit,rank)

                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player():

     def __init__(self, name):
         self.name=name
         self.all_cards=[]

     def remove_one(self):
         return self.all_cards.pop(0)

     def add_cards(self,new_cards):
         if type(new_cards)==type([]): #for multiple cards
             self.all_cards.extend(new_cards)
         else: #for single cards
             self.all_cards.append(new_cards)

     def __str__(self):
         return f' Player {self.name} has {len(self.all_cards)} cards'



#GAME_SETUP
player1 = Player('One')
player2 = Player('Two')
new_deck = Deck()
new_deck.shuffle()

#Cards Dealing
for card in range(28):
    player1.add_cards(new_deck.deal_one())
    player2.add_cards(new_deck.deal_one())



game_on=True
game_round=0

while game_on:
    game_round +=1


    if len(player1.all_cards) == 0:
        print('Player1 out of cards,  Player2 Win!')
        game_on=False
        break
    elif len(player2.all_cards) == 0:
        print('Player2 out of cards,  Player1 Win!')
        game_on=False
        break


    in_war = True
    while in_war:

        player1_cards1=[]
        player1_cards1.append(player1.remove_one())
        player2_cards2=[]
        player2_cards2.append(player2.remove_one())

        if player1_cards1[-1].value>player2_cards2[-1].value:
            player2_cards2.extend(player1_cards1)
            player1.add_cards(player2_cards2)
            print(f'round {game_round} won: Player1. ----- Player1 remaining cards:{len(player1.all_cards)} , Player2 remaining cards:{len(player2.all_cards)} ')
            in_war=False
        if player2_cards2[-1].value > player1_cards1[-1].value:
            player1_cards1.extend(player2_cards2)
            player2.add_cards(player1_cards1)
            print(f'round {game_round} won: Player2. ----- Player1 remaining cards:{len(player1.all_cards)} , Player2 remaining cards:{len(player2.all_cards)} ')
            in_war = False
        else:
            print('----WAR!-----')
            if len(player1.all_cards)<3:
                print('Player1 has less then 3 cards \n Player2 WIN!')
                game_on = False
                break
            elif len(player2.all_cards)<3:
                print('Player2 has less then 3 cards \n Player1 WIN!')
                game_on = False
                break
            else:

                for i in range(3):
                    player1_cards1.append(player1.remove_one())
                    player2_cards2.append(player2.remove_one())

















