# 第三部分 · 线一 · 橡胶逆袭
label line1_start:

    scene expression prologue_bg("images/background/同安后街巷子.png") with fade
    call fullscreen_cinematic_narration("【幕一】黄三爷的账房") from _call_fullscreen_cinematic_narration    
    narrator "同安城后街。一条狭窄巷子的尽头，立着一扇不起眼的木门。"
    show chenjiu torn at center
    chenjiu "（抬手）"
    chenjiu "（又放下）"
    narrator "阿母还在家里等他回去吃面。大哥这会儿大约已经起身下田。只要现在转身，他还能回家，把昨夜的事一五一十说出来。"
    # TODO: confirm branch —— 叩门前的玩家选择，按剧情顺序推进
    narrator "陈九攥了攥拳，终于抬手叩门。"
    hide chenjiu with dissolve

    scene expression prologue_bg("images/background/黄三爷账房.png") with fade
    narrator "账房里光线昏暗。正中摆着一张老木桌，桌上是算盘、账簿、印泥和几沓契纸。"
    show huang_sanye zoom at center
    narrator "一个干瘦老者坐在太师椅上，慢悠悠捻着手里的念珠。"
    narrator "他便是黄三爷。城里赌急了的、做买卖断了周转的、急着凑盘缠过番的，都晓得这扇门。只不过进"
    narrator "来容易，出去时欠下什么，就没人说得准了。"
    huang_sanye "（上下打量）陈家九少爷？稀客啊。"
    show chenjiu look_down onlayer front at lower_left
    chenjiu "（脚步一顿）你认得我？"
    huang_sanye "春风楼昨夜那么大的动静，我想不认得也难。"
    huang_sanye "（把玩账本）说吧，欠了多少？"
    show chenjiu bitter onlayer front at lower_left
    chenjiu "（牙关发紧）四......四十块大洋。"
    huang_sanye "（慢悠悠抬眼，语气冰冷刻薄）：四十块。月利三分，十日为期。十日之后还不上，连"
    narrator "本带利五十二块。（抬头，目光如刀）九少爷，你拿什么还？"
    chenjiu "（喉间干涩）我家还有二十亩田的契——"
    huang_sanye "（冷笑）你大哥永泰肯画押？"
    huang_sanye "田没有，铺子没有，身上怕是连一块银元也没有。"
    show chenjiu clenched onlayer front at lower_left
    chenjiu "（咬牙）以后我自然还得起。"
    huang_sanye "以后？"
    huang_sanye "九少爷，你今日来借的，就是这个“以后”。"
    chenjiu "（沉默）......"
    huang_sanye "（重新捻起念珠）听说你念过几年书？学过算盘？"
    chenjiu "（抬眼）......念过。算盘会一点。"
    huang_sanye "（笑）那倒不算一无是处。"
    show chenjiu angry onlayer front at lower_left
    chenjiu "（炸毛）你——"
    huang_sanye "年轻人，急什么。"
    huang_sanye "我这里正好有一趟货，要从厦门港往南洋去。船上缺个识字会算的，替我点货、记账、看账"
    show chenjiu shocked onlayer front at lower_left
    chenjiu "（愣了一下）南洋。"
    chenjiu "要去多久？"
    huang_sanye "顺利的话，两三个月。"
    show chenjiu look_down onlayer front at lower_left
    chenjiu "工钱多少？"
    huang_sanye "（沉默）......你眼下缺的是四十块，对不对？这样。我先替你把春风楼那四十块垫了。"
    chenjiu "（皱眉）你替我还？"
    huang_sanye "不是白替你还。（伸出一根手指，在桌面上轻轻敲了敲）船钱、吃住，再加这四十块，都记"
    narrator "在你的工账里。你到了南洋替我做事，再从工钱里慢慢扣。"
    chenjiu "（盯着他）两三个月便能还清？"
    huang_sanye "（笑）九少爷识字，会算账，又不是那些只能扛包下矿的粗人。"
    huang_sanye "怎么，连四十块都挣不回来？"
    chenjiu "（被戳中）谁说我挣不回来？！"
    huang_sanye "那不就成了。"
    narrator "黄三爷慢悠悠从账簿底下抽出一张契纸。"
    huang_sanye "年轻人出去闯几年，也未必是坏事。运气好些，回来时说不定连你大哥典出去的田都一并赎"
    chenjiu "（攥紧拳头）（沉默）（他陈九闯下的祸，自己一样能收回来）"
    huang_sanye "（看着他的神情，知道火候到了）契纸被轻轻推到陈九面前。"

    hide huang_sanye
    hide chenjiu onlayer front
    with dissolve
    
    scene expression prologue_bg("images/background/务工协约.png") with fade
    narrator "最大的几个字写得端端正正：「出洋务工协约」"

    # 交互 · 危局：这张契纸，怎么办？
    menu:
        "A｜先把四十块还上——按手印":
            jump line1_contract_a
        "B｜不对劲——先把契纸看清楚":
            jump line1_contract_b
        "C｜越听越不对——这买卖不做，赶紧跑":
            jump line1_contract_c

label line1_contract_a:
    narrator "陈九拿起契纸，匆匆扫了一眼。"
    narrator "“出洋务工”、“随船理账”、“工银抵扣”。前几行同黄三爷方才说的似乎没有什么不同。"
    narrator "再往下，字越来越小，也越来越密。春风楼只给他三日。眼下能填上那四十块，比什么都要紧。"

    chenjiu "（心声）不过出去两三个月。等回来，什么都解决了。"

    #TODO：红手印交互
    scene expression prologue_bg("images/background/务工协约-红手印.png") with fade
    narrator "“啪”鲜红的指印落在契纸上。"

    show huang_sanye zoom at right
    huang_sanye "（低头看了一眼，嘴角终于露出一点笑）"
    hide huang_sanye with dissolve

    #TODO：细节图交互
    scene expression prologue_bg("images/background/务工协约-细节图.png") with fade

    show chenjiu shocked at left
    narrator "他忽然把契纸抓回来。这一次，他从头开始，一行一行往下看。越看，脸色越白。"
    narrator "「前欠银钱、船资、膳费，均由工银抵扣......」再往下——「受雇五年。」陈九呼吸一滞。「契期未满，不得擅离。」"
    chenjiu "（猛地攥紧契纸）五年？你方才明明说两三个月！"
    show huang_sanye zoom at right
    huang_sanye "我说的是船期。"
    show chenjiu angry at left
    chenjiu "你放屁！"
    narrator "陈九“啪”地一掌拍在桌上。"
    chenjiu "你说我替你跑一趟，回来慢慢清账！"
    huang_sanye "（点了点纸上那个鲜红的指印）九少爷。契是你自己看的。印，也是你自己按的。"
    chenjiu "（将契纸狠狠摔回桌上）你要拿我去做猪仔？我陈九是欠了钱，我认！可还轮不到你拿我当牲"
    hide chenjiu 
    hide huang_sanye
    with dissolve

    jump line1_final_choice

label line1_contract_b:
    # 承接 61-64：此时 chenjiu/huang_sanye 已在 onlayer front 被 hide，契纸仍在桌上
    narrator "陈九的手已经伸向印泥，却忽然停下。"
    narrator "今天老水客的话犹在耳畔。"
    narrator "他把契纸抓回来。这一次，他从头开始，一行一行往下看。越看，脸色越白。"
    scene expression prologue_bg("images/background/务工协约-细节图.png") with fade
    narrator "「前欠银钱、船资、膳费，均由工银抵扣......」再往下——「受雇五年。」陈九呼吸一滞。「契期未满，不得擅离。」"

    show chenjiu angry at left
    show huang_sanye zoom at right
    chenjiu "（猛地攥紧契纸）五年？你方才明明说两三个月！"
    huang_sanye "我说的是船期。"
    chenjiu "你放屁！"
    narrator "陈九“啪”地一掌拍在桌上。"
    chenjiu "你说我替你跑一趟，回来慢慢清账！"
    chenjiu "（将契纸狠狠摔回桌上）你要拿我去做猪仔？我陈九是欠了钱，我认！可还轮不到你拿我当牲"
    hide chenjiu
    hide huang_sanye
    with dissolve

    jump line1_final_choice

label line1_contract_c:
    scene expression prologue_bg("images/background/黄三爷账房.png") with fade
    show chenjiu torn at left
    show huang_sanye zoom at right
    chenjiu "（盯着黄三爷看了半晌）"
    chenjiu "（心声）四十块。两三个月。船钱、吃住还全由对方先垫。这条路来得实在太巧，也太容易了"

    show chenjiu normal at left
    chenjiu "（把契纸推了回去）算了。这买卖我不做。"
    huang_sanye "四十块不借了？"
    chenjiu "（嘴硬）我自己想办法。"
    narrator "其实连自己都不知道还能有什么办法。"
    chenjiu "（站起身，转身便走）"
    huang_sanye "九少爷慢走。"
    huang_sanye "只是你若走了，我今日便只能到陈家去收账了。"

    show chenjiu angry at left
    chenjiu "（脚步骤停，慢慢回过头）什么意思？"
    huang_sanye "（抽出另一张纸，上面赫然是春风楼的债据）九指仙天还没亮，就叫人把你这笔账递过来了。"
    chenjiu "（脸色变了）我欠的是春风楼。"
    huang_sanye "现在欠我了。"
    chenjiu "谁谁谁准你接的？！"
    huang_sanye "（笑）九少爷，债是谁欠的，可不是谁收都一样？春风楼那些还不上的账，向来由我接。"
    huang_sanye "你当然可以走。只是今日太阳落山以前，我若收不到四十块——"
    huang_sanye "我便带人去陈家。田契、房契，有什么算什么。九少爷拿不出来，总有人拿得出来。"
    narrator "两人隔着昏暗的厅堂对视。"
    hide chenjiu 
    hide huang_sanye
    with dissolve

    jump line1_final_choice

# 最终选择：生死分岔
label line1_final_choice:
    menu:
        "A（死亡结局）":
            jump line1_death
        "B（主线汇合）":
            jump line1_merge

# 共享对峙 -> GAME OVER
label line1_death:
    scene expression prologue_bg("images/background/黄三爷账房.png") with fade
    show chenjiu angry at left
    narrator "这一刻，陈九忽然什么都明白了。为什么九指仙肯一把又一把借筹码给他。为什么四十块银元说借便"
    narrator "借。为什么自己今日才刚踏进门，黄三爷就已经知道得一清二楚。"
    narrator "这根本不是两桩买卖。是一张网。"
    chenjiu "春风楼跟你是一伙的。"
    show huang_sanye zoom at right
    huang_sanye "九少爷，话别说得这么难听。九指仙做他的生意，我做我的生意。"
    chenjiu "他把人逼到还不起债，再送到你这里。"
    chenjiu "你俩放屁！他在前头放账，你在后头接债，再拿这些破契把人送去南洋——"
    huang_sanye "九少爷，说话要有凭据。"
    chenjiu "（气极反笑）凭据？"
    chenjiu "老子现在就出去报官，看你还跟谁讲凭据！"
    narrator "话音刚落，他转身就往外冲。"
    show huang_sanye angry at right
    huang_sanye "（变了脸色）拦住他！"
    narrator "帘幕后立刻冲出两名壮汉。"
    narrator "陈九哪里还顾得上别的，仗着年轻腿快，一把撞开其中一人，拔腿便往门外跑。"
    chenjiu "滚开！"
    hide chenjiu 
    hide huang_sanye
    with dissolve

    scene expression prologue_bg("images/background/死胡同-昏暗.png") with fade
    narrator "木门被他“砰”地一声推开。外头是一条逼仄狭窄的后巷。陈九连头都没回，一路狂奔。身后脚步声紧"
    thug "站住！"
    show chenjiu clenched at left
    chenjiu "（气急败坏）傻子才站！"
    narrator "前面就是巷口。只要冲出去——只要到了大街上——陈九猛地一个转身。"
    narrator "却忘了这条后巷拐角极窄，墙边还凸着半截老旧的砖石门垛。"
    narrator "“砰——！”一声闷响。陈九的额角结结实实撞在砖角上。"
    show chenjiu shocked at left
    chenjiu "（心声）......完了。"
    narrator "下一刻，他软绵绵地倒了下去。"
    hide chenjiu 

    narrator "两个追出来的打手当场刹住脚。"
    thug_a "......"
    thug_b "......"
    narrator "打手甲蹲下去，试探着推了推陈九。没反应。又伸手探了探鼻息。脸色瞬间变了。"
    thug_a "三、三爷......"

    show huang_sanye angry at right
    narrator "黄三爷拄着手杖赶出来，满脸怒气。"
    huang_sanye "（看见地上的陈九，声音戛然而止）一个十六岁的毛头小子你们都——"
    huang_sanye "怎么回事？"
    thug_b "（结结巴巴）他......他自己撞的。"
    huang_sanye "撞晕了？"

    narrator "黄三爷心里“咯噔”一下。亲自蹲下去探了探。"
    show huang_sanye afraid at right
    narrator "许久。脸色比陈九还难看。"
    huang_sanye "......"
    huang_sanye "死了？"
    narrator "巷子里陷入死一般的寂静。"

    hide huang_sanye 
    with dissolve

    scene expression prologue_bg("images/background/死胡同-昏暗-麻袋.png") with fade
    show huang_sanye afraid at right
    narrator "黄三爷低头看着陈九。方才还拍着桌子骂人的陈家九少爷，此刻一动不动地躺在地上。"
    narrator "这下事情麻烦了。骗个人去南洋是一回事。陈家九少爷死在自己账房门口，又是另一回事。陈家如今"
    narrator "虽败了，到底还是同安本地有宗族、有亲眷的人家。尸首一旦叫人认出来——"
    narrator "黄三爷脸色越来越难看。"
    huang_sanye "谁看见了？"
    thug_a "没......没人吧。"
    huang_sanye "什么叫“吧”？"
    thug_b "（吓得不敢出声）。。。"
    narrator "黄三爷在原地来回踱了两步。忽然停下。望向不远处的西溪。"

    # 独立结局界面：暂停剧情，玩家只能读取存档或返回主菜单。
    call screen line1_game_over(
        "黄三爷的快递（水葬版）",
        "GAME OVER",
        "四十块银元。三日。只要找到一条路，他总能翻回来。\n\n"
        "这回倒真上路了。只是没有去成南洋，也没有回成陈家。\n"
        "西溪替黄三爷收了这一单。\n\n"
        "少爷脾气　★★★★★\n"
        "逃跑速度　★★★★★\n"
        "过弯能力　☆"
    )
    return

# 选项A/B/C-B 主线汇合
label line1_merge:
    # 【选项A 或B 或C-B 主线汇合】
    scene expression prologue_bg("images/background/黄三爷账房.png") with fade
    show chenjiu angry onlayer front at lower_left
    show huang_sanye zoom at center
    narrator "这一刻，陈九忽然什么都明白了。"
    narrator "为什么九指仙肯一把又一把借筹码给他。"
    narrator "为什么四十块银元说借便借。"
    narrator "为什么自己今日才刚踏进门，黄三爷就已经知道得一清二楚。"
    narrator "这根本不是两桩买卖。是一张网。"
    chenjiu "春风楼跟你是一伙的。"
    huang_sanye "九少爷，话别说得这么难听。九指仙做他的生意，我做我的生意。"
    chenjiu "他把人逼到还不起债，再送到你这里。"
    huang_sanye "（笑）赌是你自己赌的。筹码也是你自己借的。现在我给你一条还债的路，有什么不好？"
    huang_sanye "（扬声）五年怕什么？年轻人，有的是力气。"

    narrator "陈九盯着契纸，忽然冷笑了一声。"
    chenjiu "你真当我陈九什么都不懂？三日还没到。把债据给我。四十块，我自己想办法。"
    huang_sanye "（脸色一沉）少爷就是少爷。到了这个时候，还要讲体面。可惜。从你进这扇门开始，就已经不是三日的问题了。"
    narrator "身后传来极轻的一声。"
    narrator "“咔哒。” 木门落了闩。"
    narrator "两侧帘幕后，不知什么时候已经多了几道人影。几个壮汉慢慢走出来。"

    chenjiu "（一把抄起桌上的算盘砸过去）滚开！"
    narrator "“哗啦——”算盘摔在地上。算珠滚了一地。"
    chenjiu "（后颈忽然传来一阵剧痛。眼前的光猛地晃了一下）"
    narrator "最后看见的，是地上散落的算盘珠。一颗。两颗。滚进桌底。"

    show chenjiu despair onlayer front at lower_left
    chenjiu "阿母——"
    hide chenjiu onlayer front
    hide huang_sanye
    with dissolve

    call screen culture_note(
        "契约华工",
        "鸦片战争后，西方列强在东南沿海招募华工，签订契约，被辱称为“猪仔”“苦力”。厦门在19 世纪40 至50 年代曾是西方国家从事苦力贸易的最大中心。见华侨博物馆资料“背井离乡·契约华工”板块。契约华工制产生于19 世纪20 年代，40 至70 年代形成高潮。",
        "历史",
        "history_contract_labor"
    )
    jump line1_act03

