**Lernziel:** Ich kann am Ende des Kapitels:
- sagen, was eine Datenbank ist und warum sie so praktisch ist
- erklären, woraus eine Datenbank besteht (Tabellen, Zeilen, Spalten)
- eine Datenbank für ein eigenes Projekt planen und aufmalen
- Tabellen sinnvoll miteinander verbinden
- mit einfachen Fragen genau das aus der Datenbank herausbekommen, was ich brauche

# Was ist eine Datenbank?
**Definition:**
Eine **Datenbank** ist eine strukturie rte Sammlung von Daten, die gespeichert, geordnet, verändert und abgefragt werden können.

**Zentrale Begriffe:**
- Tabelle
- Datensatz (eine Zeile)
- Attribute (eine Spalte)
- Primärschlüssel (eindeutige ID)
# Beispiel
![Beispiel-Datenbank](https://raw.githubusercontent.com/Imacikus/Informatikuntericht/main/Klasse%2010/Mitschriften/E2E7A463-EDBE-47A1-90F2-B746B7118F4F_1_201_a.jpeg)
ID, Nachname, Vorname sind Attribute
1, Schmid
### Die 3 wichtigsten Vorteile einer Datenbank:
1. Weniger/keine Redundanz
	- Daten werden nicht unnötig oft gespeichert
2. Schneller Zugriff
	- Auch bei riesigen Datenmengen sehr schnell
3. Sichere & konsistente Struktur 
	- Weniger Fehler durch Regeln & Beziehungen
	- Änderungen wirken überall sofort richtig
# Planung & Modellierung einer Datenbank
**Problem:**
Eine Schule will Schüler, Klassen und Lehrer speichern - wie anfangen?
1. Entitäten finden z.b.:
	- Name
	- Klassen
	- Lehrer

2. Attribute bestimmen
Schüler
- Schüler ID
- Name
- Geburtsdatum
- Klasse
