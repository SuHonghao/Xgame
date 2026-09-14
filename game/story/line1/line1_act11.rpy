## line1_act11.rpy — 幕十一 · 回国 · 落叶归根（长幕，内部子 label 组织）

label line1_act11:
    scene expression prologue_bg("images/background/幕十一1.png") with fade
    call cinematic_narration("民国二十七年（1938）春。厦门港。") from _call_cinematic_narration_184
    call cinematic_narration("船快靠岸了。陈九和阿土站在甲板上，看着渐渐清晰的厦门海岸线。") from _call_cinematic_narration_185
    call cinematic_narration("四十三年前，陈九从厦门港被卖上船，还是一个十六岁的赌徒。") from _call_cinematic_narration_186
    call cinematic_narration("如今他五十九岁了，头发花白，背也驼了，可他回来了。") from _call_cinematic_narration_187
    call cinematic_narration("阿土也站在甲板上。他离开台湾四十三年了，离开厦门也将近四十年了。他望着海岸线，眼泪止不住地流。") from _call_cinematic_narration_188
    call cinematic_narration("可陈九没有流泪。他望着那片熟悉的海岸，心里只有一个念头——家在哪里？") from _call_cinematic_narration_189

    show atu full at right with dissolve
    show chenjiu despair at left with dissolve

    atu "（哽咽）九......我回来了......"
    chenjiu "（拍了拍阿土的肩膀，低声）阿土，你还有人接。我......已经没人接了。"
    atu "（一愣）你大哥......"
    chenjiu "（苦笑）我连我大哥是死是活都不知道。民国六年就听说阿母走了，坟却一直找不到。后人在哪、坟在哪，还得靠自己走回去问。"
    atu "（握住他的手）九，我陪你找。"
    chenjiu "你先回鼓浪屿。你阿母等你等了四十三年，别让她再等了。我自己去找。"
    atu "（犹豫）你一个人......"
    chenjiu "鼓浪屿的路，我帮你问过；同安的路，也该我自己走。你放心，我找着就来见你。"

    if line1_choice2 == "stay":
        call cinematic_narration("他怀里那叠侨批底稿，少说二十多封。一封都没换回回批。如今他要找的，不是收批的人，是一座朝南的坟。") from _call_cinematic_narration_190
    else:
        call cinematic_narration("他怀里底稿不多——地址空了以后，有些话根本寄不出去。可他仍然记得当年那三个月走的路。如今再走，是为了把当年没问出的村名问出来。") from _call_cinematic_narration_191

    hide atu with dissolve
    hide chenjiu with dissolve

    jump line1_act11_search_family

# ————— 场景变化：码头无亲人 —————
label line1_act11_search_family:
    scene expression prologue_bg("images/background/西溪码头.png") with fade
    call cinematic_narration("阿土去了鼓浪屿。陈九独自一人，踏上了厦门港的码头。") from _call_cinematic_narration_192
    call cinematic_narration("没有人来接他。") from _call_cinematic_narration_193
    call cinematic_narration("他在码头站了很久，看着别的归侨被亲人围着、哭着、笑着，他只是背着一个小包袱，慢慢往外走。") from _call_cinematic_narration_194

    scene expression prologue_bg("images/background/陈家大厝-清晨-破旧.png") with fade
    call cinematic_narration("陈九先回了同安。西溪还在，陈家大厝还在——只是换了主人。新主人是个开米铺的，见了陈九，一脸茫然：\"陈家？陈家是哪一户？我买这厝的时候，原主是姓陈，可早就不知道搬去了哪里。\"") from _call_cinematic_narration_195

    if line1_choice2 == "return_home":
        call cinematic_narration("他站在门口，认出锁已换过——光绪二十八年他来过一回，问过一回。那时尚有邻人摇着头告诉他不清楚；如今连那几户人都换了辈分，更无人知晓旧事。") from _call_cinematic_narration_196

    call cinematic_narration("陈九又去找族里的老人。老人换了一茬又一茬，没人记得陈万田那一支。他翻族谱，族谱上只记到陈九离家那一年，之后的格子全是空的。") from _call_cinematic_narration_197
    call cinematic_narration("他又去了大哥的岳家、母亲娘家、所有能想到的亲戚家——全是\"不知道\"。") from _call_cinematic_narration_198
    call cinematic_narration("有人说\"听讲搬去了泉州\"，有人说\"好像是漳州\"。每一条线索追下去，都是断头路。") from _call_cinematic_narration_199
    call cinematic_narration("陈九在同安待了三个月，仍未找到坟。他把带在身上的底稿一封一封拿出来问：\"陈家。西溪畔的陈家。可有人还记得？\"") from _call_cinematic_narration_200
    call cinematic_narration("没人记得。") from _call_cinematic_narration_201

    jump line1_act11_meet_oldman

# ————— 县衙老榕树下遇见老汉 —————
label line1_act11_meet_oldman:
    scene expression prologue_bg("images/background/同安后街巷子.png") with fade
    call cinematic_narration("三个月后，陈九在同安县衙门口的老榕树下坐着，一个收破烂的老汉路过，看了他一眼，忽然停下。") from _call_cinematic_narration_202

    show ragpicker zoom at right with dissolve
    show chenjiu v2_haggard at left with dissolve

    lao_han "客官，你怀里那一叠纸，能给我看看吗？"
    chenjiu "（递过去）这是我从前寄给家里的底稿。"
    lao_han "（翻了几封，忽然拍腿）陈万田的九子！你就是那个九少爷？"
    chenjiu "（一激灵，猛地站起身）你认识我阿爹？"
    lao_han "我不认识你阿爹。可我认识你大哥。永泰。"
    chenjiu "（抓住老汉的手）永泰？我大哥？他在哪里？！"
    lao_han "（叹气）你大哥......三年前就走了。"
    chenjiu "（脸色一白）走了？"
    lao_han "嗯。你大哥这些年一直在同安乡下住。你阿母欠债那阵子，举家搬到了乡下，租了几亩薄田过活。你大哥临走前，托我替他留心一件事——他说，他有个弟弟，叫陈九，很多年前没了音讯。若哪天有人来打听陈家，就告诉他，陈家在莲花镇后埔村。你阿母葬在后埔村后山，朝南。"
    chenjiu "（浑身颤抖）后埔村......我阿母......"
    lao_han "你大哥年年去上坟，直到他自己也走了。"
    chenjiu "（跪倒在地）阿母——大哥——"
    lao_han "（扶他）起来吧孩子，去后埔村。你大哥的儿女还在那里。你阿母的坟也在那里。"

    hide ragpicker with dissolve
    hide chenjiu with dissolve

    jump line1_act11_grave

# ————— 后埔村 · 认亲 · 母坟 —————
label line1_act11_grave:
    scene expression prologue_bg("images/background/幕十一13.png") with fade
    call cinematic_narration("陈九连夜赶去了莲花镇后埔村。") from _call_cinematic_narration_203
    call cinematic_narration("那是一个藏在山坳里的小村子，离同安城三十余里路。陈九赶到时，天已经黑了。他问到一户姓陈的人家，摸黑到他们家门前敲开门。") from _call_cinematic_narration_204
    call cinematic_narration("开门的是个三十来岁的后生，眉眼间有几分大哥永泰的影子。") from _call_cinematic_narration_205

    show c_nianzu calm at right with dissolve
    show chenjiu v2_haggard at left with dissolve

    c_nianzu "你找谁？"
    chenjiu "（声音发抖）我......我找陈永泰。"
    c_nianzu "（一愣）我阿爸？他三年前就......"
    chenjiu "（抓住门框）你是......永泰的儿子？"
    c_nianzu "是。我叫陈念祖。你是什么人？"
    chenjiu "（泣不成声）我是你九叔。我是陈九啊！我从南洋回来。"
    c_nianzu "（愣了半晌，忽然扑过来）九叔！阿爸天天念叨你，不知你是死是活。临终时还嘱咐我说，如果等到你回来，一定带你去给阿嬷上一柱香，你终于回来了！"
    chenjiu "（抱住侄子，嚎啕大哭）念祖......念祖......你阿嬷......你阿嬷的坟在哪里......"
    c_nianzu "（也哭了）后山。阿嬷的坟在后山。阿爸年年带我们去上坟。他说，阿嬷临终前还在念\"九啊，九啊，阿母等你\"......"
    chenjiu "（跪倒）阿母——"

    hide c_nianzu with dissolve
    hide chenjiu with dissolve

    scene expression prologue_bg("images/background/幕十一14.png") with fade
    call cinematic_narration("那一夜，陈九在阿母坟前，哭到天明。") from _call_cinematic_narration_206

    scene expression prologue_bg("images/background/幕十一17.png") with fade
    call cinematic_narration("第二天清晨，陈念祖带陈九去了后山。后山朝南，是一片缓坡，坡上长满了茅草。母亲的坟就在坡顶，矮矮的一座土丘。坟前的青石碑被日头和雨水磨得发灰，字刻得不深，但还认得出——\"先妣陈母王氏之墓\"。") from _call_cinematic_narration_207
    call cinematic_narration("碑前插着三炷香，已经烧尽了，香脚插在土里，被风吹斜了。是大哥永泰去年清明烧的，已经过去一年了。") from _call_cinematic_narration_208
    call cinematic_narration("陈九在坟前站了一会儿。他以为自己会跪下去，可腿没有动。他看着那座土丘，忽然发现它比记忆中小很多。他记得母亲个子不高，可她的声音总是能落到正厅的每个角落。现在她就在这座矮矮的土丘下面，不说话了。") from _call_cinematic_narration_209
    call cinematic_narration("他说不清自己站了多久。风从坡上吹过来，茅草蹭着他的裤腿，很轻，像有人伸手碰了他一下。他低头看见脚边的土——是同安的土，不是南洋的红土。四十三年前他走的时候，母亲给他塞了一小包家乡的泥土，后来他在橡胶园里挖过无数次土，每次挖都想起那一包。他一直以为她能等到他回来。他一直以为那句\"九会回来的\"，还有时间兑现。") from _call_cinematic_narration_210
    call cinematic_narration("他慢慢蹲下去，从怀里摸出那个红布包。布已经旧了，边角也磨破了。") from _call_cinematic_narration_211
    call cinematic_narration("他把红布包放在碑前，手指碰到青石碑的边沿。石头是凉的。凉得他想起被运往南洋那夜的船舱，凉到骨头里。他忽然跪了下来，额头抵着碑面，像抵着一扇再也推不开的门。他张嘴想说话，可第一声没出来。第二声是哑的。") from _call_cinematic_narration_212
    call cinematic_narration("\"阿母......儿回来了。儿改了，再也没赌过！儿在南洋种橡胶，赚了很多钱，还给国家捐了钱，替阿土寻了根。儿......儿也寄过批，一封一封寄，可总是寄不到，儿找不到您啊......阿母，您不知道，儿这些年，年年想，年年等......儿不知道您搬到了这里，也不知道您走的时候有没有人陪着......\"") from _call_cinematic_narration_213
    call cinematic_narration("他伏在那里，肩膀没动，声音全压在碑面上。风从南边吹过来，把他的手吹得发僵，可他没有收回去。") from _call_cinematic_narration_214
    call cinematic_narration("陈念祖站在坡下，没有上去。他只能看见九叔的肩膀在抖，像一个人背着一块石头走了很多年，终于放下来了。") from _call_cinematic_narration_215
    call cinematic_narration("陈九跪了整整一天。香燃尽了又续，续了又燃尽。陈念祖劝他起来，他不肯。他说：\"我欠阿母四十三年的香，今日要一次烧完。\"") from _call_cinematic_narration_216
    call cinematic_narration("火苗在暮色里很稳。他蹲在坟前，把碑上的土用手掌轻轻扫了一遍，像一个孩子在替母亲擦掉脸上的灰。") from _call_cinematic_narration_217
    call cinematic_narration("四十三年的悔、四十三年的等、四十三年的失联，全化成了坟前那一缕烟。") from _call_cinematic_narration_218
    call cinematic_narration("\"阿母，儿回来得晚。可儿回来了。以后哪也不去了。\"") from _call_cinematic_narration_219
    call cinematic_narration("他在后埔村住下，把母亲坟修了，又给大哥永泰立了碑。侄子陈念祖一家，成了他在故土唯一的亲人。") from _call_cinematic_narration_220

    jump line1_act11_ancestral_hall

# ————— 祖厅 · 拜祖 —————
label line1_act11_ancestral_hall:
    scene expression prologue_bg("images/background/幕十一21.png") with fade
    call cinematic_narration("安顿下来的第三日，陈念祖带陈九去了陈家祖厅。") from _call_cinematic_narration_221
    call cinematic_narration("后埔村的陈家祖厅，是陈永泰当年举家搬来时，从同安西溪畔陈家大厝分出来的一支祠堂。厅堂不大，三开间，燕尾脊，红砖赤瓦，正中悬着\"颍川衍派\"的旧匾——还是当年从厝里带出来的那块，漆色斑驳，边角缺了一块。") from _call_cinematic_narration_222
    call cinematic_narration("匾下是一架黑漆供案。案上按闽南旧俗，从里到外分三层供奉着陈家列祖列宗的牌位——最里层是始祖与历代先祖，中间是祖父与祖母，最外层正中的位置，立着两方较新的牌位，并排挨着：\"先考陈公万田之神位\"与\"先妣陈母王氏之神位\"。父亲是大哥永泰当年亲手立的，母亲的那方是后来补的，比旁边的深一些，像是上了新漆。") from _call_cinematic_narration_223
    call cinematic_narration("供案前摆着一张八仙桌，桌上按着闽南旧俗备了祭品：三牲（猪头、全鸡、全鱼）、菜碗（荤素搭配的菜肴）、五果（香蕉、柑橘、菠萝、苹果、梨子）、六斋，还有一壶老酒、一沓金纸。八仙桌上摆得满满当当。猪头上还插着一根猪尾巴。") from _call_cinematic_narration_224
    call cinematic_narration("这些都是念祖连夜备下的。他不懂祖厅的规矩，只知道人回来了，得先让祖宗知道。") from _call_cinematic_narration_225
    call cinematic_narration("陈九站在门口，腿软了。四十三年前他从同安被卖上船，连一声\"阿母，儿走了\"都没来得及说。四十三年后他回来了，阿爹阿母都成了牌位，他站在供案前，不知道自己该往里走几步才够得着他们。") from _call_cinematic_narration_226

    call screen culture_note("闽南拜祖庙", "闽南人拜祖，三牲五果六斋、三跪九叩，是活人对死人的交代：我没忘本，我没忘归路。针线引路，人回来了。", "非遗", "culture_ancestor_worship")

    show c_nianzu calm at right with dissolve
    show chenjiu v2_calm at left with dissolve

    c_nianzu "九叔，时辰到了。"
    chenjiu "（深吸一口气，整了整长衫）好。"
    c_nianzu "（递上三炷香）九叔，先点香。"
    call cinematic_narration("陈九接过香，在烛火上点燃。烟一缕一缕升起来，飘向祖厅的燕尾脊。他捧着香，站在八仙桌前，望着父亲的牌位——\"先考陈公万田之神位\"，金字已经有些发暗了。") from _call_cinematic_narration_227
    chenjiu "（声音发抖）阿爹......儿......儿回来了。"

    call cinematic_narration("陈九按闽南旧俗行了大礼。他双膝跪地，三跪九叩——一跪三叩，再跪三叩，三跪三叩，额头每次都重重磕在祖厅的青砖地上。") from _call_cinematic_narration_228
    call cinematic_narration("咚、咚、咚、咚、咚、咚、咚、咚、咚。") from _call_cinematic_narration_229
    call cinematic_narration("九声闷响，回荡在空旷的厅堂里。") from _call_cinematic_narration_230
    call cinematic_narration("念祖站在一旁充当礼生，高声唱礼：\"一叩首——拜始祖。二叩首——拜高祖。三叩首——拜曾祖。四叩首——拜祖父。五叩首——拜祖母。六叩首——拜父亲。七叩首——拜母亲。八叩首——拜兄长。九叩首——拜列祖列宗。\"") from _call_cinematic_narration_231
    call cinematic_narration("陈九每听一句，就重重磕一个头。磕到\"拜父亲\"那一句，他撑不住了，伏在地上，嚎啕大哭。") from _call_cinematic_narration_232

    chenjiu "（伏地泣告）阿爹......儿不孝......儿十六岁那年，输光了阿母的三块大洋，欠下赌债，被卖去南洋......儿这一走，就是四十三年。阿爹临终，儿没在床前尽孝；阿爹出殡，儿没扛幡送葬......儿连阿爹葬在哪里，都是今日才晓得......儿不孝啊......"
    c_nianzu "（也跪下，陪着哭）九叔，阿爸生前常说，阿公最疼的就是您。阿公走的时候，还念着\"九啊，九啊\"。阿爸说，阿公是念着您的名字走的。"
    chenjiu "（哭得更厉害）阿爹......儿改了......儿再没赌过一文钱......儿在南洋种橡胶，赚了钱，捐了四万块大洋给国家打日本人......儿回来了......儿带着钱回来，可儿带不回那四十三年......阿爹，儿对不起您，对不起阿母，对不起陈家的列祖列宗......"

    call cinematic_narration("陈九哭罢，起身献供。他亲手斟了三杯老酒，一杯敬天，一杯敬地，一杯敬祖先。酒洒在祖厅前的青石板上，渗进缝隙里，不见了。") from _call_cinematic_narration_233
    call cinematic_narration("又从怀里掏出一样东西——是一小包家乡的泥土。当年他被卖上船时，母亲按闽南出洋旧俗，曾在他行李里塞过一小包同安的泥土、一小瓶井水、几支针、几根线，说是\"一来防不服水土，二来不忘家山故水，三来针线引路，使其不忘归路\"。那包泥土，他揣了四十三年，揣过了南洋的橡胶林、海上的风暴、日本的宪兵队。如今他把它捧出来，放在父亲牌位前。") from _call_cinematic_narration_234
    call cinematic_narration("\"阿爹，儿当年出门，阿母给儿带了家乡的土。儿揣了四十三年，没敢丢。如今儿回来了，把这包土还给阿爹——儿没忘家山，儿没忘归路。针线引路，儿回来了。\"") from _call_cinematic_narration_235
    call cinematic_narration("陈九又口述了一篇祭文，让念祖代笔写下，烧在父亲牌位前。祭文写的是：") from _call_cinematic_narration_236

    # 祭文全文
    # TODO: replace with letter/document UI
    call cinematic_narration("维") from _call_cinematic_narration_237
    call cinematic_narration("民国二十七年，岁在戊寅，季春之吉，不孝男陈九，谨以三牲果合、清酌庶馐之仪，致祭于显考陈公万田府君之灵前，泣而言曰：") from _call_cinematic_narration_238
    call cinematic_narration("儿九，年十六，好赌败家，欠债被卖，远渡南洋，四十三载，未奉晨昏。父殁不知，母逝未归，兄终未见，此儿之罪，罄竹难书。") from _call_cinematic_narration_239
    call cinematic_narration("然儿在南洋，未敢忘本。改过自新，未再涉赌。勤力营生，以橡胶起家。国难当头，捐资四万，以助抗战。今儿归乡，跪拜祖厅，焚香告祖，泪洒灵前。") from _call_cinematic_narration_240
    call cinematic_narration("父兮生我，母兮鞠我。抚我畜我，长我育我。顾我复我，出入腹我。欲报之德，昊天罔极。") from _call_cinematic_narration_241
    call cinematic_narration("今儿归来，誓办学堂于西溪畔，以赎前愆，以报乡梓。愿父在天之灵，鉴儿此心。儿虽不孝，愿以余生，赎儿之罪。") from _call_cinematic_narration_242
    call cinematic_narration("伏惟尚飨。") from _call_cinematic_narration_243
    call cinematic_narration("不孝男 陈九 泣叩") from _call_cinematic_narration_244

    call cinematic_narration("祭文烧尽，金纸化灰，灰烬随风飘出祖厅，飘向后山，飘向母亲坟茔的方向。") from _call_cinematic_narration_245
    call cinematic_narration("陈九在祖厅里跪了一整夜。念祖劝他，他不肯起。他说：\"我四十三年没给阿爹阿母磕过头，今夜要一次磕完。\"") from _call_cinematic_narration_246
    call cinematic_narration("第二天清晨，陈九从祖厅出来，整个人像换了一副骨头。他的背没那么驼了，眼睛也没那么浑浊了。他对念祖说：\"走，回同安西溪畔。我要在那里办一所学堂。\"") from _call_cinematic_narration_247
    call cinematic_narration("念祖问他为何。") from _call_cinematic_narration_248
    call cinematic_narration("陈九望着西溪的方向，说：\"我阿爹当年盼我读书成器，我偏去赌。我这一生，对不起阿爹的期许。如今我办一所学堂，让穷人家的孩子也能念书——我阿爹当年盼不到的，我替别的阿爹盼到。这便是我对阿爹的祭。\"") from _call_cinematic_narration_249
    call cinematic_narration("这便是闽南人的\"拜祖\"——不止是三跪九叩、不止是三牲五果。它是活人对死人的一个交代：我没忘本，我没忘归路。针线引路，我回来了。") from _call_cinematic_narration_250

    hide c_nianzu with dissolve
    hide chenjiu with dissolve

    jump line1_act11_atu_reunion

# ————— 阿土鼓浪屿母子团聚 —————
label line1_act11_atu_reunion:
    scene expression prologue_bg("images/background/幕十一22.png") with fade
    call cinematic_narration("阿土也去了鼓浪屿。他的阿母和弟弟阿山在那里等他。") from _call_cinematic_narration_251
    call cinematic_narration("阿土的阿母已经七十多岁了，缠着足，头发全白。她站在鼓浪屿的码头，颤巍巍地望着船来的方向。") from _call_cinematic_narration_252
    call cinematic_narration("阿土一下船，就扑过去跪在阿母面前。") from _call_cinematic_narration_253

    show atu_mother zoom at right with dissolve
    show atu tearful at left with dissolve

    atu "（号啕）阿母——"
    atu_mother "（摸着阿土的脸，老泪纵横）阿土......阿土......你回来了......阿母等了你四十三年......"
    atu "（泣）阿母，儿子不孝......"
    atu_mother "回来就好......回来就好......"

    show ashan_full at right with dissolve
    ashan "阿兄，回家。我煮了面线糊。"

    hide ashan_full with dissolve
    hide atu_mother with dissolve
    hide atu with dissolve

    jump line1_act12
