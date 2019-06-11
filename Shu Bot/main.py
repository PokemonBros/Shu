import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

#env file
load_dotenv()


#Prefix
def get_prefix(bot, message):
    '''A callable Prefix for our bot. This could be edited to allow per server prefixes.'''
    try:
        prefix = '.'
    except:
        prefix = '.'
    if (not message.guild):  #Check to see if we are outside of a guild. e.g DM's etc.
        return '.' #Only allow ? to be used in DMs
    return commands.when_mentioned_or(prefix)(bot, message)
description = """AYAYAYYAYA"""
bot = commands.Bot(command_prefix= get_prefix, description = description)

startup_extensions = startup_extensions = ["modules.misc",
                    ]

#Events:
@bot.event  
async def on_ready(): 
    print("Japan #1")
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if isinstance(message.channel, discord.abc.PrivateChannel)and (message.author.id != 180852994231762945):
        channel = bot.get_user(180852994231762945).dm_channel
        if channel==None:
            channel = await bot.get_user(180852994231762945).create_dm()
        await channel.send((((('**Message from ' + str(message.author)) + '[*') + str(message.author.id)) + '*]:** ') +str(message.content))
        if message.attachments != []:
            my_message = "**Attachments**: "
            for attachement in message.attachments:
                my_message = my_message + attachement.url + "\n"
            await channel.send(my_message)
  
  
   
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
if __name__ == '__main__':
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
    bot.run(os.getenv("SECRET"))
    
   