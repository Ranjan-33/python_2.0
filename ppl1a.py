m1=int(input("enter the total marks of the first internal :"))
m2=int(input("enter the total marks of the second internal :"))
m3=int(input("enter the total marks of the third internal :"))
if(m1>m2):
    if(m2>m3):
     total=m1+m2
    else:
        total=m1+m3
elif(m1>m3):
    total=m1+m2
else:
    total=m2+m3
avg=total/2
print("the total twonbest internal is :",avg)