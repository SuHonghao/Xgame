"""这里定义所有的图鉴物品"""

default persistent.unlocked_objects = []


init python:
    collection_items = [
        {
            "id": "object1",
            "name": "神秘物件一",
            "image": "images/catalog/object/object.png",
            "description": "这是陈九在故事中见到的物件。它的来历与用途，还有待进一步探寻。",
        },
        {
            "id": "object2",
            "name": "神秘物件二",
            "image": "images/catalog/object/object2.png",
            "description": "陈九后来发现的另一件物品，其中似乎隐藏着不为人知的故事。",
        },




    ]
