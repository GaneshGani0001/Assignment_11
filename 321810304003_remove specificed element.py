l,n=[],int(input('Enter no of elements: '))
print('Enter elements:')
for i in range(0,n):
	i=input()
	l.append(i)
m=input('enter an no to b remove:')
l.remove(m)
print('list after removing',m,':',l)