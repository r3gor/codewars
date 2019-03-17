def day_and_time(mins):
    dias= int(mins/(24*60))
    horas= int((mins-(dias*24*60))/(60))
    minu=(mins-horas*60-dias*24*60)

    lista_d=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return"dias: {0}, horas: {1},minutos: {2} ".format(dias,horas,minu)

if __name__=="__main__":
	print(day_and_time(65))