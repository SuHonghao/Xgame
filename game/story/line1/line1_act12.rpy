## line1_act12.rpy — 幕十二 · 帮助阿土寻根
## 严格按 线路一.md 原文逐字实现，未改写未删减

label line1_act12:
    scene expression prologue_bg("images/background/幕十二1.png") with fade
    call cinematic_narration("民国二十七年（1938）夏。鼓浪屿。") from _call_cinematic_narration_254
    call cinematic_narration("阿土安顿下来后，心里却一直放不下一件事——他想回台湾看看，看看自己的根在哪里。可台湾还在日本人手里，回不去。") from _call_cinematic_narration_255
    call cinematic_narration("阿土在台湾彰化的老家，已经被日本人占了四十三年。他的阿爸被日本人打死了，老家的田被日本人征了。他回不去台湾，可他想知道——自己的根，到底在哪里。") from _call_cinematic_narration_256
    call cinematic_narration("有一天，阿土来找陈九。") from _call_cinematic_narration_257

    show atu full at right with dissolve
    show chenjiu v2_calm at left with dissolve

    atu "九，我想找我的根。"
    chenjiu "什么意思？"
    atu "我阿爸是台湾彰化人。可我阿爸的阿爸，是从大陆过去的。我想知道，我们家的根在大陆哪里。"
    chenjiu "你阿爸没跟你说过？"
    atu "说过。可我那时候小，记不清了。只记得阿爸说，我们家是从福建过去的。好像是......漳州？还是泉州？"
    chenjiu "（沉吟）你家里有没有族谱？"
    atu "有。可族谱在台湾，我走的时候没带出来。"
    chenjiu "那你阿母记得吗？"
    atu "我问过。阿母说，阿爸在世时提过，我们家祖上是从泉州府同安县去的台湾。具体哪个村，阿母不知道。"
    chenjiu "（一惊）同安？"
    atu "嗯。"
    chenjiu "我也是同安人。同安我去帮你找。"

    hide atu with dissolve
    hide chenjiu with dissolve

    scene expression prologue_bg("images/background/幕十二5.png") with fade
    call cinematic_narration("陈九开始帮阿土寻根。他回到同安，找到了族里年纪最大的老人，翻查陈氏族谱。可阿土不姓陈，他姓林。") from _call_cinematic_narration_258

    show lao_shushi zoom at right with dissolve
    show chenjiu v2_calm at left with dissolve

    chenjiu "老先生，我问您一件事。台湾彰化有一户姓林的人家，祖上是从同安去的。您知道同安哪个地方有林姓迁台的吗？"
    lao_shushi "（想了想）姓林......迁台......你等等。（翻出一本泛黄的族谱）同安林姓，主要在西亭、洪塘一带。西亭林氏，清朝乾隆年间有一支迁台，去了彰化。"
    chenjiu "西亭林氏？"
    lao_shushi "对。西亭林氏族谱上记着，乾隆四十二年（1777），林氏十三世孙林振声，率家眷迁台，定居彰化。"
    chenjiu "（激动）林振声！阿土的阿爸叫林振发！振字辈！"
    lao_shushi "那便是了。振字辈，是西亭林氏的第十五世。林振声是十三世，林振发是十五世，差两辈。若算下来，林振发应该是林振声的曾孙辈。"
    chenjiu "老先生，西亭林氏的祠堂还在吗？"
    lao_shushi "在。就在西亭村。祠堂里供着祖宗牌位，迁台的那一支也有记载。"
    # TODO: 大概这个角度吧，cwj留

    hide lao_shushi with dissolve
    hide chenjiu with dissolve

    call screen culture_note("台湾寻根", "资料载：\"闽南人移居台湾的历史源远流长\"\"清乾隆、嘉庆至光绪年间（1736-1894年），清政府开放港口与台湾对口通航，移民持续不断。在清领台湾的229年间，仅漳州向台湾移民就超过50多万人。\"\"台湾80%的老百姓都是闽南移民的后代。\"又载：\"1987年台湾当局开放赴大陆探亲是一个历史性的转折点，由此掀起了第一次大规模、公开化的返乡寻根热。\"阿土的寻根故事，正是这一历史脉络的缩影。", "历史", "history_taiwan_root_search")

    scene expression prologue_bg("images/background/幕十二7.png") with fade
    call cinematic_narration("陈九带着阿土去了同安西亭村。西亭林氏祠堂还在，青砖灰瓦，门楣上刻着\"西河衍派\"（林姓郡望）。") from _call_cinematic_narration_259
    call cinematic_narration("阿土跪在祠堂里，对着祖宗牌位磕了三个头。") from _call_cinematic_narration_260

    show atu tearful at right with dissolve
    show chenjiu v2_calm at left with dissolve

    atu "（流泪）列祖列宗在上，不肖子孙林阿土，从台湾回来了。我阿爸林振发，被日本人害死了。我阿母还活着。我弟弟在厦门读书。我们......我们回来了。"
    chenjiu "（站在一旁，也红了眼眶）阿土，你找到根了。"
    atu "（站起来，擦泪）九，谢谢你。我这辈子，终于知道自己是从哪里来的了。"
    chenjiu "你从同安西亭来的。你是同安人，也是台湾人。都是中国人。"
    atu "（点头，声音哽咽）都是中国人。"

    hide atu with dissolve
    hide chenjiu with dissolve

    call cinematic_narration("阿土在西亭林氏祠堂里，抄了一份族谱，带回鼓浪屿给阿母看。") from _call_cinematic_narration_261

    if line1_choice1 == "saved":
        call cinematic_narration("阿土抄完族谱，对陈九说了一句话：\"九，你记不记得船舱里那夜？你把水分给阿福，自己差点死了。我那时候就想，这个人，值得我跟他一辈子。如今我找到根了，我的根里有你一份——你救过的人，也成了我林家的亲人。\"陈九愣住，没说话，只是拍了拍阿土的肩。这份\"根里有你一份\"，是阿土给陈九最重的谢礼。") from _call_cinematic_narration_262
    elif line1_choice1 == "not_saved":
        call cinematic_narration("阿土抄完族谱，沉默了很久，忽然说：\"九，你记不记得船舱里那夜？那个后生仔死的时候，你没回头。\"陈九的脸白了。阿土接着说：\"我不怪你。可我告诉你——我找到根了，我的根里没有那个后生仔。他死在船上，连个坟都没有，连个名字都没人记。九，你办九思学堂，给孩子们念书。可你欠那个后生仔一个名字。往后学堂里，若有个孩子叫'阿福'，就算你还了他这条命。\"") from _call_cinematic_narration_263
        call cinematic_narration("陈九跪了下来。他在西亭林氏祠堂里，给一个素不相识的后生仔，磕了一个头。后来九思学堂开学，第一个报名的孩子，陈九给他取了学名，叫\"念福\"。") from _call_cinematic_narration_264

    call cinematic_narration("阿土在西亭林氏祠堂里，抄了一份族谱，带回鼓浪屿给阿母看。") from _call_cinematic_narration_265
    call cinematic_narration("阿母看了，哭了。她说：\"你阿爸在世时总说，总有一天要回老家看看。他没等到。你替他看了。\"") from _call_cinematic_narration_266
    call cinematic_narration("阿土把那份族谱供在阿爸的灵位前，烧了三炷香。") from _call_cinematic_narration_267
    call cinematic_narration("\"阿爸，儿子替您回来了。您的根，在同安西亭。\"") from _call_cinematic_narration_268

    call screen culture_note("宗祠文化", "闽南宗祠文化是闽南社会的核心。资料载，马来西亚马六甲\"同安金厦会馆\"是同乡组织，1931年成立，\"旨在联络乡谊、谋取共同利益\"。宗祠、族谱、郡望匾额（如\"西河衍派\"\"颍川衍派\"），是闽南人认祖归宗的依据。阿土寻根的故事，正是闽南宗族文化跨海延续的体现。", "非遗", "culture_ancestral_hall")

    jump line1_act13
