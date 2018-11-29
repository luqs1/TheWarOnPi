from LastYearsClasses.oldlib.movement import Movement
from LastYearsClasses.oldlib.vision import Vision
# omae wa mou shindeiru

movement = Movement()
vision = Vision()
area_limit = 1000
while True:
    blocks = vision.get_color(0, show_feed=False)
    if len(blocks) == 0:
        movement.rotate(100,5)
    for block in blocks:
        x = block['x']
        y = block['y']
        a = block['area']
    if a <= area_limit:
        if abs(x-200) <= 30:
            movement.move(20)

        elif x > 200:
            movement.stop()
            movement.rotate(20,1.5)
        else:
            movement.stop()
            movement.rotate(-20,1.5)
    else:
        movement.stop()
