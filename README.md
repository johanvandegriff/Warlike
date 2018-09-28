# Warlike

https://github.com/johanvandegriff/Warlike

## How to Run

Download warlike.py and execute in the terminal: `python3 warlike.py` or
`./warlike.py`

## Rules

Warlike is a card game that I made up based on the popular card game War. This
version of Warlike is played against a computer. To set up the game, the deck
is shuffled and each player is dealt 26 cards. During each turn, each player
has three options:

1. Play the top card, which is unknown, and discard the bottom card.

2. Play the bottom card, which is visible.

3. "Steal" by taking the opponent's top card, playing it, and putting
the bottom card in the opponent's discard pile. If the opponent
played the top card, the next card down is stolen instead.

Whoever's card is higher wins. Aces are high, and ties are broken by suit (low
to high: clubs, diamonds, hearts, spades). The winner puts both cards into their
discard pile. That pile is shuffled and re-used when the player runs out. Gain
all the cards to win the game!

## Design and Data Structures

I chose to represent each card with a tuple, with the value first, then suit.
This made it easy in debugging to print out lists of cards and to correlate them
with the cards displayed.

I decided to make a "Player" object to keep track of a single deck and discard
pile (initially, I used separate arrays and they were cumbersome). It has
methods for getting the top and bottom cards, and internally shuffles as needed.
It also solves the problem of detecting a victory condition by throwing an
exception when the deck and discard are both empty and a card is requested.

To clean up some of the random print statements that I sometimes wanted enabled,
I made a secret "debug mode" that can be activated by typing "bamboo" into the
first prompt when the game starts. When debug mode is on, the print statements
are executed, allowing me to see what cards the player and computer have and
verify that the functions are working.

The computer's AI is very simple (only 6 lines of code). It looks at the bottom
card. If that card is:
1. Within the bottom 1/3 of the 52 cards, it steals, hoping to trade the low
vaue card for a higher one.
2. Within the top 1/2 of the 52 cards, it plays the bottom card.
3. Otherwise, it plays the top card (discarding the bottom card).


## Tooling

I decided to write this game in Python (rather than Java, C++, etc.) because:
* It's a small project that is better suited to Python's scripting-like syntax.
* Python has objects that can be used if needed.
* String manipulation (to display the cards) is very easy in Python.

I only used one library, the python `random` library, for shuffling the cards
and choosing the style of the back of the cards randomly each game.

## Testing

Since this was a small project, I didn't use a unit testing framework. I did
write snippets of code, add debug print statements, and modify the players'
cards to test various edge cases, for example:
* One player steals the top card, but the other one chose the top card.
* Both players steal.
* The top card is chosen with only 1 card left.
* The game ends with each of the 9 combinations of each player's options.
