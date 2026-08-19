"""这里定义所有的图鉴物品"""

default persistent.unlocked_objects = []

default catalog_placeholder_image = "images/catalog/object.png"


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
        {
            "id": "culture_minnan_house",
            "name": "闽南古厝",
            "image": "images/catalog/culture_minnan_house.png",
            "description": "陈家大厝为闽南传统“皇宫起”民居，燕尾脊、红砖墙、出砖入石；正厅供奉祖先与保生大帝，是闽南宗族社会的缩影。",
        },
        {
            "id": "culture_baosheng_dadi",
            "name": "保生大帝信俗",
            "image": "images/catalog/culture_baosheng_dadi.png",
            "description": "保生大帝本名吴夲，北宋同安白礁人，被闽南人奉为医神。同安家家供奉，出海前必祈平安。",
        },
        {
            "id": "history_yap_ah_loy",
            "name": "叶亚来",
            "image": "images/catalog/history_yap_ah_loy.png",
            "description": "马来西亚华商叶亚来（1837—1885），同安人。下南洋后成为吉隆坡华人甲必丹，为吉隆坡发展奠定基础。",
        },
        {
            "id": "history_indentured_labor",
            "name": "契约华工",
            "image": "images/catalog/history_indentured_labor.png",
            "description": "鸦片战争后，东南沿海出现契约华工贸易。华工常被欺骗签约，远赴海外从事长期苦役。",
        },
        {
            "id": "history_nanyang_voyage",
            "name": "下南洋惨状",
            "image": "images/catalog/history_nanyang_voyage.png",
            "description": "十九世纪中后期，大量闽南华工由厦门出海。船舱拥挤、缺水、疾病和风暴，使许多人未抵达目的地便死于海上。",
        },
        {
            "id": "history_malayan_rubber",
            "name": "马来亚橡胶",
            "image": "images/catalog/history_malayan_rubber.png",
            "description": "橡胶在十九世纪末于马来亚试种成功。华侨参与种植、制造和贸易，推动橡胶业成为当地重要产业。",
        },
        {
            "id": "history_opium_tokens",
            "name": "南洋种植园鸦片与猪仔币",
            "image": "images/catalog/history_opium_tokens.png",
            "description": "种植园常以可赊欠的鸦片与只能在园内流通的代币束缚华工，使劳工难以积蓄真实货币或离开园区。",
        },
    ]
