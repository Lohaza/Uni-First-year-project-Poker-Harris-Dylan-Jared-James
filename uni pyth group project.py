import pygame
import random
import math




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
    numcardtuple = ('Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King')
    suitcardtuple=('Diamond','Hearts','clubs','spades')

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

def Probability():
    None

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
print(probabililty_high_card())



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
print(probability_one_pair())


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
print(probability_two_pair())

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
print(probability_three_of_a_kind())

def hand_input_two_cards(draw_card_one,draw_card_two):
    """
    The user knows 2 out of the seven cards in Texas Holdem. We will presume these are the cards in there hand and not on the table
    
    If the user would like to put in there cards independently.

    """
    None
def hand_input_three_cards(draw_card_one,draw_card_two,draw_card_three):
    """
    The user knows 3 out of the seven cards in Texas Holdem. We will presume 2 cards in there hand and 1 on the table
    
    If the user would like to put in there cards independently.

    """
    None
def hand_input_four_cards(draw_card_one,draw_card_two,draw_card_three,draw_card_four):
    """
    The user knows 4 out of the seven cards in Texas Holdem. We will presume 2 cards in there hand and 2 on the table

    If the user would like to put in there cards independently.

    """
    None
def hand_input_five_cards(draw_card_one,draw_card_two,draw_card_three,draw_card_four,draw_card_five):
    """
    The user knows 5 out of the seven cards in Texas Holdem. We will presume 2 cards in there hand and 3 on the table
    
    If the user would like to put in there cards independently.

    """
    None

def hand_input_six_cards(draw_card_one,draw_card_two,draw_card_three,draw_card_four,draw_card_five,draw_card_six):
    """
    The user knows 6 out of the seven cards in Texas Holdem. We will presume 2 cards in there hand and 4 on the table
    
    If the user would like to put in there cards independently.

    """
    None

def hand_input_seven_cards(draw_card_one,draw_card_two,draw_card_three,draw_card_four,draw_card_five,draw_card_six,draw_card_seven):
    """
    The user knows 7 out of the seven cards in Texas Holdem. We will presume 2 cards in there hand and 5 on the table
    
    If the user would like to put in there cards independently.

    """
    None

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
