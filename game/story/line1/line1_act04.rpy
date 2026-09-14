## line1_act04.rpy — 幕四 · 阿土 · 台湾朋友
## 严格按 线路一.md 原文逐字实现，未改写未删减

label line1_act04:
    scene expression prologue_bg("images/background/橡胶园-工棚.png") with fade
    call fullscreen_cinematic_narration("【幕四】阿土 · 台湾朋友") from _call_fullscreen_cinematic_narration_2
    call cinematic_narration("橡胶园的工棚，夜晚。") from _call_cinematic_narration_51
    call cinematic_narration("陈九累得浑身散架，躺在工棚的木板床上。工棚里挤了二十多个人，汗臭、脚臭、旱烟味混在一起。") from _call_cinematic_narration_52

    show atu zoom at right with dissolve
    show chenjiu v2_calm at left with dissolve

    chenjiu "阿兄，哪里人？"
    atu "台湾。"
    chenjiu "台湾？你怎么来马来亚了？"
    atu "你忘了？台湾割给日本了。"
    atu "我家原是台湾彰化的农户。"
    atu "日本人来了之后，征粮、拉夫、打人。"
    atu "我阿爸被日本人打死了，阿母带着我弟弟逃到山里去了，生死不知。"
    atu "我一个人......跑出来了。"

    chenjiu "跑出来就来了马来亚？"
    atu "先去了厦门。在厦门混了半年，没活路。"
    atu "被人骗上船，说是去南洋做工赚大钱。"
    atu "结果......也是猪仔。"

    chenjiu "（沉默良久）你认字吗？"
    atu "认一些。台湾的私塾念过两年。"
    chenjiu "哦对了，我叫陈九。同安人。"
    show chenjiu v2_bitter at center
    chenjiu "我也是......被卖来的。"
    atu "（迟疑了一下）我叫阿土。"
    hide chenjiu
    hide atu
    with dissolve

    call cinematic_narration("那一夜，陈九和阿土聊了很久。") from _call_cinematic_narration_53
    call cinematic_narration("陈九也讲了自己的故事，如何染上赌瘾，如何拖累家庭，又是如何被卖到了这里。") from _call_cinematic_narration_54
    call cinematic_narration("两个被命运抛到异乡的年轻人，在马来亚的橡胶林里，成了莫逆之交。") from _call_cinematic_narration_55
    call cinematic_narration("阿土只比陈九大两岁，却比陈九沉稳得多。") from _call_cinematic_narration_56
    call cinematic_narration("他不不说大话，不发牢骚，每日就是埋头干活。") from _call_cinematic_narration_57
    call cinematic_narration("陈九问他想过跑吗，他说：“跑什么？跑了也是死。在这里，至少还有口饭吃。”") from _call_cinematic_narration_58
    call cinematic_narration("陈九又问他想不想家。阿土沉默了很久，说了一句话：") from _call_cinematic_narration_59

    atu "（望着北方的夜空）想。"
    atu "我阿母还在台湾。我弟弟也在。可我连他们死活都不知道。"
    atu "（声音哽咽）我有时候想，我阿母是不是也在等我回家？"
    atu "就像......就像码头上的那些番客婶一样。"

    chenjiu "（也望着夜空，顿了顿）我阿母也在等我。"
    chenjiu "是我自己把家败了，才害她夜夜点着灯等。"

    call cinematic_narration("两人一时相顾无言。") from _call_cinematic_narration_60
    atu "台湾话“土”和“九”发音很像。咱们也是有缘。"

    show chenjiu v2_bitter at left
    chenjiu "（苦笑）有缘。两个被卖的猪仔，有缘。"
    atu "（忽然正色）九，我跟你商量个事。"
    chenjiu "什么事？"
    atu "我观察你好几天了。你割胶不行，可你算账利落。今日工头让你数胶杯，你算的比谁都快。"
    chenjiu "那又怎样？"
    atu "我割胶比你强。我手稳。我在台湾的时候种过甘蔗，割橡胶和割甘蔗差不多。你教我算账，我教你割胶。咱们互相搭把手，日子能好过些。"
    chenjiu "（沉吟）搭把手......怎么搭？"
    atu "（从铺位底下摸出几枚铜片，塞到陈九手里）你看看这个。"

    call cinematic_narration("陈九借着工棚里那盏昏黄的油灯，看清了手里的东西——几枚打磨粗糙的瓷片，上面压着\"林\"字和几道齿纹。") from _call_cinematic_narration_61

    chenjiu "这不是猪仔币吗？"
    atu "嗯，我赎身不像你是契约的，我得自己攒钱赎。烟寮抽一口，三枚；米铺买一斤米，两枚；杂货铺买一卷烟丝，一枚。可你要是想攒够赎身的真大洋——做梦。林头家的铺子，猪仔币进去，大洋出来，一比十的价。十枚猪仔币换一枚大洋，可我一天累死累活才挣五枚。我现在还赊着点，也不知道什么时候才能平账。"
    chenjiu "（心算了一遍，脸色变了）这账......不对。"
    atu "哪里不对？"
    chenjiu "假设你今日赊了一回烟，欠了三枚；明日买米又欠了两枚。林头家赊账的利是几分？"
    atu "五分。"
    chenjiu "（倒吸一口凉气）五分利！滚一个月，你欠的就不是三枚五枚，是一串了。（顿了顿）阿土，你抽不抽？"
    atu "（摇头）我不抽。可我上个月发了高烧，林头家的手下硬塞了我一口，说\"病了抽一口就好\"。那一口，我到现在还欠着账。"
    chenjiu "（把那几枚猪仔币在掌心掂了掂，忽然说）林头家的账房算账糊涂，但林头家可不糊涂。他就是故意纵容账房给咱们算糊涂账，好让咱们这些人永远还不清！阿土，你那笔烟账我替你重新算一遍，把该付的付清，把多扣的讨回来。"
    atu "（一惊）你敢去讨？"
    chenjiu "（苦笑）我赌了半辈子，最会的就是算账。能不能算得赢，我不敢说，但要把账算清——我有把握。（看着阿土）你信不信我？"
    atu "（盯着陈九看了很久，忽然笑了）信。你算账的时候，眼睛亮——跟我阿爸当年算田租的时候一个样。"

    call cinematic_narration("第二天收工，陈九真去了林头家的账房。他把阿土三个月的烟账、米账、杂货账，一笔一笔重新算了一遍——林头家的账房少记了阿土两次预支、多扣了三次利钱，里外里差了十二枚猪仔币。") from _call_cinematic_narration_62
    call cinematic_narration("账房起初不认。陈九把账册往桌上一拍，逐笔报数，分毫不差。账房脸上一阵青一阵白，最后灰溜溜地把十二枚猪仔币退了回来。") from _call_cinematic_narration_63
    call cinematic_narration("阿土攥着那十二枚铜片，手都在抖。十二枚猪仔币，在园里是两天的命。可对阿土来说，这是他到南洋以来，头一回有人替他撑腰。") from _call_cinematic_narration_64
    call cinematic_narration("那天夜里，阿土把铺位挪到陈九旁边，从枕头底下摸出一小包用芭蕉叶裹着的咸鱼——那是他攒了半个月、本来打算留着过年的口粮——硬塞给陈九一半。") from _call_cinematic_narration_65
    atu "九，往后的账，咱们一起算。往后的活，咱们一起干。你是同安人，我是台湾人，可在这座橡胶园里，咱们是一条绳上的两只蚂蚱。你帮我算账，我帮你割胶。猪仔币骗不了咱们，鸦片也锁不住咱们——咱们总有一天能熬出去。"
    call cinematic_narration("陈九接过那半包咸鱼，眼眶忽然热了。他想起母亲的红布包，想起父亲教他博饼时的红瓷碗。他已经一年多没尝过\"有人惦记\"的味道了。") from _call_cinematic_narration_66
    call cinematic_narration("这半包咸鱼，比那三块大洋还重。") from _call_cinematic_narration_67
    call cinematic_narration("这便是陈九与阿土友谊的根。不是赌桌上的\"成交\"，是在一个被卖、被拐、被当畜生的地方，有人伸手拉了他一把，说：\"我信你。\"") from _call_cinematic_narration_68
    chenjiu "（眼睛一亮）成交。"

    if line1_opium_choice == "never":
        call cinematic_narration("阿土多看他一眼：\"九，园里不抽的人，我见过的不超过三个。你能忍着疼不抽，就能熬契约。\"陈九苦笑：\"忍疼容易，忍心难。\"") from _call_cinematic_narration_69

    # 选择1回响
    if line1_choice1 == "saved":
        call cinematic_narration("阿土和陈九结拜前夜，阿土说了一句话：\"九，船舱里那夜，你把水分给阿福，自己差点死了。其实我睡你隔壁铺，我都看见了。\"陈九愣住。阿土接着说：\"我能跟你搭伙，不是因为你算账快，是因为我知道——你这个人，能交。\"") from _call_cinematic_narration_70
    elif line1_choice1 == "not_saved":
        call cinematic_narration("阿土和陈九结拜前夜，阿土说了一句话：\"九，船舱里那夜，那个后生仔死的时候，你没回头。其实我睡你隔壁铺，我都看见了。\"陈九的脸一下子白了。阿土沉默良久，又说：\"我不是说你。那水是你自己的命。可我告诉你一句话——往后咱们搭伙互相帮，莫再让身边的人死在眼皮子底下。能救一个是一个。\"") from _call_cinematic_narration_71
        call cinematic_narration("陈九没说话，点了点头。这句话，他记了一辈子。后来抗战护送难民，他宁肯自己冒险，也不肯再让人死在眼皮底下——就是因为阿土这句\"能救一个是一个\"。") from _call_cinematic_narration_72

    call screen culture_note("台湾割让", "1895年甲午战败，清政府签订《马关条约》，将台湾割让给日本。此后五十年，台湾沦为日本殖民地。大量台湾民众内渡大陆，或远走南洋。资料载：\"台湾沦为日本殖民地后，部分台民内渡。\"阿土的设定即源于此历史背景。", "历史", "history_taiwan_ceded")
    call screen culture_note("台湾寻根", "资料载：\"闽南人移居台湾的历史源远流长\"，\"台湾80%的老百姓都是闽南移民的后代\"。台湾与闽南同根同源，为后文\"帮助阿土寻根\"埋下伏笔。", "历史", "history_taiwan_root")

    hide atu with dissolve
    hide chenjiu with dissolve

    jump line1_act05
