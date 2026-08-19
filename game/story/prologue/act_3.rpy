label prologue_harbor:
    $ quick_menu = False
    scene expression prologue_asset("images/background/xixi_wharf_dawn.png") with fade
    $ prologue_play_audio("audio/bgm/prologue_harbor.ogg", channel="music", loop=True, fadein=1.0)
    $ prologue_play_audio("audio/sfx/harbor_water.ogg", channel="sound", loop=False)
    call cinematic_narration("陈九忘了自己怎样走上同安街，又怎样走到西溪码头。晨雾未散，码头已聚满出洋的人。")
    call cinematic_narration("年轻后生背着包袱，父母妻儿赶来送行。一个女人跪在地上，死死抱住男人的腿。")
    call cinematic_narration("男人狠心掰开她的手，头也不回地上船。船开了，女人伏在石阶上哭得撕心裂肺。")
    call cinematic_narration("陈九胸口发闷。四十块大洋，三日。他这辈子都还不出来。")

    $ quick_menu = True
    show old_shuike normal at portrait_left with dissolve
    old_shuike "九少爷？又输了一夜？"
    old_shuike "你阿兄替你擦屁股，还得擦到哪一年？"
    chenjiu "阿叔……您就别损了。"
    old_shuike "不损你，你当我瞎？"
    old_shuike "再这样，不如过番去。做工、开矿、种橡胶——在老家活不下去的，过番总能搏条活路。"
    old_shuike "同安叶亚来当年也是穷得叮当响去了马来亚，后来做了吉隆坡的甲必丹。"
    old_shuike "哪像你，空顶着读书少爷的名头，不思进取，败光家业、丢尽陈家的脸面。"
    hide old_shuike normal with dissolve

    call screen culture_note("叶亚来", "马来西亚华商叶亚来（1837—1885），同安人。下南洋后成为吉隆坡华人甲必丹，招募华工垦殖开矿，为吉隆坡发展奠定基础。", "历史", "history_yap_ah_loy")

    $ quick_menu = False
    call cinematic_narration("陈九没有答话。他看着船驶出西溪，渐渐消失在晨雾里。")
    call cinematic_narration("他兜里没有一分钱，却欠着四十块大洋。他的母亲，还在家里苦苦等他。")
    call cinematic_narration("三日之后，若还不上，便是无尽祸事。前路茫茫，他被迫走到了人生的三岔路口。")
    return

label prologue_return_home:
    scene expression prologue_asset("images/background/chen_mansion_courtyard_dawn.png", "images/background/chen_house_evening.png") with prologue_slow_dissolve
    $ prologue_play_audio("audio/bgm/prologue_choice.ogg", channel="music", loop=True, fadein=1.0)
    call cinematic_narration("回到陈家大厝，陈九想向母亲坦白三块大洋输光的事，话到嘴边却怎么也说不出口。")
    call cinematic_narration("他不断想起大哥来赌场赎他时的震怒，也想起母亲临走时哀切的眼神。")
    call cinematic_narration("他悔，他恨。可一个赌徒的眼泪，向来最不值得可怜。")
    call cinematic_narration("他在院子里站了一夜。")
    call cinematic_narration("天亮时，三条路摆在他面前。")
    return

label prologue_first_choice:
    $ quick_menu = True
    menu:
        "第一重大选择"

        "去找同安城里的高利贷“黄三爷”借钱，先还掉春风楼的赌债":
            jump route_one_start

        "向家人坦白，接受大哥永泰的安排，下南洋投奔亲戚":
            jump route_two_start

        "不借钱，也不坦白；继续逃避，再去一次春风楼碰碰运气":
            jump route_three_start

label route_one_start:
    jump line1_start

label route_two_start:
    scene black with fade
    call cinematic_narration("【线二 · 水客信义】")
    call cinematic_narration("陈九决定向家人坦白。大哥震怒之后，要他下南洋投奔槟城的亲戚。")
    call cinematic_narration("线二后续剧情尚待接入。")
    return

label route_three_start:
    scene black with fade
    call cinematic_narration("【线三 · 批局春秋】")
    call cinematic_narration("陈九不借钱，也不坦白。他回房蒙头昏睡，醒来后仍心存侥幸，再赴春风楼。")
    call cinematic_narration("这一次，他竟连赢七把，不仅还清四十块赌债，还净赚一百多块大洋。")
    call cinematic_narration("他携银归家，以为否极泰来。路上，一桩突如其来的世事变故即将颠覆他的人生。")
    call cinematic_narration("线三后续剧情尚待接入；具体世事变故未作擅自补写。")
    return
