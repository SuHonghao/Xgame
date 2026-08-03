define chenjiu = Character("陈九")
define mother = Character("阿母")

default persistent.unlocked_objects = []


#这里定义所有的图鉴物品
init python:
    collection_items = [
        {
            "id": "object1",
            "name": "神秘物件一",
            "image": "images/object/object.png",
            "description": "这是陈九在故事中见到的物件。它的来历与用途，还有待进一步探寻。",
        },
        {
            "id": "object2",
            "name": "神秘物件二",
            "image": "images/object/object2.png",
            "description": "陈九后来发现的另一件物品，其中似乎隐藏着不为人知的故事。",
        },
    ]


image mother normal = "images/Mother/mother_normal.png"
image chenjiu normal = "images/ChenJiu/chenjiu_normal.png"
image bg part2_act1 = "images/background/2.png"


label splashscreen:

    call screen intro_cover

    return


# 旁白设计
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


    call Part2_Act1


    return


label Part2_Act1:

    play music "audio/test.mp3" loop

    call cinematic_narration('同安陈家，祖上在这西溪畔也算数得着。陈万田老太爷年轻时勤俭持家，攒下百亩薄田、一间米铺')
    call cinematic_narration('可到了光绪年间，家道早已没落——田亩典卖过半，米铺易了主，大厝还在，底气却空了')
    call cinematic_narration('再加九子分家，犹如一锅粥舀进九只碗，舀到了老九陈九这里，只剩下"九少爷"这个空名头')
    call cinematic_narration('九少爷今年十六，生得眉清目秀，念过几年私塾，一手算盘打得噼啪响')
    call cinematic_narration('偏这聪明全用在了歪处——他好赌，常常一赌就彻夜不归。同安城里的赌场春风楼，是他的第二个家')
    call cinematic_narration('赢了笑，输了赖，家里的底子被他一点一点掏空，像白蚁蛀梁，外面看着还端正，实则里头早已烂成了糠心')
    call cinematic_narration('今日是九月初九，重阳。同安城里的赌场"春风楼"又开局了')

    stop music fadeout 1.0

    scene bg part2_act1 with fade
    $ quick_menu = True



    show mother normal with dissolve
    mother "九啊，又出去？"
    hide mother normal with dissolve

    show chenjiu normal with dissolve
    chenjiu "阿母，就去城里走走，会会朋友。"
    hide chenjiu normal with dissolve

    # 解锁图鉴物品1
    if "object1" not in persistent.unlocked_objects:
        $ persistent.unlocked_objects.append("object1")

    show mother normal with dissolve
    mother "你大哥前日才典了半亩田替你还了赌债，昨晚气得得咳了一宿。你还要往外跑？"
    hide mother normal with dissolve

    show chenjiu normal with dissolve
    chenjiu "阿母放心，今日就是去坐坐，和朋友走动走动，绝不碰赌桌，我发誓。"
    hide chenjiu normal with dissolve

    show mother normal with dissolve
    mother "你大哥前日才典了半亩田替你还了赌债，昨晚气得得咳了一宿。你还要往外跑？"
    mother '你每回都这么说'
    mother '这是阿母攒了半年的私房，三块大洋。原是......是留着给你娶媳妇的。'
    mother '前日你刚欠了债被赌场扣着，是你大哥去赎的。阿母晓得你面皮薄，怕你出门在外被人奚落、又偷偷赊账惹事。'
    mother '你拿去身上揣着，不是让你赌，是让你手头宽裕，莫再低头求人、重蹈覆辙。'
    hide mother normal with dissolve

    show chenjiu normal with dissolve
    chenjiu "阿母……我这回一定争气，好好做人，迟早把钱还给家里，好好孝顺您。"
    hide chenjiu normal with dissolve

    # 解锁图鉴物品2
    if "object2" not in persistent.unlocked_objects:
        $ persistent.unlocked_objects.append("object2")

    show mother normal with dissolve
    mother "阿母不要你还钱。阿母只要你安分守己，平平安安，别再让一家人替你担惊受怕、受人指点。"
    hide mother normal with dissolve

    return