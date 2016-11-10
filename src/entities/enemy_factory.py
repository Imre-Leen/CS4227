from src.entities.entity_factory import EntityFactory
from src.entities.enemy_tile import EnemyTile
from src.entities.damage_tile import DamageTile

class EnemyFactory(EntityFactory):
    def __init__(self):
        super(EntityFactory, self).__init__()

    def create_enemy(self, enemy_type):

        if enemy_type == "normal":
            return EnemyTile(1.0, 0.0, 0.5, 380, 350, 7, 7)
        elif enemy_type == "boss":
            return EnemyTile(1.0, 0.0, 3.0, 380, 350, 10, 10)
        else:
            return None
