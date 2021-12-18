import random,os

cardName = {
  1 : 'Ace',
  2 : 2,
  3 : 3,
  4 : 4,
  5 : 5,
  6 : 6,
  7 : 7,
  8 : 8,
  9 : 9,
  10 : 10,
  11 : 'Jack',
  12 : 'Queen',
  13 : 'King'
}
cardSuits = {
  'C' : 'Clubs',
  'H' : 'Hearts',
  'D' : 'Diamonds',
  'S' : 'Spades'
}



class Card:
  def __init__(self,rank,suit):
    self.rank = rank
    self.suit = suit
  def __str__(self):
    return (f'{cardName[self.rank]}  Of {cardSuits[self.suit]}')
  def getRank(self):
    return self.rank
  def getSuit(self):
    return self.suit

  def BJValue(self):
    if self.rank > 9:
      return 10
    else:
      return self.rank

deck = []
hand = {'computer' : [], 'human' : []}
score = {'computer' : 0,'human' : 0}
# score['computer']
# hand['computer']

for suit in cardSuits.keys():
  for rank in cardName.keys():
    deck.append(Card(rank,suit))

random.shuffle(deck)
random.shuffle(deck)
random.shuffle(deck)


# for i in deck:
#   print(i)

keepPlaying = True

def cardShow(cardHand):
  for card in cardHand:
    print(card)

def countHand(cardHand):
  count = 0
  for card in cardHand:
    count += card.BJValue()
  return count

def showCount(cardHand):
  print("Count: ", countHand(cardHand))

# cardshow(hand['human'])
# Dealer and Player.

while keepPlaying:
  # Deal the cards.
  hand['human'].append(deck.pop(0))
  hand['computer'].append(deck.pop(0))
  hand['human'].append(deck.pop(0))
  hand['computer'].append(deck.pop(0))

  playHuman = True
  bustedHuman = False

  while playHuman:
    print (f'Computer: {score["computer"]} \t Human: {score["human"]}')
   
    print(f"Computer Shows : {hand['computer'][-1]}")
    print("Your Hand: ")
    cardShow(hand['human'])
    print("Your Count: ")
    showCount(hand['human'])

  

    inputCycle = True

    while inputCycle:
      Options = input("Press (H)it, (S)tand, or (Q)uit: ").upper()
      if Options != 'H' or 'S' or 'Q':
        playHuman = False
        keepPlaying = False
      if Options == 'H':
        hand['human'].append(deck.pop(0))
        print("Your Hand: ")
        cardShow(hand['human'])
        showCount(hand['human'])
        if countHand(hand['human']) > 21:
          playHuman = False
          bustedHuman = True

      elif Options == 'S':
        playHuman = False
        inputCycle= False

      elif Options == 'Q':
        bustedHuman = True

  playComputer = True
  bustedComputer = False

  while playComputer and bustedHuman == False:
    if countHand(hand['computer']) <18:
      hand['computer'].append(deck.pop(0))
    else:
      playComputer = False
    if countHand(hand['computer']) > 21:
      playComputer = False
      bustedComputer = True

  if bustedComputer:
    print("Human wins")
    score['human'] += 1
  elif bustedHuman:
    print("Computer wins")  
    score['computer'] += 1
  elif countHand(hand['human']) == countHand(hand['computer']):
    print("Draw")
  elif countHand(hand['human']) > countHand(hand['computer']):
    print("Human wins")
    score['human'] += 1
  else:
    print("Computer wins")
    score['computer'] += 1

  print("Computer Hand: ")
  cardShow(hand['computer'])

  showCount(hand['computer'])
  
  if input('(Q)uit or press enter for next round').upper() == 'Q':
    print("Game Ends")
    keepPlaying = False
  else: 
    deck.extend(hand['human'])
    deck.extend(hand['computer'])

    del hand['computer'] [:]
    del hand['human'] [:]
    keepPlaying = True
    os.system('clear')
