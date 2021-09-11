import discord
import random
import requests
from Keep_alive import keep_alive
from discord.ext import commands
keep_alive()

bot = commands.Bot(command_prefix="-")
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print("------------------")
    print("       LOG:       ")

@bot.command()
async def about(ctx):
    await ctx.send("Since this bot was created by Snowstorm and Inventboss, this is his github link https://github.com/InventBoss")
@bot.command()
async def ball(ctx, question='no question asked'):
    if not question=='no question asked':
        response = ['certainly', 'possibly', 'impossible']
        ball = random.choice(response)
        await ctx.send(ball)
@bot.command()
async def rps(ctx, your_move='no value given'):
    move=['rock','paper','scissors']
    bot_move=random.choice(move)
    result=0
    if your_move == 'rock' and bot_move=='scissors':
        result='you win'
    if your_move == 'rock' and bot_move =='paper':
        result='you lose'
    if your_move == 'paper' and bot_move =='rock':
        result='you win'
    if your_move == 'paper' and bot_move =='scissors':
        result='you lose'
    if your_move == 'scissors'and bot_move =='paper':
        result='you win'
    if your_move == 'scissors' and bot_move =='rock':
        result='you lose'
    if your_move == bot_move:
        result='its a draw'
    await ctx.send(f"{bot_move}\n{result}")
@bot.command()
async def dog(ctx):
    picture = requests.get('https://dog.ceo/api/breeds/image/random')
    result = picture.json()
    await ctx.send(result['message'])
@bot.command()
async def coinflip(ctx):
    result = ['Heads','Tails']
    await ctx.send(random.choice(result))
@bot.command()
async def levels(ctx):
    id = random.randint(128, 70000000)
    level = requests.get(f'https://gdbrowser.com/api/level/{id}')
    result = level.json()
    await ctx.send(result)
#requests.get is the function you use to return info from the api




#line24, random.choice uses the list into a variable.



#defaultvalue = if there is nothing is provided, this is the value of the variable.
bot.run('ODUyMTUwMjczMDI3OTk3Njk2.YMCoyQ.6mb8aiDyNklY3EbIm5D5YVb20w4')

