from ninja import ModelSchema

from tocalm.models import Item


class ItemSchema(ModelSchema):
    class Config:
        model = Item
        model_fields = ['task', 'impact', 'done']
        model_fields_optional = ['impact', 'done']
