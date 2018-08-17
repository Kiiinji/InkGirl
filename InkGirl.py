#Enju
import discord
import random
import time
import os
import aiohttp
import requests
import asyncio
import pickle
import random
import io
from discord.ext import commands
from discord.ext.commands import Bot
from discord import opus
import discord
from discord.ext import commands
import youtube_dl


def get_metadata(query):
    return youtube_dl.YoutubeDL({
        "format": "ogg[abr>0]/m4a[abr>0]/webm[abr>0]/bestaudio/best",
        "ignoreerrors": True,
        "default_search": "auto",
        "source_address": "0.0.0.0",
        "quiet": True
    }).extract_info(query, download=False)['url']



OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']

def load_opus_lib(opus_libs=OPUS_LIBS):

    if opus.is_loaded():

        return True

    for opus_lib in opus_libs:

        try:

            opus.load_opus(opus_lib)

            return

        except OSError:

            pass

    raise RuntimeError('Could not load an opus lib. Tried %s' % (', '.join(opus_libs)))

load_opus_lib()

bot = commands.Bot(command_prefix='=')
bot.remove_command('help')
players = {}
opts = {}




@bot.event
async def on_ready():
	print ("Gloups Prête ! Gloups")
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='=aide'))

@bot.check
async def botcheck(ctx):
    return not ctx.message.author.bot

@bot.command()
async def aide(ctx):
    em = discord.Embed(title="Commandes d'Ink Girl", description="", color=discord.Colour.magenta())
    em.set_author(name="")
    em.add_field(name="=inkgirl", value="Envoie une image d'Ink Girl", inline=False)
    em.add_field(name="=meme", value="Envoie une image de meme Splatoon aléatoire", inline=False)
    em.add_field(name="=rip", value="Affiche l'image exprimant la profonde tristesse de Kinji suite au décés de son CD Splatoon :'(", inline=False)
    em.add_field(name="=don", value="Donne le lien pour faire un don à Kinji histoire qu'il se rachète Splatoon", inline=False)
    em.add_field(name="=join", value="Fait rejoindre Ink Girl dans le channel vocal actuel", inline=False)
    em.add_field(name="=music", value="Joue une musique aléatoire de Splatoon dans ce channel vocal", inline=False)
    em.add_field(name="=pause", value="Met la musique qui est jouée en pause", inline=False)
    em.add_field(name="=resume", value="Reprend la musique si elle est en pause", inline=False)
    em.add_field(name="=stop", value="Arrête la musique qui est actuellement jouée", inline=False)
    em.add_field(name="=leave", value="Fait quitter Ink Girl du channel vocal dans lequel elle se trouve", inline=False)
    em.add_field(name="___________________________________________", value="Bot codé par Kinji", inline=False)


    em.set_thumbnail(url = "https://i.gyazo.com/20becb6402bd2616b2d04bae2a57b51b.png")
    await ctx.send(embed=em)




@bot.command()
async def music(ctx):
	channel = ctx.message.author.voice.channel
	fp = "Data/Audio/Splatoon/{}".format(random.choice(os.listdir("Data/Audio/Splatoon")))
	ctx.voice_client.play(discord.FFmpegPCMAudio(fp), after=None)
	msg = await ctx.send('<:squidroseup:479789317779226624> Tous les céphalopodes vous souhaitent un bon moment ! <:squidroseup:479789317779226624>')
	await msg.add_reaction("<:splatoon2:479712391823622155")

@bot.command()
async def inkgirl(ctx):
    fp = "Data/Img/InkGirl/{}".format(random.choice(os.listdir("Data/Img/InkGirl")))
    msg = await ctx.send(file=discord.File(fp))
    await msg.add_reaction("<:splatoon2:479712391823622155")

@bot.command()
async def rip(ctx):
    fp = "Data/Img/Rip/{}".format(random.choice(os.listdir("Data/Img/Rip")))
    msg = await ctx.send(file=discord.File(fp))
    await msg.add_reaction("<:splatoon:479641297225908224")

@bot.command()
async def meme(ctx):
    fp = "Data/Img/Meme/{}".format(random.choice(os.listdir("Data/Img/Meme")))
    msg = await ctx.send(file=discord.File(fp))
    await msg.add_reaction("<:splatoon2:479712391823622155")


@bot.command()
async def don(ctx):
	msg = await ctx.send('https://www.gofundme.com/mon-splatoon-est-mort')
	await msg.add_reaction("<:splatoon:479641297225908224")


@bot.command()
async def join(ctx):
	channel = ctx.message.author.voice.channel
	await channel.connect()
	msg = await ctx.send('<:squidvertright:479789723301314570> Je suis là ! <:squidvertleft:479789320975417354>')
	await msg.add_reaction("<:splatoon2:479712391823622155")

@bot.command()
async def leave(ctx):
	await ctx.voice_client.disconnect()
	msg = await ctx.send('<:squidredright:479789281322205204> Bye bye ! <:squidredleft:479789280500121610>')
	await msg.add_reaction("<:splatoon2:479712391823622155")


@bot.command()
async def pause(ctx):
	ctx.voice_client.pause()
	msg = await ctx.send('<:squidroseright:479789315518365697> La vidéo a été mise en pause ! <:squidroseleft:479789313580597282>')
	await msg.add_reaction("<:splatoon2:479712391823622155")

@bot.command()
async def resume(ctx):
	ctx.voice_client.resume()
	msg = await ctx.send('<:squidroseright:479789315518365697> Reprise de la vidéo ! <:squidroseleft:479789313580597282>')
	await msg.add_reaction("<:splatoon2:479712391823622155")

@bot.command()
async def stop(ctx):
	ctx.voice_client.stop()
	msg = await ctx.send('<:squidrosedown:479789310963613696> Vidéo arrêtée ! <:squidrosedown:479789310963613696>')
	await msg.add_reaction("<:splatoon2:479712391823622155")



# @bot.command()
# async def splatoon(ctx):
#     async with aiohttp.ClientSession() as session:
#         async with session.get('https://safebooru.org//index.php?page=dapi&tags=splatoon&s=post&limit=1&q=index&json=1') as r: 
#             js = await r.json(content_type='text/html')
#             arr = js[0]
#             embed = discord.Embed(colour=discord.Colour.magenta())
#             embed.set_image(url="https://safebooru.org//images/{}/{}".format(arr['directory'],arr['image']))
#             await ctx.send(embed=embed)
            #await ctx.send("https://safebooru.org//images/{}/{}".format(arr['directory'],arr['image']))





bot.run(os.getenv("TOKEN"))
