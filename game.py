import random


decks = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2\
    ,"A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2\
        ,"A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2\
            ,"A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]

player_hands = []
dealer_hands = []


card = random.choice(decks)
player_hands.append(card)
decks.remove(card)
card = random.choice(decks)
dealer_hands.append(card)
decks.remove(card)
card = random.choice(decks)
player_hands.append(card)
decks.remove(card)
card = random.choice(decks)
dealer_hands.append(card)
decks.remove(card)

print('your hand =',player_hands)

total_player = 0
total_dealer = 0
face = ["K", "Q", "J"]
for card in player_hands:
    if card in range(1,11):
        total_player += card
    elif card in face:
        total_player += 10
    else:
        total_player += 1
    

for card in dealer_hands:
    if card in range(1,11):
        total_dealer += card
    elif card in face:
        total_dealer += 10
    else:
        total_dealer += 1

next = input()

if next == 'hit':
    card = random.choice(decks)
    player_hands.append(card)
    decks.remove(card)
    if card in face:
        total_player += 10
    elif card in range(1, 11):
        total_player += card
    else:
        total_player += 1
else:
    card = random.choice(dealer_hands)
    if card == 'hit':
        dealer_hands.append(card)
        decks.remove(card)
        if card in face:
            total_dealer += 10
        elif card in range(1, 11):
            total_dealer += card
        else:
            total_dealer += 1


if total_dealer > total_player:
    print('dealer card =', dealer_hands, 'your card =', player_hands, 'score:', total_dealer, 'vs', total_player)
    print('YOU LOSE!!')
elif total_player > total_dealer:
    print('dealer card =', dealer_hands, 'your card =', player_hands, '  score:', total_dealer, 'vs', total_player)
    print('YOU WIN!!')
else:
    print('dealer card =', dealer_hands, 'your card =', player_hands, '  score:', total_dealer, 'vs', total_player)
    print('DRAW')

