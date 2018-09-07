# The deck is divided down the middle to both players (26 cards each)
# Each player removes a card from the top of their deck. This is called a battle.
# The player with the higher card wins the battle and takes both cards.
# If the cards are of the same face value, both players continue to draw until a player loses the battle.
# The cards that are won are placed at the bottom of the deck.


# TODO: Make a dictionary to store the deck.
# Can the dictionaries be inside of the card class and suit class?
# I feel like the card_value and card_suit dictionaries below could be combined into one
# but I'm not sure the best way to do that

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

# TODO: Create a makeDeck() function which creates and initializes the playing deck.
# TODO: Create a draw() function which draws from the top of each player's deck
# TODO: Create a discard() function which puts the cards at the bottom of the player's deck.
# TODO: Create battle(), war() functions which perform the expected action


# If there's more to do, divvy it up evenly?
