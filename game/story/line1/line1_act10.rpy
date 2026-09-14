## line1_act10.rpy — 幕十 · 卖园 · 捐输（含选择3）
## 严格按 线路一.md 原文逐字实现，未改写未删减

label line1_act10:
    scene expression prologue_bg("images/background/幕十1.png") with fade
    call cinematic_narration("民国二十六年（1937）秋。雪兰莪。") from _call_cinematic_narration_157
    call cinematic_narration("陈九和阿土开始处理橡胶园的善后。半年后，他们把两千亩橡胶园以低价卖给了一个英国洋行——不是不想卖高价，是来不及了。战火已起，他们急着回国。") from _call_cinematic_narration_158
    call cinematic_narration("陈九和阿土算了一笔账。橡胶园卖了八万块大洋。这些年攒的积蓄加上，一共十二万块。") from _call_cinematic_narration_159
    call cinematic_narration("两人商量了一整夜，做了一个决定。") from _call_cinematic_narration_160

    show atu full at right with dissolve
    show chenjiu v2_calm at left with dissolve

    chenjiu "阿土，咱们这十二万块，怎么分？"
    atu "你六万，我六万。"
    chenjiu "（摇头）不。我出四万，你出四万。剩下四万，捐给国家。"
    atu "（一愣）捐？"
    chenjiu "陈嘉庚先生在南洋号召华侨捐款救国。咱们虽然不是大富豪，可这四万块，是咱俩一辈子的心血。国家有难，不出一份力，对不起\"中国人\"三个字。"
    atu "（咬牙）好。四万块，捐。"
    chenjiu "还有。我打听过了，陈嘉庚先生组织了'南洋华侨筹赈祖国难民总会'。咱们把捐的钱交给总会，由他们统一汇回国内。"
    atu "那咱们的侨汇......也走侨批的渠道？"
    chenjiu "对。我这些年寄侨批，认识了几个批局的人。他们能帮咱们把钱汇回去。不只是咱们的捐款，南洋华侨的捐款，都走侨批的渠道汇回国内。"

    hide atu with dissolve
    hide chenjiu with dissolve

    scene expression prologue_bg("images/background/幕十5.png") with fade
    call cinematic_narration("临到交钱那天，阿土犹豫了。他在鼓浪屿的阿母七十多岁了，弟弟阿山还在读书。更重要的是，战乱年月，谁知道回国后会遇上什么？手头留点钱，关键时刻能救命。") from _call_cinematic_narration_161
    call cinematic_narration("陈九也犹豫。他想捐，可他连母亲的坟还没找到，回国寻亲、安家、救急，桩桩都要钱。") from _call_cinematic_narration_162

    show atu full at right with dissolve
    show chenjiu torn at left with dissolve

    menu:
        "A · 全捐四万，不留后路":
            $ line1_choice3 = "donate_all"
            jump line1_act10_donate_all
        "B · 少捐两万，留两万做后路":
            $ line1_choice3 = "keep_reserve"
            jump line1_act10_keep_reserve

label line1_act10_donate_all:
    call cinematic_narration("陈九拍板：\"阿土，国若不存，家何以附？你阿母教你的话——'你是中国人，莫忘你的根'。\"四万大洋全捐给南侨总会。两人各剩四万，回国。南侨总会的常务委员赵清泉亲自接见，拍着他们的肩说\"乡亲，回来了就好。\"") from _call_cinematic_narration_163
    call cinematic_narration("可这四万，日后要了阿土的命。民国三十年，阿土运粮被日本人抓了，宪兵队放话——三万块大洋赎人。陈九翻遍家底，凑不出三万。他跪在熟人面前借钱，跪断了膝盖，还是晚了三天。阿土死在宪兵队里。陈九抱着阿土的尸首，哭瞎了眼。他这辈子悔的是：当初那四万，若留两万，阿土就活了。") from _call_cinematic_narration_164
    hide atu with dissolve
    hide chenjiu with dissolve
    jump line1_act10_handover

label line1_act10_keep_reserve:
    call cinematic_narration("阿土松了口气，陈九也默认了。两万捐给南侨总会，两人各剩五万。常务委员接见他们时，没说什么，只拍了拍陈九的肩：\"陈先生，祖国会记得你的付出。\"陈九当时不懂这话的意思。三年后他懂了。") from _call_cinematic_narration_165
    call cinematic_narration("民国三十年，阿土运粮被日本人抓了，宪兵队放话——三万块大洋赎人。陈九连夜凑钱，他凑得出来——因为他当初留了后路。他在码头等了三天三夜，第三天天亮，阿土被放了出来——被打得半死，可是还活着。阿土见到陈九，第一句话是：\"九，是你救了我。\"陈九抱着他，一句话也说不出来。") from _call_cinematic_narration_166
    call cinematic_narration("可阿土活着，陈九又悔了另一件事。") from _call_cinematic_narration_167
    call cinematic_narration("半年后，南洋来了消息，是水客带回来的。他乡音重，陈九听不太清，只说了几句零碎的话：\"缅甸那边......前线药不够......有批侨汇迟了，伤兵没等住。\"") from _call_cinematic_narration_168
    call cinematic_narration("陈九问：\"迟了多久？\"") from _call_cinematic_narration_169
    call cinematic_narration("水客说：\"好像是一季。具体多少，谁说得清。\"") from _call_cinematic_narration_170
    call cinematic_narration("那晚他坐在灯下，把那两万块大洋从箱底翻出来，搁在桌上，看着它们，没有动。") from _call_cinematic_narration_171
    call cinematic_narration("他知道南洋那头的账从来不是一笔对一笔的。侨汇在路上走的每一站都可能耽搁——码头、车马、雨季、战火。就算他那两万块准时到了，也未必能正好送到那一批伤兵手上。但水客那句\"迟了一季\"像一颗沙子掉进了他脑子里，不大，可出不来。") from _call_cinematic_narration_172
    call cinematic_narration("他不知道那两万块到底救了谁，或者谁也没救。他更不知道前线那些伤兵的命，是不是真的就差这两万块。他永远都不会知道。") from _call_cinematic_narration_173
    call cinematic_narration("可他又忍不住去想：如果当初那两万块他送出去了，哪怕只是其中一部分，是不是有人就能等到下一批药？阿土是一条命，那些前线战士的命也是命。他用阿土的命换了前线战士们的命——这账，如何算清？") from _call_cinematic_narration_174
    call cinematic_narration("没有答案。没有人能给他答案。") from _call_cinematic_narration_175
    call cinematic_narration("他只知道一件事：他这辈子再也没法心安理得地花任何一笔钱了。") from _call_cinematic_narration_176
    hide atu with dissolve
    hide chenjiu with dissolve
    jump line1_act10_handover

label line1_act10_handover:
    call screen culture_note("抗战侨汇", "资料载：\"1938年'南洋华侨筹赈祖国难民总会'由陈嘉庚在新加坡成立，联络南洋一千多万华侨统一支援祖国。\"又载抗战期间华侨\"认购公债13亿余元国币\"\"侨汇18亿元国币，支撑战时经济\"\"捐献飞机217架\"。陈九和阿土的捐款，正是这历史洪流中的一滴水。", "历史", "history_nanyang_fund")

    scene expression prologue_bg("images/background/幕十7.png") with fade
    call cinematic_narration("陈九和阿土把四万块大洋交给了南侨总会。常务委员赵清泉亲自接见了他们。") from _call_cinematic_narration_177
    call cinematic_narration("赵清泉问陈九：\"陈先生，你是同安人？\"") from _call_cinematic_narration_178
    call cinematic_narration("陈九说：\"是。同安西溪畔。\"") from _call_cinematic_narration_179
    call cinematic_narration("赵清泉笑了：\"我也是同安人，咱们是乡亲呐。\"") from _call_cinematic_narration_180
    call cinematic_narration("赵清泉又转向阿土：\"这位是？\"") from _call_cinematic_narration_181
    call cinematic_narration("阿土说：\"台湾彰化人。\"") from _call_cinematic_narration_182
    call cinematic_narration("赵清泉拍了拍阿土的肩膀：\"台湾也是中国的地方。你回来，就是回家。\"") from _call_cinematic_narration_183

    jump line1_act11
