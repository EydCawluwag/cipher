stabilis=list('ABCDEFGILMNOPQRSTVXZ1234')
mobilis=list('gklnprtuz&xysomqihfdbace')

def shift(arrToShift,shift):
	if shift>len(arrToShift):return algShift(arrToShift,shift%len(arrToShift))
	return algShift(arrToShift,shift)

def algShift(arrToShift,shift):
	a,b,c,d=[],len(arrToShift),arrToShift,shift
	[a.append(arrToShift[i]) for i in range(b-d,b)]
	[a.append(c[i]) for i in range(b-d)]
	return a

def enc(stringToEnc):
	print(stabilis)
	print(shift(mobilis,1))

def dec(stringToDec):
	pass



enc('LouiseCarlo')
