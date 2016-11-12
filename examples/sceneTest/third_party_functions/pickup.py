class ThirdPartyPickup():
    def __init__(self):
        return

    def add_gold(self, player):
        player.gold += 10
        print "Player has " + str(player.gold) + " gold"

    def add_mega_gold(self, player):
        player.gold += 100
        print "Player has found mega gold! Now you have " + str(player.gold) + " gold!"

    def add_health(self, player):
        player.health += 2
        print "Player healed up to " + str(player.health) + " HP!"

    def minus_health(self, player):
        player.health -= 2
        print "Player found a death kit! You have taken 2 damage! Health is " + str(player.health) + "!"
