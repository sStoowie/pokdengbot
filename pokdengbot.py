import discord
import random
bot = discord.Bot()
rank = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
add = ["♠️", "♣️", "♥️", "♣", "♦️"]
card = random.choice(add)+random.choice(rank)
@bot.event
async def on_ready():
    print("I am online!!")
@bot.slash_command(name = "hand")
async def main(ctx):
    embed = discord.Embed(title="POKDENG", description="Welcome to the Real POKDENG!!", color=0xe6337a)
    embed.add_field(name="Your hand", value=random.choice(add)+random.choice(rank)+"  "+random.choice(add)+random.choice(rank), inline=True)
    embed.add_field(name="Dealer hand", value=random.choice(add)+random.choice(rank)+"  "+random.choice(add)+random.choice(rank), inline=True)
    embed.set_thumbnail(url='https://i.imgur.com/tVbh1Ke.png')
    await ctx.respond(embed=embed)
bot.run('MTA0MTI1MjE0MTM3NDkwMjM4Mg.GxipOy.b_kWP6llWII5UHAYdjk3YhBi_-TUdD5ui5v94M')
