define e = Character("艾琳")


label splashscreen:


    call screen intro_cover


    return





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


label start:

    window hide
    $ quick_menu = False

    scene black with fade

    $ renpy.movie_cutscene("video/game_intro.webm")

    scene black

    call cinematic_narration("这是一个关于选择与命运的故事。")
    call cinematic_narration("每一次选择，都会让未来走向不同的方向。")
    call cinematic_narration("而你的故事，将从此刻开始。而你的故事，将从此刻开始。而你的故事，将从此刻开始。而你的故事，将从此刻开始。而你的故事，将从此刻开始。而你的故事，将从此刻开始。而你的故事，将从此刻开始。而你的故事，将从此刻开始。而你的故事，将从此刻开始。而你的故事，将从此刻开始。而你的故事，将从此刻开始。而你的故事，将从此刻开始。而你的故事，将从此刻开始。而你的故事，将从此刻开始。")


    scene bg room with fade
    show eileen happy

    $ quick_menu = True

    e "您已创建一个新的 Ren'Py 游戏。"

    e "当您完善了故事、图片和音乐之后，您就可以向全世界发布了！"

    return