"""所有人物及其表情图片定义"""

init python:
    # 全身或半身人物图片统一缩放，宽高比例保持不变。
    def sprite(path, width=640, height=612):
        if not renpy.loadable(path):
            return path
        return Transform(path, xysize=(width, height), fit="contain", yalign=1.0)

    # 头像图片暂时保留独立处理方式，后续需要时可以单独缩放。
    def head(path, width=None, height=None):
        if not renpy.loadable(path):
            return path
        if width is not None:
            return Transform(path, xsize=width, yalign=1.0)
        if height is not None:
            return Transform(path, ysize=height, yalign=1.0)
        return path


# 剧情中使用的角色对象
define chenjiu = Character("陈九")
define mother = Character("母亲 · 王氏")
define father = Character("父亲 · 陈万田")
define jiuzhixian = Character("九指仙")
define old_shuike = Character("老水客")
define old_sailor = Character("老水手")
define old_worker = Character("老工人")
define huang_sanye = Character("黄三爷")
define afu = Character("阿福")
define lin_toujia = Character("林头家")
define crowd = Character("众人")

# 九少爷：人物卡图片
image chenjiu angry = sprite("images/character/九少爷/九少爷_愤怒.png")
image chenjiu torn = sprite("images/character/九少爷/九少爷_纠结.png")
image chenjiu despair = sprite("images/character/九少爷/九少爷_绝望.png")
image chenjiu disgusted = sprite("images/character/九少爷/九少爷_厌恶.png")
image chenjiu clenched = sprite("images/character/九少爷/九少爷_咬牙.png")
image chenjiu upset = sprite("images/character/九少爷/九少爷_委屈.png")
image chenjiu happy = sprite("images/character/九少爷/九少爷_开心.png")
image chenjiu shocked = sprite("images/character/九少爷/九少爷_惊吓.png")
image chenjiu look_down = sprite("images/character/九少爷/九少爷_低头.png")
image chenjiu look_up = sprite("images/character/九少爷/九少爷_抬头.png")
image chenjiu smile = sprite("images/character/九少爷/九少爷_微笑.png")
image chenjiu bitter = sprite("images/character/九少爷/九少爷_苦笑.png")
image chenjiu full = sprite("images/character/九少爷/九少爷_全局.png")
image chenjiu normal = sprite("images/character/九少爷/九少爷_正常.png")

image chenjiu young_full = sprite("images/character/九少爷/九少爷1_全局.png")
image chenjiu young_zoom = sprite("images/character/九少爷/九少爷1_放大.png")
image chenjiu v2_reach = sprite("images/character/九少爷/九少爷2_伸手.png")
image chenjiu v2_low = sprite("images/character/九少爷/九少爷2_低迷.png")
image chenjiu v2_full = sprite("images/character/九少爷/九少爷2_全局.png")
image chenjiu v2_cry = sprite("images/character/九少爷/九少爷2_哭泣.png")
image chenjiu v2_pout = sprite("images/character/九少爷/九少爷2_噘嘴.png")
image chenjiu v2_afraid = sprite("images/character/九少爷/九少爷2_害怕.png")
image chenjiu v2_calm = sprite("images/character/九少爷/九少爷2_平静.png")
image chenjiu v2_surprised = sprite("images/character/九少爷/九少爷2_惊讶.png")
image chenjiu v2_haggard = sprite("images/character/九少爷/九少爷2_憔悴.png")
image chenjiu v2_bitter = sprite("images/character/九少爷/九少爷2_苦笑.png")
image chenjiu v3_full = sprite("images/character/九少爷/九少爷3_全局.png")
image chenjiu v3_disgusted = sprite("images/character/九少爷/九少爷3_厌恶.png")
image chenjiu v3_cry = sprite("images/character/九少爷/九少爷3_哭泣.png")
image chenjiu v3_upset = sprite("images/character/九少爷/九少爷3_委屈.png")
image chenjiu v3_calm = sprite("images/character/九少爷/九少爷3_平静.png")
image chenjiu v3_happy = sprite("images/character/九少爷/九少爷3_开心.png")
image chenjiu v3_surprised = sprite("images/character/九少爷/九少爷3_惊讶.png")
image chenjiu v3_angry = sprite("images/character/九少爷/九少爷3_愤怒.png")
image chenjiu v3_grin = sprite("images/character/九少爷/九少爷3_憨笑.png")
image chenjiu v3_bitter = sprite("images/character/九少爷/九少爷3_苦笑.png")
image chenjiu v4_full = sprite("images/character/九老爷/九老爷4_全局.png")
image chenjiu v4_cold = sprite("images/character/九老爷/九老爷4_冷脸.png")
image chenjiu v4_cry = sprite("images/character/九老爷/九老爷4_哭泣.png")
image chenjiu v4_upset = sprite("images/character/九老爷/九老爷4_委屈.png")
image chenjiu v4_smile = sprite("images/character/九老爷/九老爷4_微笑.png")
image chenjiu v4_shocked = sprite("images/character/九老爷/九老爷4_惊吓.png")
image chenjiu v4_frown = sprite("images/character/九老爷/九老爷4_皱眉.png")
image chenjiu v5_full = sprite("images/character/九老爷/九老爷5_全局.png")
image chenjiu v5_cold = sprite("images/character/九老爷/九老爷5_冷脸.png")
image chenjiu v5_cry = sprite("images/character/九老爷/九老爷5_哭泣.png")
image chenjiu v5_smile = sprite("images/character/九老爷/九老爷5_微笑.png")
image chenjiu v5_frown = sprite("images/character/九老爷/九老爷5_皱眉.png")
image chenjiu v6_full = sprite("images/character/九老爷/九老爷6_全局.png")
image chenjiu v6_zoom = sprite("images/character/九老爷/九老爷6_放大.png")

# 王氏：人物卡图片
image mother full = sprite("images/character/九母亲/九母亲_全局.png")
image mother disappointed = sprite("images/character/九母亲/九母亲_低头.png")
image mother normal = sprite("images/character/九母亲/九母亲_抬头.png")

# 陈万田：人物卡图片
image father middle_zoom = sprite("images/character/九父亲/中年父亲_放大.png")
image father middle_small = sprite("images/character/九父亲/中年父亲_缩小.png")
image father old_full = sprite("images/character/九父亲/老年父亲_全局.png")
image father old_zoom = sprite("images/character/九父亲/老年父亲_放大.png")

# 兄长：人物卡图片
image brother young_full = sprite("images/character/九兄长/青年兄长_全局.png")
image brother young_zoom = sprite("images/character/九兄长/青年兄长_放大.png")
image brother middle_full = sprite("images/character/九兄长/中年兄长_全局.png")
image brother middle_zoom = sprite("images/character/九兄长/中年兄长_放大.png")

# 陈念祖：人物卡图片
image chen_nianzu full = sprite("images/character/陈念祖/哥哥儿子陈念祖_全局.png")
image chen_nianzu calm = sprite("images/character/陈念祖/哥哥儿子陈念祖_平静.png")
image chen_nianzu sad = sprite("images/character/陈念祖/哥哥儿子陈念祖_难过.png")

# 阿土：人物卡图片
image atu full = sprite("images/character/阿土/阿土_背心全局.png")
image atu zoom = sprite("images/character/阿土/阿土_背心放大.png")
image atu v2_full = sprite("images/character/阿土/阿土2_全身.png")
image atu v2_zoom = sprite("images/character/阿土/阿土2_放大.png")
image atu v2_frown = sprite("images/character/阿土/阿土2_皱眉.png")
image atu v2_tearful = sprite("images/character/阿土/阿土2_含泪.png")
image atu v2_sad = sprite("images/character/阿土/阿土2_悲伤.png")
image atu v2_happy = sprite("images/character/阿土/阿土2_开心.png")
image atu v2_bitter = sprite("images/character/阿土/阿土2_苦笑.png")

# 阿土老爷：人物卡图片
image atu_laoye old_full = sprite("images/character/阿土老爷/阿土老爷旧版_全局.png")
image atu_laoye v3_full = sprite("images/character/阿土老爷/阿土老爷3_全身.png")
image atu_laoye v3_cry = sprite("images/character/阿土老爷/阿土老爷3_哭泣.png")
image atu_laoye v3_calm = sprite("images/character/阿土老爷/阿土老爷3_平静.png")
image atu_laoye v3_happy = sprite("images/character/阿土老爷/阿土老爷3_开心.png")
image atu_laoye v3_smile = sprite("images/character/阿土老爷/阿土老爷3_微笑.png")
image atu_laoye v3_angry = sprite("images/character/阿土老爷/阿土老爷3_愤怒.png")
image atu_laoye v3_sad = sprite("images/character/阿土老爷/阿土老爷3_难过.png")
image atu_laoye v4_full = sprite("images/character/阿土老爷/阿土老爷4_全身.png")
image atu_laoye v4_calm = sprite("images/character/阿土老爷/阿土老爷4_平静.png")
image atu_laoye v4_smile = sprite("images/character/阿土老爷/阿土老爷4_微笑.png")
image atu_laoye v4_angry = sprite("images/character/阿土老爷/阿土老爷4_愤怒.png")
image atu_laoye v4_sad = sprite("images/character/阿土老爷/阿土老爷4_难过.png")

# 阿土母亲：人物卡图片
image atu_mother full = sprite("images/character/阿土母亲/阿土母亲_全局.png")
image atu_mother zoom = sprite("images/character/阿土母亲/阿土母亲_放大.png")


# 阿福：人物卡图片
image afu full = sprite("images/character/阿福/后生仔阿福_全局.png")
image afu zoom = sprite("images/character/阿福/后生仔阿福_放大.png")

# 老塾师：人物卡图片
image lao_shushi full = sprite("images/character/老塾师/老塾师_全局.png")
image lao_shushi zoom = sprite("images/character/老塾师/老塾师_放大.png")

# 水客：人物卡图片
# image old_shuike full = sprite("images/character/水客/npc老水客_全局.png")
# image old_shuike zoom = sprite("images/character/水客/npc老水客_放大.png")
# image old_shuike later_full = sprite("images/character/水客/npc后期水客_全局.png")
# image old_shuike later_zoom = sprite("images/character/水客/npc后期水客_放大.png")
image old_shuike full = sprite("images/character/水客/npc水客_全局.png")
image old_shuike zoom = sprite("images/character/水客/npc水客_放大.png")

# 九指仙：人物卡图片
image jiuzhixian full = sprite("images/character/九指仙/九指仙_全局.png")
image jiuzhixian zoom = sprite("images/character/九指仙/九指仙_正面.png")
image jiuzhixian abacus = sprite("images/character/九指仙/九指仙_算盘放大.png")

# 黄三爷：人物卡图片
image huang_sanye full = sprite("images/character/黄三爷/黄三爷_全局.png")
image huang_sanye zoom = sprite("images/character/黄三爷/黄三爷_放大.png")
image huang_sanye afraid = sprite("images/character/黄三爷/黄三爷_害怕.png")
image huang_sanye angry = sprite("images/character/黄三爷/黄三爷_愤怒.png")

# 林头家：人物卡图片
image lin_toujia full = sprite("images/character/林头家/林头家_全局.png")
image lin_toujia zoom = sprite("images/character/林头家/林头家_放大.png")

# 米铺老板：人物卡图片
image rice_shop_boss full = sprite("images/character/米铺老板/米铺老板_全局.png")
image rice_shop_boss zoom = sprite("images/character/米铺老板/米铺老板_放大.png")

# 小伙计：人物卡图片
image shop_assistant standing = sprite("images/character/小伙计/npc小伙计_站立.png")
image shop_assistant running = sprite("images/character/小伙计/npc小伙计_奔跑.png")

# 收破烂的：人物卡图片
image ragpicker full = sprite("images/character/收破烂的/npc收破烂的_全局.png")
image ragpicker zoom = sprite("images/character/收破烂的/npc收破烂的_放大.png")

# 日本军官：人物卡图片
image japanese_officer full = sprite("images/character/日本军官/日本军官_全局.png")
image japanese_officer zoom = sprite("images/character/日本军官/日本军官_放大.png")

define another = Character("另一人")
define thug = Character("打手")
define thug_a = Character("打手甲")
define thug_b = Character("打手乙")
define gambler_a = Character("赌客甲")
define gambler_b = Character("赌客乙")
define brother = Character("兄长")
define shuike = Character("水客")
