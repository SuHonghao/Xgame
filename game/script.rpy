define e = Character("艾琳")


label splashscreen:


    call screen intro_cover


    return





label start:


    window hide


    $ quick_menu = False


    scene black with fade


    $ renpy.movie_cutscene("video/game_intro.webm")


    $ quick_menu = True


    scene bg room with fade


    show eileen happy


    e "您已创建一个新的 Ren'Py 游戏。"


    e "当您完善了故事、图片和音乐之后，您就可以向全世界发布了！"


    return