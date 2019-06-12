#!/usr/bin/env python

#Imports
import discord  
from discord.ext import commands

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def soviet(self, ctx):
        user = ctx.message.author
        voice_channel = "ooga"
        if user.voice != None:
            voice_channel = user.voice.channel
        channel=None
        if user.voice != None:
            channel=voice_channel.name
            await ctx.send ('User is in channel: ' + channel)
            await ctx.send ('Музыка нашей родины товарищи. ')
            await voice_channel.connect(timeout=60.0, reconnect=True)
            player = voice_channel.create_ffmpeg_player('soviet.mp3')
            player.start()
            while not player.is_done():
                await asyncio.sleep(1)
            player.stop()
            await vc.disconnect()
        elif voice_channel == "ooga":
            await ctx.send('User is not in a channel.')
                      
            
def setup(bot):
    bot.add_cog(Music(bot))
                          