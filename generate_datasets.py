import csv

f = open("data.csv")

g1 = open("data1.csv","wb")
g1w = csv.writer(g1, delimiter=',')

g2 = open("data2.csv","wb")
g2w = csv.writer(g2, delimiter=',')

g3 = open("data3.csv","wb")
g3w = csv.writer(g3, delimiter=',')

g4 = open("data4.csv","wb")
g4w = csv.writer(g4, delimiter=',')

g5 = open("data5.csv","wb")
g5w = csv.writer(g5, delimiter=',')

r = csv.reader(f)


i = 0

for l in r:

	if i >= 0 and i < 2000:
		g1w.writerow(l)
	elif i >=2000 and i<=3999:
		g2w.writerow(l)
	elif i>=4000 and i<=5999:
		g3w.writerow(l)
	elif i>=6000 and i<=7999:
		g4w.writerow(l)
	elif i>=8000 and i<=9999:
		g5w.writerow(l)
	i = i + 1


	
