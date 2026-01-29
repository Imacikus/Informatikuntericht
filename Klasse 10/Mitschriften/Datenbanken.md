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

3. Primärschlüssel erklären
Ein **Primärschlüssel** ist ein eindeutiges Merkmal, z.B. eine ID, die jeden Datensatz eindeutig identifiziert.
##### Entity-Relationship-Modell (Entitäten-Beziehungs-Modell oder kurz ERM)
|  Schüler  |   Klasse    |
| :-------: | :---------: |
| SchülerID | Klassen ID  |
|   Name    | Klassenname |

![ERM-Diagramm](https://raw.githubusercontent.com/Imacikus/Informatikuntericht/main/Klasse%2010/Mitschriften/ERM.png)
## Übungsaufgabe:
Plane eine Datenbank für eine Bibliothek (Bücher & Ausleihe)
#### Bibliothek - Datenbank-Planung
1. Entitäten finden
	- Buch / Titel
	- Exemplar
	- Leser / Person
	- Ausleihe
2. Wichtigste Attribute notieren
	1. Leser
	- Schüler ID
	- Name
	- Geburtsdatum
- Klasse
1. Beziehungen zeichnen (Pfeile + 1 / n)
	--> Ziel: Redundanz vermeiden + leicht abfragen können
	- Welche Bücher hat Max gerade ausgeliehen?
	- Welche Bücher sind überfällig?

### Beziehungen und Beziehungstypen (ERM)
| Kardinalität | Symbol | Bedeutung (ganz einfach gesagt) | Bibliotheks-Beispiel |
|-------------|--------|----------------------------------|----------------------|
| 1:1 | 1-1 | Genau eine links gehört zu genau einer rechts | Jede Person hat genau einen Bibliotheksausweis |
| 1:n | 1-n | Eine links kann zu vielen rechts gehören | Eine Person kann viele Bücher ausleihen |
| n:m | n-m | Viele links können zu vielen rechts gehören (beliebig) | Viele Bücher können von vielen Personen ausgeliehen werden (nacheinander) |

![ERM-Übung](https://raw.githubusercontent.com/Imacikus/Informatikuntericht/main/Klasse%2010/Mitschriften/ERM%20%C3%9Cbung.jpeg)

# Wichtige Datentypen für eine Bibliothek

| Feld              | Datentyp           | Hinweis                  |
| ----------------- | ------------------ | ------------------------ |
| Buch-Titel        | VARCHAR(150)       |                          |
| Autor             | VARCHAR(100)       |                          |
| Erscheinungsjahr  | INTEGER (SMALLINT) |                          |
| ISBN              | VARCHAR(13)        | Immer als Text speichern |
| Ausleihdatum      | DATE               |                          |
| Fällig am         | DATE               |                          |
| Ist überfällig?   | BOOLEAN            |                          |
| Verspätungsgebühr | DECIMAL(6,2)       | z.B. 3,50€               |
# Eine Datenbank anlegen - gute Relationen
### 1. Relationschemata
Ein **Relationenschema** beschreibt den Aufbau einer Tabelle:

![Relationsschema](https://raw.githubusercontent.com/Imacikus/Informatikuntericht/main/Klasse%2010/Mitschriften/Relationschemata.jpeg)

### 2. Relationen Entitätstypen
- Jede Tabelle hat einen Primäschlüssel (z.B. lehrID)
- Attribute haben eindeutige Bedeutung
- Alle Relationenschemata einer DB nennt man **Datenbankschma**
### 3. Entititätstypen
Um ein ERM als Datenbank zu implementieren, kann man zunächst für jeden Entitätstyp eine eigene Tabelle anlegen. Dabei wird für jedes Attribut des Entitätstyps eine Spalte in die Tabelle geplant.
Jede Tabelle benötigt außerdem einen Primärschlüssel, mit dem jeder Datensatz eindeutig identifiziert werden kann.
### 4. Beziehungstypen umsetzen
Im Folgenden betrachten wir die zwei wichtigsten Beziehungstypen und wie man sie korrekt in Tabellen umsetzt: 1:n und n:m.

--> Grundbegriffe
- Primärschlüssel (PK) --> eindeutige ID einer Zeile
- Fremdschlüssel (FK) --> verweist auf den PK einer anderen Tabelle 
- Beziehungen = Verknüpfungen zwischen Tabellen über Schlüssel

--> 1 : n Beziehung
**Definition**
Eine Entität A steht mit genau einer Entität B in Beziehung
- aber Entität B kann beliebig viele Entitäten A in Beziehung stehen (1 --> viele / n)
Wo kommt der Fremdschlüssel hin?
- Immer auf der n-Seite ! 
(Die Seite, auf der "viele" möglich sind)

- Jeder Schüler kennt nur eine Klasse (Fremdschlüssel in Schüler-Tabelle) 
- Eine Klasse kennt viele Schüler (über die n-Seite gefunden)

