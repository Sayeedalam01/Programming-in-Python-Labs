a = int(input("Enter first number: "))
b = int(input("Enter 2nd number: "))

print(f"Before Swap: \n First number = {a}\n Second number = {b}");

c = a;
a = b;
b = c;

print(f"After Swap: \n First number = {a}\n Second number = {b}");