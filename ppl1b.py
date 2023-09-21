num = input("Enter a number: ")
if num == num[::-1]:
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")
digit_count = [0]*10
for digit in num:
     digit_count[int(digit)] += 1
print("Number of occurrences of each digit in", num, ":")
for i in range(10):
    print(i, "occurs", digit_count[i],"times")
