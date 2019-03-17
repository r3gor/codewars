def shortest_to_char(s, c):

lista=[x for x in s]

for i in range(len(s)):
if c == lista[i]:
	lista[i]=0	

for i in range(len(lista)):
if i == 0 or i == len(lista)-1:
	continue
if lista[i]==0:
	if lista[i-1]!=0:
		lista[i-1]=1
	if 	lista[i+1]!=0:
		lista[i+1]=1


return lista


if __name__ == '__main__':
print(shortest_to_char('aabbaabb','a')) #should equal [0, 0, 1, 1, 0, 0, 1, 2])