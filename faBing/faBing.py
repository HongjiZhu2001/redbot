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
""",
    """
hello hello😆😆
啊，听得到吗？😮😮
ki koei de yi ma si ka？😅😅
初次见面，请多关照呀！😘😘
是你们最甜甜甜的小草莓😽😽
锵锵！😝😝
梦想是成为偶像，然后全国巡演，吃遍大江南北~~🤤🤤
what!!
但是，**{user}**我超级不擅长吃辣辣的东西的。。。。。😖😖
（咚咚）😅😅
emm。。有一回点了一份辣子鸡，只是吃了那么一小小口，辣的半天说不出话啦！🤬🤬
**{user}**我好想点上吃辣的技能呀！😣😣
咳咳。。怎么一直在说吃的呀，要是被发现就糟糕惹😱😱
练习~练习~😤😤
啦啦啦啦啦😆😆
这次的新单曲超级好听的，真想让你们快点听到呀😚😚
为了给米娜桑展现出最完美的舞台效果，**{user}**我每天都有在认真练习呢😎😎
不要不信嘛~[傲娇][傲娇]
真的有在好好练习的😳😳
dc的大家都可以为我做证！🤗🤗
现在。。。现在是劳逸结合时间😎😎
嗯嗯~~😋😋
不算啦不算啦😜😜
你们要为我保密哦！🙇🙇🙇🙇
    """,
    """
我好想做**{user}**小姐的狗啊。
可是**{user}**小姐说她喜欢的是猫，我哭了。
我知道既不是狗也不是猫的我为什么要哭的。因为我其实是一只老鼠。
我从没奢望**{user}**小姐能喜欢自己。我明白的，所有人都喜欢理解余裕上手天才打钱的萌萌的狗狗或者猫猫，没有人会喜欢阴湿带病的老鼠。
但我还是问了**{user}**小姐:“我能不能做你的狗？”
我知道我是注定做不了狗的。但如果她喜欢狗，我就可以一直在身边看着她了，哪怕她怀里抱着的永远都是狗。
可是她说喜欢的是猫。
她现在还在看着我，还在逗我开心，是因为猫还没有出现，只有我这老鼠每天蹑手蹑脚地从洞里爬出来，远远地和她对视。
等她喜欢的猫来了的时候，我就该重新滚回我的洞了吧。
但我还是好喜欢她，她能在我还在她身边的时候多看我几眼吗？
**{user}**小姐说接下来的每个圣诞夜都要和大家一起过。我不知道大家指哪些人。好希望这个集合能够对我做一次胞吞。

猫猫还在害怕**{user}**小姐。
我会去把她爱的猫猫引来的。
我知道稍有不慎，我就会葬身猫口。
那时候**{user}**小姐大概会把我的身体好好地装起来扔到门外吧。
那我就成了一包鼠条，嘻嘻。
我希望她能把我扔得近一点，因为我还是好喜欢她。会一直喜欢下去的。

我的灵魂透过窗户向里面看去，挂着的铃铛在轻轻鸣响，嘉然小姐慵懒地靠在沙发上，表演得非常温顺的橘猫坐在她的肩膀。壁炉的火光照在她的脸庞，我冻僵的心脏在风里微微发烫。
    """,
    """
兄弟们，跟你们说个事

我同学好像魔怔了

整天**{user}****{user}**的喊，连做梦都在喊

没事的时候就喜欢拽着别人给**{user}**点关注

我们班一半的人都中招了

现在一有点风吹草丛，他们就在那鬼哭狼嚎的 

“**{user}**😭😭😭**{user}**😭😭😭” 

太哈人了😰😰😰我现在怀疑**{user}**是个什么传销组织

他们的人说话都跟猜谜一样

完全看不懂

但我又不敢报警

我同学威胁我说，要是我不给**{user}**点关注

就把我家燃气管道给砸了

所以说....

等等

等等

我家燃气管道.....我家燃气管道......

**{user}**...**{user}**...**{user}**！

**{user}**我真的好喜🥰🥰....**{user}**到底是谁啊

有没有懂哥....**{user}**🥰🥰**{user}**🥵🥵....给我讲一下

**{user}**🥰🥰到底是🥵🥵是....是....

.....................**{user}**是我主人捏~🥰🥰
    """,
    """
  **{user}**小姐昨天吃了酸菜鱼，可她不知道那是我。
  其实我就是那一条鱼。我从小就生活在海里，看海浪涛涛，听海风滚滚。海面上经常有渔民来打鱼，我知道那意味着什么。从我还是一颗小鱼苗的时候，就大鱼们说，不要去咬钩子，也不要跑到渔网里面。
  我很害怕，大鱼们说会有鱼被捞上去当场就被剖开，我想如果是我，那可能必死无疑了，我好怕死。
  但是从渔民口中听到什么“**{user}**”，什么“圣**{user}**之力”，什么“我想成为**{user}**小姐的狗”，可是什么是狗，是很厉害的生物吗，我想应该成为鲨鱼的。
  然后我看到他衣服上别着一个小勋章，上面一个裙子小女生。可能那就是**{user}**吧。
  偶然间的一瞥，我便爱上了那个小东西，我用我所谓7秒的记忆，将她铭记于心直到死去。我对嘉然的思念与爱伴随着我的成长一直在长大。
  我听说鱼被抓上去是要被剖、被刀、被切成两半，被放入热油，被炸、被烤、被煎被煮！但是被抓上去也是唯一能见到人类的机会。我不怕死，我一定要遇见**{user}**。
  终于，可能是过了一年吧，那帮人，也可能是换了一波人，来抓鱼了。我毫不犹豫就游了过去，为了嘉然，为了我的爱，为了我爱的她，虽然有千千万万条鱼，我知道我只是其中微不足道的一条罢了。可是这是我唯一的机会，我想要遇见她，我不怕死。
  我从来不想死，可为了**{user}**，我作为一条鱼，在人类手中我的结局只能是死于非命。我躺在砧板上，旁边的伙伴疯狂甩尾，而我很听话地一动不动，来了一个人，提着一把大刀，一下将我拍晕，我突然成为了灵魂升上天空。我的肉体已经不成模样，我从未见过有鱼变成这样。一瞬间，从渔民到杀我的人，他们所有的模样我都忘了。可是我的灵魂中已经铭刻了她的名字--**{user}**。
  我被放在了那种盘子上，看起来金黄，我不知道我的肉体成为了什么模样了。但是就在那一刻，她出现了。她就是嘉然，我心心念念的，嘉然。
  当她把筷子将我的肉体夹起那一刻，我的灵魂似乎在发光。她将它送入了嘴里--我的灵魂已经不再与我的肉体有关想，我的灵魂进入了高天之上，我看到里海里我伙伴们的嗤笑，我长辈们的哀嚎，我的爱鱼的哭泣，可是我没有任何的悲伤，因为唯有爱，是跨越物种跨越距离穿越时空的，我的灵魂已然得到所有境界和万种轮回里最为饱满的惬意与欣喜。当我回味着这一切的时候，我的灵魂开始从九天之上极速坠落于餐盘之中。
  灵魂要陨灭了。落在餐盘里的灵魂在消散前最后那一刻，我看到了**{user}**小姐皎然的笑颜
    """,
    """
转发这群蚊子 这个夏天蚊子只叮**{user}**[嘉然_略略略]

🦟🦟🦟🦟🦟🦟🦟🦟🦟🦟🦟🦟🦟
🦟🦟🦟🦟🦟🦟🦟🦟🦟🦟🦟🦟🦟
🦟🦟🦟🦟🦟🦟🦟🦟🦟🦟🦟🦟🦟
🦟🦟🦟🦟🦟🦟🦟🦟🦟🦟🦟🦟🦟
    """,
    """
两年前我身材不错，身高189体重90，在龙舟队划前两舱，偶尔还能替队长领桨。单人五百全队前三，大伙都戏称我是最快右桨。教练每次训练之后拍着我的肩膀说下一届队长我来当，挑碳桨我也是第一个挑。健身房、桨池、下湖，每周的训练我都充满了斗志。
因为我知道回去之后，可以在微信上和喜欢的女孩子谈天说地，出去喝酒吃饭。所以每次最后一个500米我冲的比谁都快。
后来她就突然从我的生命中消失了。我也受了腰伤强制退队，摆烂长胖到210斤，以前能连做六组俯卧撑的我已经找不到了。
直到几个月前看到**{user}**读小作文的那个视频。我仿佛又找到了两年前在岸边看着我们训练的那个女孩的身影。我又回到了训练的湖中，再一次转身，举起我的七号碳桨，喊一句：“最后一个500战术，都别给我掉速度！”然后用最大的力气划起航，怒吼着口号朝岸边冲去。
**{user}**，我就有这么喜欢你
    """,
    """
我现在好想失忆然后体验一下纯路人看见这评论区到底是什么感受🤣
。
。
。
。
。
。
不行，唯独那个女孩我不能忘记😭无论我如何失忆我都不会忘记你的**{user}**😭**{user}**你带我走吧**{user}**😭
    """,
    """
**{user}**小姐
昨天，我换了个城中村的新房子，虽然是租的
这里月租2300元，占据了工资的四分之一
我很早之前在宜家看到了一个桌子
可摆下它，我摆不下那张床了
先要摆下它，房租得加500
如果我想通风，我得带上口罩
这是我在大城市新换的房子
离公司近一点，我也许晚上有时间补录播
我觉得挺好**{user}**小姐
今天，还有个好消息，我发工资了
我是大城市的高级白领，工资刚好过万
昨天的房租花了我4600，因为要押一付一
我的信用卡要还4000元，还不包含吃饭
如果我生病了，我可能吃不上饭了
不过我很健康，无所谓吧？
领导下午给我发了条微信
说明天要交代个新项目给我
尽管明天是周六
我也很开心**{user}**小姐
今天，我还是加班了，没赶上你的直播
我穿过凌晨依旧烟火气十足的小摊
一阵饥饿的腹鸣后，耳边突然想起
“**{author}**要好好吃饭哦~”
我恍然明白
完成别人对自己的期待是一件很难的事情
哪怕这个人对你很重要
哪怕这个期待很简单
也许，我要更努力一点？**{user}**小姐
还记得我刚来这座城市
我的工资，是3000元
我花了4年时间
变成了如今10000元
我工资3000元的时候
我每天想的是
我要在这里
买多少平的房子
而10000元的时候，我却总在想
找个什么理由
在我逃回老家的时候
能更体面一点
我是不是有点不争气**{user}**小姐
恭喜你
已经快100W粉丝了
我以你为荣激励着自己
从最开始的一见钟情
到现在决心此生不弃
我想
这不仅是我对你的感情
这更应该是
我对梦想的态度才对**{user}**小姐
别给自己太大压力
记得早点休息
**{author}**永远守护着你
    """,
    """
**{user}**问我：”你有多喜欢我？”
我说：“300克”
**{user}**说：“我知道，你这个太老套了。300克是心脏的重量。”
我笑了笑，殊不知，这可是我的全部
因为一只🐭🐭的重量，就是300克啊！
    """,
    """
“最最喜欢你，**{user}**。”
“什么程度?”
“像500块红包一样。
“500块红包?”**{user}**再次扬起脸，“什么500块红包?
“在拼夕夕里，你突然抽到里500块红包的大奖，你为了提现这五百块付出了无数的心血，凑够了499.99元；凑够了999.99金币，凑够了99. 99幸运值，却永远因为缺少那最关键的0.01而不能提现。你说棒不棒?”
“太哈人了😨。”
“我就这么喜欢你🥰🥰🥰。”
    """,
    """
好想变成操场，这样就能设在**{user}**的小学里
    """,
    """
    对**{user}**的喜欢就像是尿裤子，所有人都看的出来，但只有自己才能真正感觉到那股暖意😘😘
**{user}**早上好捏，记得吃早餐[给心心]
    """,
    """
    是、是的…♡我想看你的动态！我真的想要看很多你的动态！**{user}**大人♡给我…好想要…想要看你的动态…♡呜呜、不行了，我已经变成看不到你的动态就不行的笨蛋了……啊啊♡好喜欢♡更多的、可爱的动态…是、哪怕有动态也会觉得不够，什么时候都想要看好多好多动态，除了看你的动态已经什么都想不了了…♡最喜欢的就是…看你的动态了♡看十条二十条之类的，根本满足不了…想要看十万条条以上的动态♡请、满足我…拜托…[**{user}**_锤头丧气][**{user}**_锤头丧气][**{user}**_锤头丧气]
    """,
    """
    细数**{user}**七宗罪:
1 三月十五日 只吃了一份水煮菜
2 四月十八日 游戏室可爱小鸡啄米般犯困 
3 五月十一日 一天只喝了三杯奶茶 没吃饭 还说自己会改正 让**{author}**不要学她
4 五月二十七日 声称自己休息日一睡可以一整天
5 五月二十八日 **{author}**说**{user}**玩连连看可以玩到凌晨五点
6 六月五日 肩膀拉伤
7 六月十八日 推流后睡觉 被喊醒后依然迷迷糊糊
**{user}** 我的**{user}**😭 你会在健身环回说**{author}**不要吵架 你会在小作文回说**{author}**要好好吃饭 你会在每次单播结束前都让**{author}**好好睡觉 为什么不会照顾自己😢 
没有单播 **{author}**会在评论区流泪黄豆
没有直播 **{author}**也会在评论区流泪黄豆
可是真正让**{author}**难受的 是不注意身体的淘气小**{user}**猪
希望**{user}**好好休息，接连的活动和训练不要有太大的压力，嘉心糖会陪伴你的，也会继续爱着你的。
    """,
    """
    这次真的对**{user}**梁木了，叫我们好好吃饭好好睡觉，她自己做到几条了。能不能对自己好一点，就是休息一下偷个懒又能怎样，我们还能忘了你么？
    """,
    """
    她独自坐在动捕房里，冰冷的设备噪音回荡着，她对着冰冷的屏幕，竭力唱出美妙的乐音。
 他们彼此隔绝，孤独的在键盘上舞动，夏夜褪不去的燥热充斥着他们的住所。
 他们与她，都明白彼此的一切只是虚拟的幻影。
 他们之中，有人是苦苦挣扎的打工者，即使30块的sc也要仔细斟酌许久才能打得出去
 他们之中，有人是普普通通的学生，一个138可能是他们好几天的生活费。
 她也只是，一个为了生活努力提升的女孩。
 她会连续几天练舞练到膝盖淤青，会因为直播时打了个嗝就崩溃，会在下播后偷偷哭上几个小时，她只是努力地想把一个可爱的形象展现给他们。
 当他们被生活的苦海挟裹，感官都窒息在怒吼的波涛里时，她像是一道光刺破了霾暗，引导众人探出水面，聆听女孩清脆的笑声。
 他们在屋顶漏水的出租屋里，在闷热的夏夜恼人的蚊鸣声中，在一动就会发出嘎吱声的狭窄的床上，时不时对着屏幕透出的光傻笑。
 她看不见他们，他们看不见她，但他们与她，早就以一种奇妙的方式结合了起来，也许屏幕能够传达的真的太干瘪太可笑，但她与他们都相信，彼此的情意一定能超越话语，到达彼此的心中，在荒寂的枯草地里生出一丛绚烂的野花。
 也许他们与她明早醒来时，仍要为今天的生计奔波而发愁，也许还会后悔昨晚打的30sc害的午饭又得少吃一半，但我们都相信，在不可避免的尾声到来之前，爱能够携着我们，冲破荆棘。
 晚安，**{user}**小姐。
    """,
    """
    “你觉得嘉然这个名字怎么样？”鼠鼠不经意的问着另一个鼠鼠。
“**{user}**吗？算是比较典型的女生的名字吧。”
“你的意思是很普通咯？”它显得有些不满意。
“确实蛮普通的，怎么了？**{user}**是谁啊？”它反问到。
鼠鼠一听有人问起**{user}**小姐，瞬时来了兴致，它滔滔不绝的开始介绍起**{user}**小姐有多可爱，她的舞有多好看，她的声音有多让人沉醉，她对鼠鼠们多么的宽容，她有多像一个天使。它的话仿佛永远也讲不完。
另一只鼠鼠边听着边点头，一副很感兴趣的样子，似乎也知道了**{user}**小姐的好。
奈何鼠鼠的词汇有限，对**{user}**小姐的赞美终于也词穷了。但它很满意，因为又有一只鼠鼠会喜欢上**{user}**小姐，简单的告别后鼠鼠要离开了。
另一只鼠鼠目送它走后，掏出了一张照片，突然笑了起来，很开心，很欣慰。照片上是一个带着鹿角头饰的女孩，小小的很可爱，她双手指着自己的脸颊，小嘴笑成了月牙型。是的这就是嘉然小姐，它当然认识嘉然小姐，只不过在它喜欢上**{user}**小姐时，还没有多少其他鼠鼠喜欢**{user}**小姐，而现在没有几只鼠鼠不认识**{user}**小姐，除了鼠鼠还有猫猫狗狗，越来越多的人认识了**{user}**，**{user}**小姐在她梦想的路上已经越走越远了。它小心翼翼的将照片压在枕下，枕着照片入睡，今夜它会做个好梦，梦里的**{user}**小姐牵着它的手走在星辰铺成的小路上，它看不到路通向哪里，只知道路的尽头有光。
    """,
    """
    我怕哪天就看不见**{user}**了，所以把那一天单播的**{user}**给“拷贝”了出来。

  一台能倒映人记忆与心智的投影机，它扫描一个人当时的所有状态并将其全挤压在一张24kb的软盘里，我抬着它贿赂了字节运营，在**{user}**单播的时候摆在她的身后，将那一天的**{user}**给保存了下来。

  “**{author}**，你们好呀！”

  之后的日子里我一有空就打开投影仪，它会投影出一个三维的那一天的**{user}**。她会对我笑，对我讲土味情话，对我今日发生的意外表示难过，那一天的**{user}**几乎是为我一个人直播的，投影仪会根据她当时的状态模拟出她不同的反应。

  但存在一些问题，我记录下来的那一天的**{user}**只直播50分钟，一旦过了50分钟她便会重置回到刚开始准备直播的状态，毕竟投影仪只有尽可能模拟这一功能，她的记忆会重置，她在这场直播学到的知识和我与她之间的欢笑不过是过眼云烟。

  “**{author}**，今天也很开心呢，要好好休息！也要好好生活哦！晚安”

  好多年过去，我对**{user}**这个初恋情人早已释怀，现在虚拟偶像可太虚拟了，最新的投影仪配上电脑存储允许你和记录人发生肉搏。但我还是拿着老投影仪和那张24kb软盘重播那一天的嘉然，即便她储备的梗和笑话土得发酸，即便她唱的过时歌曲让我耳朵长茧。嘉然的小脑袋一直想在这50分钟里把我抛出的话题想明白，不懂装懂的样子也经常闹出笑话，有几次她提到对**{user}**未来的期望，这时我只能苦笑着发“说点能回的”之类的弹幕。每当50分钟即将来临，**{user}**就温柔会对作为观众的我说上几句关心和离别的话，这时透过**{user}**那深蓝色的眼睛也能传递出来她那一天的体温。

  每到这里我就快陷进**{user}**的情绪中去，分不清她是那一天的**{user}**还是现在的**{user}**了，因为她关于**{author}**的话从来没有重复过，她对于嘉心糖烦恼的排解也从不是几句敷衍的废话，即使这些记忆马上会随着50分钟到来消逝，记住他们的是我。

  这台老旧的投影机怎么也模拟不完**{user}**那永无止境的温柔与热爱，有一颗偶像的心在24kb软盘里不停跳动着，直到永远。
    """,
    """
    没你好看，宝贝🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤没你好看，宝贝🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤没你好看，宝贝🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤没你好看，宝贝🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤
    """,
    """
    **{user}**，我跟别人石头剪刀布只能出剪刀了，因为你是我的拳布啊😭😭😭😭😭
    """,
    """
    **{user}**求求你快直播吧😭😭😭我在床上哭了四个小时😭崩溃了16次😭撞了134次墙😭划了397次手臂😭幻觉出现两次😭幻听出现三次😭扇了自己79个巴掌😭出现濒死感一次😭刚才昏过去了现在才醒来看到外面天都黑了我顿时又崩溃了😭😭😭
 5443
 10
    """,
    """
    快 快快 快快 快快 💃💃💃大脑在牵引💃💃💃歪 歪歪 歪歪 歪歪💃💃💃疯狂的着迷 荷尔蒙陷阱 请带我逃离💃💃💃
    """,
    """
    学校叫我参加成人礼我没去，我说我不想做人我想做**{user}**的狗
    """,
    """
    她想让大家知道，“我在努力”，想让大家认可她的努力。
所以她不愿意听别人说不拉不看，她愿意听别人说这次跳的好棒。
她不愿意被说可爱，因为她想努力呈现的是性感，是腰肢扭动所创造的视觉效果。
她要做偶像，所以她努力学唱歌，学跳舞，学控场，甚至学怎么wink。她把自己锚定在传统偶像那个位置上并为之努力。所以她想听打call，想听好看，想听老婆，不想听兄弟。哪有idol当粉丝兄弟的呢？
她提前看了视频，把每一关怎么过，怎么走都探了一遍，想给大家流畅的观看体验。
然后呢，别人说她太急了，剧透太多了。
其实确实效果不是很好，所以她改了。
她记了满满一本笔记，但是她不说。
等到**{user}**卡关的时候，她来帮忙，还要先小心翼翼问一句“能说吗？”
最后，当她拿起手柄却无法展现自己的努力的时候，她哭了。
努力就能换来回报，本身就是最大的天赋了。
她哭了，是她的努力没法被看到了，是她的心血没法被看到了。
傲娇是什么呢，是我不给你看我的努力，你自己去找吧，找出来了，夸夸我，我再偷偷笑一下嘿嘿嘿。
那句话怎么说来着，悄悄努力，然后惊艳所有人。
她其实梦想那个画面好久好久了，但是没人给她摆出那个惊艳的表情啊。
    """,
    """
    “你们是想和sc聊天还是和**{user}**聊天！”
“要什么圣诞礼物呀？你们想要哪个，我可以吗？”
“可以单推，不用取关，没关系，我不会吃醋的。”
“大家要好好吃饭，每天都要开开心心的。”
“**{user}**的手帐里，百分之80都是关于**{author}**的开心事噢！”
“你们怎么突然变得这么会说话了，我有一点不习惯。”
“我的**{author}**们都是很厉害的人!”
“每天都在想怎么可以让你们更开心一点。”
[给心心][给心心][给心心][给心心][给心心]
**{user}**不让我哭，我只是眼睛进沙子了
    """,
    """
    众士兵：“渴……渴……”
　　曹操：“大家再坚持一会！大家想想**{user}**”
　　众士兵：“乃琳🤤嘿嘿🤤乃琳🤤”
　　半个时辰后——曹仁：“主公！探险队找到了大量的水源！”
　　曹操：“哈哈哈哈，大家听到了吗？终于有水喝啦”
　　众士兵：“不去……一定要找到**{user}**🤤🤤🤤……”
    """,
    """
    父母问我对相亲对象的要求，我说得是个法学生，要懂希腊神话，要会玩ow而且玩dj绝对不上墙。
他们很不理解，但还是照做了。
我上班下班偶尔会经过一栋经年的大楼，泛黄的广告位上贴着破旧的海报，海报上是曾经光彩夺目的五位姑娘。我驻足，看着她娓娓垂下的金色长发怔怔出神，心绪像沉进温热的湖底。
刚发现这里有姑娘们留下的痕迹的时候，我还时常走近细细端详，曾以为怎么也看不够。但慢慢的，姑娘们的面容也愈发模糊不清，我就换成了驻足远望，细节看不清索性就不去看细节，她的身影早就镌刻在我的记忆深处难以抹去。
初识她的时候，她便像一只恼人的狐狸，眼眸中荡漾的波光怎么也挡不住，总是做些勾人的举动还装作不自知，真要她抖搂威风的时候又怯了场，叫人心生怜惜。但若是站在真正的舞台上，她又像翩跹的蝶，待到姑娘们惊慌失措时，又还得是她如春风般化解诸多难题。
于是越陷越深，无法自拔。
待到那场盛大的演出谢幕，我躲在角落里，看着她在人群中央笑靥如花，我鼓掌，为她，也为我终将结束的那段时光。
手机传来震感，是父母发来的消息，提醒我别忘了今天跟相亲的姑娘有个约会。相亲什么的当然不是我的本意，只不过是想从父母的唠叨里解脱出来，才顺口提出的那些要求，流畅的我都觉得有些不可思议。
可心中却又有些隐隐的期待。
到了咖啡厅，一眼就看到了在角落里捧着书的姑娘。额前的刘海末梢俏皮的打着卷，微微低头看着放在桌上的书，身后的长发一如既往的娓娓垂下。
“在看什么？”我温声问道。
“啊，是你啊，这不是要跟你见面了嘛，复习一下功课，到时候好把希腊神话当故事讲给你听。”
我有些恍惚，面前的姑娘落落大方，单手捧腮似笑非笑地望向我。有一瞬间我真以为是那个谈笑自如的姑娘回来了。
呜呜呜我编不下去了，**{user}**求求你带我走吧**{user}**😭😭😭😭😭😭
    """,
    """
    我们中老年人看**{user}**🤳🤳 并不是想要图什么🌹🌹🌹也不是完全为了消磨时光🕐🕐，我们是在追随时代的脚步🦶🦶🦶展示真实的自我 记录美好的生活留下美好的回忆🕣🕤🕥，我们虽然已经不再年轻👨🏻‍🦳但是我们有一颗永远年轻的心❤️✨❤️✨，与君共勉，亲人们💪💪💪🌹🌹🌹
    """,
    """
第1次看评论区
😅集体犯病是吧
第2次看评论区
🙄无语都什么呀？
第3次看评论区
😦鼠鼠好可怜
第4次看评论区
**{user}**😭**{user}**😭**{user}**😭**{user}**😭
带我走吧然然[大哭]
第5次看评论区
**{user}****{user}****{user}****{user}****{user}****{user}****{user}****{user}****{user}****{user}****{user}****{user}****{user}****{user}****{user}****{user}****{user}****{user}****{user}****{user}****{user}****{user}****{user}****{user}****{user}****{user}****{user}****{user}****{user}****{user}****{user}****{user}**
    """,
    """
    有没有一种可能，**{user}**现在离我不到五千米
有没有一种可能，我上周走过的路，**{user}**曾经走过。

有没有一种可能，今晚梦见**{user}**的时候，嘉然也会梦见我？
有没有一种可能，当我年老住进病房的时候，旁边躺着的就是曾经的**{user}**？

可能一切都只是我的幻想，但65万个小时后，当我们氧化成风，就能变成一杯啤酒上两朵相邻的泡沫。
就能变成一盏路灯下两粒依偎的尘埃。
宇宙中的原子不会凐灭，而我们，终究也会在一起。
    """,
    """
    “最最喜欢你，**{user}**”
“什么程度？”
“像宇宙牧的考达拉幼龙”
“考达拉幼龙？”**{user}**害羞的低着头“什么考达拉幼龙？”
“传说渡劫局里，宇宙牧打防战，弹尽粮绝的时候，不知道从哪偷来一个怪盗布缆鼠，最终发现龙族跟班又
发现了考达拉幼龙——你可以使用任意次数的英雄技能，牧师心理满是惊喜，发了不知道多少个‘哇喔’的
表情一边用英雄技能把防战三十护甲打穿之后又进行斩杀，不仅上了传说，还可以投稿视频，你说棒不棒？”
“太棒了。”
“但我并不是那样喜欢你。”
**{user}**这才扬起脸，好奇的问道“那是什么？”
“其实我是那只怪盗布缆鼠，如果没有发现你，我只是一只阴冷潮湿的老鼠，屁用没有。但因为我最终发现
了你，我的生命终于有了意义，我的存在终于有了荣誉。没人在意的老鼠也有他的奇迹，那就是你。最后
牧狗获得了胜利，而我们也可以永远的在棋盘之中紧紧的贴在一起，我就这么喜欢你。”
    """,
    """
    吱吱吱吱吱吱，吱吱吱吱吱吱吱吱吱吱😡😡吱吱吱吱吱吱吱吱吱吱吱吱
😆
😄
😀
🙂
😐
😑
😞
😧
😢
😭
吱吱吱吱吱，吱吱吱吱，吱吱吱吱吱，吱吱吱吱吱吱😭😭😭😭😭😭😭吱吱!!吱吱！!🚕💨💨🐀🐀🐀吱吱吱吱吱吱吱吱吱😭!!吱吱!!😭😭😭吱吱!
吱吱！吱吱吱吱吱吱吱吱吱！吱吱！吱吱！😭😭😭😭吱吱，吱吱吱吱吱吱，吱吱!😭😭😭😭吱吱吱吱吱吱吱😭😭😭吱吱吱吱吱吱吱😭😭😭吱吱😭😭😭吱吱吱吱吱吱吱😭😭😭吱吱吱吱吱吱吱😭😭😭吱吱😭😭😭吱吱吱吱吱吱吱😭😭😭吱吱吱吱吱吱吱😭😭😭吱吱😭😭😭吱吱吱吱吱吱吱😭😭😭吱吱吱吱吱吱吱😭😭😭吱吱😭😭😭😭😭吱吱吱，吱吱吱吱😭😭😭😭😭😭吱吱，吱吱吱吱吱吱吱😭😭😭😭😭😭吱吱吱吱吱吱吱吱吱吱吱😭😭😭吱吱，吱吱吱吱吱😭😭😭😭
    """,
    """
    **{user}**我有一项特异功能给你表演一下
[抓狂]→[给心心]
**{user}**你看，我能把心心从嘴巴里面取出来
[给心心]→🤗
嘿嘿 给你炫耀一下
🤗→😱
呀！我的心心怎么不见了！
嗯？怎么**{user}**有这么多心心呀。
哦～原来，是**{user}**把我的心心都偷走了呢[爱心]
    """,
    """
    “你认为世界第一打野是谁”
“是canyon，抓爆三路，引领节奏”
“不对，他gank不到我的心中”
“是karsa，精准定位敌方打野位置”
“不对，他定位不到我的感情”
“是厂长？料敌先机，掌握全局动向”
“不对，他掌握不了我心所想”
“那你心中的第一打野是谁”
“是**{user}**，我闭眼是他，睁眼是她，在上路是她，在下路还是她，我上游戏是她，我下游戏也是她。当我发现的时候，我已经着了魔”
    """,
    """
    王**{user}**！我承认你有几分姿色，如果我40岁，我一定离婚嫁给你，如果我30岁一定分手嫁给你，如果我20岁我一定不顾一切的去追你，可是我现在只有15岁，正面临初三期末考的压力，原谅我这一次，对不起，辜负了你。
    """,
    """
    “你知道，口腔溃疡了怎么办吗？
A:多喝热水 B:减少剧烈运动 C:口含维c泡腾片 D”
“A吧，”
“不对哦，是D”
“D?D啥也没有啊？你解释解释”
“A，多喝热水对于治愈口腔溃疡没有直接作用哦”
“B我知道是凑数的，C呐?”
“会很疼的”
“D呐”
“不能吃辣辣的东西”
    """,
    """
    **{user}**，我去买肉夹馍，要老板多放辣，结果走在路上它掉地上了😭沾到泥了，吃不了了。我哭了，原来这就是
辣馍喜欢泥🥰🥰🥰
    """,
    """
    杭州的六月不冷不热，就是这两天有点儿低气压。其他没有经历过梅雨季节的北佬，现在是不是都和我一样喘不过气呢？这样想着，还是不情愿地离开住处汇入上班的大潮。

前天她捏了一个巧克力的我，小小的，黑黑的，有点粉色。我擦，是不是我哪个论坛的账号给她发现了啊？我想大概她也经常冲浪。

我好像笨手笨脚的，经常伤害别人。我在挤进地铁的时候踩到了一个人的脚，想回头道歉，却被一股巨大的力量吸进了车厢。我想我也许被裹挟了。

我好像不太会说话。我断然拒绝了端午节加班的邀请，尽管有三倍工资。虽然不加班也没有什么特别的理由，但是我就是感到不爽。他寄吧谁啊，是不是在指导我。

我好像不太会读空气。昨天有人分享了一个网红店到群里，评价很高。我说一般吧，上次他家还把奶盖给我漏了，同事说中午高峰期下单的人那么多，理解理解。
其实我也天天点这家的奶茶，也确实只漏了那么一次。
我想同事说的对，多给店家一点肯定总是会进步的，不过今天就不喝奶茶了吧。
同事问我怎么不点，我说今天减肥。

我好像疑似是自我意识过剩了，我好像很喜欢大谈资历当老嗨，我好像对熟人社会有什么归属感，我好像……我好像什么用都没有，连纯路人也都一致同意。

只有她说“我不许你们这么说自己，你们都是很厉害的人”。

我觉得她应该只是在哄我，没有人比我更懂我自己，但我还是相信了她。
就算是装的，我也要从今天开始绝不摆烂。

我扣出四个字：双向奔赴！
她伸出手，好像想和我对手指。
我也伸出手，然后摸到了滚烫的屏幕。

我像是在机场等一艘船，我像是提前看了剧透但还是强迫自己看完整部电影，我像是在缘木求鱼，我像是在等一个不存在的奇迹。

开玩笑，哪有什么奇迹，想看就看，我还非要给自己找个借口，防御力低的一批，又给自己套一堆盾，有毒唯盾，rp盾，炒作盾，身份盾，自我感动盾……
我感觉我虚拟的批爆，因为这些东西在现实生活里都用不着，我在虚拟世界好像活出了自己的价值。
我觉得我像个啥β一样，但是我又好像并不后悔。

其实我也明白为什么。

因为她是我的虚拟偶像，所以我是她的虚拟观众。
    """,
    """
    今天是最后的演出了
       鼠鼠们其实早就猜到这样的结局
       5位女孩子们都各有自己的花路要走的，和鼠鼠们的欢乐时光也不会永远持续的。
       最后的一首歌，唱的很失败，因为女孩子们都哭的唱不出来了。
       但鼠鼠们也不像往常一样刷“摆烂”、“下播”什么的了，因为鼠鼠们也哭的打不了字了。
        鼠鼠们回到了下水道。女孩子们的帐号，永远不会再直播了。
        
        过了很久很久啊。。。。。。
        已经十年过去了，现在女孩子们，有做完她们的梦吗？
        有在外觅食的鼠鼠们，捡回了一张传单，是一个武馆的广告。
        “你们不知道啊，这武馆的女老板可厉害了！听说她二十几岁，就正面硬扛了那个什么范马勇次郎的全力一击，一棍子就给他毙了，是最年轻的海皇啊。”
        听着地上的人谈论，鼠鼠们想，这个人一定是一位刚烈的女子吧，叹服的离开了。
        “不过啊，我好像经常看到那位海皇在武馆一个人跳着芭蕾唉”“谁知道呢，可能不过是年轻的梦吧”
        
        鼠鼠们还听说，这座城市的一个大公司的新老总很厉害，把整个娱乐圈搞的风生水起。听人们说，这老总工作能力极强，只要一出马，就没有谈不成的生意，而且本人还是个大美女。
       但大部分人都不知道为什么，老总生活极其简单，基本天天在吃泡面，也不怎么打理生活，只是在办公室墙上，有一把破木吉他，打理的很干净。

       律政界逐渐有了这样的故事：有一位女律师，只在这一市有律所，但几乎所有人都像让她来当自己的律师，她收费不高，但从未输过一场官司。有人问她，为什么不去更好的城市发展，她也只是笑一笑，“因为这里的奶油冰淇淋最好。”

       不知从什么时候，下水道里突然就没有了《红色高跟鞋》的歌声，一大批鼠鼠都不见了。
       后来，如浪涌般的报纸报道了同一件事：欧洲森林里的一座古堡等来了失踪已久的公主。和她一同入住的，还有一批银盔银甲的骑士，一批忠诚卫士。听说，城堡的纹章很独特，就像一个高跟鞋。
      
       鼠鼠们经常找不到芝士蛋糕，但不知道为什么，在画廊后面的井盖口，总是有小山那么高的夹心软糖。
    """,
    """
    我不想上学了，我真想马上和**{user}**结婚啊！天天在家躺着花**{user}**的钱🤤，然然要我做家务，我就躺在地上装死😋 **{user}**要家暴我，我就让她用她的奶油面包拳狠狠锤我个够🥵，每天躺在家里喝饮料，恰水果，睡觉，吃饭，玩游戏，让然然天天去直播给我赚钱花，总而言之，这个学是一天也不能上了👿
    """,
    """
    那一幕怎忘记😉😉😉初次相遇的你🥰🥰🥰
😎😎😎💃💃💃😎😎😎💃💃💃
路人闹挺挺看我滑稽😣😣😣为你一笑我愿做猴戏😃😃😃
😎😎😎💃💃💃😎😎😎💃💃💃
一生能有几序🤧🤧🤧牵肠挂肚情义😊😊😊
😎😎😎💃💃💃😎😎😎💃💃💃
你大可不必猜忌寻觅🧐🧐🧐我愿意一生为你追寻😘😘😘
😎😎😎💃💃💃😎😎😎💃💃💃
🎺🎺🎺🎺🎺🎺🎺🎺🎺🎺🎺🎺🎺
🌉🌉🌉🌉🌉天作隔两岸🌉🌉🌉🌉🌉
就这般望着你👀👀👀难免我愁愁🥺🥺🥺
😎😎😎💃💃💃😎😎😎💃💃💃
除你我禽鸟🐦🦉🦅连花草🌹🌿成双荡悠悠👯👯
😎😎😎💃💃💃😎😎😎💃💃💃
你呀你冻我心房🥶🥶🥶酸我眼眶一生的伤😭😭😭
😎😎😎💃💃💃😎😎😎💃💃💃
你呀你彼岸观望置身一旁一生两望😟😟😟
😎😎😎💃💃💃😎😎😎💃💃💃
穷极一生又何惧😤😤😤也许只是一个背影😞😞😞
🌅🌅🌅🌅🌅天亮之后就出行🌅🌅🌅🌅🌅
🎺🎺🎺🎺🎺🎺🎺🎺🎺🎺🎺🎺🎺
    """,
    """
    肯定选半感染者啊，我不选半感染者我选什么🤤**{user}**，半感染者的**{user}**，嘿嘿，到时候追着我跑，嘿嘿嘿嘿，追上我就让你，嘿嘿嘿，**{user}**的牙齿，小小的，香香的，一口咬在我颈动脉上，我的血液顺着喉管滑进胃里，通过渗透融入到然然血液里，这样我就能永远的和然然在一起了🤤🤤**{user}**，我的**{user}**
    """,
    """
    ‍**{user}**，今天听你读小作文的时候真的哭了。
我们确实没有时光机，也确实回不到过去。从12月看到现在，我清楚的知道然然在这个过程中收到了多少恶意，受到了多少压力。我到现在依然能回想出当时健身环回那满屏恶意的弹幕，和面对弹幕时不知所措的你；也依然记得新年的那几天，当跳舞时音乐突然断了的时候急得哭了出来的你，当时到底承受了多少压力。**{author}**没有办法改变过去的这一切，也深知无论多么诚挚的道歉都无法弥补那时带给你的伤害。
但看到在舞台上闪耀着的你，看到在直播中开怀大笑的你，我似乎感觉以前的日子就像一场梦，突然明白了我们终究是要向前看的。既然**{author}**无法弥补过去对你的伤害，我们就一定要将我们最好的温柔送给你。既然然然当初选择用自己最真挚的情感交给**{author}**，我们就一定会将这颗心好好地保护起来。
**{author}**永远记得与你们的鸟巢之约，期待那一天早日到来，我不知道我能不能陪着你们走完全程。但只要一个魂们还在，只要这颗真心还在，我们就一定会用自己的全力把你们捧上世界之巅！
我的文笔也许没有其他的一个魂那么好，但是喜欢你们的心是永远真挚的。
    """,
    """
    我已经根本不想写小作文了，我除了发病怪文书已经什么都写不出来了。
明明是120分的喜欢，装成70分装到今天我已经装不下去了。
明明已经只想着她了，还要讨论什么国v日v大格局，参加什么泥巴战争，我已经装不下去了。
明明已经是个铁入脑萌萌人了，还要拟态清醒人开团或者打诨我已经装不下去了。

我的二刺螈人格除了喜欢喜欢喜欢喜欢喜欢喜欢喜欢喜欢喜欢喜欢喜欢喜欢喜欢喜欢喜欢喜欢喜欢喜欢喜欢喜欢喜欢喜欢喜欢**{user}**小姐已经什么都不剩了。

如果**{user}**小姐在我面前，我只想让自己的萌萌人格会把喜欢说一万遍。
如果我的萌萌人格说了这些话，他心满意足直接入土，我大概就能回归理性了吧。
那我的病就终于好了，就不再乱喊什么喜欢喜欢吓人了。我本就不适合喜欢什么东西。这世上只会有会对我的喜欢感到困扰的人，不会有需要我的喜欢才会幸福的人。
啊，入脑结束的时候，偏偏又想起了开始啊。

**{user}**的第一条动态里说：
“希望有人会因为喜欢我感到幸福。”

发病已经够丢人了，那我就大声说吧：

我确实因为喜欢你，感到幸福。
    """,
    """
    “你还在写小作文？”室友问
“我都看腻了，”他又补充“**{user}**也看腻了”
我顿了顿，没回答，又继续写
“不会吧不会吧你不会真动心了吧？对一个虚拟主播？”他yygq起来
“我确实喜欢上她了”我头也不抬
“你魔怔啦！真不像你”他咂咂嘴
我摁灭了手机，看向他“怎么样像我？”
“谁都可以喷，谁都看不起，谁都是xx，谁都不会爱”他咧着嘴，半是嘲讽半是调侃
他说的没错，我确实是这样，谁都踩一脚可以显得自己高人一等，谁都不会爱就不会难过。就像高冷的后宫男主角，万花丛中过片叶不沾身。多潇洒。
但我喜欢上**{user}**了。
我喜欢的是谁？那个穿孕妇服的3D皮套？那个会跳舞的一米吧？营业声线的小萝莉？本音《不可思议》的小恶魔？还是可能带了变声器的大叔？
也许都不是，也许都是。
也许明天我就看到《**{user}**人设崩坏？背后辱骂粉丝p用没有》
如果我不爱你，它们会是我的笑料，我会第一时间去嘲笑信众的愚蠢
也许明天我会忘掉小作文，忘掉发病，忘掉你
但我现在确实爱你，我因爱你而快乐
我的心中升起一团火，我把它变成一把匕首送给你
**{user}**，你会刺向我，还是拥抱我？
你会是我的盔甲，还是软肋
如果明天的我会被你杀死，就请用它刻我的墓碑
就写，这是一个爱上嘉然的疯子，不是傻子
    """,
    """
    今天是周一。
早五点我就等在直播间门口了,跑得太匆忙衣服都穿不好,被风吹得瑟瑟发抖,只好把脸贴在门缝上享受一下直播间昨晚留下的暖气,隐隐约约听到身后有人在说“哈哈哈**{author}**真可怜”像个沙口一样”!
趴了两个小时超管终于来了, 硬说我是小偷要报警抓我!我连忙解释自己是来看直播的,他不耐烦地骂了一句“**{author}**看寄8直播啊”,我当时就感觉脑袋好像被电了一样一片空白,唯唯诺诺地话都说不出来,跟在他后面大气都不敢出慢慢走到了观众席!
他问我要看什么,我心中一喜赶忙大声说“然然，我的然然! ! !”,然后就站着等我的然然!没想到他满脸嫌弃,说了一句“自己看直播都不会,低能别挡着别人做生意”,我一下子慌了,赶忙连着给他鞠躬道歉,磕磕巴巴地说私密马赛私密马赛,缩到边上用我的二手华为点开了直播间!
直播到了,却没我最重要的然然,我立马急了,三步并作两步地冲到超管前头,整店的人都将目光投向我这里!我从没被这么多人注视过,手指全都在发抖,脑门上的汗一下子就下来了,迷着了眼睛又不好意思摘眼镜擦汗,只好鼓起勇气开口“阿.....瓦塔西的然然....”超管好像知道我要说什么一样,打断道“**{author}**不想看就滚!”
我脚一软险些趴倒在地,眼泪不争气地渗了出来。怕泪水流下来太丢人,我就闭着眼睛开口求他“**{user}**对我来说真的很重要...还没说完,就被不知道谁的手推了一把,重地摔倒在地,门牙磕到冰凉的地上断了两颗,我也不敢捡起来,就蜷起身子卧在地上,把脸埋进土里面哭,还隐约听到四周传来此起彼伏的笑声,我太绝望了！
    """,
    """
    要问哪个人类最博学，可能谁都答不上来；但要问哪只老鼠最博学，那肯定就是我了，因为我是住在天文台的老鼠。

自我记事起，我就住在这个圆顶的大房子里。我喜欢听我的邻居们——也就是人类们聊天，“天文台”这个词就是从他们那儿学来的。听得多了，我才知道，他们是人类里最聪明的一批，而我自然就是老鼠里最聪明的一只啦。

他们和其他人类有很大不同:其他人类都是白天工作夜里睡觉，他们却一整天都在工作，白天读书，夜里就摆弄天文台屋顶的望远镜。其他人类喜欢用各种机器发出吵闹的声音，他们却总是轻声细语的，和老鼠一样。

而我也和其他老鼠不同:我住在书架上，却从不啃食书页，也不在书架上拉屎。但我可不是害怕人类，我只是爱护书籍。

这一天，安静的天文台突然热闹起来。仔细一听才知道，原来我们的太阳捕获了一颗新的彗星。我早在书里读到过，只不过是一些冰块和石头，没什么大不了的。不过嘛，我认为，作为天文台的一份子，我也应该看看那颗属于我们的星星。

于是，在又一天的观测任务结束后，我偷偷爬上梯子，凑到了望远镜前。

夜空中有许多小小的光点，但我们的望远镜只跟准其中的一个。我眨眨眼，彗星也眨眨眼。我耸耸肩，彗星也跟着上下晃动。看着她蓝白色的长裙，我忍不住说道:“她可真美。”彗星也说:“谢谢你。”我吓了一跳，“我没想到星星也会说话。”她回敬道:“我也没想到老鼠居然会说话。”

从此，每天晚上，我都会爬上望远镜，和她聊天。我说天文台的外面是无边的松林，风吹过时就像海浪的声音。她说每次掠过太阳时，高温都会蒸发掉她的一部分身体。我说春天的微风吹得我昏昏欲睡。她说她又从土星环上带走了不少纯净的冰。我说我是世界上最博学的老鼠，她却总说我是笨蛋。

每次离开，她总是穿着那件蓝白色的长裙，像迟到的新娘一样，消失在望远镜的视野里。

地球上的太阳升了又落，望远镜里的她时远时近。后来，我的毛发失去了光泽，我的牙齿再也咬不动人类的巧克力，从书架到望远镜的路途也越来越吃力。终于有一天我躺在平台上，伤心地看着我的彗星——她又一次飞过太阳，身后拖着那条蓝白色的长裙。博学的我这才想明白，那不是长裙，是彗星的眼泪。
    """,
    """
    枝江的冬天到了。
鼠鼠们依旧和它们喜欢的姑娘待在一起。
姑娘还是那个姑娘，她依旧善待着鼠鼠，还依旧是当初那个善良的姑娘。
鼠鼠却好像不再是当初的鼠鼠，虽然它们依旧喜欢着姑娘，依旧如往常一样，去四处呼朋唤友，去为姑娘引来她喜欢的猫，而当猫真来的时候，一切却都变了。
有些猫瞧不上不起眼的鼠鼠，觉得它们脏，配不上姑娘，鼠鼠觉得猫没有资格与它们讲这些，因此它们大吵大闹没日没夜的厮打。而鼠鼠内部也出现了不同已经，有些鼠鼠觉得不能再这样下去了，要把那些瞧不起它们的猫驱逐出去，不然姑娘迟早会变心。而有些鼠鼠却觉得为了姑娘，这些猫是不能缺少的。于是，猫与鼠的厮打，变成了一场混战，它们仿佛不知疲惫的撕扯着对方。
姑娘其实早就察觉到了这一切，但她不想伤害任何一个，她不停的喊着劝着，却没能劝下被戾气蒙蔽的鼠鼠与猫。
因而在有一天，当混战仍旧继续的时候，姑娘跪坐在地上，用她那并不宽广的手臂，把扭打在一起的鼠鼠猫猫抱在了怀里，嘴里轻轻唱着:          小年兽住在蔚蓝色的深海里
头上四个犄角一身金鳞
它和爸爸妈妈幸福生活在一起
日子过得快乐无忧无虑
每年的除夕夜晚到来那一天
爸爸妈妈总要短暂分离
这次他们说小年兽你已经长大了
也是时候去完成我们的使命
人间的小镇里
红灯笼照满地
充满欢声笑语热闹不停
可是年兽的出现
好像打破了喜庆
它们被鞭炮噼里啪啦赶出村落去
又到了年初年尾相连这一天
小年兽跟着爸妈来到人间
哪怕还是会惊慌失措灰头又土脸
但一想到大家能团圆苦也甜
人间的小镇里
红灯笼照满地
充满欢声笑语热闹不停
可是年兽的出现
好像打破了喜庆
它们被鞭炮噼里啪啦赶出村落去
小年兽很委屈
哭得很伤心
不懂为什么不受人们欢迎
妈妈说我们使命
是为了温柔提醒
每个人都应该相互团结用爱相聚
……
怀里的猫猫鼠鼠仍旧在撕扯，它们内心的戾气正如屋外的寒风吹散了姑娘的歌声，但姑娘仍旧在那唱啊，唱啊……
（憋了半天文笔不好见谅，结合实际自由发挥，希望姑娘的小年兽能真正唱到大伙的心里去，去吹散那股戾气）
    """,
    """
    这是**{user}**，我最仰慕的人，也是最后的信仰。
如果可以，我会为她放弃一切，可我一无所有。
地位，荣耀，财富，连我仅剩的一点点自尊，也被淹没在生活海洋的浮浮沉沉中。
如果我是石油佬，红色的SC将永远唱着**{user}**的赞歌。
如果我是高技术力，最高雅的二创将传播**{user}**的福音。
如果我是美术角虫，所有的色彩都被用来涂鸦**{user}**的可爱。
如果我是超管，盖在嘉然小姐直播间上的大手我全力掰开。
如果我是华子姐，一搏和嘉然小姐将实现资源互换。
可我什么也不是，我什么也没有，我打消了脑内的惊涛骇浪，披上名为现实的白色工服。
我什么也不是，一个普通人，一个想我一样普通的人，能为你做什么呢？
噢对，我还有一根烂笔头，它只能写出一写长短粗细不均的黑线条。
我用这些黑色线条，堆砌出我对嘉然小姐最后的呐喊。
——————————
“这是**{author}**，是最了不起的人。”
**{user}**就这么想着，就这么画着。
她想画一个暖窝，猫猫、狗狗，甚至鼠鼠，都不再受寒风侵蚀。
她想画一个糖罐，草莓、巧克力，甚至螺蛳粉味的嘉心糖，都成为她的珍藏。
她想画一个信箱，私信发病、作文发病，甚至黑屁文，她都逐一拆封。
**{user}**就这么想着，就这么画着。
暴雨倾盆打湿她的衣裳，她攥着画笔。
大雪飞霜铺满她的秀发，她攥着画笔。
黄沙漫天蒙蔽她的双眼，她攥着画笔。
她隔着荧幕，看不到网线那头的**{author}**，她只有一支画笔，一支普普通通的画笔，她能为**{author}**画着什么？
她就这么想着，就这么画着，涂鸦出她对**{author}**最真心的回应。
    """,
    """
    不管**{author}**怎么发病逆天，**{user}**永远都报以悦耳的笑声，永远都会回复大家“**{author}**太可爱啦”

被我引来第一次看直播的朋友在旁边问我“你说她真的这么想吗？”

那恍惚的一刹我想起了女朋友，已经失去的女朋友。
她是个像春天一样明媚的女孩子，只要她在的地方，枯槁的草木都变得活力起来。哪怕是我这样摆烂的人，也会被她无数次的肯定；哪怕我做出一些常人难以理解的行为，她还是说“你好可爱”，从她的眼神我知道，她并没有骗我。
如果没有遇到过她，我一定会和他一样觉得**{user}**只是营业罢了，在直播结束后，可能她会因为不用再看狂刷的发病弹幕长舒一口气。

但是我和他说
“是的，因为在可爱的人眼里一切都会变得可爱。”

说完我又想起来她给我说过最喜欢的泰戈尔的一句诗，也可以和**{author}**共飨。

You smiled and talked to me of nothing and I felt that for this I had been waiting long。

你微微地笑着，不同我说什么话。而我觉得，为了这个，我已等待很久了。
    """,
    """
    **{user}**当然会痛
世人独爱**{user}**，却没人真的记得蒂娜。

**{user}**只是一个爱吃零食的小女孩，吃不了辣辣的东西。
**{user}**也有一个梦想，就是想当偶像在全国巡演。
**{user}**为了实现梦想很努力，不断地学习练习。

可是，即使这样也没有人爱她，她与大家第一次见面时就受尽了嘲讽。
那次之后，她好像就从舞台上永远地消失了，又或者说，她从来就没有登上过真正的舞台。

后来大家也没有关心她去哪里了，她唯一留下的自我介绍视频也只会被A友们当作一个笑料提起，甚至连她的名字都像笑话一样，只要有人提起其他人就会哈哈大笑。

现在**{user}**正躲在角落里，看着在台上的**{user}**接受着掌声和鲜花，她掉下了眼泪，羡慕地说：“**{user}**我……”
同样在角落的鼠鼠用嘲笑声打断了她，还学她的语气和动作说：“但是，**{user}**我超级不擅长吃辣辣的东西……”

可**{user}**明明想说的是：“**{user}**我也想收到大家的鲜花和掌声。”

她终究没有成为大家的甜甜小草莓，
她当然会痛。
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

    @commands.command(name="fbver", hidden=True)
    async def _pda_version(self, ctx):
        """Show PDA version"""
        ver = self.version
        await ctx.send("You are using PDA version {}".format(ver))

