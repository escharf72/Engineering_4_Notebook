def myFunc(a):
	b = []
	for stuff in a:
		b.append(stuff**2)
		return(b)

myArr = [1,3,6,23]
print(myFunc(myArr))
