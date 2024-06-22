tup1 = range(0, 20, 3)
l1 = [3, 7, 5, 6, 22, "M"]
dict1 = dict(zip(tup1, l1))  # dict1 = dict(zip(set1,set2))
set1 = set(tup1)
set2 = set([3, 7, 5, 6, 22, "M"])
set3 = set(tup1)
fset1 = frozenset(dict1)

fset2 = frozenset(zip(tup1, l1))

tom = ""

print("set3="+str(set3), "set1="+str(set1), "set2="+str(set2), "dict1=" +
      str(dict1), "fset1="+str(fset1), "fset2="+str(fset2), sep=f"{tom:^5}")

union = set1.union(set2)  # set1 | set2
print("set1 set2 union=", union)
intersection = set1.intersection(set2)  # set1 & set2
print("set1 set2 intersection=", intersection)
difference = set1.difference(set2)  # set1 - set2
print("set1 set2 difference=", difference)
symmetric_difference = set1.symmetric_difference(set2)  # set1 ^ set2
print("set1 set2 symmetric difference=", symmetric_difference)
disjoint = set1.isdisjoint(set2)
print("set1 set2 disjoint=", disjoint)
subset = set1.issubset(set2)  # set1 <= set2,  set1 < set2 (proper subset)
print("set1 set2 subset=", subset)
superset = set1.issuperset(set2)  # set1 >= set2, set1 > st2 (proper superset)
print("set1 set2 superset=", superset)

tup2 = tuple(zip(tup1, l1))
l2 = list(zip(tup1, l1))
fset3 = frozenset(tup2)
fset4 = frozenset(l2)
fset5 = frozenset(l1)
print("tup2="+str(tup2), "fset3="+str(fset3), "l2=" +
      str(l2), "fset4="+str(fset4), sep=f"{tom:<5}")
print("l1="+str(l1), "fset5="+str(fset5), sep=f"{tom:#<5}")


thisset1 = {"apple", "banana", "cherry"}
thisset1.update({"1": "pineapple", "2": "mango", "3": "papaya"})  # |=
print(thisset1)
thisset1.update(["pineapple", "mango", "papaya"])
thisset1 |= {"splinter", "cell"}
print(thisset1)
thisset1.add("Burger")
print(thisset1)
# To remove an item in a set, use the remove(), or the discard() method.
# Remove a random item by using the pop() method
# The clear() method empties the set: thisset.clear()
# The del keyword will delete the set completely: del thisset1


l3 = [fset1.copy()]
l4 = list(fset1.copy())
print(fset1)
print("The length of set is:", len(fset1))
print(l3)
print(l4)

print("tortoise")

print(max(set1))
print(min(set1))
print(max(l3))