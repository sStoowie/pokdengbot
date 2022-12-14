def calculate_score(cards):
    sumscore = 0
    comp = ["K", "Q", "J"]
    if cards[0] in comp and cards[1] in comp:
        sumscore += 0
    elif cards[0] == 10 and cards[1] == 10:
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
    if cards[0] in comp and cards1[0] in comp and cards1[1] in comp:
        sumscore += 10
    elif cards[0] == cards1[0] == cards1[1]:
        sumscore += 10
    elif cards[0] in comp:
        sumscore += 0
    else:
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
        return win()
    if aaa == bbb:
        return equal()
    else:
        return lose()

def more10(xxx, yyy, cards, cards1, var):
    sum = xxx+yyy
    comp = ["K", "Q", "J"]
    if cards[0] in comp and cards1[0] in comp and cards1[1] in comp:
        sum = sum
    elif cards[0] == cards1[0] == cards1[1]:
        sum = var*0+sum
    else:
        if xxx+yyy >= 10:
            sum -= 10
    return sum


def win():
    sent = ["You Just Won!!! 💯", "You actually Beat Dealer!! 😱", "Player on Fire!! 🔥", "ํYou got it!! 🥶", "Shoot!!! 😍"]
    return random.choice(sent)

def lose():
    sent = ["Dealer Win!! 👀", "Dealer As Always 👏🏼", "Dealer on the top!! 🥶", "Try again next round! 😗", "GG you lose 🤪"]
    return random.choice(sent)

def equal():
    sent = ["What a luck 👻", "You both Equal 😉"]
    return random.choice(sent)
