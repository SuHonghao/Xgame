## line1_act17.rpy — 幕十七 · 尾声 · 九归（含结局结算）
## 严格按 线路一.md 原文逐字实现，未改写未删减

label line1_act17:
    # 分支入口（按原文优先级）
    # - 若危H选了「自保」→ 跳转结局【鼓浪冷金】（见本幕末「残缺尾声」），不播放九思学堂石凳开场。
    # - 若危I选了「求疏通」→ 仍可进入下列主线尾声，但家书与解说牌改用「垢名换命」标注句；阿土若活着，不并肩露面，只在隔墙/来信中出现。
    # - 其余主线玩家 → 正常播放下列「九归故里」正文（与原版一致）。
    if line1_danger_h == "self_preserve" or line1_relief_choice == "self_preserve":
        jump line1_act17_cold_gold
    jump line1_act17_main

# ————— 主线 / 【九归故里】 —————
label line1_act17_main:
    scene expression prologue_bg("images/background/幕十七1.png") with fade
    call cinematic_narration("民国三十八年（1949）。同安西溪畔。") from _call_cinematic_narration_350
    call cinematic_narration("陈九已经七十岁了。他坐在九思学堂门口的石凳上，看着孩子们放学。远处是西溪，溪水缓缓流向大海。") from _call_cinematic_narration_351
    call cinematic_narration("民国三十八年（1949）深秋，陈九在同安安详辞世，享年七十岁。") from _call_cinematic_narration_352
    call cinematic_narration("临终前，他口述了最后一封家书，托阿山写下来：") from _call_cinematic_narration_353

    # 家书全文
    # TODO: replace with letter/document UI
    call cinematic_narration("阿母膝下：") from _call_cinematic_narration_354
    call cinematic_narration("儿不孝，一生多有行差踏错。然儿改了。儿这辈子，没再赌过一文钱。") from _call_cinematic_narration_355
    call cinematic_narration("儿被卖去南洋当猪仔，在橡胶园里从苦工做成园主。儿赚了钱，捐了钱给国家打日本人。") from _call_cinematic_narration_356
    call cinematic_narration("儿回了中国，没再开店做生意。儿有钱了，不需要再赚钱。儿把钱用来办了九思学堂，又办了救济所。战时，学堂成了难民的家。") from _call_cinematic_narration_357
    call cinematic_narration("儿的台湾兄弟阿土......") from _call_cinematic_narration_358

    if line1_atu_alive == False:
        call cinematic_narration("替难民送米时被日本人抓了，死了。他是为中国人死的。他是台湾人，也是中国人。儿替他养了他阿母，替他上了他阿爸的坟，替他把学堂办了下去。儿对得起阿土这条命——可儿知道，阿土的命，本可以救回来的。儿这辈子最后悔的，不是赌输了家产，是当初多捐了那两万。阿母，儿错了。儿来给阿土赔罪了。") from _call_cinematic_narration_359
    else:
        call cinematic_narration("还活着。他就在儿隔壁屋躺着，听见儿说话呢。阿土是儿的兄弟，也是儿的债。儿救了他，可儿心里一直过不去——当初若多捐两万，前线能多救几个人？这笔账儿算了一辈子，算不清。阿母，儿对不起前线那些人。可儿对得起阿土。儿来给阿母磕头了。") from _call_cinematic_narration_360

    call cinematic_narration("儿对得起阿母给的那三块大洋，对得起\"九思\"这两个字。") from _call_cinematic_narration_361
    call cinematic_narration("阿母，儿来陪您了。阿土，兄弟，我来陪你了。") from _call_cinematic_narration_362

    if line1_atu_alive == True:
        call cinematic_narration("若选B，阿土在隔壁屋喊：\"九——莫走——九——\" 可陈九已经听不见了。") from _call_cinematic_narration_363

    call cinematic_narration("不孝儿 九 叩首") from _call_cinematic_narration_364
    call cinematic_narration("民国三十八年秋") from _call_cinematic_narration_365

    if line1_reputation_stained:
        call cinematic_narration("家书多一句：\"儿脏了名，只为救兄弟。阿土活着，儿便值了。\"") from _call_cinematic_narration_366

    scene expression prologue_bg("images/background/幕十七3.png") with fade
    call cinematic_narration("阿山把那封家书烧在了陈九的灵前。") from _call_cinematic_narration_367

    if line1_atu_alive == False:
        call cinematic_narration("若选A：旁边是阿土的灵位。两个灵位并排供着，一炷香，两缕烟。") from _call_cinematic_narration_368
    else:
        if line1_reputation_stained:
            call cinematic_narration("阿土不在灵前露面——或已先走，或只托人送来一纸：\"九，名是你的，我记下了。\"") from _call_cinematic_narration_369
        else:
            call cinematic_narration("若选B：阿土坐在轮椅上，被推到陈九灵前。他挣扎着站起来，磕了三个头，说：\"九，你先走一步。我随后就来。\"阿土在陈九走后第二年也走了。两个老兄弟的灵位，并排供着，一炷香，两缕烟。") from _call_cinematic_narration_370

    call cinematic_narration("后来，九思学堂一直办到了新中国成立之后，改成了公立小学。校门口那块旧匾，被摘下来，擦干净，挂进了同安华侨历史陈列室。") from _call_cinematic_narration_371
    call cinematic_narration("匾上四个字，漆色斑驳，却还认得出：") from _call_cinematic_narration_372
    call cinematic_narration("\"九思学堂。\"") from _call_cinematic_narration_373
    call cinematic_narration("解说牌上写着：") from _call_cinematic_narration_374
    call cinematic_narration("陈九（1879—1949），同安人。早年被卖南洋为契约华工，后以橡胶业起家。抗战前回国，捐资办学、救济难民。其台湾挚友林阿土，寻根西亭，殉于/经难于救济途中。") from _call_cinematic_narration_375
    call cinematic_narration("解说牌最后一行，是一句注解：") from _call_cinematic_narration_376
    call cinematic_narration("\"他是从南洋活着回来的那一个——回来了，就再没走。\"") from _call_cinematic_narration_377

    if line1_reputation_stained:
        call cinematic_narration("【若危I为「垢名换命」】解说牌多一行小字：\"晚年因求情救友，乡议不一。\"家书中多一句：\"儿脏了名，只为救兄弟。阿土活着，儿便值了。\"阿土不在灵前露面——或已先走，或只托人送来一纸：\"九，名是你的，我记下了。\"") from _call_cinematic_narration_378

    call cinematic_narration("——橡胶逆袭。钱挣够了，就回家；回家了，就把钱撒出去。局可不开，学不可废。") from _call_cinematic_narration_379
    call cinematic_narration("可这条线的真相是：人这一辈子，每一个选择都有人在替你死，每一个选择都有人在替你活。你以为是你在选，其实是命在选。") from _call_cinematic_narration_380

    if line1_atu_alive == False:
        call screen line1_game_over("九归故里 · 万金难赎", "真结局", "人这一辈子，每一个选择都有人在替你死，每一个选择都有人在替你活。\n阿土已逝，九思长存。真结局名：【九归故里】——从南洋活着回来的那一个，回来了，就再没走。")
    else:
        if line1_reputation_stained:
            call screen line1_game_over("九归故里 · 垢名换命", "真结局 · 名节有损", "命换回来，名换出去。学堂仍在，匾额有议。真结局名：【九归故里】")
        else:
            call screen line1_game_over("九归故里 · 算不清的账", "真结局", "阿土活下来了。可这笔账，陈九算了一辈子，算不清。真结局名：【九归故里】")

    # 本线结局结算（按原文表格，展示为旁白）
    call cinematic_narration("主线通关（危A按手印→危B未偷水→危C未瘾死→危E心算→危H暗中救济→危I筹钱→选择3任意）：选择3全捐、阿土死 → 【万金难赎】 + 真结局 【九归故里】；选择3留后、阿土活 → 【算不清的账】 + 真结局 【九归故里】。") from _call_cinematic_narration_381
    call cinematic_narration("走向结算：危A拒签 不按手印按地板 GO；危A逃跑 黄三爷的快递（水葬版） GO；危B偷水 淡水自由行（单程） GO；危C日日抽 福寿膏灯 BE；危E作弊 开卷有益闭卷有命 GO；危E装傻 割胶割到退休（强制） BE；危H当街骂 发言完毕人生完毕 GO；危H自保 鼓浪冷金 残缺；危I硬闯 双陨同安 GO；危I求疏通 垢名换命 特殊；危B换符 半勺换半辈子 续；危C不抽 疼并清醒着 续。") from _call_cinematic_narration_382
    return

# ————— 残缺尾声 · 鼓浪冷金（仅危H选「自保」） —————
label line1_act17_cold_gold:
    scene expression prologue_bg("images/background/幕十七4.png") with fade
    call cinematic_narration("民国三十八年，陈九死在鼓浪屿租界洋房里。窗外是海，屋里是一箱未花完的大洋。没有乡绅送葬，没有孩子喊\"九叔\"，墙上没有\"九思学堂\"的匾。") from _call_cinematic_narration_383
    call cinematic_narration("阿土（或阿土的后人）来过一回，看了看那箱钱，没拿，只说：\"九，钱你守住了。根，你弄丢了。\"") from _call_cinematic_narration_384
    call cinematic_narration("同安华侨陈列室里，没有他的解说牌。有人记得南洋有个陈九发过财，有人记不得他回过乡。") from _call_cinematic_narration_385
    call cinematic_narration("结算：【鼓浪冷金】——钱在人在，乡望与学堂俱无。") from _call_cinematic_narration_386
    call screen line1_game_over("鼓浪冷金", "残缺结局", "钱在人在，乡望与学堂俱无。若要兴学主线，请读档回到危H选择暗中救济。")
    return
