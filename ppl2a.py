n = int(input("Enter a value for N: "))


def f(n):
 if n <= 0:
    return "Invalid input"
 elif n == 1:
    return 0
 elif n == 2:
    return 1
 else:
    return int(f(n-1))+ int(f(n-2))
print("the value of the function is:",f(n))
