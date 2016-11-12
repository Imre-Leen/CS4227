from src.entities.damage_factory import DamageFactory

class Attacks():
    def __init__(self):
        self.damage_factory = DamageFactory()

    def short_range_attack(self, entity):
        if entity.phase == 1:
            self.damageTile = self.damage_factory.create_damage("melee")
            self.damageTile.x_pos = entity.x_pos + entity.width / 2 + 8
            self.damageTile.y_pos = entity.y_pos + entity.height / 2
            return self.damageTile

        elif entity.phase == 2:
            self.damageTile.x_pos = entity.x_pos + entity.width / 2
            self.damageTile.y_pos = entity.y_pos + entity.height / 2 - 8

        elif entity.phase == 3:
            self.damageTile.x_pos = entity.x_pos + entity.width / 2 - 8
            self.damageTile.y_pos = entity.y_pos + entity.height / 2

        elif entity.phase == 4:
            self.damageTile.x_pos = entity.x_pos + entity.width / 2
            self.damageTile.y_pos = entity.y_pos + entity.height / 2 + 8

        else:
            entity.attacking = False
            entity.phase = 0
            return self.damageTile
