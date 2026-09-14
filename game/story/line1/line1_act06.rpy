## line1_act06.rpy — 幕六 · 工头 · 阿土相助（含选择2）
## 严格按 线路一.md 原文逐字实现，未改写未删减

label line1_act06:
    scene expression prologue_bg("images/background/幕六1.png") with fade
    call cinematic_narration("光绪二十六年（1900）。") from _call_cinematic_narration_85
    call cinematic_narration("陈九在账房干了两年，把整个橡胶园的进出账理得清清楚楚。林头家对他越来越信任，让他兼管了割胶工的调度。") from _call_cinematic_narration_86
    call cinematic_narration("陈九从猪仔变成了工头。虽然还是给林头家打工，但日子好过多了。他不再挨鞭子，吃得也比从前好。") from _call_cinematic_narration_87
    call cinematic_narration("可他没有忘记阿土。") from _call_cinematic_narration_88

    show chenjiu v2_calm at left with dissolve
    show lin_toujia zoom at right with dissolve

    chenjiu "头家，我有件事求您。"
    lin_toujia "什么事？"
    chenjiu "我的兄弟阿土，割胶是一把好手。我想让他当割胶队的队长。"
    lin_toujia "那个台湾人？"
    chenjiu "是。他割胶比我强，手底下也稳。让他带人，产量能上去。"
    lin_toujia "（沉吟，看了看陈九）行。你替他担保，产量上不去，你俩一起担。"
    chenjiu "谢头家。"

    hide chenjiu with dissolve
    hide lin_toujia with dissolve

    call cinematic_narration("阿土当了割胶队长。他果然没让陈九失望，带着割胶队把产量提上去了三成。林头家大喜，给两人都加了工钱。") from _call_cinematic_narration_89
    call cinematic_narration("陈九和阿土，一个管账，一个管工，成了林头家手底下最得力的两个人。") from _call_cinematic_narration_90
    call cinematic_narration("光绪二十七年（1901），陈九的\"契约\"五年期满。阿土也攒够了赎身的银钱。他们终于自由了。") from _call_cinematic_narration_91

    scene expression prologue_bg("images/background/幕六3.png") with fade
    call screen line1_danger_warning("选择 2 · 留下，还是先回家", "本选择影响后续多幕内容。建议存档。")
    call cinematic_narration("五年契约期满。陈九自由了。") from _call_cinematic_narration_92
    call cinematic_narration("阿土说：\"九，你自由了。不走？\"陈九苦笑：\"走？去哪里？回同安？我连家还在不在都不知道，往哪回。\"") from _call_cinematic_narration_93
    call cinematic_narration("阿土压低声音，说出了承包橡胶林的主意——两人凑一百多块大洋，承包林头家边缘那片荒了的二十亩橡胶林，自己干。") from _call_cinematic_narration_94
    call cinematic_narration("陈九动心了。可他心里还有一根刺——五年没回家了。他算过，两人手里一共大约一百二十块。留下创业，本钱刚好够；若先买船票回同安看一眼母亲，阿土一个人便无法承包橡胶林。") from _call_cinematic_narration_95

    show atu full at right with dissolve
    show chenjiu torn at left with dissolve

    menu:
        "A · 留下创业，先寄侨批报平安":
            $ line1_choice2 = "stay"
            jump line1_act06_stay
        "B · 先回同安找母亲，橡胶林的事回来再说":
            $ line1_choice2 = "return_home"
            jump line1_act06_return

label line1_act06_stay:
    call cinematic_narration("陈九留下了。他想：等赚了钱，衣锦还乡，母亲不知多高兴。临开工前，他托水客带回第一封侨批，信里写：\"阿母，儿在南洋，活着。儿错了，儿再没赌过。儿正在攒钱，攒够了就回去。阿母保重，等儿。\"") from _call_cinematic_narration_96
    call cinematic_narration("两人凑足本钱，向林头家承包了那片二十亩橡胶林。这是陈九这辈子第一次正经做生意。") from _call_cinematic_narration_97
    call cinematic_narration("半年后，没有回批。水客回话：\"批送到同安西溪畔了，可陈家大厝空着，门锁着，没人收。\"陈九又寄了第二封、第三封——仍无回音。他心里发慌，却安慰自己：兴许是搬家了，兴许是水客没找对门。生意刚起头，他走不开。") from _call_cinematic_narration_98
    hide atu with dissolve
    hide chenjiu with dissolve
    jump line1_act07

label line1_act06_return:
    call cinematic_narration("陈九花二十块大洋买了船票，阿土没拦他，只说：\"你去。林子的事，我先拖着。你找到人，回来咱们再干。\"") from _call_cinematic_narration_99
    scene expression prologue_bg("images/background/同安后街巷子.png") with fade
    call cinematic_narration("他回到同安，敲开陈家大厝的门——开门的是个陌生外乡人：\"陈家？早搬走了。欠了一屁股债，连夜走的，谁也不知道去了哪里。\"他去了大哥岳家、母亲娘家、族里能想到的亲戚他都跑遍了——全都回答他\"不知道\"。三个月，泉州府跑遍，一无所获。") from _call_cinematic_narration_100
    call cinematic_narration("盘缠用尽，他红着眼眶重返南洋。阿土还在等他——可那片二十亩橡胶林，已经被别人承包了。两人只能再给林头家打工两年，重新攒本。光绪三十年（1904），他们才承包下一片更边、更荒的橡胶林。") from _call_cinematic_narration_101
    call cinematic_narration("更苦的是：他亲眼确认过陈家已无人在，却连一句\"你阿母还活着吗\"都答不上。想再寄侨批——连该往哪寄都不知道了。") from _call_cinematic_narration_102
    hide atu with dissolve
    hide chenjiu with dissolve
    jump line1_act07
