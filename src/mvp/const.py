import json

sentword2opinion = {'긍정적': '긍정적', '부정적': '부정적', '중립적': '중립적'}

rest_aspect_cate_list = ['위치 일반', '음식 가격', '음식 품질', '음식 일반','분위기 일반',
                         '서비스 일반', '식당 가격', '음료 가격', '식당 기타', '음료 품질',
                         '음료 옵션', '식당 일반', '음식 옵션'
                        ]

# with open("force_tokens.json", 'r') as f:
#     force_tokens = json.load(f)

cate_list = {
    "rest": rest_aspect_cate_list,
    "rest15": rest_aspect_cate_list,
    "rest16": rest_aspect_cate_list,
}

task_data_list = {
    "acos": ["rest16"],
    "asqp": ['rest15', "rest16"],
}
force_words = {
    'acos': {
        "rest": rest_aspect_cate_list + list(sentword2opinion.values()) + ['[SSEP]'],
    },
    'asqp': {
        "rest15": rest_aspect_cate_list + list(sentword2opinion.values()) + ['[SSEP]'],
        "rest16": rest_aspect_cate_list + list(sentword2opinion.values()) + ['[SSEP]'],
    }
}


optim_orders_all = {
            "aste": {
                "laptop14": [
                    '[O] [A] [S]', '[A] [O] [S]', '[O] [S] [A]',
                    '[A] [S] [O]', '[S] [O] [A]', '[S] [A] [O]'
                ],
                "rest14": [
                    '[O] [A] [S]', '[O] [S] [A]', '[A] [O] [S]',
                    '[A] [S] [O]', '[S] [O] [A]', '[S] [A] [O]'
                ],
                "rest15": [
                    '[A] [O] [S]', '[O] [A] [S]', '[O] [S] [A]',
                    '[A] [S] [O]', '[S] [O] [A]', '[S] [A] [O]'
                ],
                "rest16": [
                    '[O] [A] [S]', '[A] [O] [S]', '[O] [S] [A]',
                    '[A] [S] [O]', '[S] [O] [A]', '[S] [A] [O]'
                ],
            },
            "tasd": {
                "rest15": [
                    '[A] [C] [S]', '[A] [S] [C]', '[C] [S] [A]',
                    '[C] [A] [S]', '[S] [C] [A]', '[S] [A] [C]'
                ],
                "rest16": [
                    '[A] [C] [S]', '[A] [S] [C]', '[C] [S] [A]',
                    '[C] [A] [S]', '[S] [C] [A]', '[S] [A] [C]'
                ]
            },
            "acos": {
                "laptop16": [  # ot null -> sp
                    '[A] [O] [S] [C]', '[A] [S] [O] [C]',
                    '[A] [O] [C] [S]', '[O] [A] [S] [C]',
                    '[O] [A] [C] [S]', '[A] [S] [C] [O]',
                    '[A] [C] [O] [S]', '[O] [C] [A] [S]',
                    '[O] [S] [A] [C]', '[A] [C] [S] [O]',
                    '[O] [C] [S] [A]', '[O] [S] [C] [A]',
                    '[S] [A] [O] [C]', '[C] [O] [A] [S]',
                    '[C] [S] [A] [O]', '[C] [A] [O] [S]',
                    '[C] [S] [O] [A]', '[C] [O] [S] [A]',
                    '[S] [O] [A] [C]', '[C] [A] [S] [O]',
                    '[S] [O] [C] [A]', '[S] [C] [O] [A]',
                    '[S] [A] [C] [O]', '[S] [C] [A] [O]'
                ],
                "rest16": [  # ot null -> sp
                    '[A] [O] [S] [C]', '[A] [O] [C] [S]',
                    '[A] [S] [O] [C]', '[O] [A] [C] [S]',
                    '[O] [A] [S] [C]', '[O] [S] [C] [A]',
                    '[A] [C] [O] [S]', '[O] [C] [A] [S]',
                    '[O] [S] [A] [C]', '[A] [S] [C] [O]',
                    '[A] [C] [S] [O]', '[O] [C] [S] [A]',
                    '[C] [O] [A] [S]', '[C] [A] [O] [S]',
                    '[C] [S] [O] [A]', '[C] [O] [S] [A]',
                    '[S] [A] [O] [C]', '[C] [S] [A] [O]',
                    '[C] [A] [S] [O]', '[S] [O] [A] [C]',
                    '[S] [C] [O] [A]', '[S] [O] [C] [A]',
                    '[S] [C] [A] [O]', '[S] [A] [C] [O]'
                ],
            },
            "asqp": {
                "rest15": [
                    '[A] [O] [S] [C]', '[O] [A] [C] [S]',
                    '[A] [O] [C] [S]', '[O] [A] [S] [C]',
                    '[O] [S] [C] [A]', '[A] [S] [O] [C]',
                    '[O] [C] [A] [S]', '[O] [S] [A] [C]',
                    '[A] [C] [O] [S]', '[O] [C] [S] [A]',
                    '[A] [C] [S] [O]', '[C] [O] [A] [S]',
                    '[A] [S] [C] [O]', '[C] [A] [O] [S]',
                    '[C] [S] [O] [A]', '[C] [O] [S] [A]',
                    '[C] [S] [A] [O]', '[C] [A] [S] [O]',
                    '[S] [A] [O] [C]', '[S] [O] [A] [C]',
                    '[S] [C] [O] [A]', '[S] [O] [C] [A]',
                    '[S] [C] [A] [O]', '[S] [A] [C] [O]'
                ],
                "rest16": [
                    '[O] [A] [C] [S]', '[A] [O] [S] [C]',
                    '[O] [A] [S] [C]', '[O] [S] [C] [A]',
                    '[A] [O] [C] [S]', '[O] [S] [A] [C]',
                    '[O] [C] [A] [S]', '[A] [S] [O] [C]',
                    '[O] [C] [S] [A]', '[A] [C] [O] [S]',
                    '[A] [C] [S] [O]', '[C] [O] [A] [S]',
                    '[A] [S] [C] [O]', '[C] [A] [O] [S]',
                    '[C] [O] [S] [A]', '[C] [S] [O] [A]',
                    '[C] [S] [A] [O]', '[S] [A] [O] [C]',
                    '[C] [A] [S] [O]', '[S] [O] [A] [C]',
                    '[S] [O] [C] [A]', '[S] [C] [O] [A]',
                    '[S] [C] [A] [O]', '[S] [A] [C] [O]'
                ],
            },
        }


heuristic_orders = {
    'aste': ['[A] [O] [S]'],
    'tasd': ['[A] [C] [S]'],
    'asqp': ['[A] [O] [C] [S]'],
    'acos': ['[A] [O] [C] [S]'],
}