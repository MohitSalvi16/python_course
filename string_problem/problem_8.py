text="My name is Mohit Salvi"

count=0;
n=len(text)

for i in range (0,n):
    if(text[i]=="a" or text[i]=="e" or text[i]=="i" or text[i]=="o" or text[i]=="u"):
        count=count+1

print(count)

        