"""Here Function"""
def sf(player_hands):
    """Returns a random card"""
    player_hands.sort()
    face = ["K", "Q", "J"]
    total = 0
    if player_hands[0] in face and player_hands[1] in face and player_hands[2] in face:
        print("เซียน")
    elif player_hands[0] == player_hands[1] == player_hands [2]: #ตอง
        total = 7
        print("ตอง")
sf()
