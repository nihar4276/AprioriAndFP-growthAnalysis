import csv
import pandas as pd
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

df = []
def read(file):
	f = open(file,"r")
	x = csv.reader(f)
	for row in x:
		df.append([r for r in row if r != ''])

	return df


def apply_apriori(file,mins):
	df = read(file)
	te = TransactionEncoder()
	te_ary = te.fit(df).transform(df)
	df = pd.DataFrame(te_ary, columns=te.columns_)

	x = apriori(df, min_support=0.2, use_colnames=True)

	print x['itemsets']


