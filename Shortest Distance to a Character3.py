import math
def shortest_to_char(s, c):

	lista=[x for x in s]

	for i in range(len(s)):
		if c == lista[i]:
			lista[i]=0	
	for i in range(len(lista)):
		d1=len(lista)
		for ii in range(len(lista)):
			if lista[ii]==0:
				d=math.fabs(ii-i)
				if d<d1:
					d1=d
		
		lista[i]=int(d1)


	return lista


if __name__ == '__main__':
	print(shortest_to_char('aabbaabb','a'))
	print(shortest_to_char("lovecodewars", "e"))