screen line1_danger_warning(title, message="这个选择可能导致死亡。建议现在保存游戏。"):
    modal True
    zorder 220

    add Solid("#090706dd")

    frame:
        align (0.5, 0.5)
        xsize 860
        padding (52, 42)
        background Solid("#3b1714f5")

        vbox:
            xfill True
            spacing 26

            text "【[title]】":
                xalign 0.5
                text_align 0.5
                size 40
                color "#e7b45d"
                font "wordtype/shanhaishengtangbangshuw.ttf"

            text "系统提示：\n[message]":
                xalign 0.5
                text_align 0.5
                size 27
                color "#f5e8d0"
                line_spacing 9

            hbox:
                xalign 0.5
                spacing 35

                textbutton "打开保存界面" action ShowMenu("save")
                textbutton "继续选择" action Return()

    key "game_menu" action Return()

screen line1_game_over(ending_name, ending_type="GAME OVER", description="请读取存档后重试。"):
    modal True
    zorder 230

    add Solid("#000000f2")

    frame:
        align (0.5, 0.5)
        xsize 920
        padding (58, 48)
        background Solid("#24100ef5")

        vbox:
            xfill True
            spacing 28

            text ending_type:
                xalign 0.5
                size 32
                color "#a53b32"

            text ending_name:
                xalign 0.5
                text_align 0.5
                size 48
                color "#e7b45d"
                font "wordtype/shanhaishengtangbangshuw.ttf"

            text description:
                xalign 0.5
                text_align 0.5
                size 27
                color "#f5e8d0"
                line_spacing 9

            hbox:
                xalign 0.5
                spacing 42

                textbutton "读取存档" action ShowMenu("load")
                textbutton "返回主菜单" action [Hide("line1_game_over"), MainMenu(confirm=False)]

    key "game_menu" action NullAction()
