# Develop a python program to convert binary to decimal, octal to hexadecimal using functions
def binToDec(b):
 return int(b, 2)
def OctToHex(o):
 return hex(int(o, 8))
print("Enter the Binary Number:" ,end= " ")
bnum = input()
dnum = binToDec(bnum)
print("\nEquivalent Decimal Value = ", dnum)
print("Enter an Octal Number: ", end="")
onum = input()
hnum = OctToHex(onum)
print("\nEquivalent Hexadecimal Value =", hnum[2:].upper())