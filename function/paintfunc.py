import math

def paint_calc(height, width, cover):
    ar= height*width
    num_of_cans= math.ceil(ar/coverage )
    print(f'the number of can {num_of_cans}')

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)