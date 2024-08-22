# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
from blackjack_helper1 import *

# Write all of your part 3 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.

opening = 'your'
hand_value = int(draw_starting_hand(opening))
if hand_value == 21:
  print ('Final hand: ' + str(hand_value) + '.')
  print ('BLACKJACK!')
elif hand_value > 21:
  print ('Final hand: ' + str(hand_value) + '.')
  print ('BUST.')
while hand_value < 21:
  should_hit = input('You have ' + str(hand_value) + ". Hit (y/n)? ")
  if should_hit == 'n':
    break
  elif should_hit == 'y':
    card_3 = draw_card()
  hand_value = int(card_3) + int(hand_value)
print_end_turn_status(hand_value)

opening = 'dealer'
hand_value_2 = int(draw_starting_hand(opening))
if hand_value_2 == 21:
  print ('Final hand: ' + str(hand_value) + '.')
  print ('BLACKJACK!')
elif hand_value_2 > 21:
  print ('Final hand: ' + str(hand_value) + '.')
  print ('BUST.')
while hand_value_2 < 17:
  print('Dealer has ' + str(hand_value))
  card_3 = draw_card()
  hand_value_2 = int(card_3) + int(hand_value)
print_end_turn_status(hand_value_2)

print_end_game_status(hand_value, hand_value_2)

