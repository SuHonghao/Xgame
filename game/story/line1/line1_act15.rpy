## line1_act15.rpy — 幕十五 · 阿土之死
## 严格按 线路一.md 原文逐字实现，未改写未删减

label line1_act15:
    scene expression prologue_bg("images/background/幕十五1.png") with fade
    call cinematic_narration("民国三十年（1941）。同安至鼓浪屿途中。") from _call_cinematic_narration_288
    call cinematic_narration("日本人加强了对沿海的控制。一次护送难民的行动中，阿土被日本兵抓住了。") from _call_cinematic_narration_289
    call cinematic_narration("那天，鼓浪屿上有一批从厦门逃出来的妇孺，饿了三天，急需粮食和安顿。阿土亲自押着两船米和药材，从同安渡海送往鼓浪屿。") from _call_cinematic_narration_290
    call cinematic_narration("半路上，日本巡逻艇截住了他们。") from _call_cinematic_narration_291

    scene expression prologue_bg("images/background/幕十五3.png") with fade
    call cinematic_narration("宪兵队里。日本军官审问阿土。") from _call_cinematic_narration_292

    show atu full at left with dissolve
    show japanese_officer zoom at right with dissolve

    japanese_officer "（用蹩脚的中文）你叫什么？"
    atu "（用日语）林阿土。"
    japanese_officer "（一愣，改用日语）你会说日语？"
    atu "（日语）我是台湾人。台湾被你们占了四十三年。"
    japanese_officer "台湾人？那你是日本国民。你为什么替中国人运粮？"
    atu "（冷笑）我是中国人。台湾是中国的地方。那些妇孺也是中国人。饿死他们，我做不到。"
    japanese_officer "（大怒，拍桌）你！"
    atu "你要杀就杀。米是给难民的，不是给你们的。"

    call screen line1_danger_warning("危I · 如何救阿土", "可能导致死亡。建议存档。")
    call cinematic_narration("宪兵队扣人，要钱或要人头。有人说夜袭，有人说走维持会。") from _call_cinematic_narration_293
    call cinematic_narration("系统提示：可能导致死亡。建议存档。") from _call_cinematic_narration_294

    show chenjiu v4_frown at left with dissolve
    show atu full at right with dissolve

    menu:
        "A · 带人硬闯宪兵队":
            $ line1_danger_i = "storm"
            $ line1_rescue_choice = "storm"
            jump line1_act15_gameover_storm
        "B · 筹钱赎人（主线岔路）":
            $ line1_danger_i = "ransom"
            $ line1_rescue_choice = "ransom"
            jump line1_act15_ransom
        "C · 求汉奸/维持会疏通":
            $ line1_danger_i = "collaborator"
            $ line1_rescue_choice = "collaborator"
            $ line1_reputation_stained = True
            jump line1_act15_stained

label line1_act15_gameover_storm:
    call cinematic_narration("夜袭失败。阿土处决，陈九中弹死在墙根。祖厅多两块并排牌位。") from _call_cinematic_narration_295
    call screen line1_game_over("双陨同安", "Game Over", "硬的是枪，软的是命。请读档，回危I。")
    return

label line1_act15_stained:
    call cinematic_narration("阿土三日后放出，半死却活着。乡传\"陈九通敌求情\"。学堂生源锐减。阿土：\"命是捡回来了，名是你的。\"") from _call_cinematic_narration_296
    call cinematic_narration("后续质感改写：仍可办学，匾额有争议；家书多一句\"儿脏了名，只为救兄弟\"。阿土再不愿并肩抛头露面。") from _call_cinematic_narration_297
    call cinematic_narration("【特殊结局 · 垢名换命】命换回来，名换出去。若要无污名主线，读档选B。") from _call_cinematic_narration_298
    $ line1_atu_alive = True
    hide chenjiu with dissolve
    hide atu with dissolve
    jump line1_act15_letters

label line1_act15_ransom:
    # 以下「选择3回响」仅当危I选B时进入
    call cinematic_narration("成败看选择3是否留后路。全捐→倾向【万金难赎】；留后→倾向【算不清的账】。") from _call_cinematic_narration_299
    call cinematic_narration("进入下方「选择3回响」（剧情同原版）。") from _call_cinematic_narration_300
    call cinematic_narration("阿土被日本人关了三个月。他什么都没说——救济所的地址、存粮的地点、陈九的名字，一个字都没吐。") from _call_cinematic_narration_301

    if line1_choice3 == "donate_all":
        call cinematic_narration("宪兵队放话——三万块大洋赎人，三日内交钱，否则撕票。") from _call_cinematic_narration_302
        call cinematic_narration("陈九连夜回同安，翻遍家底，凑了一万八。他跪在每一个熟人面前借钱。有人冷脸，有人推说没有，有人躲着不见。他在码头跪了三天三夜，凑到两万四。还差六千。") from _call_cinematic_narration_303
        call cinematic_narration("第四天清早，他抱着两万四千块大洋冲到宪兵队——晚了三个时辰。阿土已经被拖出去了。") from _call_cinematic_narration_304
        call cinematic_narration("宪兵队的人把一个沾血的布包扔给他，里面是阿土贴身带的那份族谱——寻根时抄的，西亭林氏的。") from _call_cinematic_narration_305
        call cinematic_narration("陈九抱着布包，跪在码头，一夜白头。") from _call_cinematic_narration_306
        call cinematic_narration("阿土临终前，对看守他的一个台湾籍日本兵说了一句话：") from _call_cinematic_narration_307
        atu "（虚弱）同胞......我是台湾人......也是中国人......我死了......你替我......告诉我阿母......我是为中国人死的......"
        call cinematic_narration("那个台湾籍日本兵，偷偷把阿土的话传了出来。消息辗转传到了陈九耳朵里。") from _call_cinematic_narration_308
        call cinematic_narration("陈九听完，一夜白头。") from _call_cinematic_narration_309
        $ line1_atu_alive = False
    elif line1_choice3 == "keep_reserve":
        call cinematic_narration("宪兵队放话——三万块大洋赎人，三日内交钱，否则撕票。") from _call_cinematic_narration_310
        call cinematic_narration("陈九连夜回同安，翻箱倒柜——他凑得出来。当初留的那两万，加上这几年的积蓄，刚好三万。") from _call_cinematic_narration_311
        call cinematic_narration("他在码头等了三天三夜。第三天天亮，宪兵队把阿土放了出来。") from _call_cinematic_narration_312
        call cinematic_narration("阿土被打得半死——肋骨断了两根，左眼瞎了，走路一瘸一拐。可他活着。") from _call_cinematic_narration_313
        call cinematic_narration("他见到陈九，咧嘴笑了一下，嘴唇裂开，全是血：\"九......你救了我。\"") from _call_cinematic_narration_314
        call cinematic_narration("陈九抱着他，一句话说不出来。抱了很久。") from _call_cinematic_narration_315
        call cinematic_narration("阿土活了下来。可陈九心里那笔账，永远算不清。他常想：当初若多捐两万，前线能多救几个人？阿土是一条命，前线的兵也是命。他用阿土的命换了前线那两条命——这账，他算了一辈子，算不清。") from _call_cinematic_narration_316
        call cinematic_narration("这种\"算不清\"，比\"没救回\"更折磨人。") from _call_cinematic_narration_317
        $ line1_atu_alive = True
    else:
        # 防御：choice3 异常时按 keep_reserve 处理
        $ line1_atu_alive = True

    hide chenjiu with dissolve
    hide atu with dissolve

    if line1_atu_alive == False:
        chenjiu "（跪在九思学堂改成的救济所里，对着阿土的灵位，泣不成声）阿土......阿土......你替那些难民死了......你替我死了......我当初那四万......若留两万......你就不必死......"
    else:
        chenjiu "（跪在九思学堂改成的救济所里，对着阿土的病榻，泣不成声）阿土......阿土......你活下来了......你活下来了......可我这条心，这辈子放不下了......当初多捐两万......前线那些人......"

    jump line1_act15_letters

label line1_act15_letters:
    call cinematic_narration("无论阿土是死是活，陈九都替阿土写了一封家书——给阿土的阿母。") from _call_cinematic_narration_318

    if line1_atu_alive == True:
        call cinematic_narration("若选B：这封家书是阿土口述、陈九代笔，报平安的。\"阿母，儿还活着。儿被日本人打了一顿，可命还在。九救了我。儿还要活很久，替阿母尽孝。\"") from _call_cinematic_narration_319
    else:
        call cinematic_narration("若选A：这封家书是陈九独自写的，报丧的。") from _call_cinematic_narration_320

    call cinematic_narration("陈九替阿土写了一封家书——给阿土的阿母。") from _call_cinematic_narration_321

    if line1_atu_alive == False:
        call cinematic_narration("若选A（阿土已死），家书全文：") from _call_cinematic_narration_322
        # 家书全文·选A
        # TODO: replace with letter/document UI
        call cinematic_narration("阿母膝下：") from _call_cinematic_narration_323
        call cinematic_narration("阿土走了。他是替难民送米时被日本人抓的。他什么都没说，保住了救济所里几百号人的命。可他自己的命，没了。") from _call_cinematic_narration_324
        call cinematic_narration("阿土临终前说，他是为中国人死的。阿母，您养了一个好儿子。他是台湾人，也是中国人。他没有忘记他的根。") from _call_cinematic_narration_325
        call cinematic_narration("阿土的根，在同安西亭。他的魂，会回去的。") from _call_cinematic_narration_326
        call cinematic_narration("阿母，从今往后，我就是您的儿子。阿土没做完的事，我做。阿土没尽尽的孝，我尽。九思学堂、九思救济所，我会一直办下去。") from _call_cinematic_narration_327
        call cinematic_narration("不孝儿（替阿土） 叩首") from _call_cinematic_narration_328
        call cinematic_narration("不孝义子（陈九） 叩首") from _call_cinematic_narration_329
        call cinematic_narration("民国三十年冬") from _call_cinematic_narration_330
    else:
        call cinematic_narration("若选B（阿土活着），家书全文：") from _call_cinematic_narration_331
        # 家书全文·选B
        # TODO: replace with letter/document UI
        call cinematic_narration("阿母膝下：") from _call_cinematic_narration_332
        call cinematic_narration("儿还活着。儿替难民送米，被日本人抓了三个月，打断了肋骨，瞎了一只眼。可命还在。") from _call_cinematic_narration_333
        call cinematic_narration("是九救了儿。九凑了三万块大洋，把儿赎了出来。阿母，九是儿的兄弟，也是儿的救命恩人。") from _call_cinematic_narration_334
        call cinematic_narration("儿不悔。那些妇孺也是中国人，饿死他们，儿做不到。阿母教儿的话——\"你是中国人，莫忘你的根\"——儿记着呢。") from _call_cinematic_narration_335
        call cinematic_narration("儿的根，在同安西亭。儿的命，是九给的。儿还要活很久，替阿母尽孝，替九办事。") from _call_cinematic_narration_336
        call cinematic_narration("阿母勿念。儿还活着。") from _call_cinematic_narration_337
        call cinematic_narration("不孝儿 阿土 叩首") from _call_cinematic_narration_338
        call cinematic_narration("义兄 陈九 同叩") from _call_cinematic_narration_339
        call cinematic_narration("民国三十年冬") from _call_cinematic_narration_340

    jump line1_act16
