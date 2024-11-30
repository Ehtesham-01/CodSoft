# Basic Calculator
print("----Basic Calculator----")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.division")
choice=int(input("Enter your choice= "))
if choice == 1:
   a=int(input("Enter a= "))
   b=int(input("Enter b= "))
   c = a+b
   print("Addition = ",c)
elif choice == 2:
   a=int(input("Enter a= "))
   b=int(input("Enter b= "))
   c = a-b
   print("Subtraction = ",c)
elif choice == 3:
   a=int(input("Enter a= "))
   b=int(input("Enter b= "))
   c = a*b
   print("Multiplication = ",c)
elif choice == 4:
   a=int(input("Enter a= "))
   b=int(input("Enter b= "))
   c = a/b
   print("Division = ",c)
else:
    print("Invalid choice..")