student={"name":"john", "age":20, "grade":"A"}

print(student["name"])
student["grade"]="A+"
print(student)

student["city"]="Delhi"
print(student)

mydict={"Harry": "098098", "Mohit":"5645545"}

print(mydict.keys())
print(mydict.values())


for keys,value in mydict.items():
    print(keys,value)