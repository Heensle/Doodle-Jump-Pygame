import random

def ledge_rand_x():
    return random.randint(0, 389) #all possible pixel values in which the platform is fully on screen

def ledge_controlled_x(start_range, end_range): #takes start and end of disruptive object to prevent platform generation on top of the object
    option_one = random.randint(0, start_range - 91)
    option_two = random.randint(end_range, 389)
    if random.randint(0, 1):
        return option_one
    else:
        return option_two
    
def ledge_rand_y():
    return random.randint(0, 800)

def ledge_relational_y(prev_y):
    return random.randint((prev_y - 250), prev_y)