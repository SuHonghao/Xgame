label prologue_gambling_house:
    $ quick_menu = False
    call cinematic_narration("陈九揣着母亲省吃俭用攒下的三块大洋，走出陈家大厝。")
    call cinematic_narration("起初他确实谨记叮嘱，只想安分闲逛。可骰子的吆喝声从春风楼隐约传来，侥幸便再也压不住。")
    call cinematic_narration("他总觉得自己不同：陈家最聪慧的幼子，自幼博饼手气极佳，前几次不过是运气差。")
    call cinematic_narration("只要稳下心神，用上父亲教的本事，定能翻盘获利。")
    call cinematic_narration("他折返家中，从抽屉摸出二哥留下的旧银镯子。那是亲人的念想，也是他最后的赌资。")

    scene expression prologue_bg("images/background/chunfeng_casino_night.png") with fade
    $ prologue_play_audio("audio/bgm/prologue_casino.ogg", channel="music", loop=True, fadein=1.0)
    $ prologue_play_audio("audio/sfx/casino_crowd.ogg", channel="sound", loop=False)
    call cinematic_narration("春风楼名义上是茶楼，实则是闽南有名的赌场。木楼里烟雾缭绕，骰子、牌九、番摊，样样齐全。")
    call cinematic_narration("赌桌的暖黄灯光照在每个赌徒脸上，像涂了一层金。陈九觉得，那是世上最好看的颜色。")
    call cinematic_narration("骰子落进瓷碗，叮叮当当。这声音，陈九从小听到大。")

    scene expression prologue_bg("images/background/chen_house_morning.png", "images/background/chen_house_evening.png") with fade

    $ prologue_play_audio("audio/bgm/prologue_memory.ogg", channel="music", loop=True, fadein=1.0)
    call cinematic_narration("牌九桌在眼前褪去，换成陈家正厅八仙桌上的大红瓷碗。")
    call cinematic_narration("那年中秋，厅中灯火通明。父亲陈万田召齐六个孩子，要他们博一个状元的彩头。")

    call prologue_bobing_memory

    show expression Solid("#fff7d8") as prologue_white_flash at prologue_flash
    pause 0.55
    hide prologue_white_flash
    scene expression prologue_bg("images/background/chunfeng_casino_night.png") with fade

    call cinematic_narration("金花的冷光一闪——正厅温情散去，春风楼的牌九桌回来了。")
    call cinematic_narration("陈九的指尖复刻着父亲教他的握法、腕劲与听声辨点。昔日读书人的雅技，如今沦为赌桌筹码。")
    call cinematic_narration("儿时博的是福气、前程与家族期许；如今赌的是银元、家业与几代人的心血。")
    call cinematic_narration("那只红瓷碗还在陈家正厅供着。真状元没等到，等到的是春风楼里这一桌牌九。")

    $ quick_menu = True
    show chenjiu normal at portrait_left
    show jiuzhixian normal at portrait_right
    jiuzhixian "哟，九少爷来了！今日玩什么？牌九还是番摊？"
    call cinematic_narration("四面八方的目光投来。谁不知道几日前九少爷被扣在这里，最后还是他大哥来收拾残局。")
    chenjiu "牌九。大的。"
    jiuzhixian "九少爷豪气。"

    call prologue_gambling_result
    return

label prologue_bobing_memory:
    $ quick_menu = True
    show father normal at portrait_left
    father "九啊，博饼博的是个“中”字。博个状元，讨的是读书人的彩头。"
    father "咱们陈家“颍川衍派”，你几个哥哥都不爱念书，就你最聪敏。"
    father "阿爹盼你往后潜心向学，考个功名回来，光耀门楣。"
    call cinematic_narration("父亲握住幼年陈九的手腕，教他握法、腕劲，教他听骰子落碗辨点数。")
    father "这是读书人闲暇的雅玩。博的是福气，不是银子。来——掷一把。"

    label .choose_method:
        menu:
            "【中秋博饼】父亲将六颗骰子递到陈九手中。你准备怎么掷？"

            "稳稳掷下":
                $ bobing_choice = "steady"
                $ bobing_echo = "阿爹说过，手要稳，心也要稳。"
                $ prologue_play_audio("audio/sfx/dice_roll.ogg")
                call screen bobing_roll([4, 4, 4, 2, 3, 6], "三红")
                call prologue_bobing_result

            "狠狠砸进碗里":
                $ bobing_choice = "hard"
                $ bobing_echo = "阿爹说过，心浮气躁，连一秀都守不住。"
                $ prologue_play_audio("audio/sfx/dice_bowl_hit.ogg")
                call screen bobing_roll([4, 1, 2, 3, 5, 6], "一秀")
                call prologue_bobing_result

            "查看博饼规则":
                call screen bobing_rules
                jump .choose_method

    return

label prologue_bobing_result:
    if bobing_choice == "steady":
        call cinematic_narration("四 · 四 · 四 · 二 · 三 · 六。三红！堂上一片喝彩。")
        father "好。手稳，心也要稳。往后读书，也要这般沉得住气。"
        call cinematic_narration("父亲笑着把一枚“三红”饼饵塞进他手里。")
    else:
        call cinematic_narration("四 · 一 · 二 · 三 · 五 · 六。一秀。骰子蹦出碗沿，又滚回碗底，哥哥们哄笑起来。")
        father "急什么？状元急不来。念书亦然——心浮气躁，连一秀都守不住。"
        call cinematic_narration("父亲不恼，只轻轻拍了拍他的后脑勺。")

    call cinematic_narration("父亲把去年中秋那枚“状元插金花”的金花别在陈九衣襟上。")
    father "九啊，来年阿爹等你中个真状元。"
    hide father normal
    return

label prologue_gambling_result:
    $ quick_menu = False
    call cinematic_narration("头三把，陈九赢了。三块变九块，九块变二十七块。")
    call cinematic_narration("短暂的胜利冲昏了头脑。他笃定自己今日运势滔天，绝无败理。")
    call cinematic_narration("第四把，他输了。")
    call cinematic_narration("第五把，又输了。")
    call cinematic_narration("第六把……他继续押，继续输。桌上的银元越来越少，额上的冷汗越来越密。")

    if bobing_choice == "steady":
        call cinematic_narration("手要稳，心也要稳。")
        call cinematic_narration("可他的心早已不稳。")
    else:
        call cinematic_narration("心浮气躁，连一秀都守不住。")
        call cinematic_narration("他如今，连一秀的福分也赌光了。")

    scene expression prologue_bg("images/background/chunfeng_house_dawn.png", "images/background/chunfeng_casino_night.png") with prologue_slow_dissolve
    $ prologue_play_audio("audio/bgm/prologue_despair.ogg", channel="music", loop=True, fadein=1.0)
    call cinematic_narration("天将破晓。赌场渐渐冷清，赌徒尽数散去，只剩陈九僵坐在桌前。")
    call cinematic_narration("母亲的三块大洋、二哥的银镯子，尽数输得一干二净。长衫被冷汗浸透，刺骨冰凉。")
    call cinematic_narration("九指仙慢悠悠拨动算盘。清脆的算珠声，字字敲在陈九心上。")

    $ quick_menu = True
    show chenjiu normal at portrait_left
    show jiuzhixian normal at portrait_right
   
    jiuzhixian "九少爷，今日手气不佳，运势衰竭。"
    jiuzhixian "连本带利，加上局中拆借的筹码，你一共欠春风楼四十块大洋。"
    jiuzhixian "三日之内必须还清。否则……您懂规矩。"
    chenjiu "三……三日？这根本不可能……"
    call cinematic_narration("三块大洋已是家中巨款。四十块，对落魄的陈家而言，无异于天文数字。")
    pause 0.7
    jiuzhixian "三日。"
    pause 0.5
    jiuzhixian "逾期不还，债滚债，人抵债。"
    hide chenjiu normal
    hide jiuzhixian normal
    with dissolve
    return
