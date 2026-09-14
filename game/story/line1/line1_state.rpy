## line1_state.rpy — 线一 · 橡胶逆袭 全局状态变量
## 只存放 default 剧情变量与线一新增角色 define，不包含剧情流程

# ————— 三大主线选择 —————
default line1_choice1 = None      # "saved"（救了后生仔阿福） / "not_saved"（没救）
default line1_choice2 = None      # 幕六末： "stay"（留下创业，先寄侨批） / "return_home"（先回同安找母亲）
default line1_choice3 = None      # 幕十： "donate_all"（全捐四万） / "keep_reserve"（少捐两万，留两万）

# ————— 危局选择 —————
default line1_danger_b = None     # 危B 船上： "give_water"（半勺换半辈子） / "endure"（渴死不做贼）
default line1_danger_c = None     # 危C 烟寮别名，与 line1_opium_choice 同步
default line1_danger_e = None     # 危E 考账： "mental"（心算答对） / "cheat"（偷看账本） / "pretend"（故意装傻）
default line1_danger_h = None     # 危H 救济方式： "public"（当街骂） / "secret"（暗中救济） / "self_preserve"（关门自保）
default line1_danger_i = None     # 危I 救阿土： "storm"（硬闯） / "ransom"（筹钱） / "collaborator"（求维持会）

default line1_opium_choice = None      # 危C 烟寮： "addicted"（每日赊抽） / "quit"（偶尔抽后戒断） / "never"（死也不抽）
default line1_exam_choice = None       # 危E 别名，与 line1_danger_e 同步
default line1_relief_choice = None     # 危H 别名，与 line1_danger_h 同步
default line1_rescue_choice = None     # 危I 别名，与 line1_danger_i 同步

# ————— 状态旗标 —————
default line1_atu_alive = True             # 阿土生死（危I筹钱 + 选择3决定）
default line1_reputation_stained = False   # 垢名换命：名节有损
default line1_relief_mainline = True       # 危H 自保时置 False，主线尾声不再正常进入
default line1_saved_afuku = False          # 序章船舱救阿福的回响旗标

# 线一新增角色（character.rpy 未覆盖的，避免重复 define）
define atu = Character("阿土")
define atu_mother = Character("阿土阿母")
define ashan = Character("阿山")
define lao_han = Character("老汉")
define lao_shushi = Character("老塾师")
define huoji = Character("伙计")
define japanese_officer = Character("日本军官")
define zhao_qingquan = Character("赵清泉")
define c_nianzu = Character("陈念祖")
define ragpicker = Character("收破烂老汉")

# 线一补充 image（部分立绘暂无素材，用纯色占位避免 Ren'Py 崩溃，待美术补齐后替换为 sprite）
# TODO: missing sprite — 阿山、赵清泉、伙计、陈念祖占位
image ashan_full = Solid("#000000")
image zhao_qingquan_full = Solid("#000000")
image huoji_normal = Solid("#000000")
image c_nianzu = Solid("#000000")
image c_nianzu full = Solid("#000000")
image c_nianzu calm = Solid("#000000")
image c_nianzu sad = Solid("#000000")
