#coding utf8
import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

mot1_uhrzeigersinn = GPIO.PWM(21, 50)
mot1_gegen_uhrzeigersinn = GPIO.PWM(25, 50)
mot2_uhrzeigersinn = GPIO.PWM(14, 50)
mot2_gegen_uhrzeigersinn = GPIO.PWM(24, 50)

mot1_uhrzeigersinn.start(0)
mot1_gegen_uhrzeigersinn.start(0)
mot2_uhrzeigersinn.start(0)
mot2_gegen_uhrzeigersinn.start(0)


def mot1(run_event):
    while True:

        for i in range(0, 100, 2):
            if run_event.is_set():
                mot1_uhrzeigersinn.ChangeDutyCycle(i)
                time.sleep(0.02)
            else:
                break
            time.sleep(0.02)

        for i in range(100, 0, -2):
            if run_event.is_set():
                mot1_uhrzeigersinn.ChangeDutyCycle(i)
                time.sleep(0.02)
            else:
                break
            time.sleep(0.02)

        for i in range(0, 100, 2):
            if run_event.is_set():
                mot1_gegen_uhrzeigersinn.ChangeDutyCycle(i)
                time.sleep(0.02)
            else:
                break
            time.sleep(0.02)

        for i in range(100, 0, -2):
            if run_event.is_set():
                mot1_gegen_uhrzeigersinn.ChangeDutyCycle(i)
                time.sleep(0.02)
            else:
                break
            time.sleep(0.02)
        
def mot2(run_event):
    while True:

        for i in range(0, 100, 2):
            if run_event.is_set():
                mot2_uhrzeigersinn.ChangeDutyCycle(i)
                time.sleep(0.02)
            else:
                break
            time.sleep(0.02)

        for i in range(100, 0, -2):
            if run_event.is_set():
                mot2_uhrzeigersinn.ChangeDutyCycle(i)
                time.sleep(0.02)
            else:
                break
            time.sleep(0.02)

        for i in range(0, 100, 2):
            if run_event.is_set():
                mot2_gegen_uhrzeigersinn.ChangeDutyCycle(i)
                time.sleep(0.02)
            else:
                break
            time.sleep(0.02)

        for i in range(100, 0, -2):
            if run_event.is_set():
                mot2_gegen_uhrzeigersinn.ChangeDutyCycle(i)
                time.sleep(0.02)
            else:
                break
            time.sleep(0.02)

#----- Paralleles Starten der Funktionen durch Threads -----
# Event erstellen, das den Thread stoppen kann.
run_event = threading.Event()
# Eventflagge auf True setzen
run_event.set()

# Threads erstellen, die die Funktionen "mot1" und "mot2" aufrufen
# Argumente (args) werden als Tupel übergeben, daher das Komma,
# welches bei nur einem Element erforderlich ist.
t1 = threading.Thread(target = mot1, args = (run_event,))
t2 = threading.Thread(target = mot2, args = (run_event,))

# Threads starten
t1.start()
t2.start()

print("Programm gestartet. Beenden mit [Strg] + [C]")

#----- Abbrechen des Programms bei [Strg] + [C] -----
# Code unter dem try-except-Block wird erst nach
# der Tastenkombination [Strg] + [C] ausgeführt!
try:
    # Nur der except-Teil ist als Funktion relevant, jedoch
    # darf muss Code nach der try-Anweisung vorhanden sein.
    while True:
        time.sleep(0.1)
# Bei Tastenkombination [Strg] + [C]
except KeyboardInterrupt:
    print ("Programm wird beendet.")
    # Eventflagge auf False setzen
    run_event.clear()
    # Warten bis die Threads t1 und t2 eleminiert wurden
    t1.join
    t2.join
    mot1_uhrzeigersinn.stop()
    mot1_gegen_uhrzeigersinn.stop()
    mot2_uhrzeigersinn.stop()
    mot2_gegen_uhrzeigersinn.stop()
    print ("Programm erfolgreich beendet")
