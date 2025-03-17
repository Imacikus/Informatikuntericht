# Verschiedene Varianten der Textausgabe+

print('Das ist eine Zeichenkette.')         #String mit Hochkomma
print()                                     #Leerzeile
print('Noch eine weitere zeichenkette.')
print()
print('Thats also a String')                #Quoting the quotes

help_message = '''
hallo
hii
'''
print(help_message)

#Zugriff auf einzelne Zeichen im String

str = "Python String"                   #Zu untersuchender String
print("1. Stringzeichen: ", str[0])      #zeige p
print("2. Stringzeichen: ", str[1])      #zeige y
print("6. Stringzeichen: ", str[5])      #zeige n
print()

#Stringlaenge ermitteln und ausgeben
str_len = len(str)
print(str)
print("String Length: ", str_len, "Byte")