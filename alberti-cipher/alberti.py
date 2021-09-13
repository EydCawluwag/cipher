stabilis=list('ABCDEFGILMNOPQRSTVXZ1234')
mobilis=list('gklnprtuz&xysomqihfdbace')
initialShift=0
periodicIncrement=1
periodLength=4


def shift(arrToShift,shift):
	if shift>len(arrToShift):return algShift(arrToShift,shift%len(arrToShift))
	return algShift(arrToShift,shift)

# clockwise shift!!!
def algShift(arrToShift,shift):
	a,b,c,d=[],len(arrToShift),arrToShift,shift
	[a.append(arrToShift[i]) for i in range(b-d,b)]
	[a.append(c[i]) for i in range(b-d)]
	return a

def enc(stringToEnc):
	a,b,c,d,e,f=initialShift,periodicIncrement,periodLength,len(stringToEnc),mobilis,stabilis
	for i in range(int(d/c)):
		e=shift(e,b)
		print(e)

def dec(stringToDec):
	pass



enc('LouiseCarloSalomonGwapoKaayu')
