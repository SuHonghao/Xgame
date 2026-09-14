## line1_act07.rpy — 幕七 · 承包橡胶林 · 创业与对照
## 严格按 线路一.md 原文逐字实现，未改写未删减

label line1_act07:
    scene expression prologue_bg("images/background/幕七1.png") with fade
    call cinematic_narration("光绪二十八年至三十三年（1902-1907）。（若选B，有效创业自光绪三十年起。）") from _call_cinematic_narration_103
    call cinematic_narration("陈九和阿土的橡胶林越做越好。两人起早贪黑，把荒林重新打理起来。") from _call_cinematic_narration_104
    call cinematic_narration("创业的日子比当猪仔还苦。可这苦不一样。当猪仔的苦，是替别人苦；当老板的苦，是替自己苦。") from _call_cinematic_narration_105
    call cinematic_narration("陈九管账、跑销路；阿土管割胶、晒胶片。") from _call_cinematic_narration_106

    if line1_choice2 == "stay":
        call cinematic_narration("头一年赚五十块，第二年一百，第三年三百。到光绪三十三年，橡胶林扩到一百亩，雇十几个工人。") from _call_cinematic_narration_107
    elif line1_choice2 == "return_home":
        call cinematic_narration("晚两年开工，头几年更紧。到光绪三十三年，橡胶林约七十亩，也雇了人，可陈九心里总觉得——那两年，是找母亲换来的，也是永远追不回来的。") from _call_cinematic_narration_108

    scene expression prologue_bg("images/background/幕七2.png") with fade
    call cinematic_narration("一个夜晚，两人在自家工棚里喝工夫茶。") from _call_cinematic_narration_109
    call screen culture_note("闽南工夫茶", "陈九到了南洋，工夫茶的习惯一直没丢。烫壶、温杯、高冲、低斟。阿土是台湾人，喝惯乌龙；陈九给他泡闽南铁观音，他一喝就喜欢上了。", "非遗", "culture_gongfu_tea")

    show atu full at right with dissolve
    show chenjiu v2_calm at left with dissolve

    atu "（喝了一口）九，你还记得咱们刚来的时候吗？睡工棚，挨鞭子，吃不饱。"
    chenjiu "记得。怎么会不记得。"
    atu "（顿了顿）九，我托水客打听过了——我阿母还活着。她带着我弟弟，从台湾逃到了厦门鼓浪屿，给人洗衣服过活。"
    chenjiu "（一惊，又说不出话）......真的？"
    atu "（眼眶红了）我想寄钱回去。可我不知道怎么寄。"

    if line1_choice2 == "stay":
        call cinematic_narration("陈九放下茶杯：\"寄侨批。银和信可以一起寄。我寄给我阿母的就是这个。\"阿土一愣：\"你寄过了？\"陈九苦笑：\"寄了三封了。但一直没有回批。但没关系，鼓浪屿有地址。你阿母在。我帮你写。这一封，兴许寄得到。\"") from _call_cinematic_narration_110
    elif line1_choice2 == "return_home":
        call cinematic_narration("陈九放下茶杯：\"寄侨批。银和信可以一起寄。我以前在码头见过。\"他顿了顿，声音发干：\"我回同安的时候。大厝都空了。现在我想寄都不知道往哪寄。\"") from _call_cinematic_narration_111
        call cinematic_narration("（他握住阿土的手腕）：\"你这封我帮你写。至少——要让还有家的人，能寄得了批。\"") from _call_cinematic_narration_112

    call cinematic_narration("半年后，水客带回一封回批。是阿土的阿母请人代笔写的。") from _call_cinematic_narration_113

    # 回批全文
    # TODO: replace with letter/document UI
    call cinematic_narration("阿土吾儿：") from _call_cinematic_narration_114
    call cinematic_narration("钱收到了。阿母和你弟弟都好。你在南洋要保重，莫牵挂。") from _call_cinematic_narration_115
    call cinematic_narration("阿母日夜想你。你阿爸的仇，莫忘。你是台湾人，也是中国人。莫忘你的根。") from _call_cinematic_narration_116
    call cinematic_narration("阿母 字") from _call_cinematic_narration_117
    call cinematic_narration("光绪三十三年冬") from _call_cinematic_narration_118

    atu "（看完，泣不成声）阿母......阿母还活着......"
    chenjiu "（拍他肩膀，自己的手却在抖）活着就好。活着就有盼头。"
    atu "（抹泪）九，谢谢你。"
    chenjiu "（苦笑）谢什么。咱可是出生入死的好兄弟！"

    call cinematic_narration("阿土把回批读了三遍。陈九坐在旁边没说话，只是一味的喝着茶，苦涩在嘴里蔓延。") from _call_cinematic_narration_119

    if line1_choice2 == "stay":
        call cinematic_narration("他抽屉里已有三封自己的底稿，全无回音。看见阿土的回批，他才真正懂——侨批能到，是因为那头还有人接。他那头，或许已经没人了。") from _call_cinematic_narration_120
    elif line1_choice2 == "return_home":
        call cinematic_narration("他连底稿都写不出几封——地址空着，笔悬在半空。阿土的回批像一面镜子，照出他心底的空洞：同安老厝门在，人却不在，信也无处可投。") from _call_cinematic_narration_121

    call cinematic_narration("侨批——银养身，信养心。对阿土，是线；对陈九，是刺。") from _call_cinematic_narration_122

    call screen culture_note("侨批银信合一", "侨批是海外华侨寄回家乡的\"银信合一\"的家书。本幕用阿土\"有回批\"对照陈九\"无回批/无处寄\"，让玩家在对照里感到选择的重量。这条线里，侨批是乡愁纽带，不是陈九日后的职业。", "非遗", "culture_qiaopi")

    hide atu with dissolve
    hide chenjiu with dissolve

    jump line1_act08
