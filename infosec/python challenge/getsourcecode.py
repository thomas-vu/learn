from urllib.request import urlopen

sock = urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345')
for _ in range(400):
	page = sock.read()
	print('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + str(page.split()[-1])[2:-1])
	sock = urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + str(page.split()[-1])[2:-1])
sock.close()
