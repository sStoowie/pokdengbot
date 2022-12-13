import discord
import random
from discord.ui import Button, View
from discord.ext import commands
bot = discord.Bot()

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

def more10(xxx, yyy):
    sum = xxx+yyy
    if xxx+yyy >= 10:
        sum -= 10
    return sum


def win():
    sent = ["You Just Won!!! 💯", "You actually Beat Dealer!! 😱", "Player on Fire!! 🔥", "ํYou got it!! 🥶", "Shoot!!! 😍"]
    return random.choice(sent)

def lose():
    sent = ["Dealer Win!! 👀", "Hi newbie!! 👏🏼", "You messed up! 🥶", "Damn it!! 👿", "Try again next round! 😗", "GG you lose 🤪"]]
    return random.choice(sent)

def equal():
    sent = ["What a luck 👻", "You both Equal 😉"]
    return random.choice(sent)
@bot.event
async def on_ready():
    print(bot.user, "is online!!")
@bot.slash_command(name = "hand", description="Draw Your 2 Cards")

async def main(ctx):
    dealer_card = []
    player_card = []
    player_extra_rank = []
    player_rank = []
    dealer_rank = []
    dealer_extra = []
    dealer_extra_rank = []
    for _ in range(2):
        player_rank.append(deal_rank())
        dealer_rank.append(deal_rank())
    for _ in range(2):
        player_card.append(deal_card())
        dealer_card.append(deal_card())
    dealer_extra.append(deal_card())
    dealer_extra_rank.append(deal_rank())
    embed = discord.Embed(title="This is your Card", color=0xfc0f03)
    embed.set_author(name="POKDENG", icon_url="https://i.imgur.com/yPdRjdq.jpeg")
    embed.add_field(name="Your hand", value=str(player_rank[0])+str(player_card[0])+"  "+str(player_rank[1])+str(player_card[1]), inline=True)
    embed.add_field(name="Dealer hand", value="??", inline=False)
    embed.add_field(name="Your Score", value=calculate_score(player_card), inline=True)
    embed.add_field(name="Dealer Score", value="?", inline=True)
    embed.set_thumbnail(url='https://i.imgur.com/yPdRjdq.jpeg')
    embed.set_footer(text="© copyright by tothetop", icon_url="https://i.imgur.com/yPdRjdq.jpeg")
    #embed.add_field(name="The Winner Is", value=compare(calculate_score(player_card), calculate_score(dealer_card)), inline=False)
    await ctx.respond("Welcome Mr.%s" %ctx.user, embed=embed)


    button_hit = Button(label='Hit', style=discord.ButtonStyle.green, emoji='👍')
    button_stay =Button(label='Stay', style=discord.ButtonStyle.red, emoji='🖐')
    async def stay_callback(interation):
        if interation.user == ctx.author:
            if calculate_score(dealer_card) > 4:
                embed = discord.Embed(title="", color=0xfc0f03)
                embed.set_author(name="POKDENG", icon_url="https://i.imgur.com/yPdRjdq.jpeg")
                embed.add_field(name="Your hand", value=str(player_rank[0])+str(player_card[0])+"  "+str(player_rank[1])+str(player_card[1]), inline=True)
                embed.add_field(name="Dealer hand", value=str(dealer_rank[0])+str(dealer_card[0])+"  "+str(dealer_rank[1])+str(dealer_card[1]), inline=False)
                embed.add_field(name="Your Score", value=calculate_score(player_card), inline=True)
                embed.add_field(name="Dealer Score", value=calculate_score(dealer_card), inline=True)
                embed.set_thumbnail(url='https://i.imgur.com/yPdRjdq.jpeg')
                embed.add_field(name="🏆 The Winner Is 🏆", value=compare(calculate_score(player_card), calculate_score(dealer_card)), inline=False)
                embed.set_footer(text="© copyright by tothetop", icon_url="https://i.imgur.com/yPdRjdq.jpeg")
                await interation.response.send_message("", embed=embed)
            else:
                embed = discord.Embed(title="", color=0xfc0f03)
                embed.set_author(name="POKDENG", icon_url="https://i.imgur.com/yPdRjdq.jpeg")
                embed.add_field(name="Your hand", value=str(player_rank[0])+str(player_card[0])+"  "+str(player_rank[1])+str(player_card[1]), inline=True)
                embed.add_field(name="Dealer hand", value=str(dealer_rank[0])+str(dealer_card[0])+"  "+str(dealer_rank[1])+str(dealer_card[1])+"  "+str(dealer_extra_rank[0])+str(dealer_extra[0]), inline=False)
                embed.add_field(name="Your Score", value=calculate_score(player_card), inline=True)
                embed.add_field(name="Dealer Score", value=more10(calculate_score(dealer_card), calculate_extra(dealer_extra, dealer_card)), inline=True)
                embed.set_thumbnail(url='https://i.imgur.com/yPdRjdq.jpeg')
                embed.add_field(name="🏆 The Winner Is 🏆", value=compare(calculate_score(player_card), more10(calculate_score(dealer_card), calculate_extra(dealer_extra, dealer_card))), inline=False)
                embed.set_footer(text="© copyright by tothetop", icon_url="https://i.imgur.com/yPdRjdq.jpeg")
                await interation.response.send_message("", embed=embed)
        else: await interation.response.send_message("It's Not Your Turn")
    async def button_callback(interation):
        if interation.user == ctx.author:
            if calculate_score(dealer_card) > 4:
                player_extra_card = []
                player_extra_card.append(deal_card())
                player_extra_rank.append(deal_rank())
                embed = discord.Embed(title="", color=0xfc0f03)
                embed.set_author(name="POKDENG", icon_url="https://i.imgur.com/yPdRjdq.jpeg")
                embed.add_field(name="Your hand", value=str(player_rank[0])+str(player_card[0])+"  "+str(player_rank[1])+str(player_card[1])+"  "+str(player_extra_rank[0])+str(player_extra_card[0]), inline=True)
                embed.add_field(name="Dealer hand", value=str(dealer_rank[0])+str(dealer_card[0])+"  "+str(dealer_rank[1])+str(dealer_card[1]), inline=False)
                embed.add_field(name="Your Score", value=more10(calculate_score(player_card), calculate_extra(player_extra_card, player_card)), inline=True)
                embed.add_field(name="Dealer Score", value=calculate_score(dealer_card), inline=True)
                embed.set_thumbnail(url='https://i.imgur.com/yPdRjdq.jpeg')
                embed.set_footer(text="© copyright by tothetop", icon_url="https://i.imgur.com/yPdRjdq.jpeg")
                embed.add_field(name="🏆 The Winner Is 🏆", value=compare(more10(calculate_score(player_card), calculate_extra(player_extra_card, player_card)), calculate_score(dealer_card)), inline=False)
            else:
                player_extra_card = []
                player_extra_card.append(deal_card())
                player_extra_rank.append(deal_rank())
                embed = discord.Embed(title="", color=0xfc0f03)
                embed.set_author(name="POKDENG", icon_url="https://i.imgur.com/yPdRjdq.jpeg")
                embed.add_field(name="Your hand", value=str(player_rank[0])+str(player_card[0])+"  "+str(player_rank[1])+str(player_card[1])+"  "+str(player_extra_rank[0])+str(player_extra_card[0]), inline=True)
                embed.add_field(name="Dealer hand", value=str(dealer_rank[0])+str(dealer_card[0])+"  "+str(dealer_rank[1])+str(dealer_card[1])+"  "+str(dealer_extra_rank[0])+str(dealer_extra[0]), inline=False)
                embed.add_field(name="Your Score", value=more10(calculate_score(player_card), calculate_extra(player_extra_card, player_card)), inline=True)
                embed.add_field(name="Dealer Score", value=more10(calculate_score(dealer_card), calculate_extra(dealer_extra, dealer_card)), inline=True)
                embed.set_thumbnail(url='https://i.imgur.com/yPdRjdq.jpeg')
                embed.set_footer(text="© copyright by tothetop", icon_url="https://i.imgur.com/yPdRjdq.jpeg")
                embed.add_field(name="🏆 The Winner Is 🏆", value=compare(more10(calculate_score(player_card), calculate_extra(player_extra_card, player_card)), more10(calculate_score(dealer_card), calculate_extra(dealer_extra, dealer_card))), inline=False)
            await interation.response.send_message("", embed=embed)
        else: await interation.response.send_message("It's Not Your Turn")
    button_hit.callback = button_callback
    button_stay.callback = stay_callback
    view = View()
    view.add_item(button_hit)
    view.add_item(button_stay)
    await ctx.send('',view=view)
bot.run('Token Right here')
