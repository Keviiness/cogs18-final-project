import random

# possible number values for blackjack
deck = [2,3,4,5,6,7,8,9,10,11,12] 
# different face cards for value of 11
face_cards = ['J','K','Q'] 

# deals the hands for both player and dealer
def deal_cards(deck): 
    
    hand = []
    
    # picks cards from deck
    while len(hand) < 2:
        hand.append(random.choice(deck)) 
 
    # if hand contains 11 pick a face card from the deck
    if(hand[0] == 11): 
        hand[0] = random.choice(face_cards)
    if(hand[1] == 11):
        hand[1] = random.choice(face_cards)
    
    # if card is 12 we define 12 to be an Ace which can be 1 or 11
    if(hand[0] == 12):
        hand[0] = 'A'
    if(hand[1] == 12):
        hand[1] = 'A'
        
    return hand

# calculates the total of the hand
def calc_total(hand):
    
    # total value for player/dealer hand
    total = 0
    
    # calculates the number value KQJ = 10, A = 1 OR 11
    for card in hand:            
        if(card in face_cards):
            total = total + 10
        elif(card == 'A'):
            if total >= 11: 
                total = total + 1
            else: 
                total = total + 11                
        else:
            total = total + card
    
    return total

# adds a card to the player's hand when he wishes to hit
def hit(hand):
    
    # chooses a random card from the deck
    card = random.choice(deck)
    
    if(card == 11):
        card = random.choice(face_cards)
    elif(card == 12):
        card = 'A'   
        
    # appends the card to the hand    
    hand.append(card)
    
    return hand