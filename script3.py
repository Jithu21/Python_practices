triangle_firstside = int(input("Enter a triangle number: "))
triangle_secondside = int(input("Enter a triangle number: "))
triangle_thirdside = int(input("Enter a triangle number: "))
if triangle_firstside == triangle_secondside and triangle_secondside == triangle_thirdside:
    print("Triangle numbers are equal")
elif triangle_firstside == triangle_secondside or triangle_secondside == triangle_thirdside or triangle_thirdside == triangle_firstside:
    print("Triangle numbers are Isosceles")
elif triangle_firstside != triangle_secondside !=triangle_thirdside:
    print("Triangle numbers are not equal and not isosceles and its Scalene")
else:
    print("valid Number ")
