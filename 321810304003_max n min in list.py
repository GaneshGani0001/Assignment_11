l,n=[],int(input('Enter no of elements: '))
print('Enter elements: ')
for i in range(0,n):
	i=input()
	l.append(i)
print('largest number:',max(l),'\nsmallest number:',min(l))