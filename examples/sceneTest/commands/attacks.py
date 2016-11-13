from src.entities.damage_factory import DamageFactory

class Attacks():
    def __init__(self):
        self.damage_factory = DamageFactory()
        self.damageTile = self.damage_factory.create_damage("melee")

    def short_range_attack(self, entity):
        if self.damageTile.phase == 1:
            self.damageTile.x_pos = entity.x_pos + entity.width / 2 + 8
            self.damageTile.y_pos = entity.y_pos + entity.height / 2
            return self.damageTile

        elif self.damageTile.phase == 2:
            self.damageTile.x_pos = entity.x_pos + entity.width / 2
            self.damageTile.y_pos = entity.y_pos + entity.height / 2 - 8

        elif self.damageTile.phase == 3:
            self.damageTile.x_pos = entity.x_pos + entity.width / 2 - 8
            self.damageTile.y_pos = entity.y_pos + entity.height / 2

        elif self.damageTile.phase == 4:
            self.damageTile.x_pos = entity.x_pos + entity.width / 2
            self.damageTile.y_pos = entity.y_pos + entity.height / 2 + 8

        else:
            entity.attacking = False
            self.damageTile.phase = 0