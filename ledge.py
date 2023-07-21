import random_num

class platform:
    
    def __init__ (self, image):
        self.x_pos = random_num.platform_rand_x()
        self.y_pos = random_num.platform_rand_y()
        self.image = image

    def x_range (self, start_range, end_range, image):
        self.x_pos = random_num.platform_controlled_x(start_range, end_range)
        self.y_pos = random_num.platform_rand_y
        self.image = image

    def relational_y (self, prev_y, image):
        self.x_pos = random_num.platform_rand_x
        self.y_pos = random_num.platform_relational_y(prev_y)
        self.image = image

    def x_range_relational_y (self, start_range, end_range, prev_y, image):
        self.x_pos = random_num.platform_controlled_x(start_range, end_range)
        self.y_pos = random_num.platform_relational_y(prev_y)
        self.image = image