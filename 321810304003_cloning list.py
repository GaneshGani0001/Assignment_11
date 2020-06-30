l,nl,n=[],[],int(input('Enter no of elements: '))
print('Enter elements: ')
for i in range(0,n):
	i=input()
	l.append(i)
nl=l
print('orginal list:',l)
print('new list after cloning:',nl)