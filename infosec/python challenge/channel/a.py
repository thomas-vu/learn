f = open('90052.txt')
while True:
	text = f.read()
	print(text)
	#print(text.split()[-1] + '.txt')
	f = open(text.split()[-1] + '.txt')

	# 46145.txt
