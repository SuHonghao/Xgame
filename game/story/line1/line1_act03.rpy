## line1_act03.rpy — 幕三 · 马来亚橡胶园 · 苦工
## 严格按 线路一.md 原文逐字实现，未改写未删减

label line1_act03:
    scene expression prologue_bg("images/background/马来亚橡胶园.png") with fade
    call fullscreen_cinematic_narration("【幕三】马来亚橡胶园 · 苦工") from _call_fullscreen_cinematic_narration_1

    call cinematic_narration("马来亚，雪兰莪。一片望不到头的橡胶林。") from _call_cinematic_narration
    call cinematic_narration("陈九被分到一个华人橡胶园做工。这里和锡矿场不同——锡矿是往地底下挖，橡胶是往树上割。可苦是一样的苦。") from _call_cinematic_narration_1
    call cinematic_narration("马来亚的太阳毒辣。陈九从秋天的同安来到赤道的雪兰莪，皮肤晒得像锅底。") from _call_cinematic_narration_2

    #TODO: 确认展示，如果确定了后面的背景也要同步修改
    if line1_danger_b == "give_water":
        scene expression prologue_bg("images/background/幕三3.png") with fade
        call cinematic_narration("下船时老水手把沾满油污的保生大帝符塞回他手里：活着就好。符还给你——我收过水钱，不收神钱。") from _call_cinematic_narration_3
        call cinematic_narration("陈九磕了三个头。红布包重新沉甸甸。此后每次摸符，都记得：半勺水，一条命。") from _call_cinematic_narration_4
    elif line1_danger_b == "endure":
        call cinematic_narration("他虚得站不稳，符还在包里。后来他对阿土说：海上那五日，我什么都没偷。偷了，就不是我阿母要的那个九了。") from _call_cinematic_narration_5

    call cinematic_narration("橡胶园的活是这样：每日天不亮起来，趁着凉爽割胶。用一把特制的割胶刀，在橡胶树皮上斜斜划一道口子，乳白色的胶液就一滴一滴淌进陶杯里。等太阳出来了，胶液就不流了。所以割胶必须赶早，必须快。") from _call_cinematic_narration_6
    call cinematic_narration("陈九一开始割不好。刀太利，伤到了树皮里面的形成层，树就废了。这时工头就会用鞭子抽他。") from _call_cinematic_narration_7

    call cinematic_narration("橡胶林一眼望不到头。树干笔直，树冠浓密。每一棵树上都挂着一只陶杯，用来接住树皮切口处淌下的胶液。胶液乳白，像树的眼泪。") from _call_cinematic_narration_8
    call cinematic_narration("割胶工弯着腰，一刀一棵，一刀一棵。太阳升起来之前，必须割完自己负责的那一片。") from _call_cinematic_narration_9

    call screen culture_note("马来亚橡胶", "资料载：“橡胶原产于巴西，华侨使其在马来西亚落户、发展，产量居世界首位”，又载林文庆被誉为\"马来亚橡胶之父\"，陈齐贤1896年在马六甲试种橡胶成功，陈嘉庚是首位集橡胶种植、制造和贸易为一体的企业家，被誉为\"橡胶大王\"。1910年前后，殖民政府鼓励种植橡胶，橡胶业成为马来亚经济支柱。", "历史", "history_rubber_malaya")
    show lin_toujia zoom at center
    call cinematic_narration("工头是个马来亚本地出生的华人，姓林，人称“林头家”。他手里永远握着一根藤鞭。") from _call_cinematic_narration_10

    show lin_toujia zoom at right 
    show chenjiu v2_low at left
    with dissolve

    lin_toujia "（看陈九割的树，骂）你这般割法，树皮都烂了！这棵树废了，你知道一棵橡胶树值多少钱吗？"
    chenjiu "（低头）头家，我手生......"
    show chenjiu v2_cry at left
    lin_toujia "（一鞭子抽过来）手生？手生就去死！橡胶园不养废物！"

    hide lin_toujia with dissolve
    
    show chenjiu v2_cry at center with dissolve
    call cinematic_narration("陈九挨了鞭子，但也只能咬牙忍着。他忽然想起了春风楼的赌桌，想起九指仙的算盘，想起黄三爷的账房。") from _call_cinematic_narration_11
    call cinematic_narration("他这辈子，好像永远在挨打。赌场里输光了赔不起挨赌场老板的拳头，家里挨大哥的耳光，如今到了南洋，还要挨工头的鞭子。") from _call_cinematic_narration_12
    call cinematic_narration("他忽然想笑。他这辈子，真是一步错，步步错。") from _call_cinematic_narration_13
    call cinematic_narration("橡胶园的日子，比陈九想象的还要险恶。") from _call_cinematic_narration_14
    hide chenjiu with dissolve

    scene expression prologue_bg("images/background/烟寮-福寿膏.png") with fade
    call cinematic_narration("园子里有一间“烟寮”。低矮的茅草屋，门口挂着一块发黑的木牌，上头写着“福寿膏”三个字。") from _call_cinematic_narration_15
    call cinematic_narration("每日收工，林头家的手下就在烟寮里摆开烟灯，一团团黑膏在铜灯上化开，甜腻腻的烟香飘满整个屋子。") from _call_cinematic_narration_16

    call cinematic_narration("头几天陈九不肯去。可割胶一天下来，腰像断了，手像烂了，腿像灌了铅。") from _call_cinematic_narration_17
    call cinematic_narration("隔壁铺位的老劳工劝他：“后生仔，抽上一口，身上就不疼了。”") from _call_cinematic_narration_18

    call cinematic_narration("烟香甜腻，毒蛇般缠绕着茅草屋内每个人的身体。") from _call_cinematic_narration_19
    call cinematic_narration("赊账也行。林头家从不拦。") from _call_cinematic_narration_20

    call screen line1_danger_warning("危C · 烟寮", "可能导致死亡/坏结局。建议存档。")
    call cinematic_narration("系统提示：可能导致死亡/坏结局。建议存档。") from _call_cinematic_narration_21

    menu:
        "A · 从此每日赊抽":
            $ line1_opium_choice = "addicted"
            $ line1_danger_c = "addicted"
            jump line1_act03_badend_opium
        "B · 偶尔抽一口止痛，之后咬牙戒断（主线默认）":
            $ line1_opium_choice = "quit"
            $ line1_danger_c = "quit"
            jump line1_act03_continue
        "C · 死也不抽":
            $ line1_opium_choice = "never"
            $ line1_danger_c = "never"
            jump line1_act03_continue

label line1_act03_continue:
    if line1_opium_choice == "quit":
        scene expression prologue_bg("images/background/烟寮_老劳工枯骨.png") with fade
        call cinematic_narration("试了一口，见老劳工枯骨模样，吓出冷汗。撑过最疼几夜后戒掉。") from _call_cinematic_narration_22
        call cinematic_narration("主线继续（基本剧情不变）。") from _call_cinematic_narration_23
    elif line1_opium_choice == "never":
        scene expression prologue_bg("images/background/猪仔币-袋装.png") with fade
        call cinematic_narration("疼着忍着，不欠烟债。能攒一点猪仔币。") from _call_cinematic_narration_24
        call cinematic_narration("主线继续；成交夜触发阿土敬意回响。") from _call_cinematic_narration_25
        scene expression prologue_bg("images/background/烟寮_老劳工枯骨.png") with fade

    call cinematic_narration("林头家从不阻止劳工抽鸦片，管你赊不赊账，反正最后从工钱里扣。") from _call_cinematic_narration_26
    call cinematic_narration("可工钱本就薄，膏子又贵，赊着赊着，欠下的债越滚越大。") from _call_cinematic_narration_27

    show chenjiu v2_haggard at center
    call cinematic_narration("陈九看着那些老劳工——抽了十年、二十年，眼窝深陷，皮包骨头，眼神涣散，连橡胶树和人都分不清了，可还离不了那一口。") from _call_cinematic_narration_28

    call cinematic_narration("林头家要的就是这个。") from _call_cinematic_narration_29
    call cinematic_narration("抽上了，就走不了了。") from _call_cinematic_narration_30
    call cinematic_narration("跑？跑到哪里去？身上没力，腿脚发软，园子外头是莽莽雨林和土著部落，跑出去也是死。") from _call_cinematic_narration_31
    call cinematic_narration("再说了，欠着烟账，林头家的狗腿子追到天涯海角也要把你抓回来。") from _call_cinematic_narration_32

    call cinematic_narration("这就是橡胶园留人的法子——鞭子是明的，鸦片是暗的。明的打你身，暗的锁你魂。") from _call_cinematic_narration_33
    hide chenjiu with dissolve

    scene expression prologue_bg("images/background/猪仔币-袋装.png") with fade
    call cinematic_narration("园子里不发大洋，发的是一种铜片，劳工们叫“猪仔币”。") from _call_cinematic_narration_34
    call cinematic_narration("这种铜片只在橡胶园里流通——林头家的烟寮收、林头家的米铺收、林头家的杂货铺收，出了园子，一文不值。") from _call_cinematic_narration_35
    call cinematic_narration("劳工干一天活，挣几枚猪仔币，回头又把猪仔币花回林头家的铺子里。钱转一圈，又回到了林头家手里。") from _call_cinematic_narration_36
    call cinematic_narration("劳工永远攒不下一个真大洋，永远离不了这座园子。") from _call_cinematic_narration_37

    show chenjiu v2_low at center
    call cinematic_narration("陈九算账利落，他头一个月就把这笔账算明白了：") from _call_cinematic_narration_38
    call cinematic_narration("这不是做工，是替人当牛马，还倒欠人的草料钱。") from _call_cinematic_narration_39
    call cinematic_narration("可他不敢说。") from _call_cinematic_narration_40
    call cinematic_narration("说出去，挨鞭子事小，断了烟赊事大——那些抽惯了的老劳工，为了那一口膏子，能把他活活咬死。") from _call_cinematic_narration_41


    call cinematic_narration("陈九内心一阵发凉") from _call_cinematic_narration_42
    call cinematic_narration("每每路过“烟寮”，想要逃出去的决心都远远大过那半口烟对他的诱惑。") from _call_cinematic_narration_43
    call cinematic_narration("他总会想起春风楼算盘声中宣判债款的绝望；") from _call_cinematic_narration_44
    call cinematic_narration("想起黄三爷不屑又奸诈的笑容；") from _call_cinematic_narration_45
    call cinematic_narration("想起形销骨立的老劳工麻木又癫狂的神情；") from _call_cinematic_narration_46

    show chenjiu v2_cry at center
    call cinematic_narration("最后浮现出他娘双眼含泪的模样，") from _call_cinematic_narration_47
    call cinematic_narration("从嘴里慢慢挤出那句：") from _call_cinematic_narration_48
    call cinematic_narration("“娘只希望你平平安安”") from _call_cinematic_narration_49

    call screen culture_note("南洋种植园鸦片与猪仔币", "19世纪至20世纪初，南洋种植园普遍存在两种束缚华工的手段：其一，殖民政府与园主默许、甚至纵容劳工吸食鸦片，烟膏由园主专卖、可赊欠，劳工一旦上瘾便难以脱离种植园；其二，园内以\"猪仔币\"（又称\"园币\"\"公司币\"）代发工钱，仅供园内消费使用，出园就成了废纸，使劳工永远无法积蓄真实货币赎身。此二者与契约制度并列为南洋\"猪仔贸易\"压榨华工的三大枷锁。", "历史", "history_opium_pigcoin")

    jump line1_act04

label line1_act03_badend_opium:
    scene expression prologue_bg("images/background/烟寮-内部.png") with fade
    call cinematic_narration("三日上瘾，工钱全进了烟寮。阿土劝了三次，陈九却只笑。一年后，陈九死在了烟灯旁，无人收尸。") from _call_cinematic_narration_50
    call screen line1_game_over("福寿膏灯", "Bad End", "来上一口烟，赛过活神仙，你九少爷我当神仙去了！请读档，回危C。")
    return
