import os
import discord
import logging
from dotenv import load_dotenv

logger = logging.getLogger("discord")

logger.setLevel(logging.DEBUG)

handler = logging.FileHandler(filename="discord.log",encoding='utf-8',mode='w')

handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))

logger.addHandler(handler)

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = discord.Client()

@bot.event
async def on_ready():
    server_count=0

    for i in bot.guilds:
        print("The bot is in {0}".format(i))

        server_count+=1
    print("The bot is in {0} no of servers".format(server_count))


@bot.event
async def on_message(message):
    if message.content == "hello":
        await message.channel.send("Hai bro")

bot.run(DISCORD_TOKEN)

print(DISCORD_TOKEN)