"""所有背景图片再此定义"""

init python:
    def bg(path, fallback="images/background/2.png"):
        if not renpy.loadable(path):
            path = fallback
        return Transform(path, fit="cover", xysize=(config.screen_width, config.screen_height))

image bg prologue_action1 = bg("images/background/2.png")
