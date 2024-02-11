import discord
import random
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def mem(ctx):
    images = os.listdir('images')
    img_name = random.choice(images)
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def cute(ctx):
    cutie = os.listdir('cuties')
    img_cute = random.choice(cutie)
    with open(f'cuties/{img_cute}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("MTIwMTA2Nzg5ODA4OTc2Njk5Mg.Gm3zKn.d9McsEVzukpCdbyVHt2k57RCZHCMHgd11az_6E")