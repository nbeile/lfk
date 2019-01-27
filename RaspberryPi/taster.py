#coding: utf8
# Erforderliche Bibliotheken importieren
import RPi.GPIO as GPIO

# Konvention für Pinnummerierung festlegen (BCM bzw. Board)
GPIO.setmode(GPIO.BCM)
# Warnungen, die das Ausführen des Programms verhindern, wenn
# Ausgang bereits als OUT deklariert wurde ignorieren
GPIO.setwarnings(False)
# Pin 23 als Eingangspin deklarieren. Pull-Up-Widerstand einschalten,
# um Störsignale zu filtern
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# Funktion mit dem Parameter "channel" (Pin 23) erstellen
# Funktionen werden erst beim Aufrufen ausgeführt
def callback_funktion(channel):
    print("Interrupt aufgerufen durch Pin ", channel)

# Interrupt-Handler
GPIO.add_event_detect(
    23,
    GPIO.RISING,
    callback = callback_funktion,
    bouncetime = 200)
