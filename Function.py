"""Here Function"""
def sf():
    """Returns a random card"""
    cards = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]
    rank = ["♠️", "♣️", "♥️", "♣", "♦️"]
    player_hands = [4, 5, 3]
    player_hands.sort()
    player_dok = ["♠️", "♠️", "♠️"]
    aaa = ""
    bbb = ""
    face = ["K", "Q", "J"]
    total = 0
    if player_hands[0] in face and player_hands[1] in face and player_hands[2] in face: #เซียน
        print("เซียน")
    elif player_hands[1] - player_hands[0] and player_hands[2] - player_hands[1]: #เรียง
        total = 7
        aaa = "state"
        print("State")
    elif player_hands[1] == player_hands[0] == player_hands [3]: #ตอง
        total = 7
        print("Tong")
        
    if player_dok[0] == player_dok[1] == player_dok[2]: # flush
        bbb = "flush"
        
    if aaa == "state" and bbb == "flush": #State flush
        print("state flush")
sf()
