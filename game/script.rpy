define e = Character("艾琳")


transform fade_out:

    alpha 1.0
    linear 0.8 alpha 0.0


transform intro_video_fade:

    alpha 1.0
    pause 3.2
    linear 0.8 alpha 0.0


transform cover_to_video:

    alpha 1.0
    pause 0.15
    linear 0.35 alpha 0.0


transform intro_menu_fade:

    alpha 0.0
    linear 0.8 alpha 1.0


screen intro_cover():

    modal True


    default clicked = False


    if not clicked:


        # 封面覆盖视频
        add "images/cover.png"



        # 点击区域

        button:

            xfill True
            yfill True

            background None


            action SetScreenVariable(
                "clicked",
                True
            )



        # 点击提示

        add "images/click_to_enter.png":

            xalign 0.5
            yalign 0.82



    else:


        # 点击后才创建视频，确保每次都从第 0 秒开始播放。
        add Movie(
            play="video/background.webm",
            loop=False
        ) at intro_video_fade

        # 视频首帧解码期间继续盖住画面，再平滑淡出封面。
        add "images/cover.png" at cover_to_video


        add "images/click_to_enter.png":

            xalign 0.5
            yalign 0.82

            at fade_out



        timer 4 action Return()





label splashscreen:


    call screen intro_cover


    return





label start:


    scene bg room


    show eileen happy


    e "您已创建一个新的 Ren'Py 游戏。"


    e "当您完善了故事、图片和音乐之后，您就可以向全世界发布了！"


    return