# 复用标准对话框的旁白
label cinematic_narration(text, duration=3.0):

    $ _old_quick_menu = quick_menu
    $ quick_menu = True
    window show
    "[text]"
    $ quick_menu = _old_quick_menu
    return


# 保留的电影式中央旁白，需要时可单独调用。
label fullscreen_cinematic_narration(text, duration=3.0):

    window hide

    show expression Text(
        text,
        font="wordtype/shanhaishengtangbangshuw.ttf",
        size=42,
        color="#FFFFFF",
        text_align=0.5,
        xalign=0.5,
        xmaximum=960,
        layout="subtitle",
        outlines=[(2, "#000000", 0, 0)]
    ) as fullscreen_narration at truecenter
    with Dissolve(1.0)

    pause duration

    hide fullscreen_narration
    with Dissolve(1.0)

    pause 0.5
    return
