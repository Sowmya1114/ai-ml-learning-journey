#Print multiplication table of a number
a=int(input("Enter a number: "))
for i in range(1,13):
  res=a*i
  print(a,"*",i,"=",res)

#Count numbers from 10 to 1
i=10
while i>0 and i<=10:
  print(i)

#Find factorial of a number
a=int(input("Enter a number: "))
res=1
for i in range(1,a+1):
  res*=i
print(res)

