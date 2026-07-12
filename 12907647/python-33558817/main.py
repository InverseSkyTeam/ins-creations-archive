def triangle(a,b):     # △
    return a*3+b*2+5
def at(a,b):           # @
    return triangle(a,b) - triangle(b,5) + a*b
def square(a,b):       # □
    return triangle(a,b) + at(a,b) + a*b-11
def circles(a,b):      # ◎
    return triangle(a,b) + at(a,b) + square(a,b) - 2*a*b
def star(a,b):
    if a < b:
        x = triangle(circles(a,b),a) - 2*a*b
    else:
        x = square(at(b,b),a) + 2*a*b
    return x + 11
print(-(at(star(star(2,1),11),square(triangle(at(3,7),6),8))))