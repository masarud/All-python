def henkan(x):
	try:
		y = float(x)
	except:
	    print("x must be number")
	return y

print(henkan(10))

print(henkan("Hello"))