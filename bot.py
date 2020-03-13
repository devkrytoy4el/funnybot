import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import requests
import random
import os
Bot = commands.Bot(command_prefix = '?')
Bot.remove_command('help')

@Bot.event
async def on_ready():
    print('------')
    print('Я активен!')
    print('------')
    game = discord.Game("?help")
    await Bot.change_presence(status=discord.Status.idle, activity=game)

@Bot.command()
async def cat (ctx):
    сhannel = Bot.get_channel(600384214822813696)
    author = str(ctx.message.author)
    response = requests.get('https://aws.random.cat/meow')
    data = response.json()
    await ctx.send(data['file'])
    print('[?cat] - done. Induced '+ author)
    await channel.send('[?cat] - done. Induced '+ author)
    
@Bot.command() 
async def dog (ctx):
    channel = Bot.get_channel(600384214822813696)
    author = str(ctx.message.author)
    response = requests.get('https://random.dog/woof.json')
    data = response.json()
    await ctx.send(data['url'])
    print('[?dog] - done. Induced '+ author)
    await channel.send('[?dog] - done. Induced '+ author)

@Bot.command()
@commands.has_permissions(administrator= True)
async def clear(ctx, amount: int):
    channel = Bot.get_channel(600384214822813696)
    author = str(ctx.message.author)
    await ctx.channel.purge(limit=amount)
    print("[?clear] - done. Delete " + format(amount) + " message. Induced "+ author)
    await channel.send("[?clear] - done. Delete " + format(amount) + " message. Induced "+ author)

@Bot.command()
@commands.has_permissions(administrator= True)
async def say(ctx):
    channel = Bot.get_channel(600384214822813696)
    author = str(ctx.message.author)
    args = ctx.message.content.split(' ')[1:]
    await ctx.message.delete()
    await ctx.send(' '.join(args if len(args) != 0 else '**[!] | Введите контекст сообщения!**'))    
    print("[?say] - done. Delete "+ author)
    await channel.send("[?say] - done. "+ author)
    

@Bot.command()
async def hi(ctx):
    channel = Bot.get_channel(600384214822813696)
    author = ctx.message.author
    await ctx.send('Привет ,'+ format(author.mention)+ ', ты крутой!')
    print('[?hi] - done. Induced '+ str(author))
    await channel.send('[?hi] - done. Induced '+ str(author))
    
@Bot.command()
async def help(ctx):
    channel = Bot.get_channel(600384214822813696)
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
    channel = Bot.get_channel(600384214822813696)
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
    channel = Bot.get_channel(600384214822813696)
    author = str(ctx.message.author) 
    await ctx.send("**{}, Рандомное число: __{}__**".format(ctx.message.author.mention, random.randint(1, 100)))
    await asyncio.sleep(1)
    await ctx.delete_message(ctx.message)
    print("[?rnum] - done. Induced "+ author)
    await channel.send("[?rnum] - done. Induced "+ author)
@Bot.command()
async def gnum (ctx):
    channel = Bot.get_channel(600384214822813696)
    author = str(ctx.message.author)
    rnum=random.randint(1,3)
    await ctx.send("Я загадал число от 1 до 3 ,введите ?gnum и число которое ты считается ,что я угадал. \n Пример команды:?gnum_2 ")
    print('[?cat] - done. Induced '+ author)
    await channel.send('[?gnum] - done. Induced '+ author)

@Bot.command()
@commands.has_permissions(administrator= True)
async def ahelp(ctx):
    channel = Bot.get_channel(600384214822813696)
    author = str(ctx.message.author)
    emb= discord.Embed(title = "Мои команды",color = 0x39d0d6 )
    emb.add_field(name="?clear", value= "Удалить сообщения,указывать кол-во сообщений через пробел после комманды.", inline=False)
    emb.add_field(name="?say", value= "Написать что-либ от лица бота,указывать текст сообщения через пробел после комманды.", inline=False)
    await ctx.send(embed=emb)
    print("[?ahelp - done. " +  "Induced "+ author)
    await channel.send("[ahelp] - done. " + "Induced "+ author)

    
@Bot.command()
async def coin(ctx):
    channel = Bot.get_channel(600384214822813696)
    author = str(ctx.message.author)
    choices=['Орёл','Решка']
    value=random.choice(choices)
    await ctx.send("Вам выпал(-а) - " + value)
    print("[?coin] - done. Induced "+ author)
    await channel.send("[?coin] - done. Induced "+ author)

token = os.environ.get('BOT_TOKEN')
Bot.run(str(token))

