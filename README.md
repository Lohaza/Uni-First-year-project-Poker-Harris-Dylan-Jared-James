# Hand Evaluator and Probability Checker for Texas Hold'em.  

It's purpose is to evaluate your cards, produce the different possible hands that can be formed from those cards and calculate the probability of getting those specific hands. 

## Tutorial

This tutorial will give us a comprehensible understanding on how to use `pypokerprob.py` to not only evaluate the different possible hands we could create with the cards we're dealt in a game of Texas Hold'em. But also calculate the probability of these given hands.

If we're dealt the hole and flop cards:

```
. 10 of Hearts
. 8 of Clubs
. 2 of Diamonds
. 2 of Spades
. Ace (14) of Clubs
```

Firstly, we will start by analysing the cards we currently have, of which are stated above, and evaluate them for different potential hands. To accomplish this, we must first in the next code snippet import the liabries required.

```python
import pypokerprob
import random
import math
import itertools
import collections
```

Now we can import our hole and flop cards and evaluate them for the best potential hand:


```python
pypokerprob.hand_checker_for_hole_and_flop_cards( '10' , '8' , '2' , '2' , 'A' , 'H' , 'C' , 'D' , 'S' , 'C')
```

This gives us:

```
Potential hand(s):
Pair
```

Here we see that, we get as expected the correct best possible hand from our hole and flop cards. Now that we have uncovered this, we are able to calculate the probability of getting and completing that hand. In addition, we are able to calculate the probability of the less likely possible hands aswell:


```python 
combinations_possible = pypokerprob.evaluate_all_known_cards([[ 10 , 'hearts'] , [ 8 , 'clubs'] , [ 2 , 'diamonds'] , [ 2 , 'spades'] , [ 14 , 'clubs']])

pypokerprob.probability(combinations_possible)
```

This gives us:

```
{'one_pair': 0.5328399629972248,
 'two_pair': 0.37465309898242366,
 'three_of_a_kind': 0.0666049953746531,
 'straight': 0.0,
 'flush': 0.0,
 'full_house': 0.02497687326549491,
 'four_of_a_kind': 0.0009250693802035153,
 'straight_flush': 0.0,
 'royal_flush': 0.0}
```
This is what we would expect the probability to roughly be.

## How to guides

### How to evaluate the different possible hands from your hole cards:

To accomplish this, we first must look at our dealt hole cards and import their rank and suit seperatly into the correct allocated area:

Our hole cards:

```
. 5 of Diamnods 
. 7 of Spades
```

Now that we know our hole cards, we can use the function, by:

```python 
pypokerprob.hand_checker_for_hole_cards( '5' , '7' , 'D' , 'S')
```

This will give:

```
Potential hand(s):
Straight
Four of a kind
Three of a kind
Two Pair
Pair
```

### How to evaluate the different best hand from your hole and flop cards:

To achieve this, we must input the rank and suit seperately to our dealt hole cards and the flop cards into the correct allocated area:

Our cards:

```
. 5 of Diamnods 
. 7 of Spades
. King of Clubs 
. 5 of Hearts 
. 7 of Diamonds
```
Now we can use the function by:

```python
pypokerprob.hand_checker_for_hole_and_flop_cards('5' , '7' , 'K' , '5' , '7' , 'D' , 'S' , 'C' , 'H' , 'D')
```

This gives:

```
Potential hand(s):
Two Pair
```

### How to extract the best hand you can produce from 5 or more cards:

Given the following cards:

```
. 4 of Diamonds 
. 6 of Hearts 
. 7 of Spades 
. 4 of Hearts 
. 4 of Clubs 
```
The best hand you can produce is given by:

```python 
pypokerprob.best_rank([[ 4 , 'diamonds'] , [ 6 , 'hearts'] , [ 7 , 'spades'] , [ 4 , 'hearts'] , [ 4 , 'clubs']])
```
This gives:

```
'three_of_a_kind'
```
### How to check if your hand is a flush:

If we are given the following cards:

```
. 4 of Diamonds 
. 6 of Diamonds
. 7 of Diamonds
. Ace (14) of Diamonds 
. Jack (11) of Diamonds 
```
To evaluate if this is a flush or not, we must:


```python 
pypokerprob.flush_structure([[ 4 , 'diamonds'] , [ 6 , 'diamonds'] , [ 7 , 'diamonds'] , [ 14 , 'diamonds'] , [ 11 , 'diamonds']])
```

This gives:

```
True
```

### How to examine if your hand is a four of a kind:

We are given the following cards:

```
. 5 of Diamonds 
. 6 of Diamonds
. 5 of Clubs 
. 5 of Hearts  
. 5 of Spades 
```
Now, we need to check these given cards for a four of a kind. To do this, we must:

```python 
pypokerprob.four_of_a_kind_structure([[ 5 , 'diamonds'] , [ 6 , 'diamonds'] , [ 5 , 'clubs'] , [ 5 , 'hearts'] , [ 5 , 'spades']])
```
This returns:

```
True
```

### How to check if your hand is a full house:

We're dealt the following cards:

```
. 5 of Diamonds 
. 6 of Diamonds
. 5 of Clubs 
. 6 of Hearts  
. 5 of Spades
```
With these given cards, we are able to check if this hand is a full house, by:

```python 
pypokerprob.full_house_structure([[ 5 , 'diamonds'] , [ 6 , 'diamonds'] , [ 5 , 'clubs'] , [ 6 , 'hearts'] , [ 5 , 'spades']])
```
This gives:

```
True
```

### How to determine if your hand contains a straight or not:

We're dealt the cards below:

```
. 8 of Diamonds 
. 6 of Diamonds
. 7 of Clubs 
. 9 of Hearts
. 10 of Spades
```

Given the following cards, we can determine if they contain a straight or not, by:

```python
pypokerprob.straight_structure([[ 8 , 'diamonds'] , [ 6 , 'diamonds'] , [ 7 , 'clubs'] , [ 9 , 'hearts'] , [ 10 , 'spades']])
```
This returns an output of:

```
True
```

### How to find out if your hand includes a three of a kind:

If we are dealt the following cards:

```
. 8 of Diamonds 
. 6 of Diamonds
. 7 of Clubs 
. 9 of Hearts
. 10 of Spades
```

We can find out if these cards includes a three of a kind, by:

```python 
pypokerprob.three_of_a_kind_structure([[ 10 , 'diamonds'] , [ 6 , 'diamonds'] , [ 10 , 'clubs'] , [ 9 , 'hearts'] , [ 10 , 'spades']])
```

This gives us an output of:

```
True
```

### How to evaluate if your hand contains a two pair:

We are given the cards below:

```
. 10 of Hearts 
. 6 of Spades
. 7 of Clubs 
. 6 of Clubs
. 10 of Diamond
```

With these given cards, we can evaluate whether or not the hand conatins a two pair:

```python 
pypokerprob.two_pair_structure([[ 10 , 'hearts'] , [ 6 , 'spades'] , [ 7 , 'clubs'] , [ 6 , 'clubs'] , [ 10 , 'diamond']])
```
This returns the following output:

```
True
```

### How to identify if your hand includes a one pair:

Here, we are given the following cards:

```
. 8 of Diamonds 
. 6 of Diamonds
. 7 of Clubs 
. 6 of Hearts
. 10 of Spades
```
Now, given these cards we can evaluate them to see if it includes a one pair, by:

```python 
pypokerprob.one_pair_structure([[ 8 , 'diamonds'] , [ 6 , 'diamonds'] , [ 7 , 'clubs'] , [ 6 , 'hearts'] , [ 10 , 'spades']])
```
This returns:

```
True
```

### How to estimate the starting probability of getting a royal flush:

To estimate the starting probability of getting a royal flush, we must:

```python 
pypokerprob.starting_probability_royal_flush()
```
This returns:

```
3.2320620555914674e-05
```

### How to determine the starting probability of getting a flush:

We can determine this, by:

```python 
pypokerprob.starting_probability_flush() 
```
This gives:

```
0.030254941227896553
```

### How to estimate the starting probability of getting a four of a kind:

This can be estimated, by:

```python
pypokerprob.starting_probability_four_of_a_kind()
```

This returns:

```
0.0016806722689075631
```

### How to enumerate the starting probability of getting a full house:

To do this, we must:

```python 
pypokerprob.starting_probability_full_house()
```

This will return:

```
0.025961022706955123
```

### How to find out the starting probability of getting a straight flush:

We can find this out, by:

```python 
pypokerprob.starting_probability_straight_flush()
```
This gives us:

```
0.0002785074750030945
```

### How to enumerate the starting probability of getting a straight: 

We can enumerate this, by:

```python 
pypokerprob.starting_probability_straight()
```
This gives:

```
0.046193820871406985
```

### How to calculate the starting probability of getting a three of a kind:

We can determine this, by:

```python 
pypokerprob.starting_probability_three_of_a_kind()
```
This returns:

```
0.048298697547758875
```

### How to determine the starting probability of getting a two pair:

To determine this probability, we must:

```python 
pypokerprob.starting_probability_two_pair()
```
This gives:

```
0.23495536405695844
```

### How to calculate the starting probability of getting a one pair:

To calculate the starting probabilty of the above, we'll need to:

```python 
pypokerprob.starting_probability_one_pair()
```
This will give us:

```
0.4382254574070431
```

### How to calculate the starting probability of getting a high card:

To calculate the starting probability of getting a high card before any cards are dealt, you'll need to:

```python 
pypokerprob.starting_probabililty_high_card()
```
This will return:

```
0.17411919581751437
```

### How to evaluate and enumerate the different combinations possible with the cards you currently have:

We are dealt the following cards:

```
. 5 of Diamonds
. 6 of Diamonds
. 5 of Clubs
. 5 of Hearts
. 5 of Spades
```

We can evaluate and enumerate the different combinations possible with the cards you currently have, by:  

```python 
pypokerprob.evaluate_all_known_cards([[ 5 , 'diamonds'] , [ 6 , 'diamonds'] , [ 5 , 'clubs'] , [ 5 , 'hearts'] , [ 5 , 'spades']])
```
This returns an output of: 

```
({'one_pair': 0,
  'two_pair': 0,
  'three_of_a_kind': 0,
  'straight': 0,
  'flush': 0,
  'full_house': 0,
  'four_of_a_kind': 1081,
  'straight_flush': 0,
  'royal_flush': 0},
 1081)
```

### How to calculate the probability of getting certain hands, with the cards you have:

If we are dealt the following cards:

```
. Ace (14) of Diamonds
. 8 of Hearts
. 8 of Clubs
. Queen (12) of Diamonds
. 7 of Clubs
```

We can calculate the probability of getting a certain hand with the cards above, by evaluating and enumerating the different possible combinations first; denoted by the variable name combinations_possible. Then from there caluclating the probability, by:

```python 
combiantions_possible = pypokerprob.evaluate_all_known_cards([[ 14 , 'diamonds'] , [ 8 , 'hearts'] , [ 8 , 'clubs'] , [ 12 , 'diamonds'] , [ 7 , 'clubs']])

pypokerprob.probability(combiantions_possible)

```
This will return us an output of:

```
{'one_pair': 0.5328399629972248,
 'two_pair': 0.37465309898242366,
 'three_of_a_kind': 0.0666049953746531,
 'straight': 0.0,
 'flush': 0.0,
 'full_house': 0.02497687326549491,
 'four_of_a_kind': 0.0009250693802035153,
 'straight_flush': 0.0,
 'royal_flush': 0.0}
```

### How to randomly draw cards from a deck:

We can use this function, by:

```python 
pypokerprob.draw_cards_random(2)
```
This gives:

```
([[14, 'diamonds'], [5, 'spades']],
 [[2, 'diamonds'],
  [3, 'diamonds'],
  [4, 'diamonds'],
  [5, 'diamonds'],
  [6, 'diamonds'],
  [7, 'diamonds'],
  [8, 'diamonds'],
  [9, 'diamonds'],
  [10, 'diamonds'],
  [11, 'diamonds'],
  [12, 'diamonds'],
  [13, 'diamonds'],
  [2, 'hearts'],
  [3, 'hearts'],
  [4, 'hearts'],
  [5, 'hearts'],
  [6, 'hearts'],
  [7, 'hearts'],
  [8, 'hearts'],
  [9, 'hearts'],
  [10, 'hearts'],
  [11, 'hearts'],
  [12, 'hearts'],
  [13, 'hearts'],
  [14, 'hearts'],
  [2, 'clubs'],
  [3, 'clubs'],
  [4, 'clubs'],
  [5, 'clubs'],
  [6, 'clubs'],
  [7, 'clubs'],
  [8, 'clubs'],
  [9, 'clubs'],
  [10, 'clubs'],
  [11, 'clubs'],
  [12, 'clubs'],
  [13, 'clubs'],
  [14, 'clubs'],
  [2, 'spades'],
  [3, 'spades'],
  [4, 'spades'],
  [6, 'spades'],
  [7, 'spades'],
  [8, 'spades'],
  [9, 'spades'],
  [10, 'spades'],
  [11, 'spades'],
  [12, 'spades'],
  [13, 'spades'],
  [14, 'spades']])
```

### How to see the cards remaining in the deck:

We are able to do this, by:

```python
pypokerprob.card_list()
```
This gives us:

```
[[2, 'diamonds'],
 [3, 'diamonds'],
 [4, 'diamonds'],
 [5, 'diamonds'],
 [6, 'diamonds'],
 [7, 'diamonds'],
 [8, 'diamonds'],
 [9, 'diamonds'],
 [10, 'diamonds'],
 [11, 'diamonds'],
 [12, 'diamonds'],
 [13, 'diamonds'],
 [14, 'diamonds'],
 [2, 'hearts'],
 [3, 'hearts'],
 [4, 'hearts'],
 [5, 'hearts'],
 [6, 'hearts'],
 [7, 'hearts'],
 [8, 'hearts'],
 [9, 'hearts'],
 [10, 'hearts'],
 [11, 'hearts'],
 [12, 'hearts'],
 [13, 'hearts'],
 [14, 'hearts'],
 [2, 'clubs'],
 [3, 'clubs'],
 [4, 'clubs'],
 [5, 'clubs'],
 [6, 'clubs'],
 [7, 'clubs'],
 [8, 'clubs'],
 [9, 'clubs'],
 [10, 'clubs'],
 [11, 'clubs'],
 [12, 'clubs'],
 [13, 'clubs'],
 [14, 'clubs'],
 [2, 'spades'],
 [3, 'spades'],
 [4, 'spades'],
 [5, 'spades'],
 [6, 'spades'],
 [7, 'spades'],
 [8, 'spades'],
 [9, 'spades'],
 [10, 'spades'],
 [11, 'spades'],
 [12, 'spades'],
 [13, 'spades'],
 [14, 'spades']]
```

## Explanation

## Brief overview of Texas Hold'em

Texas Hold'em is a very popular variant of the game poker. In this variant of poker, a player is dealt two cards that only they are allowed to see. These two cards are known as your 'Hole cards', from here the community cards are placed down for everyone playing to see. The community cards are revealed in the following way, the first round will reveal three cards of which are knwon as the 'Flop cards'. Then the next round will reveal one card, which is known as the 'Turn' and finally the next round will reveal the last community card, known as the 'River'. From these five community cards and your 'Hole cards', your goal is to build the strongest hand possible. This will allow you to beat your opponents and win, or play the risky way and try to mislead your opponents into folding. If you are the last person standing in the game, then you will automatically win.

Now to build a strong hand, we must first understand what the different possible hands are, and which are the strongest.
Therefore, here is a list of the different possible hands, ranking from the strongest to the weakest:

1. Royal Flush (A,K,Q,J,10 of the same suit)
2. Straight Flush (Five consecutive cards of the same suit)
3. Four of a Kind (Four of the same value cards)
4. Full House (Three of the same value cards and two of the same value cards but  not the same value as each other)
5. Flush (Any five cards of the same suit)
6. Straight (Five consecutive cards of any suit)
7. Three of a Kind (Three of the same value cards)
8. Two pair (Two cards of the same value and another two cards of the same value but not the same value as each other)
9. One pair (Two cards of the same value)
10. High card (Your highest value card)

### Calculating the starting probabilities

To calculate the starting probabilities, we must consider a variety of different factors that could alter the probability of getting the hand we want. Thus, a good place to start off with is understanding a couple of these different factors. These factors include the number of 'Hole cards' we would have at the start of the game. Secondly, the number of cards remaining in the deck after we've removed the cards in our wanted hand. Lastly, the different number of possible combinations of the hand wanted. This is just a start to trying to calculate the starting probabilities as unfortunatly we can't just divide two numbers and get the probabilities. Instead we need to venture into the world of calculations with 'choose'. Without diving deeply into what exaclty 'choose' are, it can simply be emphasisied as if we have $\binom{n}{k}$. It represents the number of ways we can select $k$ elements from a specific set of $n$ distinct elements, where the order of which does not matter. 

This can be represented mathematically by the following equation:

$$
\binom{n}{k} = \frac{n!}{(n - k)!k!}
$$

We can apply the understanding of 'choose' to aid in our calculations to find the starting probabilities of different hands, just by using these 'choose' in the context of the factors we spoke about above. For example, we can calculate the starting probability of a Royal Flush, by:

- Let $n_1$ = Number of cards remaining in the deck after we've removed the cards in our wanted hand.
- Let $k_1$ = Number of 'Hole cards' we would have at the start of the game.
- Let $n_2$ = Different number of possible combinations of the hand wanted.
- Let $k_2$ = 1. 
- Let $n_3$ = Number of cards in a deck.
- Let $k_3$ = 7 (seven card poker).
- Let $P$ = Probability of the hand 

$$

\binom{n_1}{k_1} * \binom{n_2}{k_2} = \binom{47}{2} * \binom{4}{1}  = \frac{47!}{(47 - 2)!2!} * \frac{4!}{(4 - 1)!1!} = 4324

$$

$$

\binom{n_3}{k_3} = \frac{52!}{(52 - 7)!7!} = 133,784,560 

$$

$$

P = \frac{4324}{133784560} * 100 = 0.003232

$$

Unfortunately, we are unable to use this equation universally for each hand as the different factors spoken about above, does alter how we approach the process of calculating the starting probabilities of the hands.

## Reference

### The different operations:

These are the different functions that are available in `pypokerprob`:

1. `best_rank` 
2. `card_list`
3. `draw_cards_random`
4. `evaluate_all_known_cards`
5. `flush_structure`
6. `four_of_a_kind_structure`
7. `full_house_structure`
8. `hand_checker_for_hole_and_flop_cards` 
9. `hand_checker_for_hole_cards`
10. `one_pair_structure`
11. `probability`
12. `starting_probabililty_high_card`
13. `starting_probability_flush`
14. `starting_probability_four_of_a_kind`
15. `starting_probability_full_house`
16. `starting_probability_one_pair`
17. `starting_probability_royal_flush`
18. `starting_probability_straight`
19. `starting_probability_straight_flush`
20. `starting_probability_three_of_a_kind`
21. `starting_probability_two_pair`
22. `straight_structure`
23. `three_of_a_kind_structure`
24. `two_pair_structure` 

### Installation of the `pypokerprob` library:

#### Windows:

1. Open the command terminal, abbreviated as CMD on the windows search bar.
2. If you have th folder already downloaded on your device, you can put the path pyproject.toml or "C:\Users\harri\OneDrive\Documents\Uni-First-year-project-Poker-Harris-Dylan-Jared-James\pyproject.toml" into your command terminal.
3. Once you have found the folder required, you can use the command: "pip install -e ."

If you don't have the folder on your device, you can install it through the internet by using github. To do this, input the following into your terminal: "pip install git+https://github.com//Lohaza/Uni-First-year-project-Poker-Harris-Dylan-Jared-James.git" 

These will both install the library and python folder onto your device.

### Further information

The following documents develops on and dives deeper into the whole world of mathematics and computer science behind Poker and the variant Texas Hold'em:


1. [Probabilities and Simulations in Poker](https://ualberta.scholaris.ca/server/api/core/bitstreams/5c4ba350-53a0-48d4-88af-fa64efcb172e/content)
2. [A method of computing winning probability for Texas Hold'em poker](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9601881)

### Bibliography:

- Mario de Lourdes Peña Castillo. 1999. Probabilities and Simulations in Poker. MSc, University of Alberta. Available at: https://ualberta.scholaris.ca/server/api/core/bitstreams/5c4ba350-53a0-48d4-88af-fa64efcb172e/content [Accessed: 02 of May 2026]
- Wu Fan, Zhao Hailu, Liu He, Du Song, Zhang Xiaochuan. 2021. A method of computing winning probability for Texas Hold'em poker. 2021 33rd Chinese Control and Decision Conference (CCDC). Kunming, China. 22-24 May, 2021. IEEE (Institute of Electrical and Electronics Engineers) , pp. 1820-1824.

