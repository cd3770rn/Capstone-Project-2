# The deck is divided down the middle to both players (26 cards each)
# Each player removes a card from the top of their deck. This is called a battle.
# The player with the higher card wins the battle and takes both cards.
# If the cards are of the same face value, both players continue to draw until a player loses the battle.
# The cards that are won are placed at the bottom of the deck.


# TODO: Make a dictionary to store the deck.
# SO below there's two different ways that the dictionaries could be made, let me know if either would work or if
# we should come up with a different way, I am just trying out different things.
# both of these feel like its too much code and there's prob an easier way but I'm not sure how?
# does the dictionary need to be separate from the classes or can it be combined?

# TODO: Create a Card class
    # Each card should have a suit
    # Each card should have a value (A, 2, 3, etc.)
class Card:
    card_value = {
        "TWO": 2,
        "THREE": 3,
        "FOUR": 4,
        "FIVE": 5,
        "SIX": 6,
        "SEVEN": 7,
        "EIGHT": 8,
        "NINE": 9,
        "TEN": 10,
        "JACK": 11,
        "QUEEN": 12,
        "KING": 13,
        "ACE": 14  # or should ace be 1? also, cant an ace be either a 1 or 11? Idk if that matters in this game though
    }


# TODO: Create a Suit class
class Suit:
    card_suit = {
        "SPADES": "spades",
        "CLUBS": "clubs",
        "HEARTS": "hearts",
        "DIAMONDS": "diamonds"
    }


# this is the second way I found we could do a dictionary for the deck but its a lot of code
# creates dictionary of cards and their values
# stored as key-value pairs
deck = {'Ace of Spades': 1, '2 of Spades': 2, '3 of Spades': 3, '4 of Spades': 4,
        '5 of Spades': 5, '6 of Spades': 6, '7 of Spades': 7, '8 of Spades': 8,
        '9 of Spades': 9, '10 of Spades': 10, 'Jack of Spades': 11, 'Queen of Spades': 12,
        'King of Spades': 13,

        'Ace of Hearts': 1, '2 of Hearts': 2, '3 of Hearts': 3, '4 of Hearts': 4,
        '5 of Hearts': 5, '6 of Hearts': 6, '7 of Hearts': 7, '8 of Hearts': 8,
        '9 of Hearts': 9, '10 of Hearts': 10, 'Jack of Hearts': 11, 'Queen of Hearts': 12,
        'King of Hearts': 13,

        'Ace of Diamonds': 1, '2 of Diamonds': 2, '3 of Diamonds': 3, '4 of Diamonds': 4,
        '5 of Diamonds': 5, '6 of Diamonds': 6, '7 of Diamonds': 7, '8 of Diamonds': 8,
        '9 of Diamonds': 9, '10 of Diamonds': 10, 'Jack of Diamonds': 11, 'Queen of Diamonds': 12,
        'King of Diamonds': 13,

        'Ace of Clubs': 1, '2 of Clubs': 2, '3 of Clubs': 3, '4 of Clubs': 4,
        '5 of Clubs': 5, '6 of Clubs': 6, '7 of Clubs': 7, '8 of Clubs': 8,
        '9 of Clubs': 9, '10 of Clubs': 10, 'Jack of Clubs': 11, 'Queen of Clubs': 12,
        'King of Clubs': 13}


# TODO: Create a makeDeck() function which creates and initializes the playing deck.
# TODO: Create a draw() function which draws from the top of each player's deck
# TODO: Create a discard() function which puts the cards at the bottom of the player's deck.
# TODO: Create battle(), war() functions which perform the expected action


# If there's more to do, divvy it up evenly?
