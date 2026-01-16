import cmath

print("Hello, this is a quadratic calculator, it will be expecting 3 numbers, a, b, and c")
a= int(input("Please give your value for a: "))
b= int(input("Please give your value for b: "))
c= int(input("Please give your value for c: "))

# first, catch any div by 0 errors
if a == 0:
    print("This would cause a div by 0 error, please try with new numbers")
else:
    #positive branch of sqrt first
    x1= (-b + cmath.sqrt(b**2 - 4*a*c))/(2*a)
    print(f"the first root (positive branch) is {x1:.3f}")
    x2=  (-b - cmath.sqrt(b**2 - 4*a*c))/(2*a)
    print(f"the second root (negative branch) is {x2:.3f}")
