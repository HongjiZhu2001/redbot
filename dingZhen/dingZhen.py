# Public Display of Affection cog by Yukirin#0048

# Discord
import discord

# Red
from redbot.core import commands

# Libs 
from random import choice as rnd

BaseCog = getattr(commands, "Cog", object)

__version__ = "2018.9.0"
__author__ = "Yukirin"

gifs = [
    "https://i.imgur.com/TZjlBlw.jpg",
    "https://i.imgur.com/q4L8PCS.jpg",
    "https://i.imgur.com/mcsQg4I.jpg",
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

    @commands.command()
    @commands.cooldown(6, 60, commands.BucketType.user)
    async def dingZhen(self, ctx, *, user: discord.Member=None):
        """Pat users."""
        author = ctx.author

            message = rnd(patmsgs)
            dingZhen = discord.Embed(description=message.format(user=user.name, author=author.name), color=discord.Color(0xffb6c1))
            dingZhen.set_image(url=rnd(self.gifs))
            await ctx.send(embed=dingZhen)

    @commands.command(name="pdaver", hidden=True)
    async def _dingZhen_version(self, ctx):
        """Show PDA version"""
        ver = self.version
        await ctx.send("You are using PDA version {}".format(ver))

