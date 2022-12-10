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
        if sumscore >= 10:
            sumscore -= 10
    return sumscore

def calculate_extra(cards):
    sumscore = 0
    comp = ["K", "Q", "J"]
    if cards[0] in comp:
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
    cards = ["♠️", "♣️", "♥️", "♣", "♦️"]
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

@bot.event
async def on_ready():
    print("I am online!!")
@bot.slash_command(name = "hand", description="จั่วไพ่")

async def main(ctx):
    dealer_card = []
    player_card = []
    player_extra_rank = []
    player_rank = []
    dealer_rank = []
    for _ in range(2):
        player_rank.append(deal_rank())
        dealer_rank.append(deal_rank())
    for _ in range(2):
        player_card.append(deal_card())
        dealer_card.append(deal_card())
    embed = discord.Embed(title="POKDENG", description="นี่คือไพ่ในมือคุณ", color=0xe6337a)
    embed.add_field(name="Your hand", value=str(player_rank[0])+str(player_card[0])+"  "+str(player_rank[1])+str(player_card[1]), inline=True)
    embed.add_field(name="Dealer hand", value="??", inline=False)
    embed.add_field(name="Your Score", value=calculate_score(player_card), inline=True)
    embed.add_field(name="Dealer Score", value="?", inline=True)
    embed.set_thumbnail(url='https://i.imgur.com/tVbh1Ke.png')
    #embed.add_field(name="The Winner Is", value=compare(calculate_score(player_card), calculate_score(dealer_card)), inline=False)
    await ctx.respond("มาเล่นกันเถอะ!!!!", embed=embed)


    button_hit = Button(label='Hit', style=discord.ButtonStyle.green, emoji='👍')
    button_stay =Button(label='Stay', style=discord.ButtonStyle.red, emoji='🖐')
    async def stay_callback(interation):
        embed = discord.Embed(title="POKDENG", color=0xe6337a)
        embed.add_field(name="Your hand", value=str(player_rank[0])+str(player_card[0])+"  "+str(player_rank[1])+str(player_card[1]), inline=True)
        embed.add_field(name="Dealer hand", value=str(dealer_rank[0])+str(dealer_card[0])+"  "+str(dealer_rank[1])+str(dealer_card[1]), inline=False)
        embed.add_field(name="Your Score", value=calculate_score(player_card), inline=True)
        embed.add_field(name="Dealer Score", value=calculate_score(dealer_card), inline=True)
        embed.set_thumbnail(url='https://i.imgur.com/tVbh1Ke.png')
        embed.add_field(name="🏆 The Winner Is 🏆", value=compare(calculate_score(player_card), calculate_score(dealer_card)), inline=False)
        await interation.response.send_message("", embed=embed)
    async def button_callback(interation):
        player_extra_card = []
        player_extra_card.append(deal_card())
        player_extra_rank.append(deal_rank())
        embed = discord.Embed(title="POKDENG", color=0xe6337a)
        embed.add_field(name="Your hand", value=str(player_rank[0])+str(player_card[0])+"  "+str(player_rank[1])+str(player_card[1])+"  "+str(player_extra_rank[0])+str(player_extra_card[0]), inline=True)
        embed.add_field(name="Dealer hand", value=str(dealer_rank[0])+str(dealer_card[0])+"  "+str(dealer_rank[1])+str(dealer_card[1]), inline=False)
        embed.add_field(name="Your Score", value=more10(calculate_score(player_card), calculate_extra(player_extra_card)), inline=True)
        embed.add_field(name="Dealer Score", value=calculate_score(dealer_card), inline=True)
        embed.set_thumbnail(url='https://i.imgur.com/tVbh1Ke.png')
        embed.add_field(name="🏆 The Winner Is 🏆", value=compare(more10(calculate_score(player_card), calculate_extra(player_extra_card)), calculate_score(dealer_card)), inline=False)
        await interation.response.send_message("", embed=embed)
    button_hit.callback = button_callback
    button_stay.callback = stay_callback
    # แอดปุ่ม
    view = View()
    view.add_item(button_hit)
    view.add_item(button_stay)
    await ctx.send('',view=view)
