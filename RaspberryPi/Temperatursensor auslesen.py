#!/usr/bin/env python
# coding: utf8
import time
import threading

DS12B20="/sys/bus/w1/devices/10-0008034155fb/w1_slave"

def Leser():
    while True :

        file = open(DS12B20, "r")
        data = file.read()
        file.close

        # Die Funktion partition() zerlegt eine Zeichenkette in ihre Einzelteile,
        # anhand des Teilungstextes "t=" Diese Teile werden in einem Tupel geliefert
        # Das erste Element0 liefert den Text bis zum Teilungstext " t="
        # Das dritte Element2 "reading" liefert den Text nach dem Teilungstext " t="
        
        tupel = data.partition(" t=")
        reading = tupel[2]

        # Temperatur auf 1/2 °C genau Runden
        temperature = float(reading) / 1000.0
        temperature_rounded = round(temperature * 2.0) / 2.0

        print(temperature_rounded)

        time.sleep(1)

# Temperatur in parallelem Thread auslesen
t_Leser = threading.Thread(target = Leser)
t_Leser.start()
