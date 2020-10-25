import pygame
import math
import threading
import time

import snake
import engine

delta = 0
running = True

def time_thread_funtion():
    global delta
    global running

    while running:
        delta += 1
        time.sleep(0.05)

def main():
    global delta
    global running

    eng = engine.engine(512, 512, 16)
    clock = pygame.time.Clock()
    
    time_thread = threading.Thread(target=time_thread_funtion, args=())
    time_thread.start()

    while eng.running:
        if delta >= 1:
            eng.update()
            delta = 0

        eng.draw()
        running = eng.running

    time_thread.join()



if (__name__ == '__main__'):
    main()