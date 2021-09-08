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
#### enc()
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

#### encDef()
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

#### decrypt()
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


Update: I added some features

### Updated features

#### modifying the alphabet sequence of the program

  I've made a feature that will allow u to modify the sequence of your cipher whatever u want.
  * encSeq()
  * decryptSeq()
  these are the functions
  
 
### encSeq()
  encSeq() function takes three arguments: stringToEnc,shift,sequence
  
### decryptSeq()
  decryptSeq() function takes two: stringToDec,sequence
  
both function works the same as the original, except for their sequences that u can modify :)
 
 
### here is the step-by-step guide

in order to use the function u need to add or make a new sequence that u will use.
the default sequence is "ABCDEFGHIJKLMNOPQRSTUVWXYZ", so if u wanted to add some like if u have a number in your string that u want to encrypt, just add "0123456789" on the list.

First import the ceasar file,
```python
import ceasar as csr
```
and if u look at its sequence
```python
print(csr.sequence)
```
the result would be a list from a to z
```
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
```
so if u have a number in your string, u need to add the numbers at the end of the list
so we make a new variable list and using the default sequence, lets add the numbers at the end of the sequence
```python
newSequence=csr.sequence + list("0123456789".lower()) #u can add anything u like but for this sample well just use the numbers
```
note: u need to set the string to lower caps 
u can check the number by printing if the numbers really do add up to the list

next is we'll go to the functions
for example we have a string "HelloMicTest12345" and shift it at 23 , we cannot encrypt this string using the original functions because there are numbers present on the string. So we need to add numbers to the sequence which we already did at the top. So whats left is to input those sequence into the function and encrypt out string.
```python
out=csr.encSeq('HelloMicTest12345',23,sequence)#our string, our shift, our sequence that we made earlier
print(out)
```
now the results should be this
```
4188b95zg1fgopqrs
```
an encrypted version of your string with numbers. COOL

now then, we already have the encrypted version of our string, what we want now is to decrypt it. we'll use this method
```python
out = csr.decryptSeq('4188b95zg1fgopqrs',newSequence)# our encrypted word, our new sequence
print(out)
```
note: make sure that the sequence is the same as the one used to encrypt the string
the output should be...
```
0  : 4188b95zg1fgopqrs
1  : 5299ca60h2ghpqrst
2  : 63aadb71i3hiqrstu
3  : 74bbec82j4ijrstuv
4  : 85ccfd93k5jkstuvw
5  : 96ddgea4l6kltuvwx
6  : a7eehfb5m7lmuvwxy
7  : b8ffigc6n8mnvwxyz
8  : c9ggjhd7o9nowxyz0
9  : dahhkie8paopxyz01
10 : ebiiljf9qbpqyz012
11 : fcjjmkgarcqrz0123
12 : gdkknlhbsdrs01234
13 : hellomictest12345
14 : ifmmpnjduftu23456
15 : jgnnqokevguv34567
16 : khoorplfwhvw45678
17 : lippsqmgxiwx56789
18 : mjqqtrnhyjxy6789a
19 : nkrrusoizkyz789ab
20 : olssvtpj0lz089abc
21 : pmttwuqk1m019abcd
22 : qnuuxvrl2n12abcde
23 : rovvywsm3o23bcdef
24 : spwwzxtn4p34cdefg
25 : tqxx0yuo5q45defgh
26 : uryy1zvp6r56efghi
27 : vszz20wq7s67fghij
28 : wt0031xr8t78ghijk
29 : xu1142ys9u89hijkl
30 : yv2253ztav9aijklm
31 : zw33640ubwabjklmn
32 : 0x44751vcxbcklmno
33 : 1y55862wdycdlmnop
34 : 2z66973xezdemnopq
35 : 3077a84yf0efnopqr
None
```
Now notice the string at number 13, that string is the same ass the original non-encrypted string! just that easy! now u know how to modify the sequence at your will.
Because of this feature ceasar-cipher can be hard to crack because the sequence that u will make will always be needed to crack your encrypted string. It will be more hard to crack. Plus the shift u set to the sequence. u will need two keys to unlock a encrypted string, the key shift, and the key sequence. Ha, much harder thank you for reading. this maybe the last feature or maybe not, who knows, ill probably move on to a new cipher. Im proud for this repo, i learned a lot. good work myself. 




This is the whole code for the update-series
```python
#import ceasar
import ceasar as csr

#check the default sequence
print(csr.sequence)

#create the new sequence
newSequence = csr.sequence + list("0123456789".lower())

print()
#encrypt your string using the newSequence
encrypt=csr.encSeq('HelloMicTest12345',23,newSequence)#our string, our shift, our sequence that we made earlier
print(encrypt,'\n')


#decrypt your encrypted string
decrypt = csr.decryptSeq(encrypt,newSequence)# our encrypted word, our new sequence
print(decrypt)
```

```
#default sequence
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#encrypted String
4188b95zg1fgopqrs

# decrypt the String
0  : 4188b95zg1fgopqrs
1  : 5299ca60h2ghpqrst
2  : 63aadb71i3hiqrstu
3  : 74bbec82j4ijrstuv
4  : 85ccfd93k5jkstuvw
5  : 96ddgea4l6kltuvwx
6  : a7eehfb5m7lmuvwxy
7  : b8ffigc6n8mnvwxyz
8  : c9ggjhd7o9nowxyz0
9  : dahhkie8paopxyz01
10 : ebiiljf9qbpqyz012
11 : fcjjmkgarcqrz0123
12 : gdkknlhbsdrs01234
13 : hellomictest12345
14 : ifmmpnjduftu23456
15 : jgnnqokevguv34567
16 : khoorplfwhvw45678
17 : lippsqmgxiwx56789
18 : mjqqtrnhyjxy6789a
19 : nkrrusoizkyz789ab
20 : olssvtpj0lz089abc
21 : pmttwuqk1m019abcd
22 : qnuuxvrl2n12abcde
23 : rovvywsm3o23bcdef
24 : spwwzxtn4p34cdefg
25 : tqxx0yuo5q45defgh
26 : uryy1zvp6r56efghi
27 : vszz20wq7s67fghij
28 : wt0031xr8t78ghijk
29 : xu1142ys9u89hijkl
30 : yv2253ztav9aijklm
31 : zw33640ubwabjklmn
32 : 0x44751vcxbcklmno
33 : 1y55862wdycdlmnop
34 : 2z66973xezdemnopq
35 : 3077a84yf0efnopqr
None
```


