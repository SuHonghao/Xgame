## line1_act14.rpy — 幕十四 · 沦陷 · 救济（含危H）
## 严格按 线路一.md 原文逐字实现，未改写未删减

label line1_act14:
    scene expression prologue_bg("images/background/幕十四1.png") with fade
    call cinematic_narration("民国二十七年（1938）五月。厦门沦陷。") from _call_cinematic_narration_276
    call cinematic_narration("学堂刚开学两个月，日本人就打到了厦门。") from _call_cinematic_narration_277
    call cinematic_narration("厦门沦陷后，大批难民逃往同安、鼓浪屿。城里挤满了无家可归的人。番客婶们断了南洋侨汇，孩子饿得哭，老人饿得倒。") from _call_cinematic_narration_278
    call cinematic_narration("陈九本来可以躲进鼓浪屿的洋房里养老。可他看着难民，想起了自己当年在橡胶园挨饿的日子。") from _call_cinematic_narration_279

    show atu full at right with dissolve
    show chenjiu v4_frown at left with dissolve

    chenjiu "阿土，学堂先停课。校舍腾出来，给难民住。"
    atu "九，你还要怎么办？"
    chenjiu "开粥厂。我还有钱。天天熬粥，让逃难的人有口热的吃。"
    atu "钱会烧得很快。"
    chenjiu "烧就烧。钱是人挣的，人没了，钱有什么用？（正色）阿土，你帮我管粥厂。你算账利落，每一升米、每一文钱，都记清楚。莫让人贪了难民的口粮。"
    atu "好。咱们再搭一回手。"

    hide atu with dissolve
    hide chenjiu with dissolve

    scene expression prologue_bg("images/background/幕十四5.png") with fade
    call screen line1_danger_warning("危H · 救济的方式", "可能导致死亡。建议存档。")
    call cinematic_narration("有人鼓动当街骂敌发粮；有人劝躲进鼓浪屿关门做寓公。") from _call_cinematic_narration_280
    # TODO: 第二张，cwj留
    call cinematic_narration("系统提示：可能导致死亡。建议存档。") from _call_cinematic_narration_281

    show chenjiu v4_frown at center with dissolve

    menu:
        "A · 当街骂日军、公开发粮":
            $ line1_danger_h = "public"
            $ line1_relief_choice = "public"
            $ line1_relief_mainline = False
            jump line1_act14_gameover_public
        "B · 暗中开粥厂、学堂改救济所（主线）":
            $ line1_danger_h = "secret"
            $ line1_relief_choice = "secret"
            $ line1_relief_mainline = True
            jump line1_act14_mainline
        "C · 关门自保，躲鼓浪屿洋房":
            $ line1_danger_h = "self_preserve"
            $ line1_relief_choice = "self_preserve"
            $ line1_relief_mainline = False
            jump line1_act14_badend_cold_gold

label line1_act14_mainline:
    # 以下旁白仅当危H选B时播放
    call cinematic_narration("不喊口号，只给人一口热粥。主线继续（幕十五等基本剧情不变）。") from _call_cinematic_narration_282
    call cinematic_narration("九思学堂变成了九思救济所。校舍里住着难民，天井里支起大锅熬粥。陈九每天清晨起来，看着阿土记账、看着乡亲分粥，觉得这比在南洋数胶片踏实得多。") from _call_cinematic_narration_283
    call cinematic_narration("同安的乡绅们私下说：陈家老九发了南洋财回来，没盖大厝，没娶小妾，把钱全砸在学堂和粥厂上。这败家子，倒成了正经人。") from _call_cinematic_narration_284
    call screen culture_note("抗战救济", "资料载抗战期间华侨\"毁家纾难，回国参战，有力支援了中国抗战\"。南洋华侨不仅捐飞机、捐公债，也有大量回乡者投入本地救济。陈九的粥厂，是华侨实业家回乡后的另一种贡献方式——不碰批局，专做公益。", "历史", "history_wartime_relief")
    hide chenjiu with dissolve
    jump line1_act15

label line1_act14_gameover_public:
    call cinematic_narration("城门喊了一句，枪响。当场枪决。粥厂散，阿土收尸。") from _call_cinematic_narration_285
    call screen line1_game_over("发言完毕，人生完毕", "Game Over", "勇气可敬，方式送命。请读档，回危H。")
    return

label line1_act14_badend_cold_gold:
    call cinematic_narration("学堂停，粥厂不开。乡骂\"国难缩头\"。阿土仍私送粮，被扣时陈九更难借乡望。") from _call_cinematic_narration_286
    call cinematic_narration("尾声改写：一九四九年死在洋房，无乡绅送葬，无九思匾额。灵前一箱未花完的大洋。") from _call_cinematic_narration_287
    # 残缺结局【鼓浪冷金】在幕十七入口正式结算，此处先继续后续幕
    hide chenjiu with dissolve
    jump line1_act15
