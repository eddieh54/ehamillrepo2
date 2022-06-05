#Poker
import random
import sys

suits = ('hearts', 'diamonds', 'spades', 'clubs')
ranks = ('ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king')
values = {'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven': 7, 'eight':8, 'nine':9, 'ten': 10, 'jack':10, 'king':10, 'queen': 10, 'ace':11}

playing = True

class Card:
  def __init__(self, suit, rank):
      #assigns cards a suit and value
      self.rank = rank
      self.suit = suit
  def __str__(self):
    #converts type to string to create a "card"
    return self.rank + ' of ' + self.suit

class Deck:
  def __init__(self):
    self.deck = [] #initializes list
    for suit in suits: #calls item from suits
      for rank in ranks: #calls item from ranks
        self.deck.append(Card(suit,rank)) #uses card suit to append individual combinations to deck list
  def __str__(self):
    deck_makeup = ''
    for card in self.deck:
      deck_comp +=  '\n' + card.__str__()
    return 'The deck has:' + deck_comp
  def shuffle(self):
    random.shuffle(self.deck) #gives a random card from the deck
  def deal(self): #assigns a random card as an object
    single_card = self.deck.pop()
    return single_card

class Hand: #generates a randomized set of cards
  def __init__(self):
    self.cards = []
    self.value = 0
    self.aces = 0
  def add_card(self,card):
    self.cards.append(card)
    self.value += values[card.rank]
  def adjust_for_ace(self): #if value exceeds 21 w/ace automatically changes value to 1
    while self.value > 21 and self.aces:
      self.value -= 10
      self.aces -= 1

class Money:
  def __init__(self):
    self.total = 500 #starting amount of money
    self.bet = 0
  def win_bet(self):
    self.total += self.bet
  def lose_bet(self):
    self.total -= self.bet

def take_bet(money):
  while True:
    try:
        money.bet = int(input("\nHow much money would you like to wager? "))
    except ValueError:
        print ("Input most be a dollar amount")
    else:  
        if money.bet > money.total:
            print(" You don't have enough money for that high of a bet, maybe you should invest instead of gambling ")
        else:
            break

def hit(deck, hand):
  hand.add_card(deck.deal()) #adds another card to the players hand
  hand.adjust_for_ace() #again, incase they're dealt an ace and the value is over 21

def hit_or_stay(deck,hand): #provides the player witht the option to hit or stay
  global playing
  while True: #while game is being played
    x = input(" Would you like to hit or stay? Type 'h' to hit or 's' to stay ")
    
    if x[0].lower() == 'h':
        hit(deck,hand)
    elif x[0].lower() == 's':
        print("dealer's turn")
    else:  
      print(" Wrong Key ")
      continue
    break

def show_some(player,dealer):
    print("\nDealers Hand:")
    print(" <card hidden.")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep = '\n ')

def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep = '\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep= '\n ')
    print("Player's Hand =", player.value)

#gamefunctions

def player_busts(player,dealer,money):
    print("You busted (went over 21)")
    money.lose_bet()

def player_wins(player,dealer,money):
    print("You Won!")
    money.win_bet()

def dealer_busts(player,dealer,money):
    print("Dealer Busts!")
    money.win_bet()

def dealer_wins(player,dealer,money):
    print("Dealer Wins!")
    money.lose_bet()

def push(player,dealer):
    print("You pushed (tied with the dealer)")

#game
while True:

    print("Welcome to BlackJack!\nYou'll start with $500\n Your goal is to get as close as possible to 21 without going over.\n The Dealer hits until they're at 17\n Aces count as 1 or 11, which ever one plays to your advantage.")

    #set up money
    player_wager = Money()

    while playing:

      #deck creation
      deck = Deck()
      deck.shuffle()

      # 2 card hand creation
      player_hand = Hand()
      player_hand.add_card(deck.deal())
      player_hand.add_card(deck.deal())

      # dealer hand creation
      dealer_hand = Hand()
      dealer_hand.add_card(deck.deal())
      dealer_hand.add_card(deck.deal())

      #set up wager
      take_bet(player_wager)

      #shows the player whats on the table
      show_some(player_hand, dealer_hand)

      if player_hand.value == 21:
        if dealer_hand.value != 21:
          player_wins(player_hand,dealer_hand,player_wager)
          pass
        else: push(player_hand, dealer_hand)
    
      hit_or_stay(deck, player_hand) #asks player to hit or stay
      show_some(player_hand, dealer_hand)

      if player_hand.value > 21:
          if dealer_hand.value > 21:
              push(player_hand,dealer_hand)
          player_busts(player_hand, dealer_hand, player_wager)

      if player_hand.value <= 21:

          hit_or_stay(deck, player_hand)
          if player_hand.value > 21:
              if dealer_hand.value > 21:
                  push(player_hand,dealer_hand)
              player_busts(player_hand, dealer_hand, player_wager)
          
          while dealer_hand.value < 17: #hits for the dealers deck if the player hasn't busted, and the dealer is under 17
              hit(deck, dealer_hand)

          show_all(player_hand, dealer_hand)

          if dealer_hand.value > 21:
              dealer_busts(player_hand, dealer_hand, player_wager)

          elif dealer_hand.value > player_hand.value:
              dealer_wins(player_hand, dealer_hand, player_wager)

          elif dealer_hand.value < player_hand.value:
              player_wins(player_hand, dealer_hand, player_wager)

          else:
              push(player_hand,dealer_hand)

      print("\nYour current balance is", player_wager.total)

      new_game = input("Would you like to play again? Type 'y' for yes or 'n' for no ")

      if new_game[0].lower() == 'y':
          continue

      if new_game[0].lower() == 'n':
          print("Good choice!")
          sys.exit()
