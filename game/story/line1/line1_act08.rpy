## line1_act08.rpy — 幕八 · 橡胶贸易商 · 发家与死讯
## 严格按 线路一.md 原文逐字实现，未改写未删减

label line1_act08:
    scene expression prologue_bg("images/background/幕八7.png") with fade
    call cinematic_narration("光绪三十四年至民国六年（1908-1917）。") from _call_cinematic_narration_123
    call cinematic_narration("这几年是马来亚橡胶业的黄金时代。胶价飞涨，欧美轮胎需求猛增。") from _call_cinematic_narration_124
    call cinematic_narration("陈九赶上了好时候。橡胶林扩大，又开了胶片加工厂，直接和英国洋行做生意。\"九土橡胶行\"在雪兰莪一带小有名气。阿土管生产，陈九管销售。") from _call_cinematic_narration_125
    # TODO: 我找不到了www，cwj留
    call screen culture_note("橡胶贸易", "资料载：\"陈嘉庚 首位集橡胶种植、制造和贸易为一体的企业家，被誉为'橡胶大王'\"。陈九的橡胶生意，正是这一历史浪潮的缩影。", "历史", "history_rubber_trade")

    scene expression prologue_bg("images/background/幕八11.png") with fade
    call cinematic_narration("民国六年（1917），陈九三十八岁。他和阿土坐在橡胶行的办公室里——这是真正的办公室，有红木桌、有算盘、有账册，和当年的工棚天差地别。") from _call_cinematic_narration_126

    show atu full at right with dissolve
    show chenjiu v2_calm at left with dissolve

    atu "九，今年咱们赚了多少？"
    chenjiu "（拨弄算盘）连本带利，一万二千块大洋。"
    atu "（倒吸一口凉气）一万二......"
    chenjiu "嗯。可大部分要投回去。欧洲打仗（第一次世界大战），橡胶需求更大了。咱们得趁这机会多囤些胶片，等仗打完，价格还得涨。"
    atu "九，你说......咱们算有钱人了吗？"
    chenjiu "（苦笑）算了吧。在马来亚算有钱人。可回了同安，我还是那个赌输了家产的败家子。"
    atu "（正色）九，你已经不是那个赌徒了。咱也算站稳脚根了，你寻亲的事，不能再拖了。"

    hide atu with dissolve
    hide chenjiu with dissolve

    if line1_choice2 == "stay":
        call cinematic_narration("自光绪二十八年起，陈九几乎年年寄批。底稿叠起来一厚沓：报平安、报承包、报赚钱、问为何无回批......水客带回的话基本一样——\"西溪畔陈家大厝空着\"\"邻里说欠债搬走了，不知去向\"。") from _call_cinematic_narration_127
        call cinematic_narration("民国六年，阿土按住他的手：\"别再只寄批了。批寄不到人，就用人去找。这一百块大洋，我帮你托鼓浪屿熟路的水客——同安、泉州、漳州，一路问下去。找到人，钱给他；找不到，把话带回。\"") from _call_cinematic_narration_128
        call cinematic_narration("半年后，水客回来了。带回的不是回批，是一句确讯：") from _call_cinematic_narration_129
        call cinematic_narration("\"陈家确实搬走了。乡下有人说......陈家老太太那几年病倒了，后来没了。葬在哪里，谁也说不清。你大哥一脉，有人讲还在同安乡下，可村子名字对不上。这一百块，我退你。人没找着，坟也没见着，钱我不能收。\"") from _call_cinematic_narration_130
        call cinematic_narration("陈九接过那一百块，手抖得厉害。他没哭。他只是把那叠底稿翻到天亮。") from _call_cinematic_narration_131
        call cinematic_narration("他悔的不是发了财，是发了财之后，把光绪二十八年的那张船票买成了胶树，没有买成归途。侨批替他走了十几年，人却一步都没迈出去。如今\"阿母还活着吗\"终于有了答案：不在了。可坟在哪，仍旧不知。") from _call_cinematic_narration_132
    elif line1_choice2 == "return_home":
        call cinematic_narration("陈九回国那一趟，已经亲眼见过空厝。回来后他极少寄批——不是不想，是无处可投。偶有水客愿\"沿路问陈家\"，他附上银两托人，带回的仍只是散碎传闻。") from _call_cinematic_narration_133
        call cinematic_narration("民国六年，阿土说：\"你当年用脚找过三个月。如今用钱，再找一轮。这一百块，托人把你走过的地方再走一遍，没走过的也补上。活要见人，死要见话。\"") from _call_cinematic_narration_134
        call cinematic_narration("半年后，水客回来了：") from _call_cinematic_narration_135
        call cinematic_narration("\"你当年问过的那些地方，我又问了一遍。还是没有。有个走乡串户的说，陈家老太太走了好些年了，坟......听说在同安乡下哪座后山，可叫不出村名。这一百块退你。我不能拿空话赚你的钱。\"") from _call_cinematic_narration_136
        call cinematic_narration("陈九接过钱，想起光绪二十八年站在大厝门口的自己——那时候他还能摸到锁，还能问邻人。如今连锁都换了主人。") from _call_cinematic_narration_137
        call cinematic_narration("他悔的不是没留下创业，是回去了三个月，却没把\"后山\"两个字问出来。人找过了，批也难寄，死讯如今坐实了，可坟依旧不知在何处。") from _call_cinematic_narration_138

    show atu full at right with dissolve
    show chenjiu v2_haggard at left with dissolve

    chenjiu "（声音哑了）阿土......我阿母......没了。"
    atu "（也红了眼眶）九，你回去。你阿母虽然走了，可你大哥还在。你找回去，给你阿母上一炷香。"
    chenjiu "（摇头）我不回去。我没脸。"
    atu "（厉声）陈九！你听我说！你阿母等了你二十多年。她不图你赚大钱，不图你的脸面。她图的是你活着回去！你若连一炷香都不肯烧，你对得起她吗？"
    chenjiu "（愣住，泪流满面）......"
    atu "九，总有一天，咱们都要回去的。落叶归根。你回同安，我回台湾。咱们都是中国人，根在那头。"

    hide atu with dissolve
    hide chenjiu with dissolve

    call cinematic_narration("陈九没有在民国六年就立刻回国踏遍闽南寻亲。不是不想，是他清楚：再跑一趟，也改变不了\"不知坟址\"的事实。他要攒的不是虚名，是真能把同安乡下问穿的力气与盘缠。") from _call_cinematic_narration_139
    call cinematic_narration("他欠母亲的，不只是三块大洋。他还欠一句没送到的\"儿还活着\"，也欠一炷烧在碑前的香。") from _call_cinematic_narration_140
    call cinematic_narration("选择2的分野，到此落定：") from _call_cinematic_narration_141
    call cinematic_narration("- 选A：批寄得出，人没回去 → 托人得知亡故 → 愧疚是\"我为什么不早点回去\"") from _call_cinematic_narration_142
    call cinematic_narration("- 选B：人回去过，批寄不出 → 再寻仍无坟 → 遗憾是\"我明明去了，还是问不出\"") from _call_cinematic_narration_143
    call cinematic_narration("两条线此刻都已知：母亲不在了；坟，要等归国那一日再寻。") from _call_cinematic_narration_144

    jump line1_act09
