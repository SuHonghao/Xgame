label prologue_mansion:
    scene expression prologue_asset("images/background/chen_house_inner.png") with fade
    $ prologue_play_audio("audio/bgm/prologue_mansion.ogg", channel="music", loop=True, fadein=1.0)

    call cinematic_narration("光绪二十一年，秋。同安县西溪畔，陈家大厝。")
    call cinematic_narration("燕尾脊高高翘向天际，红砖赤瓦，白石墙裙。正厅悬着“颍川衍派”匾额。")
    call cinematic_narration("厅中八仙桌供着保生大帝神像。两侧楹联写着：颍水家声远，太邱世泽长。")
    call cinematic_narration("同安陈家，祖上在这西溪畔也算数得着。陈万田年轻时勤俭持家，攒下百亩薄田、一间米铺。")
    call cinematic_narration("可到了光绪年间，田亩典卖过半，米铺易了主。大厝还在，底气却空了。")
    call cinematic_narration("九子分家，犹如一锅粥舀进九只碗。舀到老九陈九这里，只剩“九少爷”这个空名头。")
    call cinematic_narration("九少爷今年十六，念过几年私塾，一手算盘打得噼啪响。偏这聪明全用在了歪处。")
    call cinematic_narration("他好赌，常常彻夜不归。赢了笑，输了赖，家底被他一点点掏空，像白蚁蛀梁。")
    call cinematic_narration("今日九月初九，重阳。同安城里的赌场“春风楼”，又开局了。")

    $ quick_menu = True
    show mother normal at portrait_left
    mother "九啊，又出去？"

    hide mother normal
    show chenjiu normal at portrait_right
    chenjiu "阿母，就去城里走走，会会朋友。"

    hide chenjiu normal
    show mother normal at portrait_left
    mother "你大哥前日才典了半亩田替你还赌债，昨晚气得咳了一宿。你还要往外跑？"

    hide mother normal
    show chenjiu normal at portrait_right
    chenjiu "阿母放心，今日就是去坐坐，和朋友走动走动，绝不碰赌桌，我发誓。"

    hide chenjiu normal
    show mother normal at portrait_left
    pause 0.4
    mother "你每回都这么说。"
    call cinematic_narration("王氏终于缓缓抬头，眼里含泪。她从袖中摸出一个红布包，搁在膝上。")
    mother "这是阿母攒了半年的私房，三块大洋。原是……是留着给你娶媳妇的。"
    pause 0.5
    mother "前日你刚欠了债被赌场扣着，是你大哥去赎的。"
    mother "阿母晓得你面皮薄，怕你在外被人奚落，又偷偷赊账惹事。"
    mother "你拿去身上揣着，不是让你赌，是让你手头宽裕，莫再低头求人、重蹈覆辙。"

    call cinematic_narration("陈九满脸发烫。他清楚这是母亲的血汗钱，也清楚自己屡教不改。")
    call cinematic_narration("家人的期许与按捺不住的赌瘾反复拉扯。犹豫许久，他终究伸手接过红布包。")

    hide mother normal
    show chenjiu normal at portrait_right
    chenjiu "阿母……我这回一定争气，好好做人。迟早把钱还给家里，好好孝顺您。"

    hide chenjiu normal
    show mother normal at portrait_left
    mother "阿母不要你还钱。"
    mother "阿母只要你安分守己，平平安安，别再让一家人替你担惊受怕、受人指点。"
    hide mother normal

    call screen culture_note("闽南古厝", "陈家大厝为闽南传统“皇宫起”民居，燕尾脊、红砖墙、出砖入石；正厅供奉祖先与保生大帝，是闽南宗族社会的缩影。", "非遗", "culture_minnan_house")
    call screen culture_note("保生大帝信俗", "保生大帝本名吴夲，北宋同安白礁人，被闽南人奉为医神。同安家家供奉，出海前必祈平安。", "非遗", "culture_baosheng_dadi")

    return
