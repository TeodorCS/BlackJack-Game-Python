import random

suits=('Inima Rosie','Romb','Inima Neagra','Trefla')
ranks=('As','Doi','Trei','Patru','Cinci','Sase','Sapte','Opt','Noua','Zece','Valet','Dama','Rege')
values={'Doi':2 ,'Trei':3, 'Patru':4 ,'Cinci':5 ,'Sase':6,'Sapte':7, 'Opt':8 ,'Noua':9 , 'Zece':10, 'Valet':10, 'Dama':10, 'Rege':10,'As':11}

playing =True

class Card :
    def __init__(self,suits,rank ):
        self.suits=suits
        self.rank=rank

    def __str__ (self):
        return self.rank + " de " + self.suits
           

class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def shuffle (self):
        random.shuffle(self.deck)

    def deal (self):
        return self.deck.pop()
        
class Hand :

    def __init__(self):
        self.cards = []
        self.value=0
        self.aces=0

    def restart(self):
        self.cards=[]
        self.value=0

    def add_card(self,card):

        self.cards.append(card)
        self.value =self.value + values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_aces(self):
        while self.value>21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

class Chips:
    total=0

    def __init__(self):
        self.bet=0

    def ask_money(self):
        self.total=int (input('Cate monezi vreti sa adaugati in joc? '))

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet






def take_bet(chips):

    while True:
        
        try :
            print('Ai un total de {} monezi'.format(player_chips.total))
            chips.bet=int(input("Cate monezi vrei sa pariezi? : "))
            print('\n')
        
        except: 
            print("Scuze! Trebuie sa introduci un numar ! ")

        else:
            if chips.bet > chips.total:
                print("Scuze ! Nu ai indeajuns de multe monezi ! Totalul tau este de {} de monezi ".format(chips.total))
            else: break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_aces()


def hit_or_stand(deck, hand):

    global playing
    OK=True

    while OK:
        print('\n')
        x= input('Hit sau Stand? Introduce h sau s: ')
        print('\n')
        if player_hand.value > 21 :
            break
        if x[0].lower() == 'h':
            hit(deck,hand)            
            player_hand.adjust_for_aces()
            show_some(player_hand,dealer_hand)                        
        elif x[0].lower() == 's':
            print("Ai ales Stands , Randul Dealerului ")
            playing = False
            OK=False
        else: 
            print("Scuze , nu ma inteles comanda ! Te rog sa introduci doar h sau s ! ")        

def show_some(player,dealer):
    
    print('\nCartile pe care le are Dealerul: ')
    print('\nCartea ascunsa !')
    print(dealer.cards[1])
    print('\n')
    print('Mana ta:\n')
    for card in player.cards:
        print(card)


def show_all(player,dealer):
    print('\nMana Dealerului')
    for card in dealer.cards:
        print(card)
    print('\n')
    print('Mana ta:')
    for card in player.cards:
        print(card)


def player_busts(player, dealer, chips):
    print('\nAI PIERDUT! ')
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print('\nAI CASTIGAT! ')
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print('\nAI CASTIGAT! DEALERUL PIERDE')
    chips.win_bet()

def dealer_wins (player, dealer, chips):
    print('\nAI PIERDUT! DEALERUL CASTIGA')
    chips.lose_bet()

def push(player, dealer):
    print('\nEgalitate intre Jucator si Dealer ! PUSH')



while True:

     print('\nBun venit la BlackJack!')

     deck=Deck()
     deck.shuffle()

     player_hand=Hand()
     player_hand.add_card(deck.deal())
     player_hand.add_card(deck.deal())
     dealer_hand = Hand()
     dealer_hand.add_card(deck.deal())
     dealer_hand.add_card(deck.deal())

     player_chips=Chips()
     player_chips.ask_money()
     take_bet(player_chips)

     show_some(player_hand,dealer_hand)

     while playing:

        hit_or_stand(deck,player_hand)
        
        if player_hand.value > 21 :
            player_busts(player_hand,dealer_hand,player_chips)
            show_all(player_hand,dealer_hand)
            
        if player_hand.value <= 21:
            
            while dealer_hand.value < player_hand.value :
                dealer_hand.add_card(deck.deal())
                hit(deck, dealer_hand )
            
            show_all(player_hand,dealer_hand)

            if dealer_hand.value > 21 :
                dealer_busts(player_hand,dealer_hand,player_chips)
            elif dealer_hand.value > player_hand.value and dealer_hand.value < 21:
                dealer_wins(player_hand,dealer_hand,player_chips)
            elif dealer_hand.value < player_hand.value and player_hand.value < 21  :
                player_wins(player_hand,dealer_hand,player_chips)
            elif player_hand.value == dealer_hand.value:
                push(player_hand,dealer_hand)

        print('\nTotalul tau este de {} de monezi'.format(player_chips.total))
        
        new_game= input("Daca vreti sa mai jucati inca o mana introduceti 'y'!\nDaca vreti sa parasesti jocul introduceti orice tasta : ")
        
        if new_game[0].lower() == 'y':
            playing=True
            player_hand.restart()
            dealer_hand.restart()
            deck.shuffle()
            if player_chips.total <= 0:
                print("Nu aveti fonturi suficiente!!")
                player_chips.ask_money()
            take_bet(player_chips)
            player_hand.add_card(deck.deal())
            player_hand.add_card(deck.deal())
            dealer_hand.add_card(deck.deal())
            dealer_hand.add_card(deck.deal())
            show_some(player_hand,dealer_hand)
            continue
        else :
            print('\nMultumesc ca ai jucat BlackJack! Ai castigat un total de {}'.format(player_chips.total))
            exit()
