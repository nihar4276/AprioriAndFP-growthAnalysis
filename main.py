import sys 
import os

"""

Authors:


Abhijeet Kumar 
Nihar Rao 



"""
sys.path.append(os.path.abspath("/home/nihar/Desktop/DWDM_project"))
import timeit
from apriori2 import *
import csv
import subprocess 

os.chdir("/home/nihar/Desktop/DWDM_project")
f = open("output.csv","wb")
g = csv.writer(f, delimiter=',')

# list to put in output csv
output =[["Algorithm","dataset #1","dataset #2","dataset #3","dataset #4","dataset #5"]]

firstrow = ["Apriori"]

#set minimum support for both algorithms
min_support = 2

#running apriori
for i in range(0,5):
	start_time = timeit.default_timer()
	print "   Itemsets for dataset  "+str(i+1)
	apply_apriori("datasets/data" + str(i+1) + ".csv",min_support)
	elapsed = timeit.default_timer() - start_time
	firstrow.append(str(elapsed))

secondrow = ["FP Growth"]

#running fpgrowth
for i in range(0,5):
	start_time = timeit.default_timer()
	FNULL = open(os.devnull, 'w')
	retcode = subprocess.call(['python','-m','fp_growth', '-s',str(min_support),'datasets/data',str(i+1)+'.csv'], stdout=FNULL, stderr=subprocess.STDOUT)
	elapsed = timeit.default_timer() - start_time
	secondrow.append(str(elapsed))

output.append(firstrow)
output.append(secondrow)

# write to csv
g.writerows(output)






