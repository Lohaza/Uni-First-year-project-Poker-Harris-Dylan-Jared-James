import pygame
import random

"""
I have created 2 tuples, tuples are non mutable lists which means that they can NOT change at run time.
They also take up less storage than a list as they have a set area in memory and not just linking to free space slots in memory.
The reason I made tuples was due to the fact that the cards will never change in a game of poker. They will always be 4 suits of 13 cards
which make up 52 cards in total. This allows me to copy these tuples into a list when playing so that when a card is drawn it is removed from
that list instead of the tuple which allows for the palyer wanting to start a new game but dosn't want to refresh the code when simulating
the game the code will create a fresh new list for them each game from these 2 tuples.

"""

numcardtuple = ('Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King')
suitcardtuple=('Diamond','Hearts','clubs','spades')

#The use of abstraction could have been used here as we could shorten down long words like Diamond into the letter 'D' instead but this may confuse people later on and we want the game to be as clear as possible.

def Probability():
    None

def draw_hand(numcardtuple,suitcardtuple):
    current_card_list=card_list(numcardtuple,suitcardtuple)
    draw_card_one=random.choice(current_card_list)
    current_card_list.remove(draw_card_one)
    draw_card_two=random.choice(current_card_list)
    current_card_list.remove(draw_card_two)
    return draw_card_one,draw_card_two

    

def card_list(numcardtuple,suitcardtuple):
    """
    This function will take the two tuples of the suits and the card numbers to generate a 2 dimentional list.
    
    """
    rows, column = 52 , 2
    cardlist=[[0 for x in range(column)] for y in range(rows)]

    position=0
    for current_suit in suitcardtuple:
        for x in range(len(numcardtuple)):
            position+=1
            cardlist[position-1][1]= current_suit
            

    for current_num in numcardtuple:
        for rep_num in range(4):
            for y in range(rows):
                index_value_current_num=numcardtuple.index(current_num)
                cardlist[index_value_current_num+(13*rep_num)][0]=current_num
    return cardlist

draw_hand(numcardtuple,suitcardtuple)

def simulation():
    pygame.init()

    # CREATING CANVAS
    canvas = pygame.display.set_mode((1280, 720))

    # TITLE OF CANVAS
    pygame.display.set_caption("poker Simulation")
    exit = False

    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
        pygame.display.update()

simulation()
