label prologue_harbor:
    $ quick_menu = False
    scene expression prologue_bg("images/background/西溪码头.png") with fade
    call fullscreen_cinematic_narration("【幕三】码头 · 清晨") from _call_fullscreen_cinematic_narration_5
    show chenjiu despair onlayer front at lower_left
    call cinematic_narration("陈九忘记他是怎么走上的同安街，经过西溪码头。晨雾未散，码头上已聚了不少人——这是出洋的季节，每月都有船从厦门港发往南洋。") from _call_cinematic_narration_536
    call cinematic_narration("码头上站满了人。有背着包袱准备下南洋的年轻后生，有来送行的父母妻儿。一个女人跪在地上，死死抱住男人的腿不放。男人狠了狠心，掰开她的手，头也不回地上了船。女人伏在码头石阶上，哭得撕心裂肺。") from _call_cinematic_narration_537
    call cinematic_narration("陈九看着这一切，忽然觉得胸口发闷。") from _call_cinematic_narration_538
    call cinematic_narration("昨晚之前，他想的还是怎么把半亩田赢回来。") from _call_cinematic_narration_539
    call cinematic_narration("现在，四十块银元几个字沉甸甸地坠在他心头，压得他进退维谷、走投无路。") from _call_cinematic_narration_540
    chenjiu "（心声）阿母，他该怎么办？"
    chenjiu "（心声）三日之后拿不出钱，九指仙会做什么，他不知道。"
    chenjiu "（心声）可有一件事知道，春风楼的人若找不到我，就会找到陈家。"
    chenjiu "（心声）找到大哥。"
    chenjiu "（心声）找到阿母。"
    chenjiu "（心声）我不能就这么跑。更不能再让大哥典第二块田来救我。"
    show old_shuike zoom at center
    call cinematic_narration("一个背着褡裢的老水客从旁经过，走出几步，又退了回来。") from _call_cinematic_narration_541
    call cinematic_narration("（他姓陈，是陈家的远房族亲，常年往来码头，替乡里人捎信送批。春风楼里，他也见过陈九几回。）") from _call_cinematic_narration_542
    old_shuike "九少爷？"
    show chenjiu look_down onlayer front at lower_left
    call cinematic_narration("陈九回过神，下意识把脸别开。") from _call_cinematic_narration_543
    call cinematic_narration("老水客看看他皱巴巴的长衫，又看看那双熬得通红的眼睛，哪里还有什么不明白的。") from _call_cinematic_narration_544
    old_shuike "昨夜又在春风楼？"
    chenjiu "（沉默）......"
    call cinematic_narration("老水客叹了口气，也没有继续追问。") from _call_cinematic_narration_545
    old_shuike "九少爷，你好歹念过几年书，又会写、又会算。整日把心思耗在春风楼里，能耗出什么来？"
    call cinematic_narration("陈九脸上有些挂不住。") from _call_cinematic_narration_546
    chenjiu "阿叔，我又没说要赌一辈子。"
    old_shuike "那最好。"
    old_shuike "你还年轻。真想做点正经事，同安城里的商号、铺子，总有地方缺个识字会算的人。先把自己的日子过稳当，比什么都强。"
    call cinematic_narration("陈九没有接话。他转过头，出神地望向江面。") from _call_cinematic_narration_547
    call cinematic_narration("晨雾里，一艘船正在缓缓离开石阶。") from _call_cinematic_narration_548
    call cinematic_narration("几个背着铺盖的年轻后生挤在船头，岸上的家人还在一遍遍朝他们挥手。") from _call_cinematic_narration_549
    call cinematic_narration("老水客顺着他的目光望过去。") from _call_cinematic_narration_550
    chenjiu "他们都是去南洋的？"
    old_shuike "有去新加坡的，有去槟榔屿的，也有到了厦门港再转别处的。"
    chenjiu "同安也不是没活做。他们为什么非要跑那么远？"
    old_shuike "（看了他一眼）九少爷，你是没真正为一口饭犯过愁。"
    call cinematic_narration("陈九一怔。") from _call_cinematic_narration_551
    old_shuike "这年头田不好种，租不好交，一家几张嘴都等着吃饭。不是人人家里都有田、有屋，城里也不是人人都能找到活计。"
    old_shuike "（朝那艘渐渐驶远的船扬了扬下巴）有些人不是想走。是留在家里，也不知道明日靠什么过活。"
    chenjiu "那去了南洋......真能挣到钱？"
    call cinematic_narration("老水客听了，笑了一声。") from _call_cinematic_narration_552
    old_shuike "你当南洋遍地都是银元，弯腰就能捡？有人出去几年挣了钱，回来起厝置田；也有人在外头熬了十年八年，连回乡的盘缠都攒不下。"
    chenjiu "（讪讪）那还去？"
    old_shuike "因为总得讨生活。到了外头，一样靠手、靠本事挣钱。做工也好，进商号也好，没有哪一条路是轻省的。"
    chenjiu "（再次望向江面，小声）若是会写会算呢？"
    call cinematic_narration("老水客看了他一眼，听出了几分意思。") from _call_cinematic_narration_553
    old_shuike "识字会算，自然比全无本事强些。商号里记账、铺面里做事，都用得上。"
    old_shuike "（拍了拍陈九的肩）不过你先别想着往外跑。能在家门口踏踏实实找份事做，何必非得漂洋过海？外头的钱不好挣，海上的命也不是闹着玩的。"
    call cinematic_narration("老水客正准备离开，又想起什么似的回过头。") from _call_cinematic_narration_554
    old_shuike "往后若真有一天起了过番的心思，也记住一件事。"
    chenjiu "什么？"
    old_shuike "找熟水客，找正经商号。那些客头嘴里说得越轻巧，越要留神。"
    chenjiu "客头？"
    old_shuike "替人招工、找船路、介绍差事的。里头有正经做买卖的，也有专挑走投无路的人下手的。"
    call cinematic_narration("船上有人远远喊他。") from _call_cinematic_narration_555
    call cinematic_narration("老水客应了一声，又回头看了陈九一眼。") from _call_cinematic_narration_556
    old_shuike "九少爷，年纪轻轻的，有本事就用在正地方。"
    old_shuike "别真把自己的路，都耗在一张赌桌上。"
    call cinematic_narration("说完，他背着褡裢匆匆朝码头走去，很快混进了送行的人群里。") from _call_cinematic_narration_557
    call cinematic_narration("陈九站在原地，没有动。那艘船越驶越远。他却一直望着。直到船影彻底隐进晨雾里。") from _call_cinematic_narration_558
    hide old_shuike
    hide chenjiu onlayer front
    with dissolve
    return

label prologue_return_home:
    $ quick_menu = False
    call cinematic_narration("选项一：去找同安城里的高利贷“黄三爷”借钱还赌债。先过了这一关再说。") from _call_cinematic_narration_559
    call cinematic_narration("→ 进入【线一·橡胶逆袭】") from _call_cinematic_narration_560
    call cinematic_narration("选项二：回家，向家人坦白。") from _call_cinematic_narration_561
    call cinematic_narration("→ 进入【线二·水客信义】") from _call_cinematic_narration_562
    call cinematic_narration("选项三：怯懦逃避，不借钱，也不坦白。回房蒙头昏睡一夜，一觉醒来，输钱的郁结并未消散。侥幸与不甘反复啃噬心神，思来想去，心一横，还是想再赌一把！") from _call_cinematic_narration_563
    call cinematic_narration("→ 进入【线三·批局春秋】") from _call_cinematic_narration_564
    call cinematic_narration("·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·") from _call_cinematic_narration_565

    $ quick_menu = True
    menu:
        "天亮时，三条路摆在陈九面前。"

        "去找同安城里的高利贷“黄三爷”借钱还赌债。先过了这一关再说。":
            jump route_one_start

        "回家，向家人坦白。":
            jump route_two_start

        "怯懦逃避，不借钱，也不坦白。回房蒙头昏睡一夜，醒来后还是想再赌一把！":
            jump route_three_start

label route_one_start:
    jump line1_start

label route_two_start:
    scene black
    call cinematic_narration("【线二·水客信义】") from _call_cinematic_narration_566
    call cinematic_narration("陈九决定向家人坦白。大哥震怒之后，要他下南洋投奔槟城的亲戚。") from _call_cinematic_narration_567
    call cinematic_narration("线二后续剧情尚待接入。") from _call_cinematic_narration_568
    return

label route_three_start:
    scene black with fade
    call cinematic_narration("【线三·批局春秋】") from _call_cinematic_narration_569
    call cinematic_narration("陈九不借钱，也不坦白。他回房蒙头昏睡一夜，一觉醒来，输钱的郁结并未消散。侥幸与不甘反复啃噬心神，思来想去，心一横，还是想再赌一把！") from _call_cinematic_narration_570
    call cinematic_narration("这一次，他竟连赢七把，不仅还清四十块赌债，还净赚一百多块大洋。") from _call_cinematic_narration_571
    call cinematic_narration("他携银归家，以为否极泰来。路上，一桩突如其来的世事变故即将颠覆他的人生。") from _call_cinematic_narration_572
    call cinematic_narration("线三后续剧情尚待接入；具体世事变故未作擅自补写。") from _call_cinematic_narration_573
    return
