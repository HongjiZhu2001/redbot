from random import choice
from typing import List

import discord
from redbot.core import commands
from redbot.core.i18n import Translator, cog_i18n

_ = Translator("Insult", __file__)

insults: List[str] = [
    _("我是你爹"),
    _("NM$L"),
    _("废物"),
    _("饭桶"),
    _("弱智"),
    _("弟中之弟"),
    _("海尔兄弟"),
    _("舒克和贝塔"),
    _("小学生"),
    _("畜生"),
    _("物以类聚人以群分，但是我还没见过像你这么招狗喜欢的。"),
    _("你别和我说话，因为我听不懂，在别人的眼中看来，我和一条猪在吵架是一件很愚蠢的事。"),
    _("你的智商停留在胎教水平吧？？"),
    _("当初你爸妈是把胎盘养大了吗？"),
    _("哥谭市里你最狂，马戏团里你最忙，麦当劳前你站岗，扑克牌里大小王"),
]


@cog_i18n(_)
class Insult(commands.Cog):
    """Airenkun's Insult Cog"""

    __author__ = ["Airen", "JennJenn", "TrustyJAID"]
    __version__ = "1.0.0"

    def __init__(self, bot):
        self.bot = bot

    def format_help_for_context(self, ctx: commands.Context) -> str:
        """
        Thanks Sinbad!
        """
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nCog Version: {self.__version__}"

    async def red_delete_data_for_user(self, **kwargs):
        """
        Nothing to delete
        """
        return

    @commands.command(aliases=["takeitback"])
    async def insult(self, ctx: commands.Context, user: discord.Member = None) -> None:
        """
        Insult the user

        `user` the user you would like to insult
        """

        msg = " "
        if user:

            if user.id == self.bot.user.id:
                user = ctx.message.author
                bot_msg = [
                    _(
                        " How original. No one else had thought of trying to get the bot to insult itself. I applaud your creativity. Yawn. Perhaps this is why you don't have friends. You don't add anything new to any conversation. You are more of a bot than me, predictable answers, and absolutely dull to have an actual conversation with."
                    ),
                    _(
                        " What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, kiddo."
                    ),
                ]
                await ctx.send(f"{ctx.author.mention}{choice(bot_msg)}")

            else:
                await ctx.send(user.mention + msg + choice(insults))
        else:
            await ctx.send(ctx.message.author.mention + msg + choice(insults))
