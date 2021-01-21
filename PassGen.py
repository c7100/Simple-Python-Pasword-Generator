import random
import string

print('''
|=====================|
| Generator de Parole |
|=====================|
	''')
caractere = string.printable.strip()

numar_parole = int(input('Introdu numarul de parole dorite: '))
lungime_parola = int(input('Cate caractere vrei sa aiba parola: '))

print('\nParolele Generate: ')

for c in range(numar_parole):
	parola = ""
	for a in range(lungime_parola):
		parola += random.choice(caractere)
	print (parola)