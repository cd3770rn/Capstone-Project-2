import random

# The deck is divided down the middle to both players (26 cards each)
# Each player removes a card from the top of their deck. This is called a battle.
# The player with the higher card wins the battle and takes both cards.
# If the cards are of the same face value, both players continue to draw until a player loses the battle.
# The cards that are won are placed at the bottom of the deck.


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

class Player:
    playerCount = 0

    def __init__(self):
        Player.playerCount += 1
        self.name = self.setName()
        self.score = 0
        self.hand = {}

        if self.name == "":
            self.name = "Player " + str(Player.playerCount)

    def setName(self):
        return input("Player " + str(Player.playerCount) + ", please enter your name: ")

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def addScore(self, score):
        self.score += score

    def setScore(self, score):
        self.score = score

    def getScore(self):
        return self.score

    def setHand(self, hand):
        self.hand = hand

    def getHand(self):
        return self.hand

    def drawCard(self):
        card = next(iter(self.hand.values()))
        print(self.name + " draws the " + str(card) + ". " + "Cards remaining: " + str(self.cardCount()))
        return card

    def viewHand(self):
        for card in enumerate(self.hand, start=1):
            print(card)

    def discard(self, card):
        return self.hand.pop(str(card))

    def hasCards(self):
        return True if self.cardCount() > 0 else False

    def cardCount(self):
        return len(self.hand)

def newGame():
    print("========== WAR: Card Game ==========")
    deck = {}
    player1 = Player()
    player2 = Player()

    makeDeck(deck)
    dealCards(deck, player1, player2)

    turnCount = 1
    while True:
        if player1.hasCards() and player2.hasCards():
            print("========== TURN " + str(turnCount) + " ==========")
            card1 = player1.drawCard()
            card2 = player2.drawCard()

            # In unison, each player reveals the top card of their deck. This is a battle.
            playCards(player1, card1, player2, card2)
            turnCount += 1
            continue

        else:

            break
    gameOver(player1, player2)

def playCards(player1, card1, player2, card2):
    hand1 = player1.getHand()
    hand2 = player2.getHand()

    # The player with the higher card takes both of the cards played and moves them to their stack.
    if card1 > card2:
        hand1.update({str(card1): player1.discard(card1)})
        hand1.update({str(card2) : player2.discard(card2)})
        print(player1.name + " wins the battle, and takes the " + str(card2) + ".\n")

    elif card1 < card2:
        hand2.update({str(card1) : player1.discard(card1)})
        hand2.update({str(card2): player2.discard(card2)})
        print(player2.name + " wins the battle, and takes the " + str(card1) + ".\n")

    # If the two cards played are of equal value, then there is a war.
    elif card1 == card2:
        print("Both players played a " + str(card1.rank) + ". THIS MEANS WAR!\n")
        war(player1, card1, player2, card2)

    return

def war(player1, card1, player2, card2):
    print("========== WAR ==========")
    hand1 = player1.getHand() # Player 1's hand
    hand2 = player2.getHand() # Player 2's hand

    stack = {}
    stack.update({str(card1): player1.discard(card1)}) # Add card1 to the stack
    stack.update({str(card2): player2.discard(card2)}) # Add card2 to the stack

    while True:
        # Player 1 draws 2 cards. One face-down, one face-up. They are added to the stack.
        if player1.hasCards() and player2.hasCards():
            # Player 1 draws a card
            warCard1 = player1.drawCard()
            stack.update({str(warCard1): player1.discard(warCard1)})

            # Player 1 draws a second card (if they have one)
            if player1.hasCards():
                print("The " + str(warCard1) + " is placed face-down.")
                warCard2 = player1.drawCard()
                stack.update({str(warCard2): player1.discard(warCard2)})
            else: # The player is out of cards, and the first card they played should be used in the war
                warCard2 = warCard1

            # Player 2 draws a card
            warCard3 = player2.drawCard()
            stack.update({str(warCard3): player2.discard(warCard3)})

            # Player 2 draws a second card (if they have one)
            if player2.hasCards():
                print("The " + str(warCard3) + " is placed face-down.")
                warCard4 = player2.drawCard()
                stack.update({str(warCard4): player2.discard(warCard4)})
            else:# The player is out of cards, and the first card they played should be used in the war
                warCard4 = warCard3

        else: # One of the players is out of cards, and the game is over.
            gameOver(player1, player2)

        print("--------------------")

        # The player with the higher-value card wins all of the cards in the stack.
        if warCard2 < warCard4: # If warCard2 loses...
            hand2.update(stack) # Player 2 takes all of the cards in the stack
            print("\n" + player2.name + " wins the war, and takes the following cards:")
            for card in enumerate(stack, start=1):
                print(card)
            return

        elif warCard2 > warCard4: # If warCard4 loses...
            hand1.update(stack) # Player 1 takes all of the cards in the stack
            print("\n" + player1.name + " wins the war, and takes the following cards:")
            for card in enumerate(stack, start=1):
                print(card)
            return

        # If the cards are the same value, the war continues.
        elif warCard2 == warCard4:
            print("\nThe war continues!\n")


def makeDeck(deck):
    # Initializes the playing deck (Ace of Spades, Ace of Hearts, Ace of Diamonds, Ace of Clubs, 2 of Spades, etc.)
    for rank in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]:
        for suit in [0, 1, 2, 3]:
            card = Card(rank, suit)
            deck.update({str(card) : card})

def dealCards(deck, player1, player2):
    hand1 = player1.getHand()
    hand2 = player2.getHand()

    while len(deck) > 0:
        # Randomly select a card from the deck
        card = random.choice(list(deck.keys()))
        # Update Player 1's hand with the card popped from the deck
        hand1.update({str(card) : deck.pop(card)})

        # Randomly select a card from the deck
        card = random.choice(list(deck.keys()))
        # Update Player 2's hand with the card popped from the deck
        hand2.update({str(card): deck.pop(card)})

def gameOver(player1, player2):
    print("========== GAME OVER ==========")
    if player1.cardCount() == 0:
        print("\n" + player1.name + " is out of cards. " + player2.name + " wins!")

    elif player2.cardCount() == 0:
            print("\n" + player2.name + " is out of cards. " + player1.name + " wins!")

    else:
        print("Player 1 has cards? " + str(player1.hasCards()))
        print(player1.cardCount())
        print("Player 2 has cards? " + str(player2.hasCards()))
        print(player2.cardCount())

    exit()
newGame()
