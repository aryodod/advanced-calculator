input_1 = input("""
Enter "+" for addition.\n

Enter "-" for subtraction.\n

Enter "*" for multiplication.\n

Enter "/" for division.\n

Enter "**" for exponentiation.\n

Enter "//" for quotient.\n

Enter "%" for remainder.\n

Enter "areasquare" for area of a 
square.\n

Enter "arearectangle" for area of a 
rectangle.\n

Enter 'areacircle' for area of a circle.\n

Enter 'areatriangle' for area of a triangle.\n

Enter "volumecube" for volume of a 
cube.\n

Enter "volumecuboid" for volume of a 
cuboid.\n
""")
if input_1 == "+":
    add_1 = float(input("Enter a number: "))
    add_2 = float(input("Enter another number: "))
    print("-------------")
    print(add_1)
    print("+")
    print(add_2)
    print("-------------")
    print("Answer")
    print(add_1 + add_2)
elif input_1 == "-":
    subtract_1 = float(input("Enter a number: "))
    subtract_2 = float(input("Enter another number: "))
    print("-------------")
    print(subtract_1)
    print("-")
    print(subtract_2)
    print("-------------")
    print("Answer")
    print(subtract_1 - subtract_2)
elif input_1 == "*":
    multiply_1 = float(input("Enter a number: "))
    multiply_2 = float(input("Enter another number: "))
    print("-------------")
    print(multiply_1)
    print("X")
    print(multiply_2)
    print("-------------")
    print("Answer")
    print(multiply_1 * multiply_2)
elif input_1 == "/":
    divide_1 = float(input("Enter a number: "))
    divide_2 = float(input("Enter another number: "))
    print("-------------")
    print(divide_1)
    print("/")
    print(divide_2)
    print("-------------")
    print("Answer")
    print(divide_1 / divide_2)
elif input_1 == "**":
    exponentation_1 = float(input("Enter a number:"))
    exponentation_2 = float(input("Enter another number: "))
    print("-------------")
    print(exponentation_1)
    print("**")
    print(exponentation_2)
    print("-------------")
    print("Answer")
    print(exponentation_1 **

exponentation_2)
elif input_1 == "//":
    quotient_1 = float(input("Enter a number: "))
    quotient_2 = float(input("Enter another number: "))
    print("-------------")
    print(quotient_1)
    print("//")
    print(quotient_2)
    print("-------------")
    print("Answer")
    print(quotient_1 // quotient_2)
elif input_1 == "%":
    remainder_1 = float(input("Enter a number: "))
    remainder_2 = float(input("Enter another number: "))
    print("-------------")
    print(remainder_1)
    print("%")
    print(remainder_2)
    print("-------------")
    print("Answer")
    print(remainder_1 % remainder_2)
elif input_1 == "areasquare":
    squarearea = float(input("Enter the length of the square: "))
    print("-------------")
    print(squarearea)
    print("X")
    print(squarearea)
    print("-------------")
    print("Answer")
    print(squarearea * squarearea)
elif input_1 == "arearectangle":
    rectanglearea_1 = float(input("Enter the length of the rectangle: "))
    rectanglearea_2 = float(input("Enter the width of the rectangle: "))
    print("-------------")
    print(rectanglearea_1)
    print("X")
    print(rectanglearea_2)
    print("-------------")
    print("Answer")
    print(rectanglearea_1 *

rectanglearea_2)
elif input_1 == "volumecube":
    cubevolume = float(input("Enter the length of the cube: "))
    print("-------------")
    print(cubevolume)
    print("X")
    print(cubevolume)
    print("X")
    print(cubevolume)
    print("-------------")
    print("Answer")
    print(cubevolume * cubevolume *

cubevolume)
elif input_1 == "volumecuboid":
    cuboidvolume_1 = float(input("Enter the length of the cuboid: "))
    cuboidvolume_2 = float(input("Enter the breadth of the cuboid: "))
    cuboidvolume_3 = float(input("Enter the height of the cuboid: "))
    print("-------------")
    print(cuboidvolume_1)
    print("X")
    print(cuboidvolume_2)
    print("X")
    print(cuboidvolume_3)
    print("-------------")
    print("Answer")
    print(cuboidvolume_1 *

cuboidvolume_2 * cuboidvolume_3)
elif input_1 == "areacircle":
    circlearea = input("Type in radius if you want to calculate using radius or type in diameter if you want to calculate using diameter.")
    if circlearea == "radius":
       radiuscirclearea = float(input("Enter the radius: "))
       print("-------------")
       print(radiuscirclearea)
       print("X")
       print(radiuscirclearea)
       print("X")
       print("3.14")
       print("-------------")
       print("Answer")
       print(radiuscirclearea *

radiuscirclearea * 3.14)
    elif circlearea == "diameter":
        diametercirclearea = float(input

("Enter the diameter: "))
        print("-------------")
        print(diametercirclearea)
        print("X")
        print("3.14")
        print("-------------")
        print("Answer")
        print(diametercirclearea * 3.14)

elif input_1 == "areatriangle":
    trianglelength = float(input("Enter the length of the triangle: "))
    trianglewidth = float(input("Enter the width of the triangle: "))
    print("-------------")
    print(trianglelength)
    print("X")
    print(trianglewidth)
    print("÷")
    print("2")
    print("-------------")
    print("Answer")
    print(trianglelength * trianglewidth / 2)
