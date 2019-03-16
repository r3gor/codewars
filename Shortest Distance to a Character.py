def shortest_to_char(s, c):

	lista=[x for x in s]

	for i in range(len(s)):
		if c == lista[i]:
			lista[i]=0
	
	print(lista)

	for i in range(len(s)-1):
		if lista[i+1]!=0 and type(lista[i])==int:
			lista[i+1]=lista[i]+1
	
	# for i in range(len(s)-1):
	# 	if lista[i-1]!=0 and type(lista[i])==int:
	# 		lista[i-1]=lista[i]+1

	return lista


if __name__ == '__main__':
	print(shortest_to_char('aabbaabb','a')) #should equal [0, 0, 1, 1, 0, 0, 1, 2])