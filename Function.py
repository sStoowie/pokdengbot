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
