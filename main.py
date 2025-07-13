import discord
import os
from discord.ext import tasks

intents = discord.Intents.default()
client = discord.Client(intents=intents)

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

@client.event
async def on_ready():
    print(f'Bot prisijungė kaip {client.user}')
    channel = client.get_channel(CHANNEL_ID)
    await channel.send("✅ Vinted Sniper Botas veikia!")

client.run(TOKEN)
