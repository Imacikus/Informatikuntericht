#Rechenoperation der 3. Stufe

import math                 #Mathematikpaket importieren

ZhZ1 = 2**10                #Ergebnis: 1024
print("ZhZ1 = ", ZhZ1)      #ZhZ1 ausgeben

ZhZ2 = math.pow(2, 10)      #ZhZ2 mit math.pow
print("ZhZ2 = ", ZhZ2)      #ZhZ2 ausgeben

w1 = math.sqrt(25)          #Quadratzahlen mit sqrt
print("w1   = ", w1)        # w1 ausgeben

w2 = 25**0.5                #Quadratwurzel als Potenz
print("w2   = ", w2)        #w2 ausgeben

w3 = math.pow(25, 0.5)      #Quadratwurzel mit pow
print("w3   = ", w3)        #w3 ausgeben

w4 = math.pow(25, (1/2))    #Quadratwurzel als Bruch
print("w4   = ", w4)        #w4 ausgeben

wu3 = math.pow(8, (1/3))    #dritte Wurzel mit pow
print("wu3  = ", wu3)       #dritte Wurzel ausgeben

