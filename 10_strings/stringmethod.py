s=" Mohit Salvi "

name[0]="R"
print(s)
a=len(s)

print(s.lower())
print(s.upper())
print(s.capitalize())
print(s.title())


print(s.strip());
print(s.lstrip());
print(s.rstrip());

text="Python is fun"


print(text.find("is"))
print(text.replace("fun","Amazing"))


text="apple,banana,mango"
print(text)

print(text.split(","))

print(",".join(['apple','banana','mango']))

text="Python 023"

print(text.isalpha())
print(text.isdigit())
print(text.isalnum())
print(text.isspace())