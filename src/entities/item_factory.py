from src.entities.entity_factory import EntityFactory
from src.entities.item_tile import ItemTile

class ItemFactory(EntityFactory):
    def __init__(self):
        super(EntityFactory, self).__init__()

    def create_item(self, item_type):

        if item_type == "health":
            return ItemTile(1.0, 1.0, 1.0, 0.5, 255, 4, 4)
        elif item_type == "gold":
            return ItemTile(0.7, 0.7, 0.0, 240, 280, 4, 3)
        elif item_type == "stairs":
            return ItemTile(0.5, 0.2, 0.2, 240, 280, 5, 5)
        else:
            return None
