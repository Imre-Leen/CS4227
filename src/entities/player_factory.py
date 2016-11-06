from src.entities.entity_factory import EntityFactory
from src.entities.player_tile import PlayerTile

class PlayerFactory(EntityFactory):
    def __init__(self):
        super(EntityFactory, self).__init__()

    def create_player(self):
        player = PlayerTile(1.0, 1.0, 0.0, 30, 50, 5, 5)
        return player