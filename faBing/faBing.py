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
    "https://i.imgur.com/YTGnx49.gif",
    "https://i.imgur.com/U37wHs9.gif",
    "https://i.imgur.com/BU2IQym.gif",
    "https://i.imgur.com/yp6kqPI.gif",
    "https://i.imgur.com/uDyehIe.gif",
    "https://i.imgur.com/vG8Vuqp.gif",
    "https://i.imgur.com/z4uCLUt.gif",
    "https://i.imgur.com/ZIRC9f0.gif",
    "https://i.imgur.com/s8m4srp.gif",
    "https://i.imgur.com/LKvNxmo.gif",
    "https://i.imgur.com/j4W4GFt.gif",
    "https://i.imgur.com/75bX4A1.gif",
    "https://i.imgur.com/dSlfpe3.gif",
    "https://i.imgur.com/JjxaT8e.gif",
    "https://i.imgur.com/QWBlOaQ.gif",
    "https://i.imgur.com/5448px6.gif",
    "https://i.imgur.com/4WJRAGw.gif",
    "https://i.imgur.com/v1sSh5r.gif"
]

failmsgs = [
    "你得找个人发病"
]

patmsgs = [
    """
**{user}**想要一件漂亮的衣服
和yhm一样靓丽的裙子
鼠鼠们犯了难
要是有天国的锦缎该多好啊
以金银色的光线编织
还有湛蓝的夜色与洁白的昼光
以及黎明和黄昏错综的光芒
要是然然得了这锦缎
她该有多开心啊
但是啊，鼠鼠们，如此贫穷，除了梦一无所有
于是鼠鼠们每个人拿出自己的梦
凑了一件可爱的衣裳
**{user}**穿着很合身
有了这件衣服，然然终于得了猫猫的喜爱
越来越多的猫猫依偎在然然的怀里
鼠鼠们再不敢靠近嘉然小姐了
只敢偷偷地从洞里探出脑袋
望着她，望着她
偶有发了病的鼠鼠冲出来
转瞬便葬身猫口
终于有一天
**{user}**得了天国的锦缎
身边的猫猫也嫌弃鼠鼠的衣服太过寒碜
**{user}**穿上新衣服
华丽动人，连yhm都要心生嫉妒
是时候丢掉旧衣服了
**{user}**回想起
她与鼠鼠一起度过的时光
她陪伴鼠鼠唱过的歌曲
她为鼠鼠哭泣过的夜
又于心不忍了
于是她整齐地把衣服垫在枕头下
与此同时
阴暗的洞里，一只鼠鼠悄声说道
“轻一点啊，因为你枕着我的梦”
"""
]


class FaBing(BaseCog):
    """Public Display of Affection ~!"""

    def __init__(self, bot):
        self.gifs = gifs
        self.failmsgs = failmsgs
        self.version = __version__
        self.author = __author__

    @commands.command(name="发病", hidden=True)
    async def pat(self, ctx, *, user: discord.Member=None):
        """Pat users."""
        author = ctx.author

        if not user:
            message = rnd(self.failmsgs)
            await ctx.send(message.format(author=author.name))
        else:
            message = rnd(patmsgs)
            fb = discord.Embed(description=message.format(user=user.name, author=author.name), color=discord.Color(0xffb6c1))
            await ctx.send(embed=fb)

    @commands.command(name="pdaver", hidden=True)
    async def _pda_version(self, ctx):
        """Show PDA version"""
        ver = self.version
        await ctx.send("You are using PDA version {}".format(ver))

