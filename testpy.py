list=[1,2,3]
list.append("ML")
print(list)
    
list.extend(["ML23",4,89,987])
print(list)


list.insert(2,"Test ML")
print(list)


list.remove("Test ML")
print(list)


list=[x**2 for x in [1,2,3,4,5]]

print(list)


list.pop(4)
print(list)

list.remove(16)
print(list)
'''

'''

print(type(list[1]))

print(sorted(list))

print(list[::-1])

tup1=(1,3,5)
tup2=(2,4,6)
tup3=tup1+tup2
print(tup3)

print(tup1)
del(tup1)

tup=([1,2,3],[4,5,6],[7,8,9])
print(tup)

print(len(tup))

print(tup[1][0:2])

tup[0][0]='changed'
print(tup)















