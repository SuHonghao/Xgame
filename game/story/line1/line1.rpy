default line1_danger_a = None
default line1_danger_b = None
default line1_choice_1 = None
default line1_danger_c = None
default afu_alive = False
default line1_has_talisman = True
default line1_half_water = False
default chenjiu_ship_weak = False

define huang_sanye = Character("黄三爷")
define young_afu = Character("后生仔")
define afu = Character("阿福")
define old_sailor = Character("老水手")
define lin_toujia = Character("林头家")
define old_worker = Character("老劳工")

label line1_start:
    $ line1_danger_a = None
    $ line1_danger_b = None
    $ line1_choice_1 = None
    $ line1_danger_c = None
    $ afu_alive = False
    $ line1_has_talisman = True
    $ line1_half_water = False
    $ chenjiu_ship_weak = False
    jump line1_act1

label line1_act1:
    scene expression prologue_bg("images/line1/bg/huangsan_office.png", "images/background/chen_house_evening.png") with prologue_slow_dissolve
    show expression prologue_sprite("images/character/huangsanye/huangsan_normal.png", "images/character/jiuzhixian/jiuzhixian_normal.png") as line1_huangsan at portrait_right with dissolve
    call cinematic_narration("【线一 · 橡胶逆袭】")
    call cinematic_narration("旁白1")
    call cinematic_narration("旁白2")

    $ quick_menu = True
    huang_sanye "陈家九少爷？要借多少？"
    chenjiu "四……四十块大洋。"
    huang_sanye "四十块。月利三分，十日为期。十日之后还不上，连本带利五十二块。"
    huang_sanye "九少爷，你拿什么还？"
    chenjiu "我家还有二十亩田的契——"
    huang_sanye "你大哥永泰肯画押？"
    pause 0.6
    huang_sanye "罢了。我念你是读书人，识文断字、算盘利落，是个可用之人。"
    huang_sanye "我给你条捷径。你明天替我出一趟南洋公差，帮我押送几船货物。"
    huang_sanye "来回只需两月，差事轻松。四十块赌债，我们直接去春风楼替你还了，两清。"
    chenjiu "什么货物？"
    huang_sanye "都是些寻常商货，安稳得很，不用你费心操劳。"
    huang_sanye "九少爷只需按个手印，这事便了了。"

    hide line1_huangsan with dissolve
    scene expression prologue_bg("images/line1/cg/blood_contract.png", "images/line1/bg/huangsan_office.png") with dissolve
    call cinematic_narration("旁白3")
    call screen line1_danger_warning("危A · 按手印，还是翻脸")

    menu:
        "黄三爷将泛黄的契约推到陈九面前。"

        "按手印签约":
            $ line1_danger_a = "sign"
            jump line1_danger_a_sign

        "当场翻脸拒签":
            $ line1_danger_a = "refuse"
            jump line1_danger_a_refuse

        "夺门而逃":
            $ line1_danger_a = "escape"
            jump line1_danger_a_escape

label line1_danger_a_sign:
    call cinematic_narration("旁白4")
    call cinematic_narration("自愿远赴马来亚。落地务工五年。不得私自返程，不得擅离职守。")
    chenjiu "你骗人！这根本不是两月公差，是五年苦力！"
    chenjiu "你这是拐卖猪仔！"
    with hpunch
    pause 0.4
    scene black with Dissolve(0.4)
    call cinematic_narration("旁白5")
    scene expression prologue_bg("images/line1/bg/dark_room.png") with fade
    call cinematic_narration("旁白6")
    call screen culture_note("契约华工", "鸦片战争后，东南沿海出现契约华工贸易。厦门在十九世纪中叶曾是苦力贸易的重要中心之一。华工常被欺骗签约，远赴海外从事长期苦役。", "历史", "history_indentured_labor")
    jump line1_act2

label line1_danger_a_refuse:
    call cinematic_narration("旁白7")
    chenjiu "黄三爷！你这是拐卖人口、逼人卖身当猪仔！"
    with hpunch
    pause 0.4
    with hpunch
    scene black with fade
    call cinematic_narration("旁白8")
    call screen line1_game_over("不按手印按地板", "GAME OVER", "硬刚黄三爷，先把腿交了。")
    return

label line1_danger_a_escape:
    call cinematic_narration("旁白9")
    with hpunch
    pause 0.3
    with hpunch
    scene black with fade
    call cinematic_narration("旁白10")
    huang_sanye "少爷，我给您弹首《十面埋伏》~"
    call screen line1_game_over("黄三爷的快递（水葬版）", "GAME OVER", "请读档，回危A。")
    return

label line1_act2:
    scene expression prologue_bg("images/line1/bg/xiamen_port.png", "images/background/xixi_wharf_dawn.png") with prologue_slow_dissolve
    call cinematic_narration("【幕二 · 厦门港 · 过番】")
    call cinematic_narration("旁白11")
    call cinematic_narration("旁白12")

    scene expression prologue_bg("images/line1/bg/ship_cabin.png", "images/line1/bg/dark_room.png") with fade
    call cinematic_narration("旁白13")
    call cinematic_narration("旁白14")
    with vpunch
    pause 0.5
    call cinematic_narration("旁白15")

    $ quick_menu = True
    show expression prologue_sprite("images/character/afu/afu_sick.png", "images/character/chenjiu/chenjiu_normal.png") as line1_afu at portrait_left
    show expression prologue_sprite("images/character/npc/old_sailor_normal.png", "images/character/old_shuike/old_shuike_normal.png") as line1_old_sailor at portrait_right
    with dissolve
    young_afu "阿兄，我们……我们这是要去哪里？"
    chenjiu "马来亚。橡胶园。"
    young_afu "我阿母不知道我走了……她还在等我回家吃饭……"
    old_sailor "后生仔，下过南洋没有？"
    chenjiu "没。"
    old_sailor "那你听好。这条船，开出去就回不来了。"
    old_sailor "海上死的人，比活下来的多。饿的、病的、被打死的、跳海的……"
    old_sailor "能不能撑到岸，看你的命，也看老天爷收不收你。"
    old_sailor "你这种细孑仔，最经不起折腾。海上熬不过七天，就剩一把骨头让人扔进海里。"
    old_sailor "我跑这条线跑了二十年。每趟船开出去，回来时船舱都是空的。"
    hide line1_afu
    hide line1_old_sailor
    with dissolve

    call cinematic_narration("旁白16")
    call cinematic_narration("旁白17")
    call screen line1_danger_warning("危B · 淡水")

    menu:
        "第五日，陈九嗓子冒烟。淡水桶锁在甲板上。"

        "夜里偷船工淡水":
            $ line1_danger_b = "steal"
            jump line1_danger_b_steal

        "用母亲的护身符跟老水手换半勺水":
            $ line1_danger_b = "trade_talisman"
            $ line1_has_talisman = False
            $ line1_half_water = True
            jump line1_danger_b_trade

        "咬牙忍着，一滴不偷":
            $ line1_danger_b = "endure"
            $ line1_half_water = False
            jump line1_danger_b_endure

label line1_danger_b_steal:
    call cinematic_narration("旁白18")
    with hpunch
    scene black with fade
    call cinematic_narration("旁白19")
    call screen line1_game_over("淡水自由行（单程）", "GAME OVER", "海上规矩比赌桌硬。请读档，回危B。")
    return

label line1_danger_b_trade:
    old_sailor "水是你的命。别再赌这种命。"
    call cinematic_narration("旁白20")
    jump line1_ship_choice

label line1_danger_b_endure:
    old_sailor "能忍的，兴许能活。"
    call cinematic_narration("旁白21")
    jump line1_ship_choice

label line1_ship_choice:
    scene expression prologue_bg("images/background/coolie_ship_storm.png", "images/line1/bg/ship_cabin.png") with Dissolve(1.0)
    with vpunch
    call cinematic_narration("旁白22")
    call cinematic_narration("旁白23")

    if line1_danger_b == "trade_talisman":
        call cinematic_narration("湿布里，是用护身符换来的那半勺命。")
    else:
        call cinematic_narration("湿布里，只剩陈九自己省下来的一点涎湿。")

    menu:
        "高烧的后生仔抱着陈九的胳膊，一声声喊着“阿母”。"

        "把水分一半给后生仔":
            $ line1_choice_1 = "share_water"
            $ afu_alive = True
            $ chenjiu_ship_weak = True
            call cinematic_narration("旁白24")
            afu "九哥……"
            jump line1_ship_song

        "把水全部留给自己":
            $ line1_choice_1 = "keep_water"
            $ afu_alive = False
            $ chenjiu_ship_weak = False
            call cinematic_narration("旁白25")
            young_afu "阿母……"
            young_afu "阿母……"
            scene black with Dissolve(1.0)
            call cinematic_narration("旁白26")
            jump line1_ship_song

label line1_ship_song:
    call cinematic_narration("客头行厦门，批脚来就问。番银一下来，大厝起相排。")
    call cinematic_narration("帆船十八只，大厝砖仔壁。侨汇到一单，较好农事收一山。")
    call screen culture_note("下南洋惨状", "十九世纪中后期，大量闽南华工由厦门出海。船舱拥挤、缺水、疾病和风暴，使许多人未抵达目的地便死于海上。", "历史", "history_nanyang_voyage")
    jump line1_act3

label line1_act3:
    scene expression prologue_bg("images/line1/bg/rubber_forest_day.png", "images/background/chen_house_morning.png") with prologue_memory_dissolve
    call cinematic_narration("【幕三 · 马来亚橡胶园 · 苦工】")
    call cinematic_narration("旁白27")

    if line1_danger_b == "trade_talisman":
        old_sailor "活着就好。符还给你——我收水钱，不收神钱。"
        $ line1_has_talisman = True
        call cinematic_narration("旁白28")
    else:
        call cinematic_narration("海上那五日，我什么都没偷。偷了，就不是我阿母要的那个九了。")

    if afu_alive:
        show expression prologue_sprite("images/character/afu/afu_sick.png", "images/character/chenjiu/chenjiu_normal.png") as line1_afu at portrait_left with dissolve
        afu "九哥……我跟着你。"
        call cinematic_narration("旁白29")
        hide line1_afu with dissolve
    else:
        call cinematic_narration("旁白30")

    if chenjiu_ship_weak:
        call cinematic_narration("旁白31")
    else:
        call cinematic_narration("旁白32")

    call screen culture_note("马来亚橡胶", "橡胶原产南美，十九世纪末在马来亚试种成功。华侨参与种植、制造和贸易，推动橡胶业成为当地重要产业。", "历史", "history_malayan_rubber")

    $ quick_menu = True
    show expression prologue_sprite("images/character/lintoujia/lintoujia_normal.png", "images/character/jiuzhixian/jiuzhixian_normal.png") as line1_lintoujia at portrait_right with dissolve
    lin_toujia "你这般割法，树皮都烂了！"
    lin_toujia "这棵树废了，你知道一棵橡胶树值多少钱吗？"
    chenjiu "头家，我手生……"
    lin_toujia "手生？手生就去死！橡胶园不养废物！"
    with hpunch
    call cinematic_narration("旁白33")
    hide line1_lintoujia with dissolve

    scene expression prologue_bg("images/line1/bg/worker_dorm_night.png", "images/line1/bg/rubber_forest_day.png") with dissolve
    call cinematic_narration("旁白34")
    show expression prologue_asset("images/line1/props/piggy_token.png", "images/line1/props/rubber_knife.png") as line1_prop at truecenter with dissolve
    call cinematic_narration("旁白35")
    hide line1_prop with dissolve

    scene expression prologue_bg("images/line1/bg/opium_den.png", "images/line1/bg/worker_dorm_night.png") with prologue_slow_dissolve
    call cinematic_narration("旁白36")
    show expression prologue_sprite("images/character/npc/old_worker_normal.png", "images/character/old_shuike/old_shuike_normal.png") as line1_old_worker at portrait_right with dissolve
    old_worker "后生仔，抽一口，身上就不疼了。"
    hide line1_old_worker with dissolve
    call cinematic_narration("烟香甜腻。赊账也行。林头家从不拦。")
    call screen line1_danger_warning("危C · 烟寮", "这个选择可能导致死亡或坏结局。建议现在保存游戏。")

    menu:
        "烟灯在昏黄的茅屋里明灭。"

        "从此每日赊抽":
            $ line1_danger_c = "addicted"
            jump line1_danger_c_addicted

        "偶抽一口止痛，之后咬牙戒断":
            $ line1_danger_c = "quit"
            jump line1_danger_c_quit

        "死也不抽":
            $ line1_danger_c = "never_smoke"
            jump line1_danger_c_never_smoke

label line1_danger_c_addicted:
    call cinematic_narration("旁白37")
    call cinematic_narration("后来有人曾劝过他三次，他只笑。")
    call cinematic_narration("旁白38")
    scene black with fade
    call screen line1_game_over("福寿膏灯", "BAD END", "灯还亮着，人先灭了。请读档，回危C。")
    return

label line1_danger_c_quit:
    call cinematic_narration("旁白39")
    call cinematic_narration("旁白40")
    call cinematic_narration("后来，陈九再也没进过烟寮。")
    call screen culture_note("南洋种植园鸦片与猪仔币", "种植园常以可赊欠的鸦片与只能在园内流通的代币束缚华工。烟债和园币使劳工难以积蓄真实货币，也更难离开园区。", "历史", "history_opium_tokens")
    jump line1_act3_end

label line1_danger_c_never_smoke:
    call cinematic_narration("【疼并清醒着】")
    call cinematic_narration("旁白41")
    call cinematic_narration("后来，陈九再也没进过烟寮。")
    call screen culture_note("南洋种植园鸦片与猪仔币", "种植园常以可赊欠的鸦片与只能在园内流通的代币束缚华工。烟债和园币使劳工难以积蓄真实货币，也更难离开园区。", "历史")
    jump line1_act3_end

label line1_act3_end:
    scene black with fade
    call cinematic_narration("【线一前三幕完成】")
    return
