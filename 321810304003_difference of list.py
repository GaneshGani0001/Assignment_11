l,n=[],int(input('Enter no of elements for list 1: '))
print('Enter elements: ')
for i in range(0,n):
	i=input()
	l.append(i)
l2,id,m=[],[],int(input('Enter no of elements for list 2: '))
print('Enter elements: ')
for i in range(0,m):
	i=input()
	l2.append(i)
difference=set(l).symmetric_difference(set(l2))
listd= list(difference)
print("difference blw 2 list is:",listd)