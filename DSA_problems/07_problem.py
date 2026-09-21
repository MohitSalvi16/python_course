l=[1,2,322,33,22,2,22,3]

print(l)
l.sort()

for i in range(1,8):
    if(l[i]==l[i-1]):
        l.remove(l[i])
print(l)