# ceasar-cipher
In Caesar cipher, the set of plain text characters is replaced/shifted by any other character, symbols or numbers. Although it is weak, still better to learn it

## Introduction

In the ceasar.py(the file which the algorithms lay) file, there are three functions:
: enc(stringToEnc, shift)
: encDef(stringToEnc)
: decrypt(stringToDec)

Ceasar cipher in default uses three(3) shifts in every letter of the word you want to cipher.
if you want to cipher the word CEASAR, first thing you need is to know the place of your letter in the alphabet(by defaut ABCDEFGHIJKLMNOPQRSTUVWXYZ or maybe u have numbers so use ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 or whatever u want the alphabets to be) and shift that letter three times to the right, or add three to the letters index and your new index will be ur new letter. So in the word CEASAR, the first letter C should be shifted three times to the right which will be the letter F,so C=F, E=H, A=D, S=V, A=D, R=U, so the ciphered version of the word CEASAR will be FHDVDU.


## Usage
```python
# enc(stringToEnc,shift)
out=enc("Hello World!", 5) 
print(enc)
```
the output should be
```
mjqqt 2twqi!
```