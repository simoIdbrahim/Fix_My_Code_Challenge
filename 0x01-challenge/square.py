#!/usr/bin/python3

class Square:

    side_length = 0

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """Area of the square"""
        return self.side_length * self.side_length

    def perimeter_of_my_square(self):
        """Perimeter of the square"""
        return self.side_length * 4

    def __str__(self):
        return "{}".format(self.side_length)


if __name__ == "__main__":
    s = Square(side_length=12)
    print(s)
    print("Area:", s.area_of_my_square())
    print("Perimeter:", s.perimeter_of_my_square())
