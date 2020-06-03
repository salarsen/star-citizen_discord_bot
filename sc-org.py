import os, re
import discord
from dotenv import load_dotenv
from datetime import date


# discord bot image: https://www.vectorstock.com/royalty-free-vector/pi-symbol-with-infinity-sign-abstract-icon-vector-8286697
# api ref: https://discordpy.readthedocs.io/en/latest/api.html#

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_LIST_RAW = os.getenv('CHANNELS')

ch_list = CHANNEL_LIST_RAW.split(',')
print(ch_list,flush=True)

client = discord.Client()

@client.event
async def on_ready():
    
    for guild in client.guilds:
        # print(guild.name,flush=True)
    
        # print(f'{client.id} has connected to Discord!\n {guild.name}(id: {guild.id})\n',flush=True)
        print(f'Connected to Discord!\n {guild.name}(id: {guild.id})\n',flush=True)
        for channel in guild.channels:
            # list channels in guild
            # print(f'- {channel.name}(id: {channel.id})\n',flush=True)

            if str(channel.id) in ch_list:

                today = date.today()

                targetId = 717743773781852232
                
                async for message in channel.history(limit=100):
                    if message.id == targetId:
                        date_str = "Today\'s Date: " + str(today.strftime("%B %d, %Y"))
                        await message.edit(content=str(date_str))

                async for message in channel.history(limit=20):
                #     print(f'{message.id}: {message.content}')
                    if message.author == client.user and message.id != targetId:
                        await message.clear_reactions()
                        await message.add_reaction('<:3783_salute1:652257869927940107>')

                
                #         # await message.delete()
    # close the client for the cronjob to function properly
    await client.close()

client.run(TOKEN)