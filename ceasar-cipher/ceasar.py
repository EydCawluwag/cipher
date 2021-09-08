sequence=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'.lower())
def enc(stringToEnc,shift):
	alphabet,brokenString,out=sequence,stringToEnc.split(' '),''
	for i in brokenString:
		a=list(i.lower())
		for j in range(len(a)):
			if a[j] in alphabet:
				b=alphabet.index(a[j].lower())
				if (b+shift)>len(alphabet)-1: b=(b+shift)%len(alphabet)
				else:b=b+shift
				out+=alphabet[b]
			else:
				out+=a[j]
		out+=' '
	return out
def encDef(stringToEnc):
	return encryptMod(stringToEnc,3)
def decrypt(stringToDec):
	alphabet=sequence
	for i in range(len(sequence)):
		print(':',enc(stringToDec,i))

