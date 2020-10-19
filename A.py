import sys 
sys.path.insert(1, 'dsp-modulo')

from thinkdsp import read_wave
from thinkdsp import decorate
import thinkplot
import numpy

audio = ""
waveAudio = read_wave("equipo1Hola.wav")

#Cantidad de letras
cantidadLetras = 0
tolerancia = 10
PrimerSegmento = []
PrimerSegmento.append(waveAudio.segment(start=0, duration=0.5))

frecuenciaCantidadLetras = [200, 300, 400, 800, 500, 600, 700]

for segmento in PrimerSegmento:
    espectroSegmento = segmento.make_spectrum()
    frecuenciasDominantes = []
    i = 0
    for amplitudEspectral in espectroSegmento.hs:
        if numpy.abs(amplitudEspectral) > 500:
            frecuenciasDominantes.append(espectroSegmento.fs[i])
        i = i + 1
    cantidadLetrasFrecuencia = 0
    for frecuencia in frecuenciasDominantes:
        for frecuenciaDTMF in frecuenciaCantidadLetras:
            if frecuencia > frecuenciaDTMF - tolerancia and frecuencia < frecuenciaDTMF + tolerancia:
                cantidadLetrasFrecuencia = frecuenciaDTMF
    if cantidadLetrasFrecuencia == 200:
        cantidadLetras = 8
    elif cantidadLetrasFrecuencia == 300:
        cantidadLetras = 6
    elif cantidadLetrasFrecuencia == 400:
        cantidadLetras = 5
    elif cantidadLetrasFrecuencia == 800:
        cantidadLetras = 3
    elif cantidadLetrasFrecuencia == 500:
        cantidadLetras = 7
    elif cantidadLetrasFrecuencia == 600:
        cantidadLetras = 4
    elif cantidadLetrasFrecuencia == 700:
        cantidadLetras = 2

#Tamaño del segmento
sizeSegmento = 0

SegundSegmento = []
SegundSegmento.append(waveAudio.segment(start=0.5, duration=0.3))

frecuenciaSegmento = [450, 700, 900]
tolerancia = 10

for segmento in SegundSegmento:
    espectroSegmento = segmento.make_spectrum()
    frecuenciasDominantes = []
    i = 0
    for amplitudEspectral in espectroSegmento.hs:
        if numpy.abs(amplitudEspectral) > 500:
            frecuenciasDominantes.append(espectroSegmento.fs[i])
        i = i + 1
    sizeSegmentoFrecuencia = 0
    for frecuencia in frecuenciasDominantes:
        for frecuenciaDTMF in frecuenciaSegmento:
            if frecuencia > frecuenciaDTMF - tolerancia and frecuencia < frecuenciaDTMF + tolerancia:
                sizeSegmentoFrecuencia = frecuenciaDTMF
    if sizeSegmentoFrecuencia == 450:
        sizeSegmento = 0.3
    elif sizeSegmentoFrecuencia == 700:
        sizeSegmento = 0.4
    elif sizeSegmentoFrecuencia == 900:
        sizeSegmento = 0.5

print(sizeSegmento)

#Letras
#letrasSegmento = []
#for i in range(cantidadLetras):
#    letrasSegmento.append(waveAudio.segment(start=0.8+i*sizeSegmento, duration=sizeSegmento))
#
#frecuenciaLetras = [200, 560, 920, 240, 600, 960, 280, 640, 1000, 320, 680, 1040, 360, 720, 1080, 400, 760, 1120, 480, 840, 1200, 520, 880]
#
#for segmento in letrasSegmento:
#    espectroSegmento = segmento.make_spectrum()
#    frecuenciasDominantes = []
#    i = 0
#    for amplitudEspectral in espectroSegmento.hs:
#        if numpy.abs(amplitudEspectral) > 500:
#            frecuenciasDominantes.append(espectroSegmento.fs[i])
#        i = i + 1
#    LetrasFrecuencia = 0
#    for frecuencia in frecuenciasDominantes:
#        for frecuenciaDTMF in frecuenciaLetras:
#            if frecuencia > frecuenciaDTMF - tolerancia and frecuencia < frecuenciaDTMF + tolerancia:
#                LetrasFrecuencia = frecuenciaDTMF
#    if LetrasFrecuencia == 200:
#        audio = audio + "A"
#    elif LetrasFrecuencia == 560:
#        audio = audio + "B"
#    elif LetrasFrecuencia == 920:
#        audio = audio + "C"
#    elif LetrasFrecuencia == 240:
#        audio = audio + "D"
#    elif LetrasFrecuencia == 600:
#        audio = audio + "E"
#    elif LetrasFrecuencia == 960:
#        audio = audio + "F"
#    elif LetrasFrecuencia == 280:
#        audio = audio + "G"
#    elif LetrasFrecuencia == 640:
#        audio = audio + "H"
#    elif LetrasFrecuencia == 1000:
#        audio = audio + "I"
#    elif LetrasFrecuencia == 320:
#        audio = audio + "J"
#    elif LetrasFrecuencia == 680:
#        audio = audio + "K"
#    elif LetrasFrecuencia == 1040:
#        audio = audio + "L"
#    elif LetrasFrecuencia == 360:
#        audio = audio + "M"
#    elif LetrasFrecuencia == 720:
#        audio = audio + "N"
#    elif LetrasFrecuencia == 1080:
#        audio = audio + "O"
#    elif LetrasFrecuencia == 400:
#        audio = audio + "P"
#    elif LetrasFrecuencia == 760:
#        audio = audio + "Q"
#    elif LetrasFrecuencia == 1120:
#        audio = audio + "R"
#    elif LetrasFrecuencia == 440:
#        audio = audio + "S"
#    elif LetrasFrecuencia == 800:
#        audio = audio + "T"
#    elif LetrasFrecuencia == 1160:
#        audio = audio + "U"
#    elif LetrasFrecuencia == 480:
#        audio = audio + "V"
#    elif LetrasFrecuencia == 840:
#        audio = audio + "W"
#    elif LetrasFrecuencia == 1200:
#        audio = audio + "X"
#    elif LetrasFrecuencia == 520:
#        audio = audio + "Y"
#    elif LetrasFrecuencia == 880:
#        audio = audio + "Z"
#
#print(audio)