label splashscreen:

    call screen intro_cover

    return


label start:

    window hide
    $ quick_menu = False

    scene black with fade

    $ renpy.movie_cutscene("video/game_intro.webm")

    scene black

    call Prologue_Action1

    return
