# 电影式旁白
label cinematic_narration(text, duration=3.0):

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
    ) as opening_narration at truecenter
    with Dissolve(1.0)

    pause duration

    hide opening_narration
    with Dissolve(1.0)

    pause 0.5
    return
