class Rectangle:
    def __init__(self, side_a, side_b):
        self.a = side_a
        self.b = side_b

    def change_value(self, new_a, new_b):
        self.a = new_a
        self.b = new_b

    def return_dimensions(self):
        print(f'The dimensions of the rectangle are side a: {self.a}m and side b: {self.b}m.')

    def area(self):
        return self.a * self.b

