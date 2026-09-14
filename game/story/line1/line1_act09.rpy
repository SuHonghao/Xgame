## line1_act09.rpy — 幕九 · 橡胶园主 · 巅峰
## 严格按 线路一.md 原文逐字实现，未改写未删减

label line1_act09:
    scene expression prologue_bg("images/background/幕九1.png") with fade
    call cinematic_narration("民国七年至二十四年（1918-1935）。") from _call_cinematic_narration_145
    call cinematic_narration("陈九已经五十六岁了。他和阿土的\"九土橡胶行\"已经发展成雪兰莪数一数二的橡胶行，占地两千亩，雇工三百多人，行情好的时候，年利润能超过十万块大洋。") from _call_cinematic_narration_146
    call cinematic_narration("陈九成了南洋有名的橡胶园主。同安人、台湾人、马来人、英国人，都喊他\"九叔\"。") from _call_cinematic_narration_147
    call cinematic_narration("他没有娶妻。有人问他为什么不娶，他说：\"我这条命是赌回来的。随时都可能还回去，娶媳妇耽误人家干什么。\"") from _call_cinematic_narration_148
    call cinematic_narration("阿土也没有娶妻。两人像亲兄弟一样，住在一起，吃在一起，做生意在一起。") from _call_cinematic_narration_149
    call cinematic_narration("阿土这些年一直在给台湾的阿母寄侨批。阿母和弟弟在鼓浪屿安顿下来，靠阿土的侨批过日子。阿土的弟弟阿山长大了，去了厦门读书，后来考上了厦门大学——那是陈嘉庚先生办的大学。") from _call_cinematic_narration_150

    call screen culture_note("陈嘉庚与厦门大学", "资料载：\"1921年陈嘉庚倡建厦门大学，为建校呕心沥血。\"阿土的弟弟阿山上厦门大学，正是这一历史背景的呼应。又载陈嘉庚\"首位集橡胶种植、制造和贸易为一体的企业家，被誉为'橡胶大王'\"。陈九和阿土的橡胶生意，正是追随陈嘉庚脚步的南洋华侨缩影。", "历史", "history_jiageng_xmu")

    scene expression prologue_bg("images/background/幕九2.png") with fade
    call cinematic_narration("民国二十六年（1937）七月。陈九和阿土在橡胶园的大宅里喝茶。") from _call_cinematic_narration_151
    call cinematic_narration("一个伙计匆匆跑来。") from _call_cinematic_narration_152

    show huoji_normal at right with dissolve
    show chenjiu v4_full at left with dissolve
    show atu full at center with dissolve

    huoji "九叔！土叔！大事！出大事了！"
    chenjiu "什么事？"
    huoji "（喘着气）日本人打进中国了！卢沟桥陷落了！"

    hide huoji_normal with dissolve

    call cinematic_narration("陈九和阿土对视一眼，都放下了茶杯，站了起来。") from _call_cinematic_narration_153
    call cinematic_narration("两个被日本人害过的人——一个被日本人在台湾害得家破人亡，一个因为甲午战败、台湾割让而间接走上了不归路——此刻，他们的祖国，又被日本人打了。") from _call_cinematic_narration_154

    atu "（声音发抖）九......"
    chenjiu "（沉默良久）阿土，你还记得你阿母回批里写的那句话吗？"
    atu "哪句？"
    chenjiu "\"你阿爸的仇，莫忘。你是台湾人，也是中国人。莫忘你的根。\""
    atu "（红了眼眶）记得。"
    chenjiu "咱们......该回去了。"
    atu "（一愣）回去？"
    chenjiu "回去。落叶归根。咱们在南洋待了四十二年，够了。如今国难当头，咱们得回去。一来，给国家出份力；二来......（停顿）我阿母走了，坟还没找到，一炷香都没烧上。你阿母还在鼓浪屿，也该回去看看了。"
    atu "（沉吟）可咱们的橡胶园......"
    chenjiu "卖了。"
    atu "卖了？两千亩橡胶园，我们这么多年的心血——"
    chenjiu "阿土，钱是挣不完的。可根，只有一个。咱们再不回去，怕是回不去了。咱们这条命，是从海里、从橡胶林里捡回来的。能回去，就别错过。"
    atu "（咬牙）好。回去。"

    hide atu with dissolve
    hide chenjiu with dissolve

    call cinematic_narration("陈九和阿土做了决定。他们要把橡胶园卖掉，带着所有积蓄，回国。") from _call_cinematic_narration_155
    call cinematic_narration("叶落归根。四十二年后，两个被命运抛到异乡的游子，要回家了。") from _call_cinematic_narration_156

    jump line1_act10
