

"""

The Typewriter Cipher 

A = .
B = ..
C = ...
D = !
E = "
F = /
G = @
H = $
I = --
J = &
K = '
L = ,
M = (
N = )
O = ()
P = *
Q = ?
R = +
S = =
T = %
U = :
V = ;
W = (-)
X = '''
Y = ÷ 
Z = ***


"""

UPPER_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

TYPEWRITER_CIPHER = { "A" : ".", "B" : "..", "C" : "...", "Z" : "***" }

letter = UPPER_ALPHABET[0]

print(f"{letter} : {TYPEWRITER_CIPHER[letter]}")

letter = UPPER_ALPHABET[1]

print(f"{letter} : {TYPEWRITER_CIPHER[letter]}")

letter = UPPER_ALPHABET[2]

print(f"{letter} : {TYPEWRITER_CIPHER[letter]}")




letter = UPPER_ALPHABET[25]

print(f"{letter} : {TYPEWRITER_CIPHER[letter]}")







