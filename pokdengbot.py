import discord
import random
    
bot = discord.Bot()
rank = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
add = ["♠️", "♥️", "♣", "♦️"]
card = random.choice(add)+random.choice(rank)
mycard1 = random.choice(rank)
mycard2 = random.choice(rank)
dealercard = random.choice(rank)
dealercard = random.choice(rank)
score = 0
if mycard1 in ["K", "Q", "J"]:
    score += 10
elif mycard1 == "A":
    score += 1
else:
    score += int(mycard1)
if mycard2 in ["K", "Q", "J"]:
    score += 10
elif mycard2 == "A":
    score += 1
else:
    score += int(mycard2)
@bot.event
    
async def on_ready():
    print("I am online!!")
@bot.slash_command(name = "hand")
    
async def main(ctx):
    embed = discord.Embed(title="POKDENG", description="เริ่มตาของคุณ!", color=0xe6337a)
    embed.add_field(name="Your hand", value=random.choice(add)+mycard1+"  "+random.choice(add)+mycard2, inline=True)
    embed.add_field(name="Dealer hand", value="??", inline=True)
    embed.add_field(name="Your score", value=score, inline=False)
    embed.set_thumbnail(url='https://i.imgur.com/tVbh1Ke.png')
    await ctx.respond(embed=embed)
bot.run('MTA0MTI1MjE0MTM3NDkwMjM4Mg.GxipOy.b_kWP6llWII5UHAYdjk3YhBi_-TUdD5ui5v94M')

