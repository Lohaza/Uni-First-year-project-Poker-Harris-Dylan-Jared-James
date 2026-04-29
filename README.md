# pypokerprob

A Python Libary used for finding probabilitys of future possible ranks.(Poker style - Texas Hold'em 7 card)

This libary is able to:

- Generate random cards and 52 card decks.

- Tells the starting probabilitys of getting a rank.

- Evaluates a group of cards called a hand and displays all the future combinations left that you can have in 7 card poker.

- Find the best rank you can make out of 7 cards.

- Find if 5 cards make a particular rank.

## Installation

Windows:

1. Open the Command Terminal. Abrivated as CMD on the windows search bar.

2. If you have the folder on your device you can simply put the file path for pyproject.toml
Example: "C:\Users\harri\OneDrive\Documents\Uni-First-year-project-Poker-Harris-Dylan-Jared-James\pyproject.toml"

Once you have found the folder you can then use the command:

"pip install -e ."

If you do not have the folder on your device you can simply install it from through the internet by using github.
To do this iput into your terminal:

"pip install git+https://github.com//Lohaza/Uni-First-year-project-Poker-Harris-Dylan-Jared-James.git"

These will both install the libary onto your device and python folder. Allowing you to be able to use the functions inside.

## Tutorial

I will explain the basis of how to use pypokerprob libary.

Before you use any functions you must type at the top of your script:

"import pypokerprob"

I will now explain an example of how to use each function properly and accordingly.

-   Function:

    pypokerprob.card_list()

    Input:

    ""
    Mylist=pypokerprob.card_list()
    print(Mylist)

    ""

    Output:

    ""
    [[2, 'diamonds'], [3, 'diamonds'], [4, 'diamonds'], [5, 'diamonds'], [6, 'diamonds'], [7, 'diamonds'], [8, 'diamonds'], [9, 'diamonds'], [10, 'diamonds'], [11, 'diamonds'], [12, 'diamonds'], [13, 'diamonds'], [14, 'diamonds'], [2, 'hearts'], [3, 'hearts'], [4, 'hearts'], [5, 'hearts'], [6, 'hearts'], [7, 'hearts'], [8, 'hearts'], [9, 'hearts'], [10, 'hearts'], [11, 'hearts'], [12, 'hearts'], [13, 'hearts'], [14, 'hearts'], [2, 'clubs'], [3, 'clubs'], [4, 'clubs'], [5, 'clubs'], [6, 'clubs'], [7, 'clubs'], [8, 'clubs'], [9, 'clubs'], [10, 'clubs'], [11, 'clubs'], [12, 'clubs'], [13, 'clubs'], [14, 'clubs'], [2, 'spades'], [3, 'spades'], [4, 'spades'], [5, 'spades'], [6, 'spades'], [7, 'spades'], [8, 'spades'], [9, 'spades'], [10, 'spades'], [11, 'spades'], [12, 'spades'], [13, 'spades'], [14, 'spades']]

    ""

-   Function:
    
    Input:

    ""

    ""

    Ouput:

    ""

    ""
    
