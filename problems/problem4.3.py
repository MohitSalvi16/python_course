num=input("enter the number")

reverse=""
n = len(num)

i=n-1
while(i>=0):
    reverse=reverse+num[i]
    i=i-1

print(reverse)
