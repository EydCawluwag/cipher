# ceasar-cipher
In Caesar cipher, the set of plain text characters is replaced/shifted by any other character, symbols or numbers. Although it is weak, still better to learn it

## Introduction

In the ceasar.py(the file which the algorithms lay) file, there are three functions:
* enc(stringToEnc, shift)
* encDef(stringToEnc)
* decrypt(stringToDec)

Ceasar cipher in default uses three(3) shifts in every letter of the word you want to cipher.

  If you want to cipher the word CEASAR, first thing you need is to know the place of your letter in the alphabet(by defaut ABCDEFGHIJKLMNOPQRSTUVWXYZ or maybe u have numbers so use ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 or whatever u want the alphabets to be) and shift that letter three times to the right, or add three to the letters index and your new index will be ur new letter. So in the word CEASAR, the first letter C should be shifted three times to the right which will be the letter F,so C=F, E=H, A=D, S=V, A=D, R=U, so the ciphered version of the word CEASAR will be FHDVDU. This is what the encDef() function do.

  enc() function on the other hand is a function for ceasar-cipher modified. It means that you can freely choose how many shift(thats the second argument on enc() function) u want to do with ur word to cipher.  
   ex. CEASAR with 8 shifts = KMILIZ
       CEASAR with 13 shifts = PRNFNE
   
   
  decrypt() function is just a plain vanilla brute force attack to the word to decrypt your encrypted word. go to usage to see more info about this func.


## Usage
enc() function. Takes two arguments: stringToEnc, shift
```python
import ceasar
# enc(stringToEnc,shift)
out=ceasar.enc("Hello World!", 5) 
print(enc)
```
...the output should be
```
mjqqt 2twqi!
```
... this is the ciphered/encrypted version of your string
  note: punctuation or other special characters wont be shifted 

encDef() on the other hand stand for default encryption which is a string which letters are shifted 3 positions to the right.
encDef() function, Takes one argument: stringToEnc
```python
import ceasar
#encDef(stringToEnc)
out = ceasar.encDef("Hello World!")
print(out)
```
.. the output should be
```
khoor zruog!
```
  note: the characters will all be small caps when encrypted
  
decrypt() function just takes one argument and start a brute force attack to your string.
It lets the user(you) to pick one from the 26 brute force results, if theres any word that makes sense to u
  note: only one should be the correct result u pick out of the 26 variations
```python
import ceasar
ceasar.decrypt("khoor zruog!")
```
...output shoud be
```
0  : khoor zruog!
1  : lipps asvph!
2  : mjqqt btwqi!
3  : nkrru cuxrj!
4  : olssv dvysk!
5  : pmttw ewztl!
6  : qnuux fxaum!
7  : rovvy gybvn!
8  : spwwz hzcwo!
9  : tqxxa iadxp!
10 : uryyb jbeyq!
11 : vszzc kcfzr!
12 : wtaad ldgas!
13 : xubbe mehbt!
14 : yvccf nficu!
15 : zwddg ogjdv!
16 : axeeh phkew!
17 : byffi qilfx!
18 : czggj rjmgy!
19 : dahhk sknhz!
20 : ebiil tloia!
21 : fcjjm umpjb!
22 : gdkkn vnqkc!
23 : hello world!
24 : ifmmp xpsme!
25 : jgnnq yqtnf!
```
... you need to find the word within these variations. In this example we found that at number 23(at brute force number 23) we found the only sensible word out of all the choices. So therefore the original string of "khoor zruog!" is at 23 : "hello world!"

Try it yourself, encrypt a word using the enc() function and choose the number of shifts or the encMod() function which by default shift your string at three positions, and decrypt it using the decrypt() function and find the original word! 

Have fun :)
