from canvas import Canvas
from shapes import Rectangle, Square

"""
User  Command line Interface
"""
print("Lets first make the background or canvas for the design....")
canvas_height=int(input("Enter the height of the canvas: "))
canvas_width=int(input("Enter the weidth of the canvas: "))
canvas_colour=input("Enter colour of your canvas- black or white? ")
colour=""
if canvas_colour.lower()=="white" :
    colour=(255,255,255)
elif canvas_colour.lower()=="black" :
    colour=(0,0,0)
canvas= Canvas(canvas_height, canvas_width, colour)

print("\n")
print("Now lets make the design on our canvas....")

while True:
    shape= input("which shape you would like to draw- square or rectangle? or type quit to exit ")
    if shape.lower()=="rectangle":
        rec_x=int(input("enter the x co-od of the upper left vertex of the rectangle: "))
        rec_y = int(input("enter the y co-od of the upper left vertex of the rectangle: "))
        rec_height=int(input("enter the height of the rectangle: "))
        rec_width = int(input("enter the width of the rectangle: "))
        red=int(input("enter the amount of red colour you want to have in the rectangle(Between 0 to 255): "))
        green=int(input("enter the amount of green colour you want to have in the rectangle(Between 0 to 255): "))
        blue=int(input("enter the amount of blue colour you want to have in the rectangle(Between 0 to 255): "))
        r1= Rectangle(rec_x, rec_y, rec_height, rec_width, (red, green, blue))
        r1.draw(canvas)
    if shape.lower() == "square":
        sqr_x = int(input("enter the x co-od of the upper left vertex of the square: "))
        sqr_y = int(input("enter the y co-od of the upper left vertex of the square: "))
        sqr_side = int(input("enter the side length of the square: "))
        red = int(input("enter the amount of red colour you want to have in the square(Between 0 to 255): "))
        green = int(input("enter the amount of green colour you want to have in the square(Between 0 to 255): "))
        blue = int(input("enter the amount of blue colour you want to have in the square(Between 0 to 255): "))
        s1 = Square(sqr_x, sqr_y, sqr_side, (red, green, blue))
        s1.draw(canvas)
    if shape.lower()=="quit":
        break
canvas.make("shape.png")
