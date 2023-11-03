Student={
    "name":"Alice",
    "age":25,
    "grade":"A"
    }
Student["name"]="Isha"
print(Student)
for x in Student.values():
    print(x)
for x,y in Student.items():
    print(x,y)
for key,value in Student.items():
    print("key:value")

print(Student.get("phonenumber"))
squares={num:num**2 for num in range(1,6)}
print(squares)
cubes={num:num**3 for num in range(1,6)}
print(cubes)
grade=Student.get("grade", "N/A")
print(grade)
grade=Student.get("phone")
print(grade)
del Student["age"]
print(Student)
done=Student.get("age")
print(done)
"""user_dict={}
while True:
    key=input("Enter the key:")
    value=input("Enter the value:")
    user_dict["key"]=value
print(user_dict)"""
dic1={1:2,2:3,3:4}
dic2={5:6,6:7,7:8}
dic3={56:80,90:56}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)

