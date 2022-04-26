from .dingZhen import DingZhen


def setup(bot):
    bot.add_cog(DingZhen(bot))
