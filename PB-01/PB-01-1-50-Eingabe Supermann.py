#==========================================================================
#
# PB-01-1-50-Eingabe Supermann.py
#
# (keine Bauteile)
#
#==========================================================================
#
Eingabe_Name = input ("Wie heißt Du? ")

if Eingabe_Name == "Clark Kent":
    print("TOLL, Du bist Supermann!")
else:
    print(Eingabe_Name,"  ??? Du bist nicht Supermann!")
    
    
"""
Das vorliegende MicroPython-Programm für den Raspberry Pi Pico beginnt damit,
den Benutzer nach seinem Namen zu fragen, indem die Funktion input() verwendet
wird. Die Benutzereingabe wird dann in der Variable Eingabe_Name gespeichert.

Die if-Bedingung prüft nun, ob der eingegebene Name Clark Kent entspricht.
Wenn dies der Fall ist, wird die Nachricht TOLL, Du bist Supermann! ausgegeben.

Wenn die Bedingung nicht erfüllt ist, d.h. wenn der eingegebene Name nicht
Clark Kent ist, wird die Nachricht Eingabe_Name ??? Du bist nicht Supermann!
ausgegeben. Beachte hier, dass die Variable Eingabe_Name direkt in den Text
der Ausgabe-Nachricht eingefügt wird, indem sie mit einem Komma getrennt wird.

Zusammenfassend prüft dieses Programm, ob der Benutzer als Name Clark Kent
eingibt und gibt dann eine entsprechende Nachricht aus, die entweder darauf
hinweist, dass er Supermann ist oder nicht.

Nun zur verbalen Erklärung des Codes:

Das Programm beginnt mit der Eingabeaufforderung Wie heißt Du?, die mithilfe
der input()-Funktion ausgegeben wird. Der von dem Benutzer eingegebene Name
wird dann in der Variablen Eingabe_Name gespeichert.

Die if-Bedingung prüft, ob die Eingabe des Benutzers Clark Kent entspricht.
Wenn dies der Fall ist, wird die Nachricht TOLL, Du bist Supermann! ausgegeben.

Wenn die Bedingung nicht erfüllt ist, wird die else-Bedingung ausgeführt, und
die Nachricht Eingabe_Name ??? Du bist nicht Supermann! wird ausgegeben.
Beachten Sie hierbei, dass das Komma zwischen Eingabe_Name und den
Fragezeichen dazu führt, dass der eingegebene Name in der Ausgabe-Nachricht
angezeigt wird.

Insgesamt ist dieses Programm ein einfaches Beispiel für die Verwendung von
Bedingungen in MicroPython, um auf verschiedene Eingaben des Benutzers zu
reagieren und entsprechende Nachrichten auszugeben.


>>> %Run -c $EDITOR_CONTENT
Wie heißt Du? dieter
dieter   ??? Du bist nicht Supermann!
>>>

"""
    
