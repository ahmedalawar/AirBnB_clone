#!/usr/bin/python3


def calculate_square_area(side_length):
    """Calculate the area of a square."""
    return side_length ** 2


def calculate_circle_area(radius):
    """Calculate the area of a circle."""
    return 3.14159 * radius ** 2


def calculate_triangle_area(base, height):
    """Calculate the area of a triangle."""
    return 0.5 * base * height


def main():
    """Main function to demonstrate area calculations."""
    side = 4
    radius = 3
    base = 6
    height = 5

    square_area = calculate_square_area(side)
    circle_area = calculate_circle_area(radius)
    triangle_area = calculate_triangle_area(base, height)

    print("Square area:", square_area)
    print("Circle area:", circle_area)
    print("Triangle area:", triangle_area)


if __name__ == "__main__":
    main()
