from Area import Rectangle
import math

while True:
    floor_a = float(input('Enter side A (e.g., 5.5 meters): '))
    floor_b = float(input('Enter side B (e.g., 4.2 meters): '))

    floor = Rectangle(floor_a,floor_b)

    az_a = float(input('Enter tile size (e.g., 30 cm): '))
    az_b = float(input('Enter  the other side of tile (e.g., 30 cm): '))

    tile = Rectangle(az_a, az_b)

    floor_area = floor.area()
    tile_area = tile.area()

    tile_quantity = floor_area / tile_area

    if floor_area% tile_area == 0:
        print(f'The exact quantity for completing for is of: {tile_quantity}')

    else:
        print(f'The minimum quantity for completing the floor is:  {math.ceil(tile_quantity)}')