define jiuzhixian = Character("九指仙")
define old_shuike = Character("老水客")
define crowd = Character("众人")

define prologue_slow_dissolve = Dissolve(1.5)
define prologue_memory_dissolve = Dissolve(2.0)


label splashscreen:

    call screen intro_cover

    return


label start:

    window hide
    $ quick_menu = False

    scene black with fade

    $ renpy.movie_cutscene("video/game_intro.webm")

    scene black

    jump prologue


label prologue:

    window hide
    $ quick_menu = False
    $ bobing_choice = None
    $ bobing_echo = None

    call prologue_mansion
    call prologue_gambling_house
    call prologue_harbor
    call prologue_return_home
    jump prologue_first_choice
