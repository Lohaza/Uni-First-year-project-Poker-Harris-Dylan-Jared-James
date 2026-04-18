import pygame
import random
import math
import itertools
import collections



def card_list():
    """
    This function will take the two tuples of the suits and the card numbers to generate a 2 dimentional list.

    Paremeters: None.

    I have created 2 tuples, tuples are non mutable lists which means that they can NOT change at run time.
    They also take up less storage than a list as they have a set area in memory and not just linking to free space slots in memory.
    The reason I made tuples was due to the fact that the cards will never change in a game of poker. They will always be 4 suits of 13 cards
    which make up 52 cards in total. This allows me to copy these tuples into a list when playing so that when a card is drawn it is removed from
    that list instead of the tuple which allows for the palyer wanting to start a new game but dosn't want to refresh the code when simulating
    the game the code will create a fresh new list for them each game from these 2 tuples.

    
    """
def card_list():

    numcardtuple = (2,3,4,5,6,7,8,9,10,11,12,13,14)
    suitcardtuple = ('diamonds','hearts','clubs','spades')

    cardlist = []

    for suit in suitcardtuple:
        for num in numcardtuple:
            cardlist.append([num, suit])

    return cardlist

def probability(rankings,deck_size):
    rankings_list = list(rankings.items())
    for rank in rankings_list:
        print(rank)
        index_rank=rankings_list.index(rank)
        new_probability_rank= rank[1]/deck_size
        rankings_list[index_rank] = new_probability_rank
    print(rankings_list)
    return rankings_list


def hand_checker_for_hole_cards(card_1 , card_2 , suit_card_1 , suit_card_2):
    """
    This function will evaluate the parameters of card_1, card_2, suit_card_1 and suit_card_2. 
    After evaluating these parameters, it will give an output of the potential different hand(s) you could get from those parameters.
    These cards are a representation of the first two cards you will receive whilst playing the Poker game, Texas Hold'em. 
    These cards are known by the name, Hole cards.

    For example: 
    
    If the first two cards are a 10 of Hearts and a King of Hearts, this would give the possibility of the potential hand; Royal Flush.
    
    Parameters:
    card_1: Key-value pair, of which is part of the Dictionary literal.
    card_2: Key-value pair, of which is part of the Dictionary literal.
    suit_card_1: Element of the set.
    suit_card_2: Element of the set.

    Remark: The Dictionary literal used is {'1' : 1 , '2' : 2 , '3' : 3 , '4' : 4 , '5' : 5 , '6' : 6 ,
            '7' : 7 , '8' : 8 , '9' : 9 , '10' : 10 , 'J' : 11 , 'Q' : 12 , 'K' : 13 , 'A' : 14}.
            The set used is { 'D' , 'H' , 'S' , 'C' }.

    Returns:
    After correctly inputting the parameters, you will receive one two options for an output.
    You will either receive a string literal argument that tells you the different potential hand(s) you could form,
    or you will receive another string literal argument that tells you that there is no good indication of potential hand(s).
    """

    suits = { 'D' , 'H' , 'S' , 'C' }
    ranks = { '1' : 1 , '2' : 2 , '3' : 3 ,
         '4' : 4 , '5' : 5 , '6' : 6 ,
         '7' : 7 , '8' : 8 , '9' : 9 ,
         '10' : 10 , 'J' : 11 , 'Q' : 12 ,
         'K' : 13 , 'A' : 14}
    
    print('Potential hand(s):')
    value_card_1 = ranks[card_1]
    value_card_2 = ranks[card_2]
    total_value = value_card_1 + value_card_2
    difference = abs(value_card_1 - value_card_2)
    
    if total_value >= 20 and suit_card_1 == suit_card_2:
        print('Royal Flush')
    
    if value_card_1 == 14 and value_card_2 <= 5 and suit_card_1 == suit_card_2:
        print('Straight Flush')
        
    elif value_card_2 == 14 and value_card_1 <= 5 and suit_card_1 == suit_card_2:
        print('Straight Flush')

    elif difference < 5 and suit_card_1 == suit_card_2:
        print('Straight Flush')
              

    if card_1 == card_2:
        print('Four of a kind')
        print('Full House')
        print('Flush')
        print('Three of a kind')
        print('Two Pair')
        print('Pair')
        
    if value_card_1 == 14 and value_card_2 <= 5:
        print('Straight')
        
    elif value_card_2 == 14 and value_card_1 <= 5:
        print('Straight')

    elif difference < 5:
        print('Straight')

    if card_1 == card_1 or card_2 == card_2:
        print('Four of a kind')
        print('Three of a kind')
        print('Two Pair')
        print('Pair')

    else: 
        print('No good indication of potential hands') 


    

def hand_checker_for_hole_and_flop_cards(card_1 , card_2 , card_3 , card_4 , card_5 , suit_card_1 , suit_card_2 , 
                                         suit_card_3 , suit_card_4 , suit_card_5 ):
    """
    This function will evaluate the parameters card_1, card_2, card_3, card_4, card_5, suit_card_1, suit_card_2,
    suit_card_3, suit_card_4 and suit_card_5.
    After it has evaluated these parameters, it will provide an output of the different potential hand(s) that those given
    parameters could give you. 
    Here, the cards are a representation of the first two cards you receive (known as the Hole cards) and the first three
    community cards you see (known as the Flop cards). Whilst playing the Poker game, Texas Hold'em.

    For example:

    If the Hole cards are a 10 of Diamonds and Jack of Diamonds. Then the Flop cards are a Queen of Diamonds, King of Diamonds
    and a Ace of Diamonds. Then your potential hand would be a Royal Flush. 

    Parameters:
    card_1: Key-value pair, of which is part of the Dictionary literal.
    card_2: Key-value pair, of which is part of the Dictionary literal.
    card_3: Key-value pair, of which is part of the Dictionary literal.
    card_4: Key-value pair, of which is part of the Dictionary literal.
    card_5: Key-value pair, of which is part of the Dictionary literal.
    suit_card_1: Element of the set.
    suit_card_2: Element of the set.
    suit_card_3: Element of the set.
    suit_card_4: Element of the set.
    suit_card_5: Element of the set.

    Remark: The Dictionary literal used is {'1' : 1 , '2' : 2 , '3' : 3 , '4' : 4 , '5' : 5 , '6' : 6 ,
            '7' : 7 , '8' : 8 , '9' : 9 , '10' : 10 , 'J' : 11 , 'Q' : 12 , 'K' : 13 , 'A' : 14}.
            The set used is { 'D' , 'H' , 'S' , 'C' }.

    Returns:
    Once you've correclty inputted your parameters, you will receive one of two possible things.
    You will either receive a string literal argument of which highlights to you the different possible/potential hand(s)
    you could form/have, or another string literal argument emphasising that you do not have any good indication of 
    potential hand(s).
    """

    suits = { 'D' , 'H' , 'S' , 'C' }
    ranks = { '1' : 1 , '2' : 2 , '3' : 3 ,
         '4' : 4 , '5' : 5 , '6' : 6 ,
         '7' : 7 , '8' : 8 , '9' : 9 ,
         '10' : 10 , 'J' : 11 , 'Q' : 12 ,
         'K' : 13 , 'A' : 14}
                                             
    print('Potential hand(s):')

    cards = [(card_1 , suit_card_1) , (card_2 , suit_card_2) , (card_3 , suit_card_3) , (card_4, suit_card_4) , (card_5 , suit_card_5)]
    cards_needed_for_royal_flush = {'10' , 'J' , 'Q' , 'K' , 'A'}
    check_for_royal_flush_in_your_cards = {check_for_royal_flush_in_your_card for check_for_royal_flush_in_your_card, _ in cards}

    if check_for_royal_flush_in_your_cards == cards_needed_for_royal_flush and suit_card_1 == suit_card_2 == suit_card_3 == suit_card_4 == suit_card_5:
        print('Royal Flush')
        return

    my_hole_and_flop_cards = [card_1 , card_2 , card_3 , card_4 , card_5]
    my_hole_and_flop_cards_values = sorted(ranks[c] for c in my_hole_and_flop_cards)
    difference = max(my_hole_and_flop_cards_values) - min(my_hole_and_flop_cards_values)

    a_straight = False
    a_flush = suit_card_1 == suit_card_2 == suit_card_3 == suit_card_4 == suit_card_5
    
    if  difference == 4 and len(set(my_hole_and_flop_cards_values)) == 5:
        a_straight = True  

    elif set(my_hole_and_flop_cards_values) == {14, 2 , 3 , 4 , 5}:
        a_straight = True

    if a_straight and a_flush:
        print('Straight Flush')
        return
        
    if a_straight:
        print('Straight')
        return
        
    for rank in my_hole_and_flop_cards:
        if my_hole_and_flop_cards.count(rank) == 4:
            print('Four of a kind')
            return

    the_counts = [my_hole_and_flop_cards.count(card) for card in set(my_hole_and_flop_cards)]

    if 3 in the_counts and 2 in the_counts:
        print('Full House')
        return

    if  suit_card_1 == suit_card_2 == suit_card_3 == suit_card_4 == suit_card_5:
        print('Flush')
        return

    for rank in my_hole_and_flop_cards:
        if my_hole_and_flop_cards.count(rank) == 3:
            print('Three of a kind')
            return

    if the_counts.count(2) == 2:
        print('Two Pair')
        return

    for rank in my_hole_and_flop_cards: 
        if my_hole_and_flop_cards.count(rank) == 2:
            print('Pair')
            return
    else: 
        print('No good indication of potential hands') 



def probabililty_high_card():
    """
    ** I am still working on this area of code **
    This code will provide the probability of getting a high card when all the cards that we will be recieving are still unkown to us.

    Paremeters: None.

    I don't really understand the maths here I know why we divide by the total and so on but I don't know how we get the total combinations of high cards.
    If someone could do more research on this an input it into this docstring it would be most apprecaited.
    
    
    
    """
    total_combinations_of_hand_of_seven_cards=math.comb(52,7)
    total_combinations_of_high_card= (1499*(((4)**7)+(-756)+(-4)+(-84)))
    probability_high_card_variable=total_combinations_of_high_card / total_combinations_of_hand_of_seven_cards
    return probability_high_card_variable



def probability_one_pair():

    """
    ** I am still working on this area of code **
    This code will provide the probability of getting a single pair card when all the cards that we will be recieving are still unkown to us.

    Paremeters: None.

    I don't really understand the maths here I know why we divide by the total and so on but I don't know how we get the total combinations of high cards.
    If someone could do more research on this an input it into this docstring it would be most apprecaited.
    
    
    
    """
    total_combinations_of_hand_of_seven_cards=math.comb(52,7)
    total_combinations_of_one_pair=((math.comb(13,6))-71) *6 *6 *990
    probability_one_pair_variable=total_combinations_of_one_pair / total_combinations_of_hand_of_seven_cards
    return probability_one_pair_variable


def probability_two_pair():

    """
    ** I am still working on this area of code **
    This code will provide the probability of getting a two pair when all the cards that we will be recieving are still unkown to us.

    Paremeters: None.

    I don't really understand the maths here I know why we divide by the total and so on but I don't know how we get the total combinations of high cards.
    If someone could do more research on this an input it into this docstring it would be most apprecaited.
    
    
    
    """
        
    total_combinations_of_hand_of_seven_cards=math.comb(52,7)
    total_combinations_of_two_pair= (1277*10*((6*62)+(24*63)+(6*64))+((math.comb(13,3))*((math.comb(4,2))**3)*(math.comb(40,1))))
    probability_two_pair_variable=total_combinations_of_two_pair / total_combinations_of_hand_of_seven_cards
    return probability_two_pair_variable




def probability_three_of_a_kind():

    """
    ** I am still working on this area of code **
    This code will provide the probability of getting a three of a kind when all the cards that we will be recieving are still unkown to us.

    Paremeters: None.

    I don't really understand the maths here I know why we divide by the total and so on but I don't know how we get the total combinations of high cards.
    If someone could do more research on this an input it into this docstring it would be most apprecaited.
    
    
    
    """
        
    total_combinations_of_hand_of_seven_cards=math.comb(52,7)
    total_combinations_three_of_a_kind= ((math.comb(13,5)-10)*(math.comb(5,1))*(math.comb(4,1))*((math.comb(4,1)**4)-3))
    probability_three_of_a_kind_variable=total_combinations_three_of_a_kind / total_combinations_of_hand_of_seven_cards
    return probability_three_of_a_kind_variable


def probability_straight():
    """
    ** I am still working on this area of code **
    This code will provide the probability of getting a straight when all the cards that we will be recieving are still unkown to us.

    Paremeters: None.

    I don't really understand the maths here I know why we divide by the total and so on but I don't know how we get the total combinations of high cards.
    If someone could do more research on this an input it into this docstring it would be most apprecaited.
    
    """

    total_combinations_of_hand_of_seven_cards=math.comb(52,7)
    total_combinations_straight= (217*(((4)**7)+(-756)+(-4)+(-84)))+((71)*(36)*(990))+(((10)*(5)*(4)*((256)-(3)))+(10)*(math.comb(5,2))*(2268))
    probability_straight_variable=total_combinations_straight / total_combinations_of_hand_of_seven_cards
    return probability_straight_variable


def probability_flush():
    """
    ** I am still working on this area of code **
    This code will provide the probability of getting a flush when all the cards that we will be recieving are still unkown to us.

    Paremeters: None.

    I don't really understand the maths here I know why we divide by the total and so on but I don't know how we get the total combinations of high cards.
    If someone could do more research on this an input it into this docstring it would be most apprecaited.
    
    """

    total_combinations_of_hand_of_seven_cards=math.comb(52,7)
    total_combinations_flush= ((math.comb(4,1))*(((math.comb(13,7)))-(217)))+((math.comb(4,1))*(((math.comb(13,6)))-(71))*(39))+((math.comb(4,1))*(((math.comb(13,5)))-(10))*(math.comb(39,2)))
    probability_flush_variable=total_combinations_flush / total_combinations_of_hand_of_seven_cards
    return probability_flush_variable


def probability_full_house():
    """
    ** I am still working on this area of code **
    This code will provide the probability of getting a full house when all the cards that we will be recieving are still unkown to us.

    Paremeters: None.

    I don't really understand the maths here I know why we divide by the total and so on but I don't know how we get the total combinations of high cards.
    If someone could do more research on this an input it into this docstring it would be most apprecaited.
    
    """

    total_combinations_of_hand_of_seven_cards=math.comb(52,7)
    total_combinations_full_house= ((math.comb(13,2))*((math.comb(4,3))**2)*(math.comb(44,1)))+((math.comb(13,1))*(math.comb(12,2))*(math.comb(4,3))*((math.comb(4,2))**2))+((math.comb(13,1))*(math.comb(12,1))*(math.comb(11,2))*(math.comb(4,3))*(math.comb(4,2))*((math.comb(4,1))**2))
    probability_full_house_variable=total_combinations_full_house / total_combinations_of_hand_of_seven_cards
    return probability_full_house_variable


def probability_four_of_a_kind():
    """
    ** I am still working on this area of code **
    This code will provide the probability of getting a four of a kind when all the cards that we will be recieving are still unkown to us.

    Paremeters: None.

    I don't really understand the maths here I know why we divide by the total and so on but I don't know how we get the total combinations of high cards.
    If someone could do more research on this an input it into this docstring it would be most apprecaited.
    
    """

    total_combinations_of_hand_of_seven_cards=math.comb(52,7)
    total_combinations_four_of_a_kind= (math.comb(13,1))*(math.comb(48,3))
    probability_four_of_a_kind_variable=total_combinations_four_of_a_kind / total_combinations_of_hand_of_seven_cards
    return probability_four_of_a_kind_variable


def probability_straight_flush():
    """
    ** I am still working on this area of code **
    This code will provide the probability of getting a straight flush when all the cards that we will be recieving are still unkown to us.

    Paremeters: None.

    I don't really understand the maths here I know why we divide by the total and so on but I don't know how we get the total combinations of high cards.
    If someone could do more research on this an input it into this docstring it would be most apprecaited.
    
    """

    total_combinations_of_hand_of_seven_cards=math.comb(52,7)
    total_combinations_straight_flush= (math.comb(9,1))*(math.comb(4,1))*(math.comb(46,2))
    probability_straight_flush_variable=total_combinations_straight_flush / total_combinations_of_hand_of_seven_cards
    return probability_straight_flush_variable


def probability_royal_flush():
    """
    ** I am still working on this area of code **
    This code will provide the probability of getting a royal flush when all the cards that we will be recieving are still unkown to us.

    Paremeters: None.

    I don't really understand the maths here I know why we divide by the total and so on but I don't know how we get the total combinations of high cards.
    If someone could do more research on this an input it into this docstring it would be most apprecaited.
    
    """

    total_combinations_of_hand_of_seven_cards=math.comb(52,7)
    total_combinations_royal_flush= (4)*(math.comb(47,2))
    probability_royal_flush_variable=total_combinations_royal_flush / total_combinations_of_hand_of_seven_cards
    return probability_royal_flush_variable





def flush_structure(cards):
    suits = [c[1] for c in cards]
    return len(set(suits)) == 1


def one_pair_structure(cards):
    ranks = [c[0] for c in cards]
    counts = collections.Counter(ranks)
    return list(counts.values()).count(2) == 1



def two_pair_structure(cards):
    ranks = [c[0] for c in cards]
    return list(collections.Counter(ranks).values()).count(2) == 2


def three_of_a_kind_structure(cards):
    return 3 in collections.Counter([c[0] for c in cards]).values()


def four_of_a_kind_structure(cards):
    return 4 in collections.Counter([c[0] for c in cards]).values()

def full_house_structure(cards):
    counts = collections.Counter([c[0] for c in cards]).values()
    return sorted(counts) == [2,3]



def straight_structure(cards):

    if isinstance(cards[0][0], list):
        cards = [c[0] for c in cards]

    ranks = [c[0] if isinstance(c, list) else c for c in cards]
    ranks = sorted(set(ranks))

    for i in range(len(ranks) - 4):
        if all(ranks[i + j] == ranks[i] + j for j in range(5)):
            return True

    return set([14,2,3,4,5]).issubset(ranks)




def evaluate_all_known_cards(known_cards):
    
    deck = card_list()
    deck = [card for card in deck if card not in known_cards]

    unknown_count = 7 - len(known_cards)

    rankings = {
        "one_pair": 0,
        "two_pair": 0,
        "three_of_a_kind": 0,
        "straight": 0,
        "flush": 0,
        "full_house": 0,
        "four_of_a_kind": 0,
        "straight_flush": 0,
        "royal_flush": 0
    }

    for combo in itertools.combinations(deck, unknown_count):

        seven_cards = list(known_cards) + list(combo)

        rank = best_rank(seven_cards)

        if rank:
            rankings[rank] += 1

    total = math.comb(len(deck), unknown_count)

    return rankings, total






def best_rank(seven_cards):
    


    rank_value = {
     "straight_flush": 8,
        "four_of_a_kind": 7,
        "full_house": 6,
        "flush": 5,
        "straight": 4,
        "three_of_a_kind": 3,
        "two_pair": 2,
        "one_pair": 1,
        None: 0
    }

    best = None

    for five_cards in itertools.combinations(seven_cards, 5):

        suits = [c[1] for c in five_cards]
        nums = [c[0] for c in five_cards]

        is_flush = flush_structure(five_cards)
        is_straight = straight_structure(five_cards)
        is_four = four_of_a_kind_structure(five_cards)
        is_full = full_house_structure(five_cards)
        is_three = three_of_a_kind_structure(five_cards)
        is_two_pair = two_pair_structure(five_cards)
        is_pair = one_pair_structure(five_cards)

        if is_straight and is_flush:
            current = "straight_flush"
        elif is_four:
            current = "four_of_a_kind"
        elif is_full:
            current = "full_house"
        elif is_flush:
            current = "flush"
        elif is_straight:
            current = "straight"
        elif is_three:
            current = "three_of_a_kind"
        elif is_two_pair:
            current = "two_pair"
        elif is_pair:
            current = "one_pair"
        else:
            current = None

        if best is None or rank_value[current] > rank_value[best]:
            best = current

            # early exit (can't beat straight flush)
            if best == "straight_flush":
                return best

    return best




def draw_hand():
    """
    Using the list creation function 'card_list'. This will generate 2 cards at random from the list, remove those cards from the current list, return both the cards and the current list back to the use for further use.
    
    paremters: None.
    
    """

    current_card_list=card_list()
    draw_card_one=random.choice(current_card_list)
    current_card_list.remove(draw_card_one)
    draw_card_two=random.choice(current_card_list)
    current_card_list.remove(draw_card_two)
    return draw_card_one,draw_card_two, current_card_list
    




card_one=[14 ,'hearts']
card_two=[2,'spades']
card_three=[6,'hearts']
card_four=[8,'spades']

print(evaluate_all_known_cards([card_one , card_two , card_three , card_four]))




def simulation():
    """
    This funcrtion is the main simulation of the game. We can take this as an unbias non scued estimator on how our texas holdem probability counter puts up in a real world
    experience. 
    
    """
    menu=True
    pygame.init()
    canvas = pygame.display.set_mode((1280, 720))

    pygame.display.set_caption("poker Simulation")
    exit = False



    pygame.display.flip()
    

    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
        if menu == True:
            mouse=pygame.mouse.get_pos()

            background_home_color=(0, 100, 0)
            black=(0,0,0)
            white=(255,255,255)
            Font_home=pygame.font.SysFont('Arial.ttf',50)
            Font_home_title=pygame.font.SysFont('Arial.ttf',300)
            canvas.fill(background_home_color)

            title_Home_text=Font_home_title.render('Poker', True, black)
            title_Home_text_rectangle = title_Home_text.get_rect()
            title_Home_text_rectangle.center = (665,150)
            canvas.blit(title_Home_text,title_Home_text_rectangle)


            sim_text=Font_home.render('Simulator', True, black)
            sim_text_rectangle = sim_text.get_rect()
            sim_text_rectangle.center = (80,25)
            canvas.blit(sim_text,sim_text_rectangle)
            if 565 <= mouse[0] <= 765 and 300 <= mouse[1] <= 400 :
                button_Play_outline=pygame.draw.rect(surface=canvas,color=white,rect=[565,300,200,100])
                button_Play_background=pygame.draw.rect(surface=canvas,color=black,rect=[570,305,190,90])
                button_Play_text=Font_home.render('Play', True, white)
                button_Play_text_rectangle = button_Play_text.get_rect()
                button_Play_text_rectangle.center = (665,350)
                canvas.blit(button_Play_text,button_Play_text_rectangle)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    menu=False
                    Play=True
            else:
                button_Play_outline=pygame.draw.rect(surface=canvas,color=black,rect=[565,300,200,100])
                button_Play_background=pygame.draw.rect(surface=canvas,color=white,rect=[570,305,190,90])
                button_Play_text=Font_home.render('Play', True, black)
                button_Play_text_rectangle = button_Play_text.get_rect()
                button_Play_text_rectangle.center = (665,350)
                canvas.blit(button_Play_text,button_Play_text_rectangle)
            
            if 565 <= mouse[0] <= 765 and 450 <= mouse[1] <= 550 : 
                button_settings_outline=pygame.draw.rect(surface=canvas,color=white,rect=[565,450,200,100])
                button_settings_background=pygame.draw.rect(surface=canvas,color=black,rect=[570,455,190,90])
                button_Settings_text=Font_home.render('Settings', True, white)
                button_Settings_text_rectangle = button_Settings_text.get_rect()
                button_Settings_text_rectangle.center = (665,500)
                canvas.blit(button_Settings_text,button_Settings_text_rectangle)
            else:
                button_settings_outline=pygame.draw.rect(surface=canvas,color=black,rect=[565,450,200,100])
                button_settings_background=pygame.draw.rect(surface=canvas,color=white,rect=[570,455,190,90])
                button_Settings_text=Font_home.render('Settings', True, black)
                button_Settings_text_rectangle = button_Settings_text.get_rect()
                button_Settings_text_rectangle.center = (665,500)
                canvas.blit(button_Settings_text,button_Settings_text_rectangle)


            if 565 <= mouse[0] <= 765 and 600 <= mouse[1] <= 750 :
                button_quit_outline=pygame.draw.rect(surface=canvas,color=white,rect=[565,600,200,100])
                button_quit_background=pygame.draw.rect(surface=canvas,color=black,rect=[570,605,190,90])
                button_Quit_text=Font_home.render('Quit', True, white)
                button_Quit_text_rectangle = button_Quit_text.get_rect()
                button_Quit_text_rectangle.center = (665,650)
                canvas.blit(button_Quit_text,button_Quit_text_rectangle)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    exit=True
            else:
                button_quit_outline=pygame.draw.rect(surface=canvas,color=black,rect=[565,600,200,100])
                button_quit_background=pygame.draw.rect(surface=canvas,color=white,rect=[570,605,190,90])
                button_Quit_text=Font_home.render('Quit', True, black)
                button_Quit_text_rectangle = button_Quit_text.get_rect()
                button_Quit_text_rectangle.center = (665,650)
                canvas.blit(button_Quit_text,button_Quit_text_rectangle)
        elif Play == True:
            canvas.fill(white)
            



        pygame.display.update()
simulation()
