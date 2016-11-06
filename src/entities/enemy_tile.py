from src.graphics.drawable_I import DrawableRectangle

class EnemyTile(DrawableRectangle):
    def __init__(self, red_val, green_val, blue_val, x_pos, y_pos, width, height):
        super(EnemyTile, self).__init__(x_pos, y_pos, width, height, red_val, green_val, blue_val)