import os, re
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    
    for guild in client.guilds:
        # print(guild.name,flush=True)
    
        print(f'{client.user} has connected to Discord!\n {guild.name}(id: {guild.id})\n',flush=True)


# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
    
#     if re.match(r'^\!+.',message.content):
        
#         # list instructions for std user

#         # list followers

#         # add follower (check if in list already, otherwise add, restart twitter stream with new followers)
#         # require approval from admin in DM?

#         # remove follower (verify if in list of approved users who can remove first)


        
#         response = "Command entered"
#         await message.channel.send(response)



client.run(TOKEN)