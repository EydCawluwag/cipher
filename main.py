import sys
import ceasar


def main(arg):
	a=ceasar.encryptMod(arg,5)
	print(a)


if __name__ == '__main__':
	try:
		arg = sys.argv
		main(' '.join(arg[1:]))
	except IndexError as e:
		raise SystemExit(f"Usage: {sys.argv[0]} <string-to-cipher>, <string-to-cipher> <cipher-shift>")

