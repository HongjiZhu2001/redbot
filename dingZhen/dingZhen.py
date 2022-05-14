# Public Display of Affection cog by Yukirin#0048

# Discord
import discord

# Red
from redbot.core import Config, commands

# Libs 
from random import choice as rnd

BaseCog = getattr(commands, "Cog", object)

__version__ = "2018.9.0"
__author__ = "Yukirin"

gifs = [
    "https://i.imgur.com/TZjlBlw.jpg",
    "https://i.imgur.com/mcsQg4I.jpg",
    "https://i.imgur.com/UkSYd6R.jpg",
    "https://i.imgur.com/pd3tgDO.jpg",
    "https://i.imgur.com/lGwFNev.jpg",
    "https://i.imgur.com/Bq2tRJh.jpg",
    "https://i.imgur.com/L6aoZOh.jpg",
    "https://i.imgur.com/grhsNBm.jpg",
    "https://i.imgur.com/4s8ozAp.jpg",
    "https://i.imgur.com/GahBA2q.jpg",
    "https://i.imgur.com/RzaqEes.jpg",
    "https://i.imgur.com/UvGtSJv.jpg",
    "https://i.imgur.com/KafNEK1.jpg",
    "https://i.imgur.com/PYNOjF9.jpg",
    "https://i.imgur.com/6kRR5FS.jpg",
    "https://i.imgur.com/vJXtazp.jpg",
    "https://i.imgur.com/q4L8PCS.jpg",
    "https://i.imgur.com/GB6mTMt.jpg",
    "https://i.imgur.com/0eK2r2j.jpg",
    "https://i.imgur.com/l1hhmEQ.jpg",
    "https://i.imgur.com/w04Styw.jpg",
    "https://i.imgur.com/mCYq654.jpg",
    "https://i.imgur.com/MvPYDYe.jpg",
    "https://i.imgur.com/bDAdrUW.jpg",
    "https://i.imgur.com/VTXVKbL.jpg",
    "https://i.imgur.com/xhkGRys.jpg",
    "https://i.imgur.com/lYyzwAN.jpg",
    "https://i.imgur.com/NQKMrdp.jpg",
    "https://i.imgur.com/rwj8S5G.jpg",
    "https://i.imgur.com/M8NAq7g.jpg",
    "https://i.imgur.com/EsZcTD9.jpg",
    "https://i.imgur.com/sbjlyfc.jpg",
    "https://i.imgur.com/mNRMD2u.jpg",
    "https://i.imgur.com/oWtW4qQ.jpg",
    "https://i.imgur.com/Q5ubvy6.jpg",
    "https://i.imgur.com/jGvRPRg.jpg",
    "https://i.imgur.com/99gelhU.jpg",
    "https://i.imgur.com/AywQYmB.jpg",
    "https://i.imgur.com/8Q9CNpX.jpg",
    "https://i.imgur.com/9Cg7QIz.jpg",
    "https://i.imgur.com/RSj2lqI.jpg",
    "https://i.imgur.com/uQeGSsB.jpg",
    "https://i.imgur.com/Au5QFUe.jpg",
    "https://i.imgur.com/evtQepL.jpg",
    "https://i.imgur.com/cu5CHyW.jpg",
    "https://i.imgur.com/TVS85lq.png",
    "https://i.imgur.com/1rmG2WN.jpg",
    "https://i.imgur.com/9NK0y7u.jpg"
]

failmsgs = [
    "{author} is trying to pat non-existent entity ... and failed.",
    "{author}: *pats non-existent entity*. This bad boy can accept so many pats.",
    "To be honest, I don't know what's {author} been smoking, but sorry, you can't pat non-existent entity",
    "Oh come on, is it that hard to correctly use this command?",
    "You must pat valid and existing user. Try using @ mention, username or nickname.",
    "(╯°□°）╯︵ ┻━┻"
]

patmsgs = [
    ""
]


class DingZhen(BaseCog):
    """Public Display of Affection ~!"""

    def __init__(self, bot):
        self.gifs = gifs
        self.failmsgs = failmsgs
        self.version = __version__
        self.author = __author__
        
    @commands.Cog.listener()
    async def on_message(self, message):
        keyword = "RESPOND"
        if keyword in message.content:
            await message.channel.send(set_image(url=rnd(self.gifs)))
        else:
            return
 """           
    @commands.command(name="来点丁真", hidden=True)
    async def dz(self, ctx, *,user: discord.Member=None):
        """Pat users."""
        author = ctx.author
        if not user:
            message = rnd(patmsgs)
            dz = discord.Embed(description=message, color=discord.Color(0x206694))
            dz.set_image(url=rnd(self.gifs))
            await ctx.send(embed=dz)

        else:
            message = rnd(patmsgs)
            dz = discord.Embed(description=message, color=discord.Color(0x206694))
            dz.set_image(url=rnd(self.gifs))
            await ctx.send(embed=dz)
"""
    @commands.command(name="dingZhenver", hidden=True)
    async def _pda_version(self, ctx):
        """Show PDA version"""
        ver = self.version
        await ctx.send("You are using PDA version {}".format(ver))

