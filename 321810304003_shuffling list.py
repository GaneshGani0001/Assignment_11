from random import shuffle
l,n=[],int(input('Enter no of elements: '))
print('Enter elements: ')
for i in range(0,n):
	i=input()
	l.append(i)
shuffle(l)
print("shuffled list:",l)