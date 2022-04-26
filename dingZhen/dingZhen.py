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
    "https://i.imgur.com/mcsQg4I.jpg",
    "https://i.imgur.com/UkSYd6R.jpg"
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
    "**{user}** got a pat from **{author}**",
    "**{author}** affectionately pat **{user}**",
    "Without hesitation, **{author}** pats **{user}** with love"
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
    async def dz(self, ctx, *, user: discord.Member=None):
        """Pat users."""
        author = ctx.author

        if not user:
            message = rnd(self.failmsgs)
            await ctx.send(message.format(author=author.name))
        else:
            message = rnd(patmsgs)
            dz = discord.Embed(description=message.format(user=user.name, author=author.name), color=discord.Color(0xffb6c1))
            dz.set_image(url=rnd(self.gifs))
            await ctx.send(embed=dz)

    @commands.command(name="pdaver", hidden=True)
    async def _pda_version(self, ctx):
        """Show PDA version"""
        ver = self.version
        await ctx.send("You are using PDA version {}".format(ver))

