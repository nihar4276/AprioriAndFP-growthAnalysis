import csv;
min_support = 2

database = []
def n_slices(n, list_):
    for i in xrange(len(list_) + 1 - n):
        yield list_[i:i+n]

def isSublist(list_, sub_list):
    for slice_ in n_slices(len(sub_list), list_):
        if slice_ == sub_list:
            return True
    return False

def read(file):
	f = open(file,"r")
	x = csv.reader(f)
	for row in x:
		database.append([r for r in row if r != ''])

def gen_c1():
	retlist = []
	for trans in database:
		for ele in trans:
			if ele not in retlist:
				retlist.append(ele)
	return retlist

def scanD(l):
	retlist = []
	supp = {}
	for trans in database:
		for can in l:
			if isSublist(trans,can):
				if can not in supp:
					supp[can] = 1;
				else:
					supp[can] +=1
	for can in supp:
		if supp[can] >= min_support:
			retlist.append(can);
	return retlist,supp

def apriori_gen(l,k):
	retlist =[]
	for i in range(len(l)):
		for j in range(i+1,len(l)):
			l1 = list(l[i])
			l2 = list(l[j])
			l1 = l1[:k-2]
			l2 = l2[:k-2]
			l1.sort()
			l2.sort()
			if l1==l2:
				retlist.append(l[i] | l[j])
	return retlist


def apply_apriori(file,mins):
	read(file)
	# database = map(set,database)
	c1 = gen_c1()
	l,supp = scanD(c1)
	k = 2
	l=[l]
	while(len(l[k-2]) > 0):
		ck =  apriori_gen(l[k-2],k)
		l1,supk = scanD(ck)
		supp.update(supk)
		l.append(l1)
		k += 1








 
