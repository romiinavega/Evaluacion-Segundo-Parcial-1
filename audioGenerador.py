import sys
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate


frecuenciaSegmento = SinSignal(freq=900, amp=1, offset=0)
frecuenciaTexto = SinSignal(freq=600, amp=1, offset=0)
frecuenciaH = SinSignal(freq=640, amp=1, offset=0)
frecuenciaO = SinSignal(freq=1080, amp=1, offset=0)
frecuenciaL = SinSignal(freq=1040, amp=1, offset=0)
frecuenciaA = SinSignal(freq=200, amp=1, offset=0)


#para la cantidad de letras
wave_Texto = frecuenciaTexto.make_wave(duration=0.5, start=0, framerate=44100)

#para el Segmento
wave_Segmento = frecuenciaSegmento.make_wave(duration=0.3, start=0.5, framerate=44100)

#H
wave_H = frecuenciaH.make_wave(duration=0.5, start=0.8, framerate=44100)

#O
wave_O = frecuenciaO.make_wave(duration=0.5, start=1.3, framerate=44100)

#L
wave_L = frecuenciaL.make_wave(duration=0.5, start=1.8, framerate=44100)

#A
wave_A = frecuenciaA.make_wave(duration=0.5, start=2.3, framerate=44100)




wave_audio = wave_Segmento + wave_Texto + wave_H + wave_O + wave_L + wave_A

wave_audio.write("equipo1Hola.wav")