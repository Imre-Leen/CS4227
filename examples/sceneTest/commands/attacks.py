from src.entities.damage_factory import DamageFactory

class Attacks():
    def __init__(self):
        self.damage_factory = DamageFactory()
        self.damageTile = self.damage_factory.create_damage("melee")

    def short_range_attack(self, entity):
        if entity.phase == 1:
            self.damageTile.x_pos = entity.x_pos + 8
            self.damageTile.y_pos = entity.y_pos
            return self.damageTile

        elif entity.phase == 2:
            self.damageTile.x_pos = entity.x_pos
            self.damageTile.y_pos = entity.y_pos - 8

        elif entity.phase == 3:
            self.damageTile.x_pos = entity.x_pos - 8
            self.damageTile.y_pos = entity.y_pos

        elif entity.phase == 4:
            self.damageTile.x_pos = entity.x_pos
            self.damageTile.y_pos = entity.y_pos + 8

        else:
            entity.attacking = False
            return self.damageTile
