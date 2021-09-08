sequence=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower())

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
	return enc(stringToEnc,3)

def decrypt(stringToDec):
	alphabet=sequence
	for i in range(len(sequence)):
		if i<10:print(i,' :',enc(stringToDec,i))
		else:print(i,':',enc(stringToDec,i))

def encSeq(stringToEnc,shift,seq):
	alphabet,brokenString,out=seq,stringToEnc.split(' '),''
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

def decryptSeq(stringToDec,seq):
	alphabet=seq
	for i in range(len(alphabet)):
		if i<10:print(i,' :',encSeq(stringToDec,i,seq))
		else:print(i,':',encSeq(stringToDec,i,seq))


