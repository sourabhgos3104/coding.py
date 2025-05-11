
set={1,2,3,4,5}
set.add(101)
set.add("hello")
set.add(101)
set.pop()
set.remove(101)
set.discard(101)
set.update(range(10,16))
set.clear()
print(set)


s={1,2,3,5,6}
a=s
s.add(101)
print(a)
print(s)


s={1,2,3,5,6}
a=s.copy()
s.add(101)
print(a)
print(s)


s1={1,2,3,4,5,7}
s2={1,2,3,4,5,6}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))

li=[1,2,3,2,4,5,6,5,8,6,5]
li.insert(3,201)
li.append(202)
li.pop()
li.remove(201)
li.pop(8)
print(li)


d={100:"durga",200:"ravi",300:"shiva"}
print(d)
del d[100]
print(d)
del d[300]
print(d)
print(d.get(200))


d={"name":"manoj", "age": 24}
d.clear()
print(len(d))
print(d)
print(d.get("age"))
del d




d={"name":"manoj", "age": [18,5,25,56,78,41]}

d.setdefault ("grade","A")
print(d)


print(range(0,6))
print(list(range(0,6)))
print(list(range(0,6,1)))
print(list(range(0,-8,-1)))
print(list(range(1,11,3)))