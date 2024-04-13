A =  int(input("Enter first number: "))
B =  int(input("Enter second number: "))

print("For Operation Enter '1' for Addition\n '2' for Subtraction\n '3' for Multiplication\n '4' for Division")
C = input("Enter operation: ")

if  C == "1":
    print("Addition of given number is ",A + B)
elif C == "2":
    print("Subtraction of given number is ",A - B)
elif C == "3":
    print("Multiplication of given number is ",A * B)
elif C == "4":
    print("Division of given number is ",A/B)
else:
    print("Invalid Input")