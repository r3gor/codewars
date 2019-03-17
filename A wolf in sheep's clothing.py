def warn_the_sheep(queue):
    if queue[len(queue)-1]=='wolf':
        return "Pls go away and stop eating my sheep"
    for i in range(len(queue)-1):
        if queue[i] == "wolf":
            return "Oi! Sheep number {}! You are about to be eaten by a wolf!".format(len(queue)-(i+1))

if __name__ == "__main__":
	print(warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep']))