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
    #"https://i.imgur.com/TVS85lq.png",
    "https://i.imgur.com/1rmG2WN.jpg",
    "https://i.imgur.com/9NK0y7u.jpg",
    #"https://i.imgur.com/UkeZd5G.gif",
    "https://i.imgur.com/dMS0sAw.jpg",
    "https://i.imgur.com/5y6T40n.jpg",
    "https://i.imgur.com/nZAduYj.jpg",
    #"https://i.imgur.com/rSHJa51.gifv",
    "https://i.imgur.com/UiOXqqG.jpg",
    "https://i.imgur.com/OxlpS8S.jpg",
    "https://i.imgur.com/z230EZi.jpg",
    "https://i.imgur.com/MrYEtBG.jpg",
    "https://i.imgur.com/Q9sx9kM.jpg",
    "https://i.imgur.com/njBkmj3.jpg",
    "https://i.imgur.com/S0SDMwI.jpg",
    "https://i.imgur.com/Td202O2.jpg",
    "https://i.imgur.com/YOVsqJn.jpg",
    "https://i.imgur.com/09tKVLq.jpg",
    "https://i.imgur.com/nhUFLs2.jpg",
    "https://i.imgur.com/G4GN1vL.jpg",
    "https://i.imgur.com/zX8lVFf.jpg",
    "https://i.imgur.com/TBZvE2u.jpg",
    "https://i.imgur.com/ul0hZmA.jpg",
    "https://i.imgur.com/OwG3eJq.jpg",
    "https://i.imgur.com/A6O5dbx.jpg",
    "https://i.imgur.com/gdxkZ5R.jpg",
    "https://i.imgur.com/m95SJSn.jpg",
    "https://i.imgur.com/3ekcB1p.jpg",
    "https://i.imgur.com/omIGL44.jpg",
    "https://i.imgur.com/wIlXuXE.jpg",
    "https://i.imgur.com/enYSOvC.jpg",
    "https://i.imgur.com/LEbIBRY.jpg",
    "https://i.imgur.com/TWXLqaC.jpg",
    "https://i.imgur.com/4Xe7VMI.jpg",
    "https://i.imgur.com/hWQKH6T.jpg",
    "https://i.imgur.com/o4fFkCj.jpg",
    "https://i.imgur.com/wdcSR07.jpg",
    "https://i.imgur.com/o0zyvuJ.jpg",
    "https://i.imgur.com/K7eP1pi.jpg",
    "https://i.imgur.com/2UUWS5o.jpg",
    "https://i.imgur.com/4yroRIr.jpg",
    "https://i.imgur.com/tZXnyM7.jpg",
    "https://i.imgur.com/erMcCFc.jpg",
    "https://i.imgur.com/BZkBgY3.jpg",
    "https://i.imgur.com/cFYh2DE.jpg",
    "https://i.imgur.com/jeX6fva.jpg",
    "https://i.imgur.com/RDzLvf5.jpg",
    "https://i.imgur.com/tFaWkDZ.jpg",
    "https://i.imgur.com/TEB9zbO.jpg",
    "https://i.imgur.com/KRIhGFK.jpg",
    "https://i.imgur.com/2jBGFwz.jpg",
    "https://i.imgur.com/Z9DxpaI.jpg",
    "https://i.imgur.com/UKDPllH.jpg",
    "https://i.imgur.com/NWT8pIm.jpg",
    "https://i.imgur.com/YjyOzIU.jpg",
    "https://i.imgur.com/mB3qh7f.jpg",
    "https://i.imgur.com/S7UQkrt.jpg",
    "https://i.imgur.com/xUq1rnr.jpg",
    "https://i.imgur.com/acvkE3b.jpg",
    "https://i.imgur.com/EZx0HeB.jpg",
    "https://i.imgur.com/hNnVCFh.jpg",
    "https://i.imgur.com/mkM5VrX.jpg",
    "https://i.imgur.com/mYieHs4.jpg",
    "https://i.imgur.com/ZKuemB8.jpg",
    "https://i.imgur.com/VaTtveC.jpg",
    "https://i.imgur.com/LQPOcAO.jpg",
    "https://i.imgur.com/znIcPDP.jpg",
    "https://i.imgur.com/gmYEVq2.jpg",
    "https://i.imgur.com/JViMdqd.jpg",
    "https://i.imgur.com/ZOKqysl.jpg",
    "https://i.imgur.com/QBjKpE8.jpg",
    "https://i.imgur.com/3pSdYMS.jpg",
    "https://i.imgur.com/ue83Ghm.jpg",
    "https://i.imgur.com/Uxo71Ve.jpg",
    "https://i.imgur.com/8GHcTiP.jpg",
    "https://i.imgur.com/jMvviV2.jpg",
    "https://i.imgur.com/VWCjvOz.jpg",
    "https://i.imgur.com/lSOFiYg.jpg",
    "https://i.imgur.com/8zoC5iW.jpg",
    "https://i.imgur.com/oiVVZ4c.jpg",
    "https://i.imgur.com/WsshL54.jpg",
    "https://i.imgur.com/qQpre6T.jpg",
    "https://i.imgur.com/OrTBn1V.jpg",
    "https://i.imgur.com/6GbeBKw.jpg",
    "https://i.imgur.com/21EJUlI.jpg",
    "https://i.imgur.com/npMo0tt.jpg",
    "https://i.imgur.com/HcMNw1g.jpg",
    "https://i.imgur.com/0hhIWav.jpg",
    "https://i.imgur.com/JQQAZGY.jpg",
    "https://i.imgur.com/BppQgOq.jpg",
    "https://i.imgur.com/8T3bUxN.jpg",
    "https://i.imgur.com/iX3B4dM.jpg",
    "https://i.imgur.com/jHBBDSU.jpg",
    "https://i.imgur.com/Jk20ePd.jpg",
    "https://i.imgur.com/ui7vBAS.jpg",
    "https://i.imgur.com/tqGtDq7.jpg",
    "https://i.imgur.com/7LxDscd.jpg",
    "https://i.imgur.com/VRtEBk3.jpg",
    "https://i.imgur.com/CrmmDQP.jpg",
    "https://i.imgur.com/zVfhGGS.jpg",
    "https://i.imgur.com/MVTqCvV.jpg",
    "https://i.imgur.com/mWbDwvY.jpg",
    "https://i.imgur.com/7vMouol.jpg",
    "https://i.imgur.com/18NjeRy.jpg",
    "https://i.imgur.com/HFXJ6e4.jpg",
    "https://i.imgur.com/GEWYGWq.jpg",
    "https://i.imgur.com/yeM8Mmk.jpg",
    "https://i.imgur.com/0Ia807k.jpg",
    "https://i.imgur.com/jVUaM6A.jpg",
    "https://i.imgur.com/jhbexKF.jpg",
    "https://i.imgur.com/lTwEtGU.jpg",
    "https://i.imgur.com/k0nrj5a.jpg",
    "https://i.imgur.com/EXBCWq7.jpg",
    "https://i.imgur.com/E4U6Lfy.jpg",
    "https://i.imgur.com/YMfJlKb.jpg",
    "https://i.imgur.com/IiRV2Dq.jpg",
    "https://i.imgur.com/Cu5geqq.jpg",
    "https://i.imgur.com/4HLp3Gj.jpg",
    "https://i.imgur.com/JFfjX2M.jpg",
    "https://i.imgur.com/2a6fldW.jpg",
    "https://i.imgur.com/3icXVB9.jpg",
    "https://i.imgur.com/evXIGen.jpg",
    "https://i.imgur.com/jkCfTmR.jpg",
    "https://i.imgur.com/3Bc0uVw.jpg",
    "https://i.imgur.com/NcFQuhX.jpg",
    "https://i.imgur.com/gqfU9Y5.jpg",
    "https://i.imgur.com/lqHmMb6.jpg",
    "https://i.imgur.com/2pT6ElK.jpg",
    "https://i.imgur.com/JKGLfga.jpg",
    "https://i.imgur.com/uyifNnF.jpg",
    "https://i.imgur.com/h6MVCTi.jpg",
    "https://i.imgur.com/fMz2QTr.jpg",
    "https://i.imgur.com/97yklNV.jpg",
    "https://i.imgur.com/F8DHu4r.jpg",
    "https://i.imgur.com/ZzNwJEW.jpg",
    "https://i.imgur.com/sBNniai.jpg",
    "https://i.imgur.com/9Z24HrD.jpg",
    "https://i.imgur.com/x0hW1oH.jpg",
    "https://i.imgur.com/YgILAxq.jpg",
    "https://i.imgur.com/2lgxM7T.jpg",
    "https://i.imgur.com/rOohCcf.jpg",
    "https://i.imgur.com/KvAoYpw.jpg",
    "https://i.imgur.com/pCpEkIB.jpg",
    "https://i.imgur.com/AQf8qVD.jpg",
    "https://i.imgur.com/xtUhmTt.jpg",
    "https://i.imgur.com/w4wnu9S.jpg",
    "https://i.imgur.com/yJj6GKh.jpg",
    "https://i.imgur.com/yRS6K9V.jpg",
    "https://i.imgur.com/YcyTGAy.jpg",
    "https://i.imgur.com/Gb3La3R.jpg",
    "https://i.imgur.com/f8201y9.jpg",
    "https://i.imgur.com/ScAEGxO.jpg",
    "https://i.imgur.com/37nPIHV.jpg",
    "https://i.imgur.com/fxpj7jb.jpg",
    "https://i.imgur.com/093EMe1.jpg",
    "https://i.imgur.com/9VFkk6i.jpg",
    "https://i.imgur.com/cbxtHZK.jpg",
    "https://i.imgur.com/2oMOHLU.jpg",
    "https://i.imgur.com/ZePNfiw.jpg",
    "https://i.imgur.com/p3enszF.jpg",
    "https://i.imgur.com/BCfJed2.jpg",
    "https://i.imgur.com/kfhP9C9.jpg",
    "https://i.imgur.com/wlNLpQm.jpg",
    "https://i.imgur.com/eox6E7C.jpg",
    "https://i.imgur.com/0IfN7xl.jpg",
    "https://i.imgur.com/9EIkrqz.jpg",
    "https://i.imgur.com/ivTV2E3.jpg",
    "https://i.imgur.com/zU4fGnh.jpg",
    "https://i.imgur.com/JyOqp2H.jpg",
    "https://i.imgur.com/gTXhZXs.jpg",
    "https://i.imgur.com/kM9nlNs.jpg",
    "https://i.imgur.com/jSRmDlq.jpg",
    "https://i.imgur.com/UNiHVaI.jpg",
    "https://i.imgur.com/AqrO1PE.jpg",
    "https://i.imgur.com/GsiDkap.jpg",
    "https://i.imgur.com/xEuJQQH.jpg",
    "https://i.imgur.com/sSSawKt.jpg",
    "https://i.imgur.com/bdJZjHe.jpg",
    "https://i.imgur.com/006kgI1.jpg",
    "https://i.imgur.com/ZSn0QjF.jpg",
    "https://i.imgur.com/0vhOPXA.jpg",
    "https://i.imgur.com/81r4rmM.jpg",
    "https://i.imgur.com/gKH3zkz.jpg",
    "https://i.imgur.com/CNBFlN8.jpg",
    "https://i.imgur.com/33CP6Y8.jpg",
    "https://i.imgur.com/WCI2Hma.jpg",
    "https://i.imgur.com/97IW2p8.jpg",
    "https://i.imgur.com/m6fRmHV.jpg",
    "https://i.imgur.com/ntkhP9x.jpg",
    "https://i.imgur.com/3MQR4vL.jpg",
    "https://i.imgur.com/e2uh24y.jpg",
    "https://i.imgur.com/IlyPbUv.jpg",
    "https://i.imgur.com/mj9f6zk.jpg",
    "https://i.imgur.com/7NBTEYS.jpg",
    "https://i.imgur.com/rJ0wzI8.jpg",
    "https://i.imgur.com/qBM0xrr.jpg",
    "https://i.imgur.com/1eKflx3.jpg",
    "https://i.imgur.com/bcxnTAE.jpg",
    "https://i.imgur.com/BCj3298.jpg",
    "https://i.imgur.com/8eD6PEe.jpg",
    "https://i.imgur.com/uXqLgCQ.jpg",
    "https://i.imgur.com/CGSA4CL.jpg",
    "https://i.imgur.com/8aJfwcm.jpg",
    "https://i.imgur.com/vtgYxpw.jpg",
    "https://i.imgur.com/HMZGHuL.jpg",
    "https://i.imgur.com/9fgErAi.jpg",
    "https://i.imgur.com/NkceFwf.jpg",
    "https://i.imgur.com/5sr7A69.jpg",
    "https://i.imgur.com/GoP67JP.jpg",
    "https://i.imgur.com/UHvqUeE.jpg",
    "https://i.imgur.com/MfLUqgC.jpg",
    "https://i.imgur.com/H7r9dtV.jpg",
    "https://i.imgur.com/eooh8SG.jpg",
    "https://i.imgur.com/7zhg1pK.jpg",
    "https://i.imgur.com/bzvKyaI.jpg",
    "https://i.imgur.com/x5Rc6gT.jpg",
    "https://i.imgur.com/uvrhJBP.jpg",
    "https://i.imgur.com/Pta9PpP.jpg",
    "https://i.imgur.com/Lxixcb1.jpg",
    "https://i.imgur.com/X5fze7h.jpg",
    "https://i.imgur.com/MIRLQPx.jpg",
    "https://i.imgur.com/7wgkJmT.jpg",
    "https://i.imgur.com/XgqW78o.jpg",
    "https://i.imgur.com/epJzDz7.jpg",
    "https://i.imgur.com/rNJhQDB.jpg",
    "https://i.imgur.com/0iapdjQ.jpg",
    "https://i.imgur.com/vIvu2gM.jpg",
    "https://i.imgur.com/mLbRQF6.jpg",
    "https://i.imgur.com/tp3HmB9.jpg",
    "https://i.imgur.com/YGknYFv.jpg",
    "https://i.imgur.com/iLCVA38.jpg",
    "https://i.imgur.com/nKmSGNS.jpg",
    "https://i.imgur.com/9CCZ06t.jpg",
    "https://i.imgur.com/UzVR9Wc.jpg",
    "https://i.imgur.com/oTC8b7Y.jpg",
    "https://i.imgur.com/AYAFuAp.jpg",
    "https://i.imgur.com/iIqPZRE.jpg",
    "https://i.imgur.com/vrRwxs8.jpg",
    "https://i.imgur.com/uGnWQt2.jpg",
    "https://i.imgur.com/jKDGh0z.jpg",
    "https://i.imgur.com/4P3f7WN.jpg",
    "https://i.imgur.com/LcLSZkr.jpg",
    "https://i.imgur.com/uYhBQtE.jpg",
    "https://i.imgur.com/d1W918q.jpg",
    "https://i.imgur.com/MoEVktk.jpg",
    "https://i.imgur.com/sEKbjhk.jpg",
    "https://i.imgur.com/a07TLVS.jpg",
    "https://i.imgur.com/ruLM3Xl.jpg",
    "https://i.imgur.com/9NK0y7u.jpg",
    "https://i.imgur.com/1rmG2WN.jpg",
    "https://i.imgur.com/cu5CHyW.jpg",
    "https://i.imgur.com/TVS85lq.png",
    "https://i.imgur.com/evtQepL.jpg"    
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

#keyword = "RESPOND"

class DingZhen(BaseCog):
    """Public Display of Affection ~!"""

    def __init__(self, bot):
        self.gifs = gifs
        self.failmsgs = failmsgs
        self.version = __version__
        self.author = __author__

    @commands.command(aliases=["来点丁真", "丁真"], hidden=True)
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

    @commands.command(name="dingZhenver", hidden=True)
    async def _pda_version(self, ctx):
        """Show PDA version"""
        ver = self.version
        await ctx.send("You are using PDA version {}".format(ver))

