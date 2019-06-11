import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import requests
import random

Bot = commands.Bot(command_prefix = '?')
Bot.remove_command('help')
token ='NTY5NDYwMDgyMTY1ODA5MTUz.XPvtxg.MTpLkeGzPunQ2NujO3W0g0ZWOAI'
channel = Bot.get_channel(572075184606150657)

@Bot.event
async def on_ready():
    print('------')
    print('Я активен!')
    print('------')
    game = discord.Game("?help")
    await Bot.change_presence(status=discord.Status.idle, activity=game)

@Bot.command()
async def cat (ctx):
    author = str(ctx.message.author)
    response = requests.get('https://aws.random.cat/meow')
    data = response.json()
    await ctx.send(data['file'])
    print('[?cat] - done. Induced '+ author)
    await channel.send('[?cat] - done. Induced '+ author)
@Bot.command() 
async def dog (ctx):
    author = str(ctx.message.author)
    response = requests.get('https://random.dog/woof.json')
    data = response.json()
    await ctx.send(data['url'])
    print('[?dog] - done. Induced '+ author)
    await channel.send(print('[?dog] - done. Induced '+ author))

@Bot.command()
@commands.has_permissions(administrator= True)
async def clear(ctx, amount: int):
    author = str(ctx.message.author)
    await ctx.channel.purge(limit=amount)
    print("[?clear] - done. Delete " + format(amount) + " message. Induced "+ author)
    await channel.send("[?clear] - done. Delete " + format(amount) + " message. Induced "+ author)
@Bot.command()
async def hi(ctx):
    author = ctx.message.author
    await ctx.send('Привет ,'+ format(author.mention)+ ', ты крутой!')
    print('[?hi] - done. Induced '+ str(author))
    await chanel.send('[?hi] - done. Induced '+ str(author))
@Bot.command()
async def help(ctx):
    author = str(ctx.message.author)
    emb= discord.Embed(title = "Мои команды",color = 0x39d0d6 )
    emb.add_field(name="?hi", value= "Если ты еще сегодня ни с кем не здоровался,я сделаю это вместо твоих друзей.", inline=False)
    emb.add_field(name="?cat", value= "Получить рандомную фотографию(или ГИФку) кошки.", inline=True)
    emb.add_field(name="?dog", value= "Получить рандомную фотографию(или ГИФку) собаки.", inline=True)
    emb.add_field(name="?ava", value= "Показывает аватар пользователя, если он не указан - показывает аватар автора сообщения.", inline=False)
    emb.add_field(name="?rnum",value="Получить рандомное число от 1 до 100.",inline=True)
    emb.add_field(name="?coin", value= "Бросить монетку.", inline=False)
    await ctx.send(embed=emb)
    print("[?help] - done. Induced "+ author)
    await channel.send("[?help] - done. Induced "+ author)

@Bot.command()
async def ava(ctx, member : discord.Member = None):
    author = str(ctx.message.author) 
    user = ctx.message.author if (member == None) else member
    await ctx.message.delete()
    embed = discord.Embed(title=f'Аватар пользователя {user}',color=user.color)
    embed.set_footer(text= f'Вызвано: {ctx.message.author}', icon_url= str(ctx.message.author.avatar_url))
    embed.set_image(url=user.avatar_url)
    await ctx.send(embed=embed)
    print("[?ava] - done. Induced "+ author)
    await channel.send("[?ava] - done. Induced "+ author)
@Bot.command(pass_context= True)
async def rnum(ctx):
    author = str(ctx.message.author) 
    await ctx.send("**{}, Рандомное число: __{}__**".format(ctx.message.author.mention, random.randint(1, 100)))
    await asyncio.sleep(1)
    await ctx.delete_message(ctx.message)
    print("[?rnum] - done. Induced "+ author)
    await channel.send("[?rnum] - done. Induced "+ author)

@Bot.command()
async def coin(ctx):
    author = str(ctx.message.author)
    num=random.randint(1,2)
    if (num == 1):
       	await ctx.send("Вам выпал - `Орёл`")
       	print("[?coin] - done. Induced "+ author)
        await channel.send("[?coin] - done. Induced "+ author)
    if(num == 2):	
       	await ctx.send("Вам выпала - `Решка`")
       	print("[?coin] - done. Induced "+ author)
        await channel.send("[?coin] - done. Induced "+ author)



Bot.run(token)
