#coding: utf8
# Erforderliche Bibliotheken importieren
import RPi.GPIO as GPIO
import time

# Konvention für Pinnummerierung festlegen (BCM bzw. Board)
GPIO.setmode(GPIO.BCM)
# Warnungen, die das Ausführen des Programms verhindern, wenn
# Ausgang bereits als OUT deklariert wurde ignorieren
GPIO.setwarnings(False)
# Pins als Ausgänge deklarieren
GPIO.setup(21, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

# PWM für Richtungen mit Frequenz festlegen
uhrzeigersinn = GPIO.PWM(21, 50)
gegen_uhrzeigersinn = GPIO.PWM(25, 50)
# PWM mit Tastgrad 0% initialisieren
uhrzeigersinn.start(0)
gegen_uhrzeigersinn.start(0)


'''
Hoch- und Herunterfahren mit anschließendem Richtungswechsel
'''

# try ermöglicht das Abbrechen des Programms mit der
# Tastenkombination [Strg] + [C]
try:
    print("Programm gestartet. Beenden mit [Strg] + [C]!")
    # While True - Endlosschleife
    while True:

        #---Im Uhrzeigersinn---
        
        # Tastgrad von 0 % auf 100 % mit Schrittweite 2 erhöhen
        for i in range(0, 100, 2):
            # Tastgrad auf i [%] ändern
            uhrzeigersinn.ChangeDutyCycle(i)
            time.sleep(0.02)
        # Tastgrad von 100 % auf 0 % mit Schrittweite 2 erniedrigen
        for i in range(100, 0, 2):
            # Tastgrad auf i [%] ändern
            uhrzeigersinn.ChangeDutyCycle(i)
            time.sleep(0.02)

        #---Gegen den Uhrzeigersinn---

        # Tastgrad von 0 % auf 100 % mit Schrittweite 2 erhöhen
        for i in range(0, 100, 2):
            # Tastgrad auf i [%] ändern
            gegen_uhrzeigersinn.ChangeDutyCycle(i)
            time.sleep(0.02)
        # Tastgrad von 100 % auf 0 % mit Schrittweite 2 erniedrigen
        for i in range(100, 0, 2):
            # Tastgrad auf i [%] ändern
            gegen_uhrzeigersinn.ChangeDutyCycle(i)
            time.sleep(0.02)
except KeyboardInterrupt:
    uhrzeigersinn.stop()
    print("Programm beendet")

            
