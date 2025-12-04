### Lernziele
- verstehen, was eine Klasse und ein Objekt sind
- einen Konstruktor (```__init__```) schreiben
- Attribute und Methoden erlären
- eigene Klassen programmieren
- die Methode ```__str__```
- einfache Kapselung anwenden

## Was ist OOP?
Objektorientierte Programmierung bedeutet:
Wir programmieren mit Objekten, die Eigenschaften und Fähigkeiten haben.

Beispiel im echten Leben:
- Ein Auto hat Eigenschaften --> Farbe, Marke, Geschwindigkeit
- und Methode --> fahren(), bremsen()

In der OOP nennt man das eine Klasse.

## Klassen und Objekte
Eine ==Klasse== ist eine Vorlage. 
Ein ==Objekt== ist ein Beispiel dieser Vorlage

**Beispiel:** eine einfache Klasse
```
class Auto:
	pass # die Klasse ist leer
```
#### Ein Objekt erstellen
```
mein_auto=Auto()
```

#### Der Konstruktor (```__init__```)
Der Konstruktor wird benutzt, wenn ein neues Objekt erstellt wird. Hier definieren wir die Anfangswerte (Attribute).

**Beispiel**:
```
class Auto:
	def__init__(self, farbe, marke)
		self.farbe = farbe
		self.marke = marke
```
#### Ein Objekt erstellen:
```
auto1 = Auto("rot", "BMW")
auto2 = Auto("blau", "Toyota")
```

## Methoden (Funktion innerhalb einer Klasse)
**Methoden** beschreiben, was ein Objekt tun kann.
```
class Auto:
	def__init__(self, farbe, marke)
		self.farbe = farbe
		self.marke = marke
		
	def fahren(self):
		print("Das Auto fährt los!")
```
