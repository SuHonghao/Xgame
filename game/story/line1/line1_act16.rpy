## line1_act16.rpy — 幕十六 · 抗战胜利 · 隐退
## 严格按 线路一.md 原文逐字实现，未改写未删减

label line1_act16:
    scene expression prologue_bg("images/background/幕十六1.png") with fade
    call cinematic_narration("民国三十四年（1945）八月。日本投降。抗战胜利。") from _call_cinematic_narration_341
    call cinematic_narration("陈九已经六十六岁了。他坐在九思学堂的天井里，面前是一杯凉透的工夫茶。") from _call_cinematic_narration_342
    call cinematic_narration("抗战胜利了。难民渐渐散去。九思学堂重新开学。") from _call_cinematic_narration_343
    call cinematic_narration("可陈九老了。他的眼睛花了，背更驼了。他把学堂交给了阿土的弟弟阿山——那个厦门大学毕业的年轻人——来管。") from _call_cinematic_narration_344

    show chenjiu v5_full at center with dissolve
    show ashan_full at right with dissolve

    chenjiu "阿山，学堂交给你了。"
    ashan "（跪下）九叔——"
    chenjiu "（扶他起来）莫跪。你阿兄阿土用命护过这些人。你替他把学堂办下去。（停顿）只有一样，你记住——"
    ashan "九叔请讲。"
    chenjiu "办学堂，不为名，不为利。为的是让穷人家的孩子也有书念。你阿兄说过，咱们都是中国人。中国人，就得让下一代站得直。"
    ashan "（含泪）侄儿记住了。"

    hide chenjiu with dissolve
    hide ashan_full with dissolve

    call cinematic_narration("陈九把学堂交给阿山后，搬回同安陈家大厝养老。") from _call_cinematic_narration_345

    if line1_choice3 == "donate_all" and line1_atu_alive == False:
        call cinematic_narration("他每日去母亲坟前上一炷香，再去西亭林氏祠堂给阿土的祖宗上一炷香。他把阿土的灵位供在自己家里，与母亲的牌位并排。两个牌位，一炷香，两缕烟。他常对着阿土的灵位说话，说生意上的事，说学堂里的事，说哪家的孩子考上了中学。有时说着说着，就哭。哭完，擦擦眼，又笑：\"阿土，你听到了没有？我替你活着呢。\"") from _call_cinematic_narration_346
    else:
        call cinematic_narration("阿土没死，可身子垮了。他住在陈家大厝隔壁，陈九每日搀着他去母亲坟前上一炷香，再去西亭林氏祠堂给祖宗上一炷香。两个老兄弟，一瘸一拐，走在同安的石板路上，像两根快燃尽的蜡烛。") from _call_cinematic_narration_347
        call cinematic_narration("阿土常说：\"九，我这命是你给的。我多活的这些年，都是赚的。\"陈九每次听了，就沉默。他心里那笔账——\"阿土的命 vs 前线那两条命\"——还是算不清。有时他会对阿土说：\"阿土，你活着，我高兴。可我有时想，当初若多捐两万......\"阿土就打断他：\"九，莫想。你救了我，这是事实。前线的事，是老天的事。咱们管不了老天。\"") from _call_cinematic_narration_348
        call cinematic_narration("两个老兄弟，就这样互相劝着，劝了八年。") from _call_cinematic_narration_349

    jump line1_act17
