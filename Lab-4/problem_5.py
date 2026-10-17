N = int(input("Enter a number (N): "))
a = 0
b = 1
print(f"Fibonacci numbers below {N} are:")
while a < N:
    print(a, end=" ")
    a, b = b, a + b
print()