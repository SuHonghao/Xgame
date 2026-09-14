label prologue_mansion:
    scene expression prologue_bg("images/background/陈家大厝-清晨.png") with fade
    call fullscreen_cinematic_narration("【幕一】陈家大厝 · 黄昏") from _call_fullscreen_cinematic_narration_3
    call cinematic_narration("同安陈家，祖上在这西溪畔也算数得着。陈万田老太爷年轻时勤俭持家，攒下百亩薄田、一间米铺。") from _call_cinematic_narration_387

    scene expression prologue_bg("images/background/陈家大厝-清晨-破旧.png") with Dissolve(2.0)
    call cinematic_narration("可到了光绪年间，家道早已没落——田亩典卖过半，米铺易了主，大厝还在，底气却空了。") from _call_cinematic_narration_388
    call cinematic_narration("再加九子分家，犹如一锅粥舀进九只碗，到了第九个儿子陈九这里，只剩下“九少爷”这个空名头。") from _call_cinematic_narration_389 

    show chenjiu normal at center
    call cinematic_narration("九少爷今年十六，生得眉清目秀，念过几年私塾，一手算盘打得噼啪响。偏这聪明劲全用在了歪处") from _call_cinematic_narration_390
    call cinematic_narration("他好赌，常常一赌就彻夜不归，本就不殷实的家底经他挥霍，更是雪上加霜") from _call_cinematic_narration_391
    hide chenjiu normal with dissolve
    call cinematic_narration("今日是九月初九，重阳。同安城里的赌场“春风楼”又开局了。") from _call_cinematic_narration_392

    scene expression prologue_bg("images/background/陈家大厝-厅堂.png") with fade
    $ quick_menu = True
    show mother normal at left
    call cinematic_narration("母亲王氏坐在正厅矮凳上，一双缠足搁在脚踏上，手里捻着佛珠。听见脚步声，缓缓抬起头。") from _call_cinematic_narration_393
    mother "九啊，又出去？"

    show chenjiu smile at right
    chenjiu "（脚步一顿，笑着凑过去）阿母，你怎么每回都听得出来是我？我走路有这么响？"

    mother "你几个哥哥走路，没你这么心虚。"

    chenjiu "（噎了一下，随即又笑）阿母——"

    mother "哪有心虚。今日重阳，几个朋友叫我进城喝茶。我总不能叫人家说，陈家九少爷如今连门都不敢出了。"
    call cinematic_narration("王氏看着他，没有责怪，只轻轻叹了口气。") from _call_cinematic_narration_394

    show mother disappointed at left
    mother "前日才出了那样的事，今日出去玩归玩，赌桌就别再碰了。"

    show chenjiu bitter at right
    call cinematic_narration("陈九脸上的笑僵了一瞬，很快又恢复过来。") from _call_cinematic_narration_395
    chenjiu "阿母，那日是我手气背，才叫他们看了笑话。今日我又不赌。"

    mother "九啊，手气好也罢，手气背也罢，沾上赌，都是赌。你这个性子，旁人一激，便什么都顾不得。"

    chenjiu "（有些不服气）那也得看什么事。我陈九再胡闹，输了认输，欠了认欠，什么时候做过没脸面的事？"
    call cinematic_narration("王氏望着他，神情软下来。") from _call_cinematic_narration_396


    show mother normal at left
    mother "阿母知道你心不坏。"
    show chenjiu look_down at right
    call cinematic_narration("她从袖中摸出一个红布包，塞到陈九手里。") from _call_cinematic_narration_397
    call cinematic_narration("陈九打开一看，是三块银元，立刻皱眉。") from _call_cinematic_narration_398

    chenjiu "阿母，这钱我不要。"
    mother "拿着吧。拿着傍身。"
    chenjiu "你攒这些钱不容易。"
    call cinematic_narration("他把红布包递回来，王氏却轻轻推了回去。") from _call_cinematic_narration_399
    mother "正因为不容易，才不想再看你为了几个钱跟人争、跟人欠。你打小就好面子，阿母知道你这两天心理难受得紧，这钱放在身上傍身，别再去赌。"
    
    call cinematic_narration("陈九捏着红布包，没有说话。") from _call_cinematic_narration_400
    mother "你大哥嘴上说得重，心里还是疼你。那半亩田的事，你记在心里便好，往后慢慢还。"

    show chenjiu look_up at right
    chenjiu "（抬起头）我当然还。等我以后挣了钱，不止半亩，我给他买十亩回来。"
    call cinematic_narration("王氏被他说得笑了一下。") from _call_cinematic_narration_401

    show mother disappointed at left
    mother "你啊，话总是说得大。"
    chenjiu "那是你儿子以后有本事。"
    call cinematic_narration("王氏替他理了理衣领。") from _call_cinematic_narration_402
    mother "有没有大本事，阿母不求。阿母只求你晓得什么事能做，什么事不能做。"
    call cinematic_narration("陈九低头看了看手里的红布包，终于收进怀里。") from _call_cinematic_narration_403
    chenjiu "晓得了。"
    mother "（点点头）阿母信你。"

    show chenjiu smile at right
    call cinematic_narration("陈九怔了一下，随即又笑起来。") from _call_cinematic_narration_404
    chenjiu "那今晚给我留碗面。"
    mother "好。"
    chenjiu "加个蛋。"
    call cinematic_narration("王氏笑着轻拍他一下。") from _call_cinematic_narration_405
    mother "早些回来。"
    call cinematic_narration("陈九应了一声，转身出了门。") from _call_cinematic_narration_406

    hide chenjiu normal with dissolve
    hide mother normal with dissolve

    call screen culture_note("闽南古厝", "陈家大厝为闽南传统“皇宫起”民居，燕尾脊、红砖墙、出砖入石；正厅供奉祖先与保生大帝，是闽南宗族社会的缩影。", "非遗", "culture_minnan_house")
    call screen culture_note("保生大帝信俗", "保生大帝本名吴夲，北宋同安白礁人，被闽南人奉为医神。同安家家供奉，出海前必祈平安。", "非遗", "culture_baosheng_dadi")

    return
