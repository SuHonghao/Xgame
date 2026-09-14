label prologue_gambling_house:
    $ quick_menu = False
    scene expression prologue_bg("images/background/春风楼-外部.png") with fade
    call fullscreen_cinematic_narration("【幕二】春风楼 · 入夜") from _call_fullscreen_cinematic_narration_4
    call cinematic_narration("春风楼上胜春风。") from _call_cinematic_narration_407
    call cinematic_narration("同安城内，有个响当当的茶楼，名叫“春风楼”。这名义上是茶楼，实则是闽南一带有名的赌场。") from _call_cinematic_narration_408
    call cinematic_narration("上到二楼别有洞天，烟气混着茶气、人声与汗味扑面而来。八张赌桌一字排开，牌九、番摊、骰宝，桌桌围得水泄不通。铜钱撞在木桌上叮当作响，骰盅起落之间，喝彩声、咒骂声此起彼伏。") from _call_cinematic_narration_409
    
    show chenjiu normal at center
    call cinematic_narration("红布包揣在怀里，三块银元随着脚步轻轻撞着胸口。") from _call_cinematic_narration_410
    call cinematic_narration("陈九一路都没碰它。") from _call_cinematic_narration_411
    call cinematic_narration("直到走过街口，春风楼里骤然传出一阵喝彩。骰子撞进瓷碗，哗啦作响。") from _call_cinematic_narration_412
    call cinematic_narration("陈九脚下一顿，朝那边看了一眼。") from _call_cinematic_narration_413
    chenjiu "（心声）就去看看。"
    chenjiu "（心声）看看总不算赌。"
    call cinematic_narration("他继续往前走了两步，又停下来。") from _call_cinematic_narration_414
    chenjiu "（心声）他们玩他们的，我在旁边瞧两把，连银子都不摸。"
    call cinematic_narration("他转了方向。春风楼的灯火已经近在眼前。") from _call_cinematic_narration_415
    call cinematic_narration("越往前走，前几日输掉的赌债、哥哥典出去的半亩田，便越在脑子里打转。") from _call_cinematic_narration_416

    show chenjiu happy at center
    chenjiu "（心声）三块。"
    chenjiu "（心声）若赢成六块呢？"
    chenjiu "（心声）若今日真把前几日输掉的钱赢回来......大哥那半亩田就能赎回来。到时候，他把阿母的三块银元原封不动摆回她手里，再叫那些等着看他笑话的人看看——"
    chenjiu "（心声）他陈九哪里是什么只会败家的纨绔少爷。"
    call cinematic_narration("想到这里，陈九停在了春风楼门前。") from _call_cinematic_narration_417
    call cinematic_narration("怀里的红布包忽然又沉了几分。") from _call_cinematic_narration_418
    call cinematic_narration("“阿母信你。”阿母的话在耳边响了一遍。") from _call_cinematic_narration_419
    chenjiu "（心声）我又不是去赌个倾家荡产。"
    chenjiu "（心声）就三块。"
    chenjiu "（心声）赢回那半亩田，我立刻走。"
    call cinematic_narration("他抬起头。") from _call_cinematic_narration_420
    call cinematic_narration("春风楼内灯火通明。") from _call_cinematic_narration_421
    call cinematic_narration("陈九迈进了门。") from _call_cinematic_narration_422
    hide chenjiu with dissolve

    # 回忆场景慢叠化
    define memory_dissolve = Dissolve(1.8)
    scene expression prologue_bg("images/background/春风堂-内部.png") with fade
    call cinematic_narration("骰子落进瓷碗，叮叮当当。") from _call_cinematic_narration_423
    call cinematic_narration("这声音，陈九从小听到大。") from _call_cinematic_narration_424
    # 短暂停顿，让“从小听到大”落下来
    pause 0.5
    # 画面叠化——春风楼的牌九桌褪去，
    scene expression prologue_bg("images/background/陈家大厝-厅堂-大红瓷碗.png") with memory_dissolve
    call cinematic_narration("那年中秋，父亲陈万田把六个孩子召齐，六颗骰子滚进碗底，博一个状元的彩头。") from _call_cinematic_narration_425


    call prologue_bobing_memory from _call_prologue_bobing_memory

    # 叠化回现实：陈家正厅的回忆结束，画面回到春风楼。
    scene expression prologue_bg("images/background/春风堂-内部.png") with memory_dissolve
    call cinematic_narration("回忆结束。") from _call_cinematic_narration_426
    
    call cinematic_narration("“开——！”一声吆喝骤然撞进耳中。") from _call_cinematic_narration_427
    call cinematic_narration("陈家正厅的灯火、兄长们的笑声、父亲的身影，一齐散去。") from _call_cinematic_narration_428
    call cinematic_narration("眼前重新变成春风楼。还是骰子落碗的叮当声。只是那时候，一桌人等着他博个好彩头；如今，一屋子人等着看谁输、谁赢。") from _call_cinematic_narration_429
    call cinematic_narration("陈九站在门边，恍惚了一瞬。父亲那句话似乎还留在耳边——“今日的彩头靠福气，往后的功名，可得靠你自己。”") from _call_cinematic_narration_430
    call cinematic_narration("可也只是一瞬。") from _call_cinematic_narration_431
    call cinematic_narration("很快，春风楼里的喧闹便将那点旧日声音淹了过去。") from _call_cinematic_narration_432

    show jiuzhixian zoom onlayer front at lower_left      
    call cinematic_narration("就在这时，一个声音从人群中高高扬起。") from _call_cinematic_narration_433
    jiuzhixian "哟，九少爷来了！今日玩什么？牌九还是番摊？"
    call cinematic_narration("这一声“九少爷”喊得极响。四周顿时有人回过头来。") from _call_cinematic_narration_434
    call cinematic_narration("前几日陈九输光了钱，被扣在春风楼里走不得，还少爷脾气地大喊大叫“你知道我是谁吗？”，最后还是大哥典了田来收拾残局。这事早成了赌客们茶余饭后的笑谈。") from _call_cinematic_narration_435

    crowd "九少爷又来翻本了？"
    crowd "今日可别又叫家里人来领。"

    hide jiuzhixian onlayer front with dissolve
    call cinematic_narration("四下响起几声哄笑。") from _call_cinematic_narration_436
    
    #TODO:把陈九的图片改成脸红的
    show chenjiu bitter onlayer front at lower_left
    call cinematic_narration("陈九脸上一阵发热。") from _call_cinematic_narration_437
    call cinematic_narration("方才站在门外时，他还想着只拿三块银元试一试。此刻被众人这么盯着，那点本就摇摇欲坠的克制顿时变成了另一股劲。") from _call_cinematic_narration_438
    call cinematic_narration("他最受不得别人看轻。") from _call_cinematic_narration_439
    call cinematic_narration("陈九从怀里掏出红布包。手指碰到布结的一瞬，他迟疑了一下。") from _call_cinematic_narration_440
    chenjiu "（被人盯得窘极，一把把三块大洋拍在桌上）牌九。大的。"
    jiuzhixian "（眯眼笑）嘿~九少爷豪气~"

    hide jiuzhixian onlayer front with dissolve

    show chenjiu normal onlayer front at lower_left

    call cinematic_narration("第一把，陈九赢了。第二把，又赢。第三把，仍是赢。") from _call_cinematic_narration_441
    call cinematic_narration("三块银元很快翻成九块，九块又滚成二十余块。") from _call_cinematic_narration_442
    call cinematic_narration("桌边原本等着看笑话的人渐渐没了声音。") from _call_cinematic_narration_443
    call cinematic_narration("有人开始往他身后围。") from _call_cinematic_narration_444
    crowd "九少爷今日手旺啊！"

    show chenjiu happy onlayer front at lower_left
    call cinematic_narration("陈九听见这一声，腰背都直了几分。") from _call_cinematic_narration_445
    call cinematic_narration("他望着桌上越堆越高的银元，只觉得自己方才进来这一趟，再正确不过。") from _call_cinematic_narration_446
    call cinematic_narration("他早就说过——") from _call_cinematic_narration_447
    call cinematic_narration("前几次只是运气不好。") from _call_cinematic_narration_448
    call cinematic_narration("他会算，会看牌，从小博饼又总比几个哥哥手气旺。若不是前几回心急乱了阵脚，怎么会输成那副模样？") from _call_cinematic_narration_449
    call cinematic_narration("现在看来，果然如此。") from _call_cinematic_narration_450
    call cinematic_narration("再赢几把！把大哥典出去的半亩田赎回来。再把阿母那三块银元放回她手里。到时候，他还能多塞几块给她。想到这里，陈九嘴角压不住地扬起来。") from _call_cinematic_narration_451
    chenjiu "（心声）再赢一把就走。"
    call cinematic_narration("第四把。") from _call_cinematic_narration_452
    call cinematic_narration("输了。") from _call_cinematic_narration_453
    call cinematic_narration("陈九低头看了看被收走的银元，神色未变。") from _call_cinematic_narration_454
    chenjiu "再来。"
    call cinematic_narration("第五把。") from _call_cinematic_narration_455
    call cinematic_narration("又输。") from _call_cinematic_narration_456
    call cinematic_narration("方才围在身后捧场的人安静了些。") from _call_cinematic_narration_457

    show chenjiu normal onlayer front at lower_left
    call cinematic_narration("陈九坐直身体。") from _call_cinematic_narration_458
    chenjiu "（心声）无妨，不过两把。"
    call cinematic_narration("第六把。") from _call_cinematic_narration_459
    call cinematic_narration("还是输。") from _call_cinematic_narration_460
    call cinematic_narration("桌上的银元已经少了大半。") from _call_cinematic_narration_461
    jiuzhixian "九少爷，今日这运势......像是转了啊。"
    chenjiu "输几把就叫转运了？"
    jiuzhixian "自然不是。只是赌桌上的事，见好就收，也是本事。"
    call cinematic_narration("这一句落在陈九耳里，却像是在劝他认输。") from _call_cinematic_narration_462
    call cinematic_narration("他冷笑一声。") from _call_cinematic_narration_463
    chenjiu "急什么？继续。"
    hide jiuzhixian with dissolve
    call prologue_gambling_result from _call_prologue_gambling_result
    return

label prologue_bobing_memory:
    $ quick_menu = True
    call cinematic_narration("【交互 · 中秋博饼】") from _call_cinematic_narration_464
    call cinematic_narration("设计说明：本段为玩家可操作的掷骰交互。规则取自闽南中秋博饼（六骰入碗，以“四”之多少定奖），用以教学民俗，并与后文赌博形成反讽。交互结果仅影响回忆彩头与一句台词回响，不改变序章主线走向。") from _call_cinematic_narration_465
    call screen bobing_rules

    call cinematic_narration("厅堂里灯火通明，兄弟们围着八仙桌挤作一团。红瓷碗摆在正中，骰子每落一回，四周便跟着一阵起哄叫好。") from _call_cinematic_narration_466
    crowd "二举！二举！"
    crowd "才二举就喊成这样，等会儿九弟给你们博个状元看看！"
    call cinematic_narration("年幼的陈九早已经挤到桌边，伸手去抓骰子。") from _call_cinematic_narration_467

    show chenjiu young_zoom at center
    chenjiu "我来！我今年肯定博状元！"
    call cinematic_narration("众人笑起来。") from _call_cinematic_narration_468
    show father middle_zoom onlayer front at lower_left
    father "你倒是年年都要状元。"
    chenjiu "（理直气壮）去年差一点，今年总该轮到我了。"
    call cinematic_narration("陈万田被他逗笑了，把六颗骰子放进他手里。") from _call_cinematic_narration_469
    father "博饼图的是中秋团圆，博个好彩头。状元、榜眼、探花，叫着喜庆罢了。"
    call cinematic_narration("他看着陈九。") from _call_cinematic_narration_470
    father "真想中状元，可不能指望这六颗骰子。"
    call cinematic_narration("几个哥哥都笑起来。陈九却昂着头。") from _call_cinematic_narration_471
    chenjiu "那我以后真考一个回来。"
    father "好。"
    call cinematic_narration("父亲笑着拍了拍他的肩。") from _call_cinematic_narration_472
    #TODO:父亲立绘变成开心欣慰的
    father "那阿爹就等着。愿我九儿往后文运亨通，金榜题名，也给咱们陈家添个真正的好彩头。"
    hide chenjiu
    hide father onlayer front
    with dissolve

    call cinematic_narration("【玩家点击掷骰子】") from _call_cinematic_narration_473
    $ bobing_result = renpy.random.choice(["three_red", "one_show"])
    if bobing_result == "three_red":
        call screen bobing_roll([4, 4, 4, 2, 1, 3], "三红")

        $ renpy.movie_cutscene("video/骰子转动选项A.mp4")
        scene expression prologue_bg("images/background/序章-幕二16.png")

        call cinematic_narration("骰子停稳。三枚“四”赫然朝上。") from _call_cinematic_narration_474
        crowd "（桌边先是一静，随即爆出一阵喝彩。）三红！三红！"
        crowd "九弟好彩头！博了个“探花”！"
        call cinematic_narration("陈九眼睛一下亮起来，忙趴到桌边数了又数。") from _call_cinematic_narration_475
        call cinematic_narration("陈万田笑着把“三红”的彩头递给他。") from _call_cinematic_narration_476

        show father middle_zoom onlayer front at lower_left
        father "好。今日先讨个“探花”的喜气。往后书念好了，再自己挣个金榜题名回来。"
        call cinematic_narration("陈九接过彩头，却还盯着碗里的骰子。") from _call_cinematic_narration_477
        show chenjiu young_zoom at center
        chenjiu "可都三红了......"
        father "嗯？"
        chenjiu "再来一次，说不定就是状元呢。"

        menu:
            "陈九盯着碗里的骰子，到底要不要再掷一次？"
            "见好就收：三红已经很好了":
                $ bobing_greed = False
                call cinematic_narration("陈九看了看手里的彩头，到底还是把骰子放了回去。") from _call_cinematic_narration_478
                father "（笑）这就对了。好彩头讨到了，还得给哥哥们留些福气。"
                call cinematic_narration("众人笑着催下一人上桌。") from _call_cinematic_narration_479
            "再掷一次：万一下一把就是状元呢？":
                $ bobing_greed = True
                chenjiu "再一把！就一把！"
                crowd "三红还不够？九弟这是非状元不要啊！"
                chenjiu "差一点也是差！万一下一把就是呢？"
                father "（无奈摇头）你这个性子啊，得了好的，还总惦记着更好的。"

                hide chenjiu
                hide father onlayer front
                with dissolve

                call screen bobing_roll([4, 1, 2, 3, 5, 6], "一秀")
                call cinematic_narration("第二把骰子滚落。") from _call_cinematic_narration_480
                call cinematic_narration("这一次——") from _call_cinematic_narration_481
                call cinematic_narration("一秀。") from _call_cinematic_narration_482
                call cinematic_narration("四周又是一阵笑。") from _call_cinematic_narration_483
                call cinematic_narration("陈九盯着碗底，脸上的得意顿时垮了下来。") from _call_cinematic_narration_484
                crowd "瞧！探花叫你自己博成秀才了！"
                show chenjiu young_zoom at center
                show father middle_zoom onlayer front at lower_left
                chenjiu "（不服气）方才那把才算！"
                call cinematic_narration("陈万田笑着把骰子收走。") from _call_cinematic_narration_485
                father "好了。博饼讨的是彩头，又不是非要赢个高低。"
                call cinematic_narration("他把先前那份“三红”重新塞回陈九手里。") from _call_cinematic_narration_486
                father "今日有三红，就是你的福气。记着，福气来了要惜，不能总想着下一把。"
                call cinematic_narration("陈九嘴上没应，只低头摆弄着手里的彩头。") from _call_cinematic_narration_487
                hide chenjiu
                hide father
                with dissolve
    else:

        call screen bobing_roll([4, 1, 2, 3, 5, 6], "一秀")

        $ renpy.movie_cutscene("video/骰子转动选项B.mp4")
        scene expression prologue_bg("images/background/序章-幕二11.png")

        call cinematic_narration("六颗骰子停稳。只有一枚“四”。") from _call_cinematic_narration_488
        crowd "一秀！"
        call cinematic_narration("哥哥们笑着拍桌。") from _call_cinematic_narration_489
        crowd "九弟，你那状元呢？"
        call cinematic_narration("陈九低头看着碗里的骰子，明显不满意。") from _call_cinematic_narration_490
        show chenjiu young_zoom at center
        chenjiu "才一秀？"
        call cinematic_narration("陈万田把属于他的那份彩头递过去。") from _call_cinematic_narration_491
        show father middle_zoom onlayer front at lower_left
        father "一秀也是彩头。今日讨个“秀才”的喜气，往后书可得自己好好念。"
        call cinematic_narration("陈九接过，却没有走。") from _call_cinematic_narration_492
        call cinematic_narration("他仍盯着六颗骰子。") from _call_cinematic_narration_493
        menu:
            "陈九盯着碗里的骰子，到底要不要再掷一次？"
            "收下彩头：一秀也是好彩头":
                $ bobing_greed = False
                call cinematic_narration("陈九虽然还有些不甘，到底还是抱着彩头退到一旁。") from _call_cinematic_narration_494
                father "这才好。博饼靠的是福气，不能什么都由着自己挑。"
            "再掷一次：这一把手气不好":
                $ bobing_greed = True
                chenjiu "阿爹。"
                father "怎么？"
                chenjiu "方才那把手气不好。再来一次，我肯定能博个大的。"
                crowd "你怎么知道下一把就大？"
                chenjiu "我就是知道。"

                hide chenjiu
                hide father onlayer front
                with dissolve

                call screen bobing_roll([4, 4, 4, 2, 3, 6], "三红")
                call cinematic_narration("骰子再次落碗。叮叮当当。慢慢停住。") from _call_cinematic_narration_495
                call cinematic_narration("三枚“四”。") from _call_cinematic_narration_496
                crowd "三红！"

                show chenjiu young_zoom at center
                call cinematic_narration("陈九愣了一下，紧接着整个人都跳起来。") from _call_cinematic_narration_497
                chenjiu "我就说吧！我就说下一把能中！"
                call cinematic_narration("满堂都是笑声。父亲也笑。") from _call_cinematic_narration_498
                call cinematic_narration("这一次偶然的好运，被陈九牢牢记在了心里。") from _call_cinematic_narration_499
    hide chenjiu
    hide father onlayer front
    with dissolve
    return

label prologue_gambling_result:
    $ quick_menu = True
    call cinematic_narration("【交互】") from _call_cinematic_narration_500
    call cinematic_narration("【注释 删除】此前不管哪个随机结果，若选择A见好就收，则触发线二；如果选择B再来，则触发线一；") from _call_cinematic_narration_501
    call cinematic_narration("没多久，桌上只剩最后几块银元。") from _call_cinematic_narration_502
    call cinematic_narration("再一把。") from _call_cinematic_narration_503
    call cinematic_narration("输。") from _call_cinematic_narration_504

    show chenjiu shocked onlayer front at lower_left
    call cinematic_narration("陈九盯着空下来的桌面，久久没有动。") from _call_cinematic_narration_505
    call cinematic_narration("三块银元没了。") from _call_cinematic_narration_506
    call cinematic_narration("方才赢来的二十余块，也没了。") from _call_cinematic_narration_507
    call cinematic_narration("只要现在站起来，事情还来得及。") from _call_cinematic_narration_508
    call cinematic_narration("大不了回家。") from _call_cinematic_narration_509
    call cinematic_narration("大不了承认自己又犯了一回浑。") from _call_cinematic_narration_510
    call cinematic_narration("可就在陈九起身时，身后不知是谁笑了一声。") from _call_cinematic_narration_511
    crowd "九少爷这就走了？"
    crowd "方才不是还说玩大的么？"

    show jiuzhixian zoom at center
    jiuzhixian "（靠在柜边，也不留他，只悠悠添了一句）今日也赢过二十几块，差的不过一点运气。可惜了。"
    chenjiu "（猛地回过头）二十几块......"
    call cinematic_narration("方才明明已经到手了。") from _call_cinematic_narration_512
    call cinematic_narration("只要再来一把......") from _call_cinematic_narration_513
    call cinematic_narration("只要把本钱拿回来......") from _call_cinematic_narration_514
    show chenjiu clenched onlayer front at lower_left
    chenjiu "借我。"
    call cinematic_narration("九指仙没有立刻回答。") from _call_cinematic_narration_515
    chenjiu "（抬眼）怎么？怕我陈九还不起？"
    call cinematic_narration("少爷脾气又上来了。") from _call_cinematic_narration_516


    jiuzhixian "九少爷说的哪里话。陈家再怎么说，也是同安有头有脸的人家。"
    call cinematic_narration("他抬手示意伙计拿来筹码。") from _call_cinematic_narration_517
    jiuzhixian "借多少？"
    chenjiu "（咬了咬牙）三块。"
    call cinematic_narration("三块。") from _call_cinematic_narration_518
    call cinematic_narration("输。") from _call_cinematic_narration_519
    call cinematic_narration("再借。") from _call_cinematic_narration_520
    call cinematic_narration("再输。") from _call_cinematic_narration_521
    call cinematic_narration("每输一次，陈九都在心里重新算一遍。") from _call_cinematic_narration_522
    call cinematic_narration("下一把赢回来，立刻收手。") from _call_cinematic_narration_523
    call cinematic_narration("下一把。") from _call_cinematic_narration_524
    call cinematic_narration("就下一把。") from _call_cinematic_narration_525
    call cinematic_narration("到后来，他已经不再想半亩田，也不再想阿母。") from _call_cinematic_narration_526
    call cinematic_narration("他只剩下一个念头——") from _call_cinematic_narration_527
    call cinematic_narration("{color=#ff0000}{b}不能就这样输着出去。{/b}{/color}") from _call_cinematic_narration_528
    hide chenjiu onlayer front
    hide jiuzhixian
    with dissolve

    scene expression prologue_bg("images/background/春风堂-内部-无人.png") with fade
    call cinematic_narration("天将破晓。喧闹的赌场渐渐冷清，赌徒尽数散去，只剩陈九僵坐在赌桌前，身前空空如也。陈九一身长衫被冷汗浸透，贴身黏在身上，刺骨冰凉。") from _call_cinematic_narration_529
    call cinematic_narration("九指仙慢悠悠拨动算盘，清脆的算珠声，字字敲在陈九心上。") from _call_cinematic_narration_530
    call cinematic_narration("“啪。”") from _call_cinematic_narration_531
    call cinematic_narration("“啪。”") from _call_cinematic_narration_532
    call cinematic_narration("清脆的算珠声，一下一下落在空荡荡的春风楼里。陈九从小算盘打得极好。这一刻，却第一次不愿意听见算盘响。") from _call_cinematic_narration_533
    show jiuzhixian zoom at center
    show chenjiu shocked onlayer front at lower_left
    jiuzhixian "（慢悠悠抬头）九少爷，今日手气不佳，运势衰竭呀！连本带利、加上局中拆借的筹码，你一共欠春风楼四十块大洋。三日之内必须还清，否则......您懂规矩。"
    chenjiu "（脸色惨白，彻底慌神）三......三日？这根本不可能......"
    call cinematic_narration("三块大洋已是家中巨款，四十块大洋，对落魄的陈家而言，无异于天文数字。") from _call_cinematic_narration_534
    jiuzhixian "（语气冰冷，不容置喙）三日。逾期不还，债滚债，人抵债。"
    call cinematic_narration("·  ·  ·  ·  ·") from _call_cinematic_narration_535
    hide jiuzhixian
    hide chenjiu onlayer front
    with dissolve
    return
