import random
class Card():
    suit_names = ['Clubs','Diamonds','Hearts','Spades']
    rank_names = [None, 'Ace', '2','3','4', '5','6', '7', '8','9','10','Joker','Queen','King' ]
    
    
    def __str__(self):
        return '%.1s of %.10s' % (Card.rank_names[self.suit], Card.suit_names[self.suit])


class Deck():
    def __init__(self):
        self.cards = []
        for suit in range[4]:
            for rank in range (1,14):
                card = Card (suit, rank)
                self.cards.append(card)
    
    def __str__(self):
        res =[]
        for card in self.cards :
            res.append(str(card))
        return '\n'.join(res)

    #remove the card from the deck and return it 
    def pop_card(self, card):
        return self.cards.pop()


    def add_card(self, card):
        self.cards.append(card)

    def shuffle (self, card):
        random.shuffle(self.cards)

    def move_card(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())


class Hand (Deck):
    def __init__(self, label = ''):
        self.cards = []
        self.label = label



deck = Deck()
print(deck)

# card1=Card()
# card1.suit=3
# card1.rank=2
# print(card1)

    

    

    


