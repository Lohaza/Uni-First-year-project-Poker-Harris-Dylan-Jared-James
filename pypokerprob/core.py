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
    numcardtuple = (2,3,4,5,6,7,8,9,10,11,12,13,14)
    suitcardtuple = ('diamonds','hearts','clubs','spades')
    cardlist = []
    for suit in suitcardtuple:
        for num in numcardtuple:
            cardlist.append([num, suit])

    return cardlist

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
    difference = abs(value_card_1 - value_card_2)
    
    
    if value_card_1 >= 10 and value_card_2 >= 11  and suit_card_1 == suit_card_2:
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
        return 

    if suit_card_1 ==  suit_card_2:
        print('Flush')
        
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



def starting_probabililty_high_card():
    """
    This code will provide the probability of getting a high card when all the cards that we will be recieving are still unkown to us.
    This is when all 7 of the cards are unknow to us but we are wanting a probability counter for the what are the chances of getting this rank.

    Paremeters: None.

    The maths formulas used in this function has been taken from the wiki, although have been coded independently. 
    https://en.wikipedia.org/wiki/Poker_probability
    
    
    """
    total_combinations_of_hand_of_seven_cards=math.comb(52,7)
    total_combinations_of_high_card= (1499*(((4)**7)+(-756)+(-4)+(-84)))
    probability_high_card_variable=total_combinations_of_high_card / total_combinations_of_hand_of_seven_cards
    return probability_high_card_variable



def starting_probability_one_pair():

    """
    This code will provide the probability of getting a single pair card when all the cards that we will be recieving are still unkown to us.
    This is when all 7 of the cards are unknow to us but we are wanting a probability counter for the what are the chances of getting this rank.

    Paremeters: None.

    The maths formulas used in this function has been taken from the wiki, although have been coded independently. 
    https://en.wikipedia.org/wiki/Poker_probability
    
    
    """
    total_combinations_of_hand_of_seven_cards=math.comb(52,7)
    total_combinations_of_one_pair=((math.comb(13,6))-71) *6 *6 *990
    probability_one_pair_variable=total_combinations_of_one_pair / total_combinations_of_hand_of_seven_cards
    return probability_one_pair_variable


def starting_probability_two_pair():

    """
    This code will provide the probability of getting a two pair when all the cards that we will be recieving are still unkown to us.
    This is when all 7 of the cards are unknow to us but we are wanting a probability counter for the what are the chances of getting this rank.

    Paremeters: None.

    The maths formulas used in this function has been taken from the wiki, although have been coded independently. 
    https://en.wikipedia.org/wiki/Poker_probability
    
    
    """
        
    total_combinations_of_hand_of_seven_cards=math.comb(52,7)
    total_combinations_of_two_pair= (1277*10*((6*62)+(24*63)+(6*64))+((math.comb(13,3))*((math.comb(4,2))**3)*(math.comb(40,1))))
    probability_two_pair_variable=total_combinations_of_two_pair / total_combinations_of_hand_of_seven_cards
    return probability_two_pair_variable




def starting_probability_three_of_a_kind():

    """
    This code will provide the probability of getting a three of a kind when all the cards that we will be recieving are still unkown to us.
    This is when all 7 of the cards are unknow to us but we are wanting a probability counter for the what are the chances of getting this rank.

    Paremeters: None.

    The maths formulas used in this function has been taken from the wiki, although have been coded independently.
    https://en.wikipedia.org/wiki/Poker_probability

    """
        
    total_combinations_of_hand_of_seven_cards=math.comb(52,7)
    total_combinations_three_of_a_kind= ((math.comb(13,5)-10)*(math.comb(5,1))*(math.comb(4,1))*((math.comb(4,1)**4)-3))
    probability_three_of_a_kind_variable=total_combinations_three_of_a_kind / total_combinations_of_hand_of_seven_cards
    return probability_three_of_a_kind_variable


def starting_probability_straight():
    """
    This code will provide the probability of getting a straight when all the cards that we will be recieving are still unkown to us.
    This is when all 7 of the cards are unknow to us but we are wanting a probability counter for the what are the chances of getting this rank.

    Paremeters: None.

    The maths formulas used in this function has been taken from the wiki, although have been coded independently. 
    https://en.wikipedia.org/wiki/Poker_probability
    
    """

    total_combinations_of_hand_of_seven_cards=math.comb(52,7)
    total_combinations_straight= (217*(((4)**7)+(-756)+(-4)+(-84)))+((71)*(36)*(990))+(((10)*(5)*(4)*((256)-(3)))+(10)*(math.comb(5,2))*(2268))
    probability_straight_variable=total_combinations_straight / total_combinations_of_hand_of_seven_cards
    return probability_straight_variable


def starting_probability_flush():
    """
    This code will provide the probability of getting a flush when all the cards that we will be recieving are still unkown to us.
    This is when all 7 of the cards are unknow to us but we are wanting a probability counter for the what are the chances of getting this rank.

    Paremeters: None.

    The maths formulas used in this function has been taken from the wiki, although have been coded independently. 
    https://en.wikipedia.org/wiki/Poker_probability
    """

    total_combinations_of_hand_of_seven_cards=math.comb(52,7)
    total_combinations_flush= ((math.comb(4,1))*(((math.comb(13,7)))-(217)))+((math.comb(4,1))*(((math.comb(13,6)))-(71))*(39))+((math.comb(4,1))*(((math.comb(13,5)))-(10))*(math.comb(39,2)))
    probability_flush_variable=total_combinations_flush / total_combinations_of_hand_of_seven_cards
    return probability_flush_variable



def starting_probability_full_house():
    """
    This code will provide the probability of getting a full house when all the cards that we will be recieving are still unkown to us.
    This is when all 7 of the cards are unknow to us but we are wanting a probability counter for the what are the chances of getting this rank.

    Paremeters: None.

    The maths formulas used in this function has been taken from the wiki, although have been coded independently. 
    https://en.wikipedia.org/wiki/Poker_probability
    
    """

    total_combinations_of_hand_of_seven_cards=math.comb(52,7)
    total_combinations_full_house= ((math.comb(13,2))*((math.comb(4,3))**2)*(math.comb(44,1)))+((math.comb(13,1))*(math.comb(12,2))*(math.comb(4,3))*((math.comb(4,2))**2))+((math.comb(13,1))*(math.comb(12,1))*(math.comb(11,2))*(math.comb(4,3))*(math.comb(4,2))*((math.comb(4,1))**2))
    probability_full_house_variable=total_combinations_full_house / total_combinations_of_hand_of_seven_cards
    return probability_full_house_variable


def starting_probability_four_of_a_kind():
    """
    This code will provide the probability of getting a four of a kind when all the cards that we will be recieving are still unkown to us.
    This is when all 7 of the cards are unknow to us but we are wanting a probability counter for the what are the chances of getting this rank.

    Paremeters: None.

    The maths formulas used in this function has been taken from the wiki, although have been coded independently. 
    https://en.wikipedia.org/wiki/Poker_probability
    """

    total_combinations_of_hand_of_seven_cards=math.comb(52,7)
    total_combinations_four_of_a_kind= (math.comb(13,1))*(math.comb(48,3))
    probability_four_of_a_kind_variable=total_combinations_four_of_a_kind / total_combinations_of_hand_of_seven_cards
    return probability_four_of_a_kind_variable


def starting_probability_straight_flush():
    """
    This code will provide the probability of getting a straight flush when all the cards that we will be recieving are still unkown to us.
    This is when all 7 of the cards are unknow to us but we are wanting a probability counter for the what are the chances of getting this rank.

    Paremeters: None.

    The maths formulas used in this function has been taken from the wiki, although have been coded independently. 
    https://en.wikipedia.org/wiki/Poker_probability
    """

    total_combinations_of_hand_of_seven_cards=math.comb(52,7)
    total_combinations_straight_flush= (math.comb(9,1))*(math.comb(4,1))*(math.comb(46,2))
    probability_straight_flush_variable=total_combinations_straight_flush / total_combinations_of_hand_of_seven_cards
    return probability_straight_flush_variable


def starting_probability_royal_flush():
    """
    This code will provide the probability of getting a royal flush when all the cards that we will be recieving are still unkown to us.
    This is when all 7 of the cards are unknow to us but we are wanting a probability counter for the what are the chances of getting this rank.

    Paremeters: None.

    The maths formulas used in this function has been taken from the wiki, although have been coded independently. 
    https://en.wikipedia.org/wiki/Poker_probability
    """

    total_combinations_of_hand_of_seven_cards=math.comb(52,7)
    total_combinations_royal_flush= (4)*(math.comb(47,2))
    probability_royal_flush_variable=total_combinations_royal_flush / total_combinations_of_hand_of_seven_cards
    return probability_royal_flush_variable





def flush_structure(cards):
    """
    simple: This function checks if the hand is a flush and if so it returns True if so.

    This is becausse it checks the second column of the list in which the suits are stored. This is done by extracting the second list item in each card in the hand
    into a brand new list called suits, this is achieved by a count control loop inside a list which allows for the elements in the list to be added by how many cards
    there are. If all the suits are the same then the length of the list would equal 1. 
    
    parameters: The hand of the cards provided in a 2 dimentional list. For example:
                [[5, 'hearts'],[2,'clubs'],[12,'spades']]
                This function takes in 5 cards for a hand.

    """
    suits = [c[1] for c in cards]
    return len(set(suits)) == 1

def one_pair_structure(cards):
    """ 
    simple: This function checks if the hand contains a singular pair and if so it will return True.

    This will create a locally stored list called ranks in which is will append the first column of the cards that have been entered which is the value of the card
    it will then count the frequency of how many times a value comes up. We are then able to see if a value comes up exactly 2 times by using the .count built in python function on the span of the counts.
    We only want one pair so we check if the list is equal to strictly 1.

    parameters: The hand of the cards provided in a 2 dimentional list. For Example:
                [[5, 'hearts'],[2,'clubs'],[12,'spades']]
                This function takes in 7 cards for a hand.

    """
    ranks = [c[0] for c in cards]
    counts = collections.Counter(ranks)
    return list(counts.values()).count(2) == 1



def two_pair_structure(cards):
    """ 
    simple: This function checks if the hand contains a two pairs and if so it will return True.

    This will create a locally stored list called ranks in which is will append the first column of the cards that have been entered which is the value of the card
    it will then count the frequency of how many times a value comes up. We are then able to see if a value comes up exactly 2 times by using the .count built in python function on the span of the counts.
    We only want two pair so we check if the list is equal to strictly 2.

    parameters: The hand of the cards provided in a 2 dimentional list. For Example:
                [[5, 'hearts'],[2,'clubs'],[12,'spades']]
                This function takes in 7 cards for a hand.

    """
    ranks = [c[0] for c in cards]
    return list(collections.Counter(ranks).values()).count(2) == 2


def three_of_a_kind_structure(cards):
    """
    simply: This function checks if the hand contains a three identical cards and if so it will return True.

    This will create a locally stored list called ranks in which is will append the first column of the cards that have been entered which is the value of the card
    it will then count the frequency of how many times a value comes up. if it comes up 3 times it will return True.

    parameters: The hand of the cards provided in a 2 dimentional list. For Example:
                [[5, 'hearts'],[2,'clubs'],[12,'spades']]
                This function takes in 7 cards for a hand.
    """
    return 3 in collections.Counter([c[0] for c in cards]).values()


def four_of_a_kind_structure(cards):
    """
    simply: This function checks if the hand contains a four identical cards and if so it will return True.

    This will create a locally stored list called ranks in which is will append the first column of the cards that have been entered which is the value of the card
    it will then count the frequency of how many times a value comes up. if it comes up 4 times it will return True.

    parameters: The hand of the cards provided in a 2 dimentional list. For Example:
                [[5, 'hearts'],[2,'clubs'],[12,'spades']]
                This function takes in 7 cards for a hand.
    """
    return 4 in collections.Counter([c[0] for c in cards]).values()

def full_house_structure(cards):
    """
    simply:  This function will check if the hand contains both 3 identical cards and 2 other identical cards.

    This will create a locally stored list called ranks in which is will append the first column of the cards that have been entered which is the value of the card
    it will then count the frequency of how many times a value comes up which will be stored in a list called counts. It will then check if the first item in the list is 2 and the second is 3 as the list will be
    ordered it will always following in that way using the keyword sorted.

    parameters: The hand of the cards provided in a 2 dimentional list. For Example:
                [[5, 'hearts'],[2,'clubs'],[12,'spades']]
                This function takes in 7 cards for a hand.

    """
    counts = collections.Counter([c[0] for c in cards]).values()
    return sorted(counts) == [2,3]



def straight_structure(cards):
    """
    simply: This function will check if the cards inputted are a straight.

    This is done by making sure that the length of the first column values does not exceed 5.
    
    parameters: The hand of the cards provided in a 2 dimentional list. For Example:
                [[5, 'hearts'],[2,'clubs'],[12,'spades']]
                This function takes in 7 cards for a hand.
    """

    if isinstance(cards[0][0], list):
        cards = [c[0] for c in cards]
    ranks = [c[0] if isinstance(c, list) else c for c in cards]
    ranks = sorted(set(ranks))
    for i in range(len(ranks) - 4):
        if all(ranks[i + j] == ranks[i] + j for j in range(5)):
            return True
    return set([14,2,3,4,5]).issubset(ranks)




def evaluate_all_known_cards(known_cards):
    
    """
    Simply: This function will generate the amount of future combinations that can happen for each rank by computing every single combination left out of 7 cards poker.
    
    This function will first use the function card_list which generates a list of all possible cards. It will then re generate the deck without the cards that are known.
    we will find out how many cards are unknown to us by doing 7 cards which can be the max we can have removing the length of the list of the cards which we do know (total count - known count = unknow count)
    We are then able to declare a dictionary which has every type of poker ranking there is, this will be used for our output as we can add to this dictionary throughout the code.
    we can then loop through every unknown combination, this is because we have an equal chance of getting each remaining card in a different order. This is done by using the pre-existing python libary called
    itertools which has the function .combination which takes the parameters, the list of total remaining cards and how many cards we want in each rotation of our combination which is our unknow cards.
    we can then use the known cards that was inputed and the current combination of cards to create a hand in which we can input into best rank to check if it follows a specific rank.
    If it does contain a specific rank then we can store it in the variable rank. If rank does not contain anything like before then we move to the next combination otherwise we manipulate the
    dictionary 'rankings'. we tell the name rank in rankings dictionary to increment by one and then move on to the next combination.
    Once all combinations have been ran passed. We can find the total combinations completed by doing the length of the deck choose (nCr, combination formula) the length of the unknown cards.
    and return both in a tuple which python automatically will do when not suggest how to return a function with 2 return variables.

    parameters: The hand of the cards provided/known in a 2 dimentional list. For Example:
                [[5, 'hearts'],[2,'clubs'],[12,'spades']]


    """

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
    for current in itertools.combinations(deck, unknown_count):
        seven_cards = list(known_cards) + list(current)
        rank = best_rank(seven_cards)
        if rank:
            rankings[rank] += 1
    total = math.comb(len(deck), unknown_count)
    return rankings, total



def best_rank(seven_cards):
    
    """
    simple: This functions finds the best rank available from 7 cards.
            Keep in mind, For a rank it will only take it 5 cards which means it has to be a combination of those 7 cards which therefore requires itertools.combinations .

            First we have to create a dictionary to order the values of each rank in how important they are, we call this rank_value.
            As we declare variables at the start we set best = None which is the item we will return.
            We are then able to use a count controlled loop of itertools.combinations to find 5 cards out of the list of seven cards which would result in 21 different combinations that need to be cycled through.
            with each combination we input it into the rank structure functions to produce a result if it has that rank.
            Then we can use a series of selection statements in a specified order of hierarchy to achieve which is the best rank.
            These selection statements check whether there is a value contained in that specified rank variable obtained by putting the 5 card combination in the structure functions.
            Once we have found the best rank it will then be returned to the user or any other function that needs it.

        parameters: The hand of the cards provided/known in a 2 dimentional list. For Example:
            [[5, 'hearts'],[2,'clubs'],[12,'spades']]
            This function takes in strictly 7 cards.





    """


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
            if best == "straight_flush":
                return best
    return best


def draw_cards_random(amount):
    """
    Using the list creation function 'card_list'. This will generate amount inputted amount worth of cards at random from the list, remove those cards from the current list, return both the cards and the current list back to the use for further use.
    
    paremters: amount of cards you want to pick
    
    returns: 2 dimentional tuple, the first has the cards that have been picked the second has the remaining card list which is 2 dimentional.
    
    Example: ([Cards picked],[remaining list of cards])
    
    """
    current_card_list=card_list()
    cards_picked=[]
    for current in range(0,amount):
        draw_card=random.choice(current_card_list)
        current_card_list.remove(draw_card)
        cards_picked.append(draw_card)
    return cards_picked,current_card_list
    

def probability(evalulate_ranking_total):
    """
    Simple: Produced a probability of your hand for each available rank.

    This function will take in the tuple of both the ranking combinations stored as a dictionary and total combinations that was produced by the previouse evalutaing hand function.
    This will then make the tuple into a list so that is can be used and seperated if needed. it will divide the rank combination by the total combimations done which will be done to each rank
    by using a count control loop. This will then be added into a 2 dimentional list of which it has 1 row for each rank, where the first column is the ranks name and the second column
    is the probabilitiy of getting that rank. 

    parameters: a tuple/list of 2 items, the first being a dictionary which conatains the combinations of each rank and the sencond containing the total combinations done.
                This is easily achieved by using the evaluate_all_known_cards function.

    """
    list_rank_probability_return=[]
    list_evalulate_ranking_total=list(evalulate_ranking_total)
    evalulate_ranking=list_evalulate_ranking_total[0]
    evalulate_total=list_evalulate_ranking_total[1]
    for rank in evalulate_ranking:
        rank_probability=evalulate_ranking[rank] / evalulate_total
        list_rank_probability_return.append([rank, rank_probability])
    dictionary_rank_probability_return = {}
    for key, value in list_rank_probability_return:
        dictionary_rank_probability_return[key] = value
    return dictionary_rank_probability_return
        
        
