import functions

# total possible cards to get in our deck

possible_deck = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
test_hand = functions.deal_cards(functions.deck)

# checking if our cards in our hand are valid from our 

assert(test_hand[0] in possible_deck)
assert(test_hand[1] in possible_deck)

# checking if calculating total is correct/accurate

# An ace is 11 or 1 depending on the player's total
assert(functions.calc_total(['A','A']) == 12)
# Face cards are a 10 in value
assert(functions.calc_total(['J','A']) == 21)
assert(functions.calc_total([10,2]) == 12)

# checking if hitting has correct behavior

functions.hit(test_hand)
# if a player hits a card is added into their hand
assert(len(test_hand) > 2)
# checking if the added card is also in the possible deck
assert(test_hand[-1] in possible_deck)

