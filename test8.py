a = "mary had a little lamb"
print(a)
print(a.isupper())
print(a.upper())
print(a)
b = "THE QUICK BROWN FOX JUMPS OVER A LAZY DOG"
print(b)
print(b.islower())
print(b.lower())
print(b)
print(a.find("f"))
print(b.find("A"))
print(b.replace("A", "b"))
print(b)
print("a" in a)

print(b[5])
print(b[-5])
print(b[0:5])
print(b[::5])
print(len(b))
print(b[-5::-1])
print(b[-5:0:-1])
print(b[-5:])
# print(b[-5:-42]) no output
print(b[-5:-42:-1])
print(b[-1::-1])

for i in b:
    print(i, end=" ")
print()
for i in range(len(b)-1, -1, -1):
    print(b[i], end=" ")
print()

l1 = [i for i in range(201) if i % 19 == 0]
print(l1)
l1.extend("fish")
print(l1)
l1.append(b)
print(l1)
print(type(l1))
l1.insert(7, "007")
print(l1)
print(f"{"":#^200}")
l2 = l1.copy()  # Shallow Copy
l2.extend(a)
print(l1, l2, sep=" ** ")
l2 = l1  # Deep Copy
l2.clear()
print("empty", l1, l2)
l1 = [i for i in range(201) if i % 19 == 0]
print("original", l1)
print(l1)
del l1[2]
print("del index 2", l1)
print("pop index 2", l1.pop(2))
print("pop index 2", l1)
l1.pop()
print("pop", l1)
l1.reverse()
print(l1)
l1.sort()
print(l1)
l1.remove(19)
print("remove 19", l1)
l1.append(190)
l2.append(209)
l2.append(228)
l1.extend(l2)
l1.extend(l2)
print(l1)
print(len(l1))
print("max", max(l1))
l1.append(l2)
print(l1)
# print("max", max(l1)) error
print(a.count("a"))
print(list(a).count("a"))
print("count 209 l1", l1.count(209))
print("count 209 l1", l1[-1].count(209))
print(l1.index(209))
print(max(l2))
print(min(l2))
print(l1.pop())
print(len(l1))
print(max(l1))
print(min(l1))
print("count 209 l1", l1.count(209))
for i in range(len(l1)-1, -1, -1):
    print(l1[i])

print(f"{00:#^100}")
l1 = [i for i in range(1, 41) if i % 2 == 0]
l2 = [i for i in range(1, 41) if i % 3 == 0]
l3 = [i for i in range(1, 41) if i % 4 == 0]
print(len(l3))
print(l1, l2, l3, sep="\n")
for i1, i2, i3 in zip(l1, l2, l3):
    print(i1, i2, i3)

print(a.split("l"))
l4 = a.split("a")
print(l4)
print(b.split())

set1 = {i for i in range(95, 99)}
set2 = {95, 98, 97, 96, 97, 97}
print(set1, set2)
print(type(set1))
set1.update(i for i in range(20, 51, 10))
print(set1)
set3 = set(b.split())
print(set3)
set3.update(a.split())
print(set3)
set3.add("PaNgRaM")
print(set3)
print("pop", set3.pop())
print(set3)
set3.remove("PaNgRaM")
print(set3)
set2.discard(97)  # no error throw
print(set2)
set3.clear()
print(set3)
print(type(set3))
print(b.index("QUICK"))
print(b.index("Q"))
print(b.split().index("FOX"))
set4 = {1, 5, 7, 6, 2, 3, 4}
# dict1 = dict(("d", "b", "c")) throws error
dict1 = dict(("ef", "ab", "cd"))
print(dict1)
set4.update(dict1)
set4.update(("22", "333", "4444"))
print(set4)

tup1 = 21, 65, 99, 34, 56, 81, 32, 99, 99
print(type(tup1))
print(tup1[2])
print(tup1.count(99))
print(tup1.index(99))
print("min", min(tup1))
print("max", max(tup1))
print("sum", sum(tup1))
print(len(tup1))
print(tup1[:7:2])
values: tuple[int | str, ...] = (1, 2, 4, "Geek")
print(values)

marks = {"maths": 96, "chemistry": 92, "physics": 98}
student = {"raju": "amit", "sunita": "ankush", "binod": "raj"}
print(marks["physics"])
print(student["raju"])
marks["english"] = 91
print(marks)
marks["maths"] = 88
print(marks)
details = {'name:': 'python', "fees:": 8000, 'duration:': "2 months"}
for i in marks:
    print(i, marks[i])
for i in details:
    print(i, details[i])
for i in marks:
    print(i, marks.get(i))
print(marks.values())
print(marks.keys())
print(marks.items())

del student["raju"]
print(student)
print(details.pop("name:"))
print(details)
print(marks.popitem())
print(marks)
student.update({"raju": "amit", "akshay": "kumar", "sanjay": "dutt"})
print(student)
student.clear()
print("student dictionary clear()", student)
x = "x1", "x2", "x3"
y = [2, 3]
new_dict = dict.fromkeys(x, y)
# new_dict = dict.fromkeys(x,list(y))
print(new_dict)
y.append(4)
print(new_dict)
seq = {'a', 'b', 'c', 'd', 'e'}
list1 = [2, 3]
res_dict2 = {key: list1 for key in seq}
res_dict3 = {key: list(list1) for key in seq}
print(res_dict2)
print(res_dict3)
list1.append(5)
print(res_dict2)
print(res_dict3)
dict2 = {"name": "amit", "surname": "sen"}
print(dict2.setdefault("name", "ravi"))
print(dict2.setdefault("midname", "kumar"))
print(dict2)
course1 = {
    "php": {"duration": "2 months", "fees": "3000"},
    "python": {"duration": "3 months", "fees": "5000"},
    "java": {"duration": "4 months", "fees": "6000"},
    "C++": {"duration": "1 month", "fees": "4500"}
}
print(course1)
print(course1["php"])
print(course1["php"]["fees"])
for k, v in course1.items():
    print(k, v)
    print(v["duration"], v["fees"])
course1["java"]["fees"] = "20000"
for k in course1:
    print(k, course1[k]["duration"], course1[k]["fees"])
print(course1.popitem())
for k in course1:
    print(k, course1[k]["duration"], course1[k]["fees"])
