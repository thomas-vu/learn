import pickle

with open('banner.p', 'rb') as f:
    data = pickle.load(f)

for x in data:
	for y in x:
		a, b = y
		print(a*b, end='')
	print()
