#!/usr/bin/python3

#######################################
##                                   ##
##         Warlike Card Game         ##
##        by Johan Vandegriff        ##
##        https://johanv.xyz/        ##
##      MIT License (see below)      ##
##                                   ##
##   This program uses Bej's cards   ##
##   http://ascii.co.uk/art/cards    ##
##                                   ##
#######################################

"""
Copyright (c) 2018 Johan Vandegriff

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import random, sys

#card and suit information
#         2   3   4   5   6   7   8   9   10   11  12  13  14
cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
cardNames = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]
#                 0        1          2          3
suits =     [    "+",     "O",       "#",       "@" ]
suitNames = ["clubs", "diamonds", "hearts", "spades"]
suitsDisplay = ' '.join([suits[i] + " = " + suitNames[i] for i in range(4)])

#I made the card backs, but the cards themselves (further down) are from http://ascii.co.uk/art/cards
rawCardBacks = [
r"""
 _________ 
|*/*/%/*/*|
|/*/%#%/*/|
|*/%#:#%/*|
|/%#:-:#%/|
|*/%#:#%/*|
|/*/%#%/*/|
|*/*/%/*/*|
 ~~~~~~~~~ 
""",

r"""
 _________ 
|+:+:|:+:+|
|:+:] [:+:|
|+:]   [:+|
|:]     [:|
|+:]   [:+|
|:+:] [::+|
|+:+:|:+:+|
 ~~~~~~~~~ 
""",

r"""
 _________ 
|+:+[\]+:+|
|:+[\/\]+:|
|+[\/\/\]+|
|[\/\/\/\]|
|+[\/\/\]+|
|:+[\/\]:+|
|+:+[\]+:+|
 ~~~~~~~~~ 
""",

r"""
 _________ 
|/\/\/\/\/|
|\/\/+/\/\|
|/\/+:+/\/|
|\/+:+:+/\|
|/\/+:+/\/|
|\/\/+/\/\|
|/\/\/\/\/|
 ~~~~~~~~~ 
""",

r"""
 _________ 
|++++/\\/\|
|+++/\\/\\|
|++/\\/\\/|
|+/\\/\\/+|
|/\\/\\/++|
|\\/\\/+++|
|\/\\/++++|
 ~~~~~~~~~ 
""",

r"""
 _________ 
|++++/\/ /|
|++++\   \|
|++/\/ /\/|
|++\   \++|
|/\/ /\/++|
|\   \++++|
|/ /\/++++|
 ~~~~~~~~~ 
""",

r"""
 _________ 
| \   \/_/|
|\/ /\__ \|
|   \/_/\ |
| /\__ \/ |
| \/_/\   |
|\__ \/ /\|
|/_/\   \ |
 ~~~~~~~~~ 
""",

r"""
 _________ 
|/\+++\/+/|
|\/+/\+++\|
|+++\/+/\+|
|+/\+++\/+|
|+\/+/\+++|
|\+++\/+/\|
|/+/\+++\/|
 ~~~~~~~~~ 
""",

r"""
 _________ 
|/\   \/ /|
|\/ /\   \|
|   \/ /\ |
| /\   \/ |
| \/ /\   |
|\   \/ /\|
|/ /\   \/|
 ~~~~~~~~~ 
""",

r"""
 _________ 
|/\\/\\///|
|\///\\/\\|
|\/\\///\\|
|//\\/\\//|
|\\///\\/\|
|\\/\\///\|
|///\\/\\/|
 ~~~~~~~~~ 
""",

r"""
 _________ 
|  \/\  / |
|  /  \/\ |
|\/\  /  \|
|/  \/\  /|
|\  /  \/\|
| \/\  /  |
| /  \/\  |
 ~~~~~~~~~ 
""",

r"""
 _________ 
|\  /\  /\|
| \/  \/  |
| /\  /\  |
|/  \/  \/|
|\  /\  /\|
| \/  \/  |
| /\  /\  |
 ~~~~~~~~~ 
""",

r"""
 _________ 
|\\//\\//\|
|\\//\\//\|
|//\\//\\/|
|//\\//\\/|
|\\//\\//\|
|\\//\\//\|
|//\\//\\/|
 ~~~~~~~~~ 
""",

r"""
 _________ 
|\\//\\//\|
| \/  \/  |
| /\  /\  |
|//\\//\\/|
|\\//\\//\|
| \/  \/  |
| /\  /\  |
 ~~~~~~~~~ 
""",

r"""
 _________ 
|\/\/\/\/\|
| \/  \/  |
| /\  /\  |
|/\/\/\/\/|
|\/\/\/\/\|
| \/  \/  |
| /\  /\  |
 ~~~~~~~~~ 
""",

r"""
 _________ 
|+++/\\//\|
|++/  \/  |
|+/\  /\  |
|//\\//\\/|
|\\//\\//+|
| \/  \/++|
| /\  /+++|
 ~~~~~~~~~ 
""",

r"""
 _________ 
|+++/\/\/\|
|++/  \/  |
|+/\  /\  |
|/\/\/\/\/|
|\/\/\/\/+|
| \/  \/++|
| /\  /+++|
 ~~~~~~~~~ 
""",

r"""
 _________ 
|++++/\/\/|
|+++/////\|
|++/\/\///|
|+/////\/+|
|/\/\///++|
|////\/+++|
|/\///++++|
 ~~~~~~~~~ 
""",

r"""
 _________ 
|++++/  \+|
|+++/\ \ \|
|++/  \  /|
|+/\ \ \/+|
|/  \  /++|
|\ \ \/+++|
|+\  /++++|
 ~~~~~~~~~ 
""",

#r"""
# _________ 
#|++++/\+\/|
#|+++/\ \/\|
#|+++\ \/\/|
#|+/\/\ \++|
#|+\ \  /++|
#|+/\ \/+++|
#|+\  /++++|
# ~~~~~~~~~ 
#""",

r"""
 _________ 
|+++++\ \+|
|+++/\+\/+|
|++/\ \/\+|
|++\ \/\/+|
|/\/\ \+++|
|\ \  /+++|
|/\ \/++++|
 ~~~~~~~~~ 
""",

r"""
 _________ 
|+:+:+:+:+|
|:| / / |:|
|+|/\/\/|+|
|:| / / |:|
|+|/\/\/|+|
|:| / / |:|
|+:+:+:+:+|
 ~~~~~~~~~ 
""",

r"""
 _________ 
|+:+:+:+:+|
|:|\/\/\|:|
|+|/ / /|+|
|:|\/\/\|:|
|+|/ / /|+|
|:|\/\/\|:|
|+:+:+:+:+|
 ~~~~~~~~~ 
""",

r"""
 _________ 
|:-:-:-:-:|
|-| / / |-|
|:|/\/\/|:|
|-| /+/ |-|
|:|/\/\/|:|
|-| / / |-|
|:-:-:-:-:|
 ~~~~~~~~~ 
""",

r"""
 _________ 
|/\/\/\/\/|
|\ \_\_\ \|
|/\|___|\/|
|\|__|__|\|
|/\|___|\/|
|\ \ \ \ \|
|/\/\/\/\/|
 ~~~~~~~~~ 
""",

r"""
 _________ 
|___|___|_|
|_|_/\/\__|
|__/ / /|_|
|_|\/\/\__|
|__/ / /|_|
|_|\/\/___|
|___|___|_|
 ~~~~~~~~~ 
""",

r"""
 _________ 
|/\/\/\/\/|
|\ \ \ \ \|
|/\/\/\/\/|
| / / / / |
|/\/\/\/\/|
|\ \ \ \ \|
|/\/\/\/\/|
 ~~~~~~~~~ 
""",

r"""
 _________ 
|///\+/\\\|
|//\+++/\\|
|/\+++++/\|
|+++++++++|
|\/+++++\/|
|\\/+++\//|
|\\\/+\///|
 ~~~~~~~~~ 
""",

r"""
 _________ 
|%/./\.\%\|
|/./%%\.\%|
|./%/\%\.\|
|/%/./%/./|
|\%\.\/./%|
|.\%\../%/|
|\.\%\/%/.|
 ~~~~~~~~~ 
""",

r"""
 _________ 
| /=/\=\ \|
|/=/  \=\ |
|=/ /\ \=\|
|/ /=/ /=/|
|\ \=\/=/ |
|=\ \==/ /|
|\=\ \/ /=|
 ~~~~~~~~~ 
""",

r"""
 _________ 
| /\/\/\ \|
|/\/  \/\ |
|\/ /\ \/\|
|/ /\/ /\/|
|\ \/\/\/ |
|/\ \/\/ /|
|\/\ \/ /\|
 ~~~~~~~~~ 
""",

r"""
 _________ 
|+:+:+:+:+|
|:+:+:+:+:|
|+/|_|_|\+|
|:)_|_|_(:|
|+\|_|_|/+|
|:+:+:+:+:|
|+:+:+:+:+|
 ~~~~~~~~~ 
""",

r"""
 _________ 
|:::::::::|
|:+::+::+:|
|:::::::::|
|:+::+::+:|
|:::::::::|
|:+::+::+:|
|:::::::::|
 ~~~~~~~~~ 
"""
]

#"raw" card ASCII, has been partly separated with emacs macros,
#will be futher segmented into individual cards.
#  Clubs +             Diamonds O          Hearts #            Spades @
rawCardArt = [
r"""
 _________           _________           _________           _________ 
|A        |         |A        |         |A        |         |A        |
|+   *    |         |O  /~\   |         |# _   _  |         |@   *    |
|    !    |         |  / ^ \  |         | / ~V~ \ |         |   / \   |
|  *-+-*  |         | (  ) |  |         | \ Bej / |         |  /_@_\  |
|    |    |         |  \ v /  |         |  \ # /  |         |    !    |
|   ~~~  +|         |   \_/  O|         |   `.'  #|         |   ~ ~  @|
|        V|         |        V|         |        V|         |        V|
 ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~ 
""",

r"""
 _________           _________           _________           _________ 
|K |/|\|  |         |K |/|\|  |         |K |/|\|  |         |K |/|\|  |
|+ /o,o\  |         |O |o.o|  |         |# %*,*%  |         |@ \- -/  |
|  \_-_/  |         |   \v/   |         |  \_o_/  |         | ! |-|   |
| ~-_-~-_ |         |  XXXXX  |         | #>-=-<# |         |  % I %  |
|  /~-~\  |         |   /^\   |         |  /~o~\  |         |   |-| ! |
|  \o`o/ +|         |  |o'o| O|         |  %*'*% #|         |  /- -\ @|
|  |\|/| X|         |  |\|/| X|         |  |\|/| X|         |  |\|/| X|
 ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~ 
""",

r"""
 _________           _________           _________           _________ 
|Q |~~~|  |         |Q |~~~|  |         |Q |~~~|  |         |Q |~~~|  |
|+ /o,o\  |         |O |o.o|  |         |# %*,*%  |         |@ \- -/  |
|  \_-_/  |         |   \v/   |         |  \_o_/  |         | o |-|   |
| _-~+_-~ |         |  XXOXX  |         | -=<*>=- |         |  I % I  |
|  /~-~\  |         |   /^\   |         |  /~o~\  |         |   |-| o |
|  \o`o/ +|         |  |o'o| O|         |  %*'*% #|         |  /- -\ @|
|  |___| Q|         |  |___| Q|         |  |___| Q|         |  |___| Q|
 ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~ 
""",

r"""
 _________           _________           _________           _________ 
|J /~~|_  |         |J /~~|_  |         |J /~~|_  |         |J /~~|_  |
|+ | o`,  |         |O ( o\   |         |# % *`.  |         |@ ! -\   |
|  | -|   |         |  ! \l   |         |  % <~   |         |  \ -!   |
| =~)+(_= |         | ^^^Xvvv |         | %% / %% |         |  ',\',  |
|   |- |  |         |   l\ I  |         |   _> %  |         |   I- \  |
|  `.o | +|         |   \o ) O|         |  `,* % #|         |   \- I @|
|  ~|__/ P|         |  ~|__/ P|         |  ~|__/ P|         |  ~|__/ P|
 ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~ 
""",

r"""
 _________           _________           _________           _________ 
|10+   +  |         |10O   O  |         |10#   #  |         |10@   @  |
|+   +    |         |O   O    |         |#   #    |         |@   @    |
|  +   +  |         |  O   O  |         |  #   #  |         |  @   @  |
|         |         |         |         |         |         |         |
|  +   +  |         |  O   O  |         |  #   #  |         |  @   @  |
|    +   +|         |    O   O|         |    #   #|         |    @   @|
|  +   +0l|         |  O   O0l|         |  #   #0l|         |  @   @0l|
 ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~ 
""",

r"""
 _________           _________           _________           _________ 
|9 +   +  |         |9 O   O  |         |9 #   #  |         |9 @   @  |
|+        |         |O        |         |#        |         |@        |
|  +   +  |         |  O   O  |         |  #   #  |         |  @   @  |
|    +    |         |    O    |         |    #    |         |    @    |
|  +   +  |         |  O   O  |         |  #   #  |         |  @   @  |
|        +|         |        O|         |        #|         |        @|
|  +   + 6|         |  O   O 6|         |  #   # 6|         |  @   @ 6|
 ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~ 
""",

r"""
 _________           _________           _________           _________ 
|8 +   +  |         |8 O   O  |         |8 #   #  |         |8 @   @  |
|+        |         |O        |         |#        |         |@        |
|  +   +  |         |  O   O  |         |  #   #  |         |  @   @  |
|         |         |         |         |         |         |         |
|  +   +  |         |  O   O  |         |  #   #  |         |  @   @  |
|        +|         |        O|         |        #|         |        @|
|  +   + 8|         |  O   O 8|         |  #   # 8|         |  @   @ 8|
 ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~ 
""",

r"""
 _________           _________           _________           _________ 
|7        |         |7        |         |7        |         |7        |
|+ +   +  |         |O O   O  |         |# #   #  |         |@ @   @  |
|    +    |         |    O    |         |    #    |         |    @    |
|  +   +  |         |  O   O  |         |  #   #  |         |  @   @  |
|         |         |         |         |         |         |         |
|  +   + +|         |  O   O O|         |  #   # #|         |  @   @ @|
|        L|         |        L|         |        L|         |        L|
 ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~ 
""",

r"""
 _________           _________           _________           _________ 
|6        |         |6        |         |6        |         |6        |
|+ +   +  |         |O O   O  |         |# #   #  |         |@ @   @  |
|         |         |         |         |         |         |         |
|  +   +  |         |  O   O  |         |  #   #  |         |  @   @  |
|         |         |         |         |         |         |         |
|  +   + +|         |  O   O O|         |  #   # #|         |  @   @ @|
|        9|         |        9|         |        9|         |        9|
 ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~ 
""",

r"""
 _________           _________           _________           _________ 
|5        |         |5        |         |5        |         |5        |
|+        |         |O        |         |#        |         |@        |
|  +   +  |         |  O   O  |         |  #   #  |         |  @   @  |
|    +    |         |    O    |         |    #    |         |    @    |
|  +   +  |         |  O   O  |         |  #   #  |         |  @   @  |
|        +|         |        O|         |        #|         |        @|
|        S|         |        S|         |        S|         |        S|
 ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~ 
""",

r"""
 _________           _________           _________           _________ 
|4        |         |4        |         |4        |         |4        |
|+        |         |O        |         |#        |         |@        |
|  +   +  |         |  O   O  |         |  #   #  |         |  @   @  |
|         |         |         |         |         |         |         |
|  +   +  |         |  O   O  |         |  #   #  |         |  @   @  |
|        +|         |        O|         |        #|         |        @|
|        b|         |        b|         |        b|         |        b|
 ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~ 
""",

r"""
 _________           _________           _________           _________ 
|3        |         |3        |         |3        |         |3        |
|+   +    |         |O   O    |         |#   #    |         |@   @    |
|         |         |         |         |         |         |         |
|    +    |         |    O    |         |    #    |         |    @    |
|         |         |         |         |         |         |         |
|    +   +|         |    O   O|         |    #   #|         |    @   @|
|        E|         |        E|         |        E|         |        E|
 ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~ 
""",

r"""
 _________           _________           _________           _________ 
|2        |         |2        |         |2        |         |2        |
|+        |         |O        |         |#        |         |@        |
|    +    |         |    O    |         |    #    |         |    @    |
|         |         |         |         |         |         |         |
|    +    |         |    O    |         |    #    |         |    @    |
|        +|         |        O|         |        #|         |        @|
|        Z|         |        Z|         |        Z|         |        Z|
 ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~ 
"""
]

#this is how the cardArt data structure will be organized after the cards have been separated
"""
cardArt = [#all cards
    [#2
        #2 of clubs
        [
            "row 0",
            "row 1",
            "row 2",
            #...
        ],
        #2 of diamonds
        [
            "row 0",
            "row 1",
            "row 2",
            #...
        ],
        #2 of hearts
        [...],
        #2 of spades
        [...]
    ],
    [#3...
    ]
    #...
]
"""


cardArt = []

for card in range(2,15):
    allSuits = []
    cardArt.append(allSuits) #will hold each suit of the card
    for suit in range(4):
        thisSuit = []
        allSuits.append(thisSuit)
        art = rawCardArt[14-card].split("\n")
        for i in range(1,10):
            thisSuit.append(art[i][0+suit*20:11+suit*20])

#select a random card back style
cardBackNum = random.randrange(len(rawCardBacks))
cardBack = rawCardBacks[cardBackNum].split('\n')[1:10]

#cut out the middle and put the word "STEAL"
cardBackSteal = cardBack[:]
cardBackSteal[3] = cardBackSteal[3][0:2] + "       " + cardBackSteal[3][9:11]
cardBackSteal[4] = cardBackSteal[4][0:2] + " STEAL " + cardBackSteal[4][9:11]
cardBackSteal[5] = cardBackSteal[5][0:2] + "       " + cardBackSteal[5][9:11]

"""
def printCard(card, suit):
    if card is None:
        if suit == 0:
            art = cardBack
        else:
            art = cardBackSteal
    else:
        art = cardArt[card-2][suit]
    for i in range(9):
        print(art[i])
"""

#will print a list of cards horizontally by combining each row of text individually
def printCards(cardList, spacing=9):
    allArt = [[] for i in range(9)]
    for card, suit in cardList:
        if card is None:
            if suit == 0:
                art = cardBack
            else:
                art = cardBackSteal
        else:
            art = cardArt[card-2][suit]
        for i in range(9):
            allArt[i].append(art[i])

    for art in allArt:
        print((' '*spacing).join(art))

#returns a value from 0-51 representing the card's ordering in the deck
def getCardValue(card):
    return (card[0]-2)*4 + card[1]

#when a player runs out of cards (and loses the game)
class OutOfCardsException(Exception):
    def __init__(self, message, who):
        super().__init__(message)
        self.who = who #keeps track of who lost so the handler can display who won

#a class that represents a player (human or computer)
class Player:
    #the player is given a name and a personal deck of cards
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck
        self.discard = [] #the discard pile starts out empty

    #functions to look at or remove the top and bottom cards of the deck
#    def peekTop(self):
#        self.shuffleIfNeeded()
#        return self.deck[0]
    def peekBottom(self):
        self.shuffleIfNeeded()
        return self.deck[-1]
    def popTop(self):
        self.shuffleIfNeeded()
        return self.deck.pop(0)
    def popBottom(self):
        self.shuffleIfNeeded()
        return self.deck.pop(-1)

    #this makes sure that the deck has cards, and if the deck and discard are both empty, it throws an exception saying that this player has lost.
    def shuffleIfNeeded(self):
        if len(self.deck) == 0:
            if len(self.discard) == 0:
                print("{} is out of cards!".format(self.name))
                raise OutOfCardsException("No cards left in discard when deck ran out!", self.name)
            else:
                print("{} shuffles.".format(self.name))
            self.deck = self.discard
            random.shuffle(self.deck) #use the random library to shuffle the array
            self.discard = []

    #when a player wins the round, this is called to give the winnings back
    def discardCard(self, card):
        self.discard.append(card)

    #discard the bottom card unless the deck is empty and therefore about to be shuffled anyway
    def discardBottomIfAvailable(self):
        if len(self.deck) > 0:
            self.discardCard(self.popBottom())

    #retrns the lengths of the deck and discard
    def getDeckLen(self):
        return len(self.deck)
    def getDiscardLen(self):
        return len(self.discard)



### THE MAIN CODE STARTS HERE! ###

#print the welcome screen
print("""


                                     Warlike

                               by Johan Vandegriff
                           https://johan.vandegriff.net/



"""+'\n'.join(["               "+cardArt[12][3][i]+"         "+cardBack[i]+"         "+cardArt[0][0][i] for i in range(9)])+"""



                                   Press ENTER

""")
#read the input
secret = input()

#check if the secret debug code was entered
debug = False
if secret == "bamboo":
    debug = True
    #I spent too long drawing this debug screen :(
    print("""


                              You are bamboo enough.
                          ____________________________
                         ()_)_)_)_)_)_)_)_)_)_)_)_)_)_)


                         Debug mode has been activated.











                                   Press ENTER

""")
    input()

#loop through all the card values, then suits, and add them to the deck
deck = []
for card in range(2,15):
    for suit in range(4):
        deck.append((card,suit))

#show the deck before shuffling if debug mode is on
if debug:
    #cut the deck up into segments of 6 cards so they fit in the terminal window
    for i in range(0,52, 6):
        printCards(deck[i:i+6],1)
    print("^^ deck before shuffling ^^")
    input()

#shuffle the deck with the random library
random.shuffle(deck)

#cut the deck in half and give half to each player. This method would get you kicked out of a casino!
player = Player("Player", deck[0:26])
computer = Player("Computer", deck[26:52])

#for testing purposes, here are scenarios where the player or computer is about to win:
#player = Player("Player", deck[0:50])
#computer = Player("Computer", deck[50:52])

#player = Player("Player", deck[0:2])
#computer = Player("Computer", deck[2:52])

#a little test to try out the discardBottomIfAvailable function
#for i in range(4):
#    print("computerCards: {}".format(computer.deck))
#    print("computerDiscard: {}".format(computer.discard))
#    computer.discardBottomIfAvailable()
#quit()


#if debug is enabled, show the deck after shuffling and each player's cards
if debug:
    for i in range(0,52,6):
        printCards(deck[i:i+6],1)
    print("^^ deck after shuffling ^^")
    input()
    #printCards([(3,2),(5,1),(8,0),(None,0),(None,1)])
    for i in range(0,26,6):
        printCards(player.deck[i:i+6],1)
    print("^^ player's cards ^^")
    input()
    for i in range(0,26,6):
        printCards(computer.deck[i:i+6],1)
    print("^^ computer's cards ^^")
    input()

#show the game rules
print("""


                               === How to play ===

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

                                   Press ENTER

""")
input()

#this will be used later to tell the player what the computer did
choiceNames = ["the top card.", "the bottom card.", "to steal!"]

try:
    while True:
        #get the value of the computer's bottom card so it can decide what option to choose
        computerVaule = getCardValue(computer.peekBottom())

        #the next 6 lines are the entire AI logic of the computer.
        if computerVaule <= 52/3: #if the value of the bottom card is low:
            computerChoice = 3 #steal from the player to hopefully dump the low card to get a higher one
        elif computerVaule >= 52/2: #if the value of the bottom card is high:
            computerChoice = 2 #play the bottom card
        else: #if the value of the bottom card is not very high or too low:
            computerChoice = 1 #play the top card

            #if debug is on, show the entire deck, discard, and choices of the player and computer
            if debug:
                print("playerCards: {}".format(player.deck))
                print("computerCards: {}".format(computer.deck))
                print("playerDiscard: {}".format(player.discard))
                print("computerDiscard: {}".format(computer.discard))
                print("computerChoice: {}".format(computerChoice))
                print("computerVaule: {}".format(computerVaule))
                print("\n")

        #show the player the options: top card (value unknown), bottom card (value known), steal
        playerBottomCard = player.peekBottom()
        print("DECK: {}  DISCARD: {}  TOTAL: {}   {}\n".format(player.getDeckLen(), player.getDiscardLen(), player.getDeckLen() + player.getDiscardLen(), suitsDisplay))
        print("1. TOP CARD       2. BOTTOM CARD         3. STEAL")
        printCards([(None, 0), playerBottomCard, (None,1)]) #display the actual cards
        print("\n\n")

        #ask the player for a choice. This takes only 5 lines of code compared to the computer's choice which takes 6, therefore the player is inherently dumber than the computer.
        playerChoice = None
        while playerChoice not in ("1", "2", "3"):
            sys.stdout.write("Pick one and press ENTER (1-3):")
            playerChoice = input()
        playerChoice = int(playerChoice)

        print("\n")

        #evaluate the player and computer's choices.

        playerCard = None
        #player selecting top card needs to be checked first in case computer steals from player later
        if playerChoice == 1: #top
            playerCard = player.popTop()
            #the rules (that I made up) dictate that the bottom card is discarded when the top card is played
            player.discardBottomIfAvailable()

        if computerChoice == 1: #top
            computerCard = computer.popTop()
            computer.discardBottomIfAvailable()
        elif computerChoice == 2: #bottom
            computerCard = computer.popBottom()
        else: #steal
            player.discardCard(computer.popBottom())
            computerCard = player.popTop()


        if playerChoice == 2: #bottom
            playerCard = player.popBottom()
        elif playerChoice == 3: #steal
            computer.discardCard(player.popBottom())
            playerCard = computer.popTop()

        #if debug is on, print the cards chosen in tuple form
        if debug:
            print("playerCard: {}".format(playerCard))
            print("computerCard: {}".format(computerCard))
            print("\n\n")

        #print the choices of the players (top, bottom, steal), and two cards chosen
        print("Player chose {} Computer chose {}\n".format(choiceNames[playerChoice-1], choiceNames[computerChoice-1]))

        print("PLAYER CARD        COMPUTER CARD")
        printCards([playerCard, computerCard])

        #determine the winner winner chicken dinner for this round round get around I get around
        if getCardValue(computerCard) > getCardValue(playerCard):
            print("Computer wins this round.")
        else:
            print("Player wins this round.")

        print("\nPress ENTER")
        input()

        #based on the winner, put the winnings into that player's discard pile
        if getCardValue(computerCard) > getCardValue(playerCard):
            computer.discardCard(computerCard)
            computer.discardCard(playerCard)
        else:
            player.discardCard(computerCard)
            player.discardCard(playerCard)

#when a player needs a card, either to look at or to draw, but they are completely out:
except OutOfCardsException as e:
    #determine the winner of the game based on who ran out of cards
    if e.who == "Computer":
        print("Player wins the game! :)")
    else:
        print("Computer wins the game... :(")

#print the end screen
print("""

                                Thanks for playing

                                     Warlike

                               by Johan Vandegriff
                          https://johan.vandegriff.net/

    Fun Fact: The style of the back of the cards changes every time you play!

                        Original (buggy) Project on Scratch:
                      https://scratch.mit.edu/projects/3020183/
""")
