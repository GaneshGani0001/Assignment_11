l,n,x=[],int(input('Enter no of elements: ')),1
print('Enter elements: ')
for i in range(0,n):
	i=int(input())
	l.append(i)
for i in range (0,n):
	x*=l[i]
print("list after multiplying elements:",x)	