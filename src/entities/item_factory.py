from src.entities.entity_factory import EntityFactory
from src.entities.item_tile import ItemTile

class ItemFactory(EntityFactory):
    def __init__(self):
        super(EntityFactory, self).__init__()

    def create_item(self, item_type):

        if item_type == "health":
            return ItemTile(1.0, 0.0, 0.5, 0.5, 255, 0, 0)
        elif item_type == "gold":
            return ItemTile(1.0, 0.0, 0.5, 0.5, 218, 165, 32)
        else:
            return None