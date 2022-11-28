import discord
bot = discord.Bot()


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")
bot.run("45a110830e8682b6102822d786450b7d499e9d6535421361f887a89870e8b694")
# 45a110830e8682b6102822d786450b7d499e9d6535421361f887a89870e8b694
