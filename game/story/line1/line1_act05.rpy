## line1_act05.rpy — 幕五 · 割胶学徒 · 立足
## 严格按 线路一.md 原文逐字实现，未改写未删减

label line1_act05:
    scene expression prologue_bg("images/background/幕五1.png") with fade
    call cinematic_narration("时间推移。光绪二十二年至二十四年（1896-1899）。") from _call_cinematic_narration_73
    call cinematic_narration("陈九和阿土在橡胶园里互相教学。阿土教陈九割胶，陈九教阿土算账。三年下来，陈九成了一把割胶好手，阿土也学会了记账。") from _call_cinematic_narration_74
    call cinematic_narration("陈九这辈子第一次发现，自己的聪明用对地方，是能活命的。") from _call_cinematic_narration_75
    call cinematic_narration("割胶讲究\"深浅快稳\"四个字。深，指要割透树皮，不能太浅，太浅胶液流不出来；也不能太深，太深伤到形成层，树就废了。浅，是说割的沟槽要薄，越薄胶液流得越多。快，是一刀下去，干脆利落，不能拖泥带水。稳，是手腕要稳，一刀一棵，棵棵一样。") from _call_cinematic_narration_76
    call cinematic_narration("阿土教他的这四个字，他练了整整一年。") from _call_cinematic_narration_77

    show atu full at right with dissolve
    show chenjiu v2_calm at left with dissolve

    atu "九，你割胶比我还快了。"
    chenjiu "那不也是你教的。"
    atu "是你有天赋。你那双手，天生就是割胶的。"
    chenjiu "（苦笑）我这双手，原来是赌牌九的。"
    atu "（正色）我跟你说个事。林头家最近看你有点不顺眼，上次你不是带我去找账房要回了猪仔币吗，他好像记住你了。"
    chenjiu "那怎么办？"
    atu "这么下去不是办法。我看，你不如换个位置。"
    chenjiu "换什么位置？"
    atu "去管账。你算账比谁都快。橡胶园这么大，胶杯、胶液、晒干后的胶片，每天进进出出多少账？而且林头家那个老账房总是算错帐，不中用了，他最近好像在找新的账房。你去毛遂自荐，替他管账。管账的活比割胶轻省，赚的也多。"
    chenjiu "（犹豫）他会信我？一个猪仔？"
    atu "你不去试，怎么知道？"

    hide atu with dissolve
    hide chenjiu with dissolve

    scene expression prologue_bg("images/background/幕五4.png") with fade
    call screen line1_danger_warning("危E · 考账", "可能导致死亡/坏结局。建议存档。")
    call cinematic_narration("陈九毛遂自荐。林头家冷笑：\"前几天刚从我的账房那要回了几个猪仔币，今天就敢来要管账了？胆子不小啊。不过我也不是那么不通情达理的人，只要你能通过考账我就敢用，但你要是敢诈我，你看我能不能让你活着回去。\"") from _call_cinematic_narration_78
    call cinematic_narration("随口报数：三百七十二加四百一十八加二百五十六加一百九十三得几。账本翻开半页在桌角。") from _call_cinematic_narration_79
    call cinematic_narration("系统提示：可能导致死亡/坏结局。建议存档。") from _call_cinematic_narration_80

    show lin_toujia zoom at right with dissolve
    show chenjiu v2_calm at left with dissolve

    menu:
        "A · 凭心算答对（主线）":
            $ line1_danger_e = "mental"
            $ line1_exam_choice = "mental"
            jump line1_act05_mainline
        "B · 偷看账本作弊":
            $ line1_danger_e = "cheat"
            $ line1_exam_choice = "cheat"
            jump line1_act05_gameover_cheat
        "C · 故意装傻推脱":
            $ line1_danger_e = "pretend"
            $ line1_exam_choice = "pretend"
            jump line1_act05_badend_pretend

label line1_act05_mainline:
    call cinematic_narration("\"一千二百三十九。\"林头家算了半天，没错。陈九进账房，成了新的账房先生。主线继续（幕六起基本剧情不变）。") from _call_cinematic_narration_81
    hide lin_toujia with dissolve
    hide chenjiu with dissolve
    call screen culture_note("闽南算盘文化", "陈九的算盘本事，是闽南商业文化的缩影。闽南人重商，算盘是基本功夫。资料载侨批业中\"花码\"等商业数字系统，正是闽南商业文化的产物。陈九从赌徒到账房，靠的正是这把算盘——同一个本事，用错地方是赌徒，用对地方是商人。", "非遗", "culture_abacus")
    jump line1_act06

label line1_act05_gameover_cheat:
    call cinematic_narration("眼风一扫账本。林头家：\"狗东西！\"打断手脚扔出园，伤口化脓无人医。感染而死。") from _call_cinematic_narration_82
    call screen line1_game_over("开卷有益，闭卷有命", "Game Over", "赌徒的手再害一命。请读档，回危E。")
    return

label line1_act05_badend_pretend:
    call cinematic_narration("\"我......算不清。\"被赶回割胶，账房给了别人。") from _call_cinematic_narration_83
    call cinematic_narration("若执意不读档：因为得罪了林头家，契约五年变十年。中年死于胶林。阿土独自发家，回乡之后还念叨着：\"同安有个陈九，本可逆袭的。\"") from _call_cinematic_narration_84
    call screen line1_game_over("割胶割到退休（强制）", "Bad End", "算盘放下，刀就放不下。可读档重选A回归主线。")
    return
