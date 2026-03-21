import pygame
import time
import os

pygame.mixer.init()

def play_audio(file_path):

    pygame.mixer.music.load(str(file_path))
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.05)

    # important for windows: release file lock
    pygame.mixer.music.unload()

    try:
        os.remove(file_path)
    except Exception as e:
        print("Delete error:", e)


def stop_audio():
    pygame.mixer.music.stop()


def is_playing():
    return pygame.mixer.music.get_busy()