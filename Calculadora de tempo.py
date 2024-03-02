from datetime import datetime, timedelta
d=int(input("Digite a quantidade de dias:"))
data=datetime.today()
if d<0:
	data=data-(timedelta(-d))
elif d>=0:
	data=data+timedelta(d)
print("A data indicada é {:02d}/{:02d}/{}".format(data.day, data.month, data.year))