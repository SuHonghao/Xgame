"""所有人物的表情和对应图片再此定义"""

init python:
    #半身全身人像
    def sprite(path, zoom=0.85):
        if renpy.loadable(path):
            return Transform(path, zoom=zoom, yalign=1.0)
        return path
    #人头像
    def head(path, width=None, height=None):
        if not renpy.loadable(path):
            return path
        if width is not None:
            return Transform(path, xsize=width, yalign=1.0)
        if height is not None:
            return Transform(path, ysize=height, yalign=1.0)
        return path

#chenjiu
define chenjiu = Character("陈九")
image chenjiu normal = sprite("images/character/chenjiu/chenjiu_normal.png")
image chenjiu embarrassed = sprite("images/character/chenjiu/chenjiu_embarrassed.png")
image chenjiu head redface = head("images/character/chenjiu/chenjiu_head_redface.png")

#mother
define mother = Character("母亲 · 王氏")
image mother normal = sprite("images/character/mother_wangshi/mother_wangshi_normal.png")


#father
define father = Character("父亲 · 陈万田")
image father normal = sprite("images/character/father_chenwantian/father_chenwantian_normal.png")


# supporting characters used in the prologue
image jiuzhixian normal = sprite("images/character/jiuzhixian/jiuzhixian_normal.png")
image old_shuike normal = sprite("images/character/old_shuike/old_shuike_normal.png")

