def calculate_score(cards):
    sumscore = 0
    comp = ["K", "Q", "J"]
    if cards[0] in comp and cards[1] in comp:
        sumscore += 0
    else:
        if type(cards[0]) == int:
            sumscore += cards[0]
        if type(cards[1]) == int:
            sumscore += cards[1]
        if cards[0] == "A":
            sumscore += 1
        if  cards[1] == "A":
            sumscore += 1
        if cards[0] in comp:
            sumscore += 0
        if cards[1] in comp:
            sumscore += 0
        if cards[0] == 10:
            sumscore += 0
        if cards[1] == 10:
            sumscore += 0
        if sumscore >= 10:
            sumscore -= 10
    return sumscore

def calculate_extra(cards, cards1):
    sumscore = 0
    cards += cards1
    comp = ["K", "Q", "J"]
    if cards[0] == "J" and cards[1] == "K" and cards[2] == "Q":
        sumscore += 7
    elif cards[0] in comp:
        sumscore += 0
    else:
        if cards[0] == cards1[0] == cards1[1]:
            sumscore += 7
        if type(cards[0]) == int:
            sumscore += cards[0]
        if cards[0] == "A":
            sumscore += 1
        if cards[0] in comp:
            sumscore += 10
        if sumscore >= 10:
            sumscore -= 10
    return sumscore


def deal_card():
    """Returns a random card"""
    cards = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]
    return random.choice(cards)

def deal_rank():
    """Returns a random card"""
    cards = ["♠️", "♣️", "♥️", "♦️"]
    return random.choice(cards)

def compare(aaa,bbb):
    if aaa > bbb:
        return "Player on Fire!! 🔥"
    if aaa == bbb:
        return "You both Equal! 🤝🏻"
    else:
        return "Dealer Win!! 😭"

def more10(xxx, yyy):
    sum = xxx+yyy
    if xxx+yyy >= 10:
        sum -= 10
    return sum

def win():
    sent = ["You Just Won!!! 💯", "You actually Beat Dealer!! 😱", "Player on Fire!! 🔥", "ํYou got it!! 🥶"]
    return random.choice(sent)

def lose():
    sent = ["Dealer Win!! 👀", "Nice Try 👏🏼", "You messed up 🥶", "Dealer Bang!! 🙄"]
    return random.choice(sent)

def equal():
    sent = ["What a luck 👻", "You both Equal 😉"]
    return random.choice(equal)

import random
cards = ['K', 'Q', 'J', 10, 9, 8, 7, 6, 5, 4, 3, 2]
ranks = ["♠️", "♣️", "♥️", "♣", "♦️"]
namedcard = {'A': 1, 'J': 11,'Q': 12, 'K': 13}
def pick_a_card(cards, ranks):
    card = random.choices(cards, k=3)
    rank = random.choices(ranks, k=3)
    hand = card + rank
    print(hand)
    if hand[3] == hand[4] == hand[5]:
        print('You Got A Flush')
    elif hand[0] == hand[1] == hand[2]:
        print('You Got A Three of Kind')
    if 'K' in hand and 'Q' in hand and 'J' in hand:
        print('That a sage')
pick_a_card(cards, ranks)


def isflush(hand):
    if hand[3] == hand[4] == hand[5]:
        print('You Got A Flush')

def isthreeofkind(hand):
    if hand[0] == hand[1] == hand[2]:
        print('You Got A Three of Kind')
    
def isstrightflush(hand, card):
    if (max(card) - min(card) + 1) == len(card) and hand[3] == hand[4] == hand[5]:    ###ทำไงให้มันมองข้อความเป็นเลขตาม dict ฟังชั่นนี้ฉันไม่สามารถ😱
        print('It a strightflush, so luckly la~')

def issage(hand):
    if 'K' in hand and 'Q' in hand and 'J' in hand:
        print('That a sage! godly')





