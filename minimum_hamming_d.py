import random
import numpy as np
import pandas as pd
from hamming_parctice import hamming
from itertools import combinations

df = pd.read_csv('sample.csv', names=['word','bin'])

words = [df.iloc[i,0] for i in range(0, len(df))]
bins = [df.iloc[i,1] for i in range(0, len(df))]

count = 0
minimum_hd = 32
for alpha, beta in combinations(zip(words, bins), 2):
	hd = hamming(alpha[1], beta[1])
	print(count, "(", alpha[0], beta[0], ")", "hamming_distance: ", hd)
	if  minimum_hd > hd:
		minimum_hd = hd
	count+=1
print("min hamming distance", minimum_hd)
	

