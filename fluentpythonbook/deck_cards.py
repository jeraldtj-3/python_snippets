import collections
Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck:
    ranks = [str(i) for i in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split() 

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks] 
    
    def __len__(self):
        return len(self._cards) 
    def __getitem__(self,position):
        return self._cards[position]

deck = FrenchDeck()
# len(deck)

beer_card = Card('3','diamonds');
# picking a random card : python already has a function to get a random item from a sequence; random.choice 
from random import choice 
random_card = choice(deck); 

# if the collection has no __contain__ method, the in operator does a sequential scan.
# So, in operator words with FrenchDeck class because it is iterable. 

Card('Q','hearts') in deck;
# sorting 
suit_values = dict(spades = 3,hearts = 2, diamonds = 1,clubs = 0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank) 
    return rank_value*len(suit_values) + suit_values[card.suit] 

# getting sorted cards based on the key spades_high 
for card in sorted(deck,key = spades_high):
    print(card) 

'''
Although FrenchDeck implicitly inherits from object, its functionality 
is not inherited but comes from leveraging the data model and composition.
By implementing the special methods __len__ and __getitem__  our FrenchDeck 
behaves like a standard python sequence, allowing it to benefit from core 
language features - like iteration and slicing and using functionalities 
from the standard libraries ( sorted, reversed, random.choice ...) 
'''
from math import hypot 
class Vector: 
    def __init__(self,x = 0, y = 0):
        self.x = x 
        self.y = y 
    def __repr__(self):
        return f'Vector({self.x},{self.y})'
    def __abs__(self):
        return hypot(self.x,self.y) 
#     def __bool__(self):
#         return bool(abs(self))
    def __add__(self,other):
        x = self.x + other.x 
        y = self.y + other.y 
        return Vector(x,y) 
    def __mul__(self,scalar):
        return Vector(self.x*scalar, self.y * scalar)
    # a faster implementation of vector._bool__ is ; 
    def __bool__(self):
        return bool(self.x or self.y) 

v1 = Vector(2,4) 
v2 = Vector(2,1)

'''
* The __rep__ special method is called by the repr built-in to get string
 representationof the object for inspection. If we did not implement __rep__,
 vector instances wouldbe shown in the console like <Vector object at 0x10e100070>
 '''

