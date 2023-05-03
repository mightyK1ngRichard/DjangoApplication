from django.db import models

INFO = [
    {
        'id': f'{i}',
        'title': f'Title {i}',
        'text': f'text {i}'
    } for i in range(10)
]
