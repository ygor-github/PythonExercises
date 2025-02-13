import math
class Sphere:
    def __init__(self, color, radius):
        self.color = color
        self.radius = radius

    def volume(self):
        vol = (4/3) * math.pi * self.radius**3
        return vol

    def area(self):
        ar = 4 * math.pi * self.radius**2
        return ar

ball1 = Sphere('Red',4)
ball2 = Sphere('Blue', 7)

print(f'The volume of the ball 1 is {ball1.volume()} cm3')
print(f'The surface area of ball 1 is {ball1.area()} cm2')

print(ball1.volume())
print(Sphere.volume(ball1))

