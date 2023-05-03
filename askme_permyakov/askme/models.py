from django.db import models

INFO = [
    {
        'id': f'{i}',
        'logo': '',
        'title': f'Title {i}',
        'text': f'text {i}',
        'count_response': f'{i * 10}',
        'tags': [
            {
                'id_tag': f'{i2}',
                'name_tag': f'black_{i2}'
            } for i2 in range(i)
        ]
    } for i in range(10)
]
