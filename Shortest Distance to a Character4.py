import math
def shortest_to_char(s, c):

	lista=[x for x in s]

	for i in range(len(lista))
		d1=len(lista)
		for ii in range(len(lista)):
			if lista[ii]==c:
				d=math.fabs(i-lista.index(c))
				if d<d1:
					d1=d

	return lista


if __name__ == '__main__':
	print(shortest_to_char('aabbaabb','a'))
	print(shortest_to_char("lovecodewars", "e"))