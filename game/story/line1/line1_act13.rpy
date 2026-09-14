## line1_act13.rpy — 幕十三 · 回乡兴学 · 九思学堂
## 严格按 线路一.md 原文逐字实现，未改写未删减

label line1_act13:
    scene expression prologue_bg("images/background/幕十三15.png") with fade
    call cinematic_narration("民国二十七年（1938）初。同安西溪畔。") from _call_cinematic_narration_269
    call cinematic_narration("陈九回国后，手里还有八万块大洋（卖园所得十二万，已捐四万给南侨总会）。他没有开店，也没有再做生意——他已经很有钱了，不需要再赚钱。他想做一件更长久的事。") from _call_cinematic_narration_270
    call cinematic_narration("陈九站在后埔村祖厅的天井里，看着那块\"颍川衍派\"的旧匾。他忽然想起南洋时听过的一句话——陈嘉庚先生说：\"金钱如肥料，撒播才有用。\"") from _call_cinematic_narration_271
    call cinematic_narration("他这辈子赚的钱，是橡胶树上淌出来的胶液换来的，是无数华工的血汗换来的。他不想把这些钱带进棺材。") from _call_cinematic_narration_272

    show chenjiu v4_full at center with dissolve
    show atu full at right with dissolve
    show c_nianzu calm at left with dissolve

    chenjiu "我想办一所学堂。"
    c_nianzu "（一愣）九叔，学堂？"
    chenjiu "同安乡下许多孩子念不起书。我当年念过几年私塾，靠着识字算账，才从猪仔熬成了园主。我想让同安的孩子，也能识字、会算盘。"
    atu "九，你打算办多大？"
    chenjiu "不大。一所小学就够。就在西溪畔，靠近咱们陈家的田。我出钱盖校舍、请先生、免学费。穷人家的孩子，也能来念。"
    c_nianzu "（红了眼眶）九叔......阿嬷和我阿爸若在，会高兴的。阿爸生前一直念叨您，说您若回来，定能做番大事。"
    atu "学堂叫什么名？"
    chenjiu "（沉吟片刻）叫\"九思学堂\"。君子有九思。我赌了半辈子，从没思量过。如今把这三个字挂在学堂上，算是给自己一个交代，也给孩子们一个盼头。"

    hide atu with dissolve
    hide c_nianzu with dissolve
    hide chenjiu with dissolve

    scene expression prologue_bg("images/background/幕十三19.png") with fade
    call cinematic_narration("民国二十七年春，九思学堂在同安西溪畔落成。红砖校舍，燕尾脊，门口挂着\"九思学堂\"四字匾额。开学那天，来了八十多个孩子，多数是佃户家的、番客婶家的。") from _call_cinematic_narration_273
    call cinematic_narration("陈九站在校门口，看着孩子们背着书包走进去，忽然想起自己十六岁那年揣着三块大洋走进赌场的样子。") from _call_cinematic_narration_274
    call cinematic_narration("他想：若当年有人送他进学堂，而不是送他进赌场，他的命，会不会不一样？") from _call_cinematic_narration_275

    call screen culture_note("华侨兴学", "资料载：\"华侨华人热切关注祖籍国的教育事业，捐资助学蔚然成风。\"陈嘉庚创办集美学村、厦门大学；李光前创办国光学村。陈九办九思学堂，正是这一\"文教兴国\"传统的缩影。线一用\"兴学\"收束，与线三的\"开批局\"彻底分开。", "历史", "history_overseas_school")

    show atu full at right with dissolve
    show chenjiu v4_smile at left with dissolve

    atu "九，你这辈子，从赌徒到猪仔，从猪仔到橡胶园主，从橡胶园主到办学堂的乡绅。你这条命，活得值了。"
    chenjiu "（摇头）值不值，不看赚了多少。看最后把钱花在了哪里。我把钱花在孩子们身上，这是我这辈子做得最对的一件事。"

    hide atu with dissolve
    hide chenjiu with dissolve

    jump line1_act14
