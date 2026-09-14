#!/usr/bin/env python3
"""把 demo.xlsx 的 RenPy剧本 工作表中 line1 段直接生成到 game/story/line1/line1.rpy。

用法：
    python3 tools/excel_to_renpy.py

输出：
    game/story/line1/line1.rpy
    game/story/line1/missing_assets.txt

说明：
    Excel 474-475 行之前为 prologue（已在 game/story/prologue/act_*.rpy 中实现，不重复生成）。
    本脚本只生成 line1（第三部分 · 线一，从“第三部分· 线一”标记之后开始），直接覆盖 line1.rpy。
    重复运行可随 Excel 更新同步剧情。
"""
import re
from pathlib import Path
import openpyxl

ROOT = Path(__file__).resolve().parent.parent
XLSX = ROOT / "demo.xlsx"
OUT_DIR = ROOT / "game" / "story" / "line1"
OUT_RPY = OUT_DIR / "line1.rpy"
MISSING = OUT_DIR / "missing_assets.txt"
BG_DIR = ROOT / "game" / "images" / "background"

ROLE_MAP = {
    "陈九": "chenjiu", "陈九心声": "chenjiu",
    "陈万田": "father", "王氏": "mother",
    "黄三爷": "huang_sanye", "九指仙": "jiuzhixian",
    "老水客": "shuike", "兄长": "brother",
    "另一人": "another", "众人": "crowd",
    "赌客": "crowd", "赌客甲": "gambler_a", "赌客乙": "gambler_b",
    "打手甲": "thug_a", "打手乙": "thug_b", "（打手）": "thug",
    "两个人": "crowd",
}
SPRITE_MAP = {
    ("陈九", "九少爷_抬头"): "chenjiu look_up",
    ("陈九", "九少爷_低头"): "chenjiu look_down",
    ("陈九", "九少爷_苦笑"): "chenjiu bitter",
    ("陈九", "九少爷_厌恶"): "chenjiu disgusted",
    ("陈九", "九少爷_惊吓"): "chenjiu shocked",
    ("陈九", "九少爷1_放大"): "chenjiu young_zoom",
    ("陈九心声", "九少爷_惊吓"): "chenjiu shocked",
    ("陈九心声", "九少爷_厌恶"): "chenjiu disgusted",
    ("王氏", "九母亲_低头"): "mother disappointed",
    ("陈万田", "中年父亲_放大"): "father middle_zoom",
    ("黄三爷", "黄三爷_放大"): "huang_sanye zoom",
    ("黄三爷", "黄三爷_害怕"): "huang_sanye afraid",
    ("老水客", "npc水客_放大"): "shuike zoom",
}
POS_MAP = {
    "chenjiu": "right", "father": "center", "mother": "left",
    "brother": "left", "another": "left", "jiuzhixian": "left",
    "huang_sanye": "left", "shuike": "left", "old_shuike": "left",
    "crowd": "left", "gambler_a": "left", "gambler_b": "left",
    "thug_a": "left", "thug_b": "left", "thug": "left",
}
NOISE = (
    "批注[Napel","答复[Napel","CWJ","【必须点击】","【新增】","对话要加双引号","人物表情看着脚本换","人物眨眼gif",
    "压缩包内的图片","写在前面","可加可不加","如果后期有需要","整体排版见","见mp4","交互按钮见ui",
    "旁白用空背景","画面叠化见我做的","发现在这里复制图片更快","【sos】","（楚榕你看看","cwj 留言",
    "中间的手印渐显","开头是不合法文字渐显","在红瓷碗图片上弹出","可以用我的骰子视频","四个骰子向上的图片",
    "背景幕一10、幕一11.1","选择按钮见ui","序章-幕二16（三个4","这里也不用人物立绘","不用出现人物立绘","不出现立绘",
    "图层","排版参考","对应背景","仅背景，无立绘","设计说明","怎么还多了","怎么下面的也改了","TvT",
    "规则提示","个同点","皆同点","四进一个","少定奖","不改变序章主线",
)
def is_noise(text, role):
    return any(m in (text or "") for m in NOISE) or any(m in (role or "") for m in NOISE)

def find_bg(name: str) -> str:
    if not name or name in ("待确认","待定"): return ""
    cands=[name]
    if name.startswith("序幕-"): cands.append(name.replace("序幕-","序章-",1))
    for c in list(cands):
        for ext in (".png",".jpg",".webp"):
            if (BG_DIR/f"{c}{ext}").exists(): return f"images/background/{c}{ext}"
    return ""

def escape(text: str) -> str:
    text=text.replace("\\","\\\\")
    text=re.sub(r'"([^"]*)"', lambda m: "“"+m.group(1)+"”", text)
    return text.replace('"',"”")

class Gen:
    def __init__(self):
        self.lines=[]; self.cur_bg=None; self.shown={}; self.missing_bg=set(); self.missing_sprite=set()
    def scene(self, bg):
        if not bg or bg in ("待确认","待定"): return
        if bg==self.cur_bg: return
        real=find_bg(bg)
        if real: self.lines.append(f'    scene expression prologue_bg("{real}") with fade')
        else:
            self.missing_bg.add(bg)
            self.lines.append(f'    # TODO: missing background: {bg}')
            self.lines.append(f'    scene expression prologue_bg("images/background/{bg}.png") with fade')
        self.cur_bg=bg; self.shown.clear()
    def show_sprite(self, sprite, expr):
        if not expr or expr in ("待确认",): return
        if sprite in ("背景","仅背景，无立绘","待确认","图层","排版参考","对应背景","设计说明"): return
        img=SPRITE_MAP.get((sprite,expr))
        if not img:
            base=re.sub(r"（[^）]*）","",sprite)
            img=SPRITE_MAP.get((base,expr))
        if not img:
            self.missing_sprite.add((sprite,expr)); return
        tag=img.split()[0]; pos=POS_MAP.get(tag,"left")
        if self.shown.get(tag)==(img,pos): return
        if tag in self.shown: self.lines.append(f"    hide {tag}")
        self.lines.append(f"    show {img} at {pos}"); self.shown[tag]=(img,pos)
    def label(self,name,desc=""):
        if self.lines and self.lines[-1].strip()!="": self.lines.append("")
        if desc: self.lines.append(f"# {desc}")
        self.lines.append(f"label {name}:")

def emit_row(g, r):
    num,typ,role,text,bg,spr,expr=r["num"],r["typ"],r["role"],r["text"],r["bg"],r["spr"],r["expr"]
    if typ=="标签":
        g.lines.append(f"    # {text}" if text else "    # 标签"); return
    if typ=="场景标记":
        if bg and bg not in ("待确认","待定"): g.scene(bg)
        return
    if typ=="交互节点":
        g.lines.append(f"    # 交互节点：{text}"); return
    if is_noise(text, role):
        g.lines.append(f"    # 编辑备注（#{num}）：{text or role}"); return
    if not text and role in ("背景","图层","排版参考","对应背景","仅背景，无立绘","设计说明"): return
    if role=="背景" and text: g.scene(text); return
    if bg and bg not in ("待确认","待定"): g.scene(bg)
    if typ=="旁白" and re.match(r"^【(非遗|历史)·", text):
        m=re.match(r"^【(非遗|历史)·([^】]+)】\s*(.*)$", text); cat,title,content=m.group(1),m.group(2),m.group(3)
        g.lines.append(f'    call screen culture_note("{title}", """{escape(content)}""", "{cat}", "history_contract_labor")')
        return
    if "【这个字号变成红色加粗】" in text:
        text=text.replace("【这个字号变成红色加粗】","")
        g.lines.append(f'    narrator "{{color=#ff0000}}{{b}}{escape(text)}{{/b}}{{/color}}"'); return
    xin = role=="陈九心声"
    if typ=="对白":
        base=re.match(r"^(.*?)（([^）]*)）$", role)
        paren=""; bname=role
        if base and base.group(1) in ROLE_MAP: bname,paren=base.group(1),base.group(2)
        who=ROLE_MAP.get(bname)
        if who:
            body=text
            if xin: body=f"（心声）{body}"
            elif paren: body=f"（{paren}）{body}"
            g.lines.append(f'    {who} "{escape(body)}"')
        else:
            if text: g.lines.append(f'    # TODO(未知角色 #{num})：{role}'); g.lines.append(f'    narrator "{escape(text)}"')
        sp=spr if spr not in ("背景","仅背景，无立绘","待确认","图层","排版参考","对应背景","") else bname
        g.show_sprite(sp, expr)
        return
    if typ=="旁白":
        m=re.match(r"^(陈九|陈万田|王氏|黄三爷|九指仙|老水客)（([^）]*)）?[：:](.*)$", text)
        if m:
            g.lines.append(f'    {ROLE_MAP[m.group(1)]} "（{m.group(2)}）{escape(m.group(3))}"'); g.show_sprite(m.group(1), expr); return
        m2=re.match(r"^(陈九|陈万田|王氏|黄三爷|九指仙|老水客)[：:](.*)$", text)
        if m2:
            g.lines.append(f'    {ROLE_MAP[m2.group(1)]} "{escape(m2.group(2))}"'); g.show_sprite(m2.group(1), expr); return
        g.lines.append(f'    narrator "{escape(text)}"')
        if spr and expr: g.show_sprite(spr, expr)
        return

def main():
    wb=openpyxl.load_workbook(XLSX, data_only=True); ws=wb["RenPy剧本"]
    rows=[]
    for row in ws.iter_rows(min_row=2, values_only=True):
        vals=(list(row)+[""]*7)[:7]
        rows.append(dict(num=("" if vals[0] is None else str(vals[0]).strip()), typ=("" if vals[1] is None else str(vals[1]).strip()), role=("" if vals[2] is None else str(vals[2]).strip()), text=("" if vals[3] is None else str(vals[3]).strip()), bg=("" if vals[4] is None else str(vals[4]).strip()), spr=("" if vals[5] is None else str(vals[5]).strip()), expr=("" if vals[6] is None else str(vals[6]).strip())))
    i_line1=None
    for i,r in enumerate(rows):
        if "第三部分" in r["role"]:
            i_line1=i+1; break
    if i_line1 is None: raise SystemExit("line1 marker not found")
    # 定位关键交互
    def find_from(s,pred):
        for k in range(s,len(rows)):
            if pred(rows[k]): return k
        return None
    i_contract=find_from(i_line1, lambda r: r["typ"]=="交互节点" and "危局" in r["text"])
    opt_a=find_from(i_contract+1, lambda r: r["text"].startswith("A｜")) if i_contract is not None else None
    opt_b=find_from(i_contract+1, lambda r: r["text"].startswith("B｜")) if i_contract is not None else None
    opt_c=find_from(i_contract+1, lambda r: r["text"].startswith("C｜")) if i_contract is not None else None
    i_final=None
    if opt_c is not None:
        for k in range(opt_c+1,len(rows)):
            if rows[k]["typ"]=="交互节点" and rows[k]["text"].strip()=="【玩家选择】": i_final=k; break
    i_gameover=find_from(i_final+1, lambda r: r["typ"]=="标签" and "GAME OVER" in r["text"]) if i_final is not None else None
    i_merge=find_from((i_gameover+1 if i_gameover is not None else i_final+1), lambda r: r["typ"]=="标签" and "汇合" in r["text"]) if i_final is not None else None

    g=Gen()
    g.lines.append("# 本文件由 tools/excel_to_renpy.py 从 demo.xlsx 自动生成（line1 段），请勿手工修改剧情文本。")
    g.lines.append("# 重新生成：python3 tools/excel_to_renpy.py")
    g.lines.append("# 入口：prologue 通过  jump line1_start  进入本文件。")
    g.lines.append("")
    g.label("line1_start","第三部分 · 线一 · 橡胶逆袭")
    # line1_start 前的铺垫（叩门前）
    k=i_line1
    while k < (i_contract if i_contract is not None else len(rows)):
        # 叩门处的无选项玩家选择，跳过交互标记直接推进
        if rows[k]["typ"]=="交互节点" and "【玩家选择】" in rows[k]["text"] and (i_contract is None or k < i_contract-10):
            g.lines.append("    # TODO: confirm branch —— 叩门前的玩家选择（Excel 未给出选项），按剧情顺序推进")
            k+=1; continue
        emit_row(g, rows[k]); k+=1
    # 危局三选一
    if i_contract is not None and opt_a is not None:
        g.lines.append("")
        g.lines.append("    # 交互 · 危局：这张契纸，怎么办？")
        g.lines.append("    menu:")
        g.lines.append(f'        "{escape(rows[opt_a]["text"])}":')
        g.lines.append("            jump line1_contract_a")
        g.lines.append(f'        "{escape(rows[opt_b]["text"])}":')
        g.lines.append("            jump line1_contract_b")
        g.lines.append(f'        "{escape(rows[opt_c]["text"])}":')
        g.lines.append("            jump line1_contract_c")
        # A
        g.label("line1_contract_a"); k=opt_a+1
        while k < opt_b:
            emit_row(g, rows[k]); k+=1
        g.lines.append("    jump line1_final_choice")
        # B
        g.label("line1_contract_b"); k=opt_b+1
        while k < opt_c:
            emit_row(g, rows[k]); k+=1
        g.lines.append("    jump line1_final_choice")
        # C
        g.label("line1_contract_c"); k=opt_c+1
        while k < i_final:
            emit_row(g, rows[k]); k+=1
        g.lines.append("    jump line1_final_choice")
        # 最终分岔
        g.label("line1_final_choice","最终选择：生死分岔")
        g.lines.append("    menu:")
        g.lines.append('        "A（死亡结局）":')
        g.lines.append("            jump line1_death")
        g.lines.append('        "B（主线汇合）":')
        g.lines.append("            jump line1_merge")
        # death（共享对峙 + GAME OVER）
        g.label("line1_death","共享对峙 -> GAME OVER"); k=i_final+1
        while k < (i_gameover if i_gameover is not None else len(rows)):
            emit_row(g, rows[k]); k+=1
        if i_gameover is not None:
            g.lines.append(f"    # {rows[i_gameover]['text']}")
            k=i_gameover+1
            while k < (i_merge if i_merge is not None else len(rows)):
                emit_row(g, rows[k]); k+=1
        g.lines.append("    return")
        # merge
        g.label("line1_merge","选项A/B/C-B 主线汇合")
        if i_merge is not None:
            g.lines.append(f"    # {rows[i_merge]['text']}")
            k=i_merge+1
            while k < len(rows):
                emit_row(g, rows[k]); k+=1
        g.lines.append("    return")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_RPY.write_text("\n".join(g.lines)+"\n", encoding="utf-8")
    with MISSING.open("w", encoding="utf-8") as f:
        f.write("缺失背景：\n")
        for b in sorted(g.missing_bg): f.write(f"- {b}\n")
        f.write("\n缺失人物立绘/表情：\n")
        for s_,e in sorted(g.missing_sprite): f.write(f"- {s_} / {e}\n")
    # 清理旧的 excel_demo 残留
    old=ROOT/"game"/"story"/"excel_demo"
    if old.exists():
        import shutil; shutil.rmtree(old)
        print(f"removed old {old}")
    print(f"rows line1: {len(rows)-i_line1}, output: {OUT_RPY}, missing bg: {len(g.missing_bg)}, missing sprite: {len(g.missing_sprite)}")

if __name__=="__main__":
    main()
