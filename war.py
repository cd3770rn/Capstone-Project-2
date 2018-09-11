import random

# The deck is divided down the middle to both players (26 cards each)
# Each player removes a card from the top of their deck. This is called a battle.
# The player with the higher card wins the battle and takes both cards.
# If the cards are of the same face value, both players continue to draw until a player loses the battle.
# The cards that are won are placed at the bottom of the deck.


# ==============================================
# Kenya - I edited (and by edited I mean basically rewrote) your code.
# The Card class did not have an __init__ method so it wouldn't have done anything as far as making an object.
# I'm real sorry but all the 'Ace of Spades', 'Two of Hearts' that you wrote out was deleted.
# You are right, it takes up a lot of space in code. Instead, I wrote a small function which initializes the deck
# without the need to write it all out. See makeDeck().
# There is still more to be done but I'm going to take a break for now. Been coding for like 2 or 3 hours.
# The following code creates a deck. You can do print(deck) inside playGame() to see how it looks.
# ==============================================



class Card:
    # Initializes the card with a suit and rank (value)
    def __init__(self, rank, suit):
        self.suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        # Ranks contains None so that the index corresponds to the rank
        self.ranks = [None, "Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

        self.suit = self.suits[suit]
        self.rank = self.ranks[rank]
        self.value = 14 if rank == 1 else rank

    # Defines how the card will be displayed when it is printed.
    def __str__(self):
        return '%s of %s' % (self.rank, self.suit)

    def __repr__(self):
        return self.__str__()

    # The methods below allow card comparisons (cardA < cardB, etc.)
    def __lt__(self, other):
        return self.value < other.value
    def __gt__(self, other):
        return self.value > other.value
    def __eq__(self, other):
        return self.value == other.value
    def __ne__(self, other):
        return self.value != other.value
    def __ge__(self, other):
        return self.value >= other.value
    def __le__(self, other):
        return self.value <= other.value


def playGame():
    print("===== WAR =====")
    deck = {}
    makeDeck(deck)
    # TODO: Give players their cards [try random.choice(mydict.values())]
    # TODO: Make the war(), battle() functions do something
    # TODO: Create a while loop that runs the game


def makeDeck(deck):
    # Initializes the playing deck (Ace of Spades, Ace of Hearts, Ace of Diamonds, Ace of Clubs, 2 of Spades, etc.)
    for rank in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]:
        for suit in [0, 1, 2, 3]:
            card = Card(rank, suit)
            deck.update({str(card) : card})

def draw(playerDeck):
    print("")

def discard(card, playerDeck):
    print("")

def battle():
    print("")

def war():
    print("")


# TODO: Create a makeDeck() function which creates and initializes the playing deck.
# TODO: Create a draw() function which draws from the top of each player's deck
# TODO: Create a discard() function which puts the cards at the bottom of the player's deck.
# TODO: Create battle(), war() functions which perform the expected action

# If there's more to do, divvy it up evenly?

playGame()