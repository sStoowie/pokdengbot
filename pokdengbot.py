import discord
import random
bot = discord.Bot()

def calculate_score(cards):
    sumscore = 0
    comp = ["K", "Q", "J"]
    if type(cards[0]) == int:
        sumscore += cards[0]
    if type(cards[1]) == int:
        sumscore += cards[1]
    if cards[0] == "A":
        sumscore += 1
    if  cards[1] == "A":
        sumscore += 1
    if cards[0] in comp:
        sumscore += 10
    if cards[1] in comp:
        sumscore += 10
    if sumscore >= 10:
        sumscore -= 10
    return sumscore
def deal_card():
    """Returns a random card"""
    cards = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2, "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2,\
             "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2, "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]
    return random.choice(cards)

def compare(aaa,bbb):
    if aaa > bbb:
        return "Player on Fire"
    else:
        return "Dealer As always"

add = ["♠️", "♣️", "♥️", "♣", "♦️"]

dealer_card = []
player_card = []
dealer_score = 0
player_score = 0
for _ in range(2):
    player_card.append(deal_card())
    dealer_card.append(deal_card())
dealer_score = calculate_score(dealer_card)
player_score = calculate_score(player_card)
@bot.event
async def on_ready():
    print("I am online!!")
@bot.slash_command(name = "hand", description="จั่วไพ่")

async def main(ctx):
    embed = discord.Embed(title="POKDENG", description="เริ่มตาของคุณ!!!", color=0xe6337a)
    embed.add_field(name="Your hand", value=random.choice(add)+str(player_card[0])+"  "+random.choice(add)+str(player_card[1]), inline=True)
    embed.add_field(name="Dealer hand", value=random.choice(add)+str(dealer_card[0])+"  "+random.choice(add)+str(dealer_card[1]), inline=False)
    embed.add_field(name="Your Score", value=calculate_score(player_card), inline=True)
    embed.add_field(name="Dealer Score", value=calculate_score(dealer_card), inline=True)
    embed.set_thumbnail(url='https://i.imgur.com/tVbh1Ke.png')
    embed.add_field(name="The Winner Is", value=compare(calculate_score(player_card), calculate_score(dealer_card)), inline=False)
    await ctx.respond("มาเล่นกันเถอะ!!!!", embed=embed)
    #ตอนกดปุ่ม(interation)
    button_hit = Button(label='Hit', style=discord.ButtonStyle.green, emoji='👍')
    button_stay = Button(label='Stay', style=discord.ButtonStyle.red, emoji='✋')
    async def button_callback(interation):
        await interation.response.send_message('ทำไงต่ออะ')
    button_hit.callback = button_callback
    button_stay.callback = button_callback
    # แอดปุ่ม
    view = View()
    view.add_item(button_hit)
    view.add_item(button_stay)
    await ctx.send('',view=view)
bot.run('MTA0MTI1MjE0MTM3NDkwMjM4Mg.GWV-Wr.Nsw3we4p9g0yQU_KvsWbiINZaEsc8egfzt6c88')

