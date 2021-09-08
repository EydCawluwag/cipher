import sys
import ceasar as csr

def encrypt():
	print('out:',csr.enc(input("String to encrypt:"),int(input("Shift for the encrypt:"))))

def decrypt():
	print('out:',csr.decrypt(input('String to decrypt:')))

def encryptFast():
	print('out:',csr.enc(input("String to encrypt:"),3))

def decryptFast():
	print('out:',csr.decryptDef(input("String to decrypt:"),3))

def encryptWithSequence():
	print('out',csr.enc(input("String to encrypt:"),int(input("Shift for the encrypt:")),input("Sequence for the encrypt:")))

def decryptWithSequence():
	print('out',csr.decryptSeq(input('String to decrypt:'),input('Sequence for the decrypt:')))

def main(arg):
	if arg=='decrypt':decrypt()
	elif arg == 'decryptWithSequence':decryptWithSequence()
	elif arg == 'encrypt': encrypt()
	elif arg == 'encryptFast': encryptFast()
	elif arg == 'decryptFast': decryptFast()
	elif arg == 'encryptWithSequence':encryptWithSequence()
	else: print('Function not found')

if __name__ == '__main__':
	arg=sys.argv
	main(arg[1])