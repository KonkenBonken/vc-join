import discord
from discord.ext import commands
from time import sleep

intents = discord.Intents.default()
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_voice_state_update(member, before, after):
    if after.channel is not None and not bot.voice_clients:
        if member.id == 417331788436733953:
            voice_client = await after.channel.connect()
            voice_client.play(discord.FFmpegPCMAudio('./glass.mp3'))
            sleep(5)
            await voice_client.disconnect()
        if member.id == 390107369146810380:
            voice_client = await after.channel.connect()
            voice_client.play(discord.FFmpegPCMAudio('./seagulls.mp3'))
            sleep(17)
            await voice_client.disconnect()
            
bot.run('TOKEN')