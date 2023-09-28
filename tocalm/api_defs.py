import logging
from typing import List

from ninja import NinjaAPI

from tocalm.models import Item
from tocalm.schemas import ItemSchema

api = NinjaAPI()


@api.post('/items', description='Add a new item')
def add(request, data: ItemSchema):
    new_item = data.dict()
    if request.user.is_authenticated:
        new_item['user_id'] = request.user.id
    new_item = Item.objects.create(**new_item)
    logging.info(new_item)
    return {'id': new_item.id}


@api.get('/items', response=List[ItemSchema])
def get(request):
    user_id = None
    if request.user.is_authenticated:
        user_id = request.user.id
    items = Item.objects.filter(user_id=user_id)
    return list(items)

