# Faça um Programa em python que abra e reproduza o áudio de um arquivo MP3.

print(f"{'DESAFIO 21':=^20}")
print("Tocando um MP3")


# 1° FORMA
# Antes de importar o módulo rode o comando abaixo no terminal
# $ pip install playsound

#from playsound import playsound
#playsound('./DESAFIOS/MUSIC/ex021.mp3')


# 2° FORMA
# Antes de importar o módulo rode o comando abaixo no terminal
# $ pip install pygame

#import pygame
#pygame.mixer.init()
#pygame.init()
#pygame.mixer.music.load('./DESAFIOS/MUSIC/ex021.mp3')
#pygame.mixer.music.play()
#pygame.event.wait()


# 3° FORMA
# Antes de importar o módulo rode o comando abaixo no terminal
# $ pip install python-vlc

#import vlc
#vlc.MediaPlayer('./DESAFIOS/MUSIC/ex021.mp3').play()
#input()
