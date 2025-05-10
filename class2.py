a=10
b=10
print(id(a))
print(id(b))


a=20
b=10

print(id(a))
print(id(b))

a=10
b=20
print(a**2)
print(b**2)

li1=[101,1,2,6,8]
li2=[101,2,5,4,8]

print(id(li1))
print(id(li2))



tup=(1,2,3,4,5,6,1,7,7,8,9,4,8,9)

print(max(tup))
print(min(tup))
print(type(tup))
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[4])
print(tup.count(1))
print(tup.count(7))


li=[1,2,3,4,5,6,7,8,9,12,13]
li=set(li)

set={1,2,3,4,5,14}

print(li)