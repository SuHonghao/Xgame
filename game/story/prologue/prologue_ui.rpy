default bobing_choice = None
default bobing_echo = None

init python:
    def prologue_asset(path, fallback="images/background/2.png"):
        if renpy.loadable(path):
            return path
        return fallback

    def prologue_bg(path, fallback="images/background/2.png"):
        if not renpy.loadable(path):
            path = fallback
        return Transform(path, fit="cover", xysize=(config.screen_width, config.screen_height))

    def prologue_sprite(path, fallback="images/character/chenjiu/chenjiu_normal.png"):
        if not renpy.loadable(path):
            path = fallback
        return Transform(path, ysize=config.screen_height, yalign=1.0)

    def prologue_play_audio(path, channel="sound", loop=False, fadein=0.0):
        if renpy.loadable(path):
            renpy.music.play(path, channel=channel, loop=loop, fadein=fadein)

    def unlock_collection_item(item_id):
        if item_id and item_id not in persistent.unlocked_objects:
            persistent.unlocked_objects.append(item_id)
            renpy.save_persistent()

screen culture_note(title, content, category="非遗", collection_id=None):
    modal True
    zorder 200

    on "show" action Function(unlock_collection_item, collection_id)

    add Solid("#130e0acc")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 960
        padding (56, 44)
        background Solid("#f4ead8f5")

        vbox:
            xfill True
            spacing 24

            text "【[category] · [title]】":
                xalign 0.5
                size 38
                color "#9b3e25"
                font "wordtype/shanhaishengtangbangshuw.ttf"

            text content:
                size 27
                color "#493e38"
                line_spacing 10
                text_align 0.0

            textbutton "返回":
                xalign 0.5
                action Return()

    key "game_menu" action Return()

screen bobing_rules():
    modal True
    zorder 210

    add Solid("#130e0add")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1040
        ysize 650
        padding (50, 36)
        background Solid("#f4ead8fa")

        vbox:
            xfill True
            spacing 18

            text "中秋博饼":
                xalign 0.5
                size 42
                color "#9b3e25"
                font "wordtype/shanhaishengtangbangshuw.ttf"

            viewport:
                xfill True
                ysize 390
                mousewheel True
                draggable True
                scrollbars "vertical"

                vbox:
                    xfill True
                    spacing 8

                    text "{color=#000000}{b}状元插金花：{/b}4个四 + 2个一{/color}" xalign 0.5 text_align 0.5
                    text "{color=#000000}{b}六博红：{/b}6个四{/color}" xalign 0.5 text_align 0.5
                    text "{color=#000000}{b}遍地锦：{/b}6个一{/color}" xalign 0.5 text_align 0.5
                    text "{color=#000000}{b}五红：{/b}5个四{/color}" xalign 0.5 text_align 0.5
                    text "{color=#000000}{b}五子带一秀：{/b}5个同点 + 1个四{/color}" xalign 0.5 text_align 0.5
                    text "{color=#000000}{b}四点红：{/b}4个四{/color}" xalign 0.5 text_align 0.5
                    text "{color=#000000}{b}六博黑：{/b}二、三、五、六某一点六骰相同{/color}" xalign 0.5 text_align 0.5
                    text "{color=#000000}{b}对堂：{/b}1、2、3、4、5、6{/color}" xalign 0.5 text_align 0.5
                    text "{color=#000000}{b}三红：{/b}3个四{/color}" xalign 0.5 text_align 0.5
                    text "{color=#000000}{b}四进带二举{/b}{/color}" xalign 0.5 text_align 0.5
                    text "{color=#000000}{b}四进带一秀{/b}{/color}" xalign 0.5 text_align 0.5
                    text "{color=#000000}{b}四进{/b}{/color}" xalign 0.5 text_align 0.5
                    text "{color=#000000}{b}二举：{/b}2个四{/color}" xalign 0.5 text_align 0.5
                    text "{color=#000000}{b}一秀：{/b}1个四{/color}" xalign 0.5 text_align 0.5
                    text "{color=#000000}{b}罚黑：{/b}其余结果{/color}" xalign 0.5 text_align 0.5

            textbutton "查看百度百科：中秋节（中秋博饼）":
                xalign 0.5
                action OpenURL("https://baike.baidu.com/item/%E4%B8%AD%E7%A7%8B%E8%8A%82%EF%BC%88%E4%B8%AD%E7%A7%8B%E5%8D%9A%E9%A5%BC%EF%BC%89/49930019")

            textbutton "返回":
                xalign 0.5
                action Return()

    key "game_menu" action Return()

screen bobing_roll(result, award):
    modal True
    zorder 205
    default phase = 0

    add Solid("#2a1006dd")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1100
        ysize 620
        padding (48, 38)
        background Solid("#5c1f16f2")

        vbox:
            xalign 0.5
            spacing 36

            text "六颗骰子落进大红瓷碗":
                xalign 0.5
                size 35
                color "#f8e7bf"
                font "wordtype/shanhaishengtangbangshuw.ttf"

            fixed:
                xalign 0.5
                xsize 820
                ysize 280

                if renpy.loadable("images/background/red_bowl.png"):
                    add "images/background/red_bowl.png":
                        xsize 820
                        ysize 280
                        fit "cover"
                else:
                    add Solid("#8f1f18")

                hbox:
                    align (0.5, 0.58)
                    spacing 18

                    for i in range(6):
                        $ shown_value = result[i] if phase >= 8 else ((phase + i * 2) % 6) + 1
                        $ die_path = "images/background/dice_%d.png" % shown_value
                        if renpy.loadable(die_path):
                            add die_path:
                                xsize 100
                                ysize 100
                                fit "contain"
                        else:
                            frame:
                                xsize 100
                                ysize 100
                                background Solid("#fff9e8")
                                text "[shown_value]":
                                    align (0.5, 0.5)
                                    size 52
                                    color "#b3231e"

            if phase >= 8:
                text " · ".join(["一", "二", "三", "四", "五", "六"][n - 1] for n in result):
                    xalign 0.5
                    size 32
                    color "#fff3d6"
                text "[award]！":
                    xalign 0.5
                    size 48
                    color "#f2c14e"
                    font "wordtype/shanhaishengtangbangshuw.ttf"

    if phase < 8:
        timer 0.10 action SetScreenVariable("phase", phase + 1) repeat True
    else:
        timer 1.7 action Return()

transform prologue_memory_overlay:
    alpha 0.0
    linear 1.2 alpha 1.0

transform prologue_flash:
    alpha 0.0
    linear 0.12 alpha 0.85
    linear 0.45 alpha 0.0
