from src.entities.entity_factory import EntityFactory
from src.entities.damage_tile import DamageTile

class DamageFactory(EntityFactory):
    def __init__(self):
        super(EntityFactory, self).__init__()

    def create_damage(self, damage_type):

        if damage_type == "melee":
            return DamageTile(1.0, 0.0, 0.5, 380, 350, 3, 3, 2)
        elif damage_type == "fireball":
            return DamageTile(6.0, 0.0, 0.0, 380, 350, 3, 3, 5)
        else:
            return None
