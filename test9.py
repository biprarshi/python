l1 = [1,2,3,[4]]
l2 = list(l1)
print(id(l1)==id(l2))
print(l1,l2)

my_list1 = [1,2,3,4,5,6]
n = len(my_list1)
if n > 5:
    print(f"List has {n} elements")

my_list2 = [1,2,3,4,5,6]
if (n := len(my_list2)) > 5:
    print(f"List has {n} elements")
