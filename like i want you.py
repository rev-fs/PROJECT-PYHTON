import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("\n""See you face to face, I'm thinking 'bout the days we used to be", 0.05),
        ("But I can't make a scene, but I can't make a scene", 0.07),
        ("See you face to face, I'm thinking 'bout the days we used to be", 0.05),
        ("But I can't make a scene, but I can't make it seem", 0.07),
        ("Like I want you", 0.16),
        ("You", 0.35),
        ("Even if it's true", 0.17),
        ("Even if it's true", 0.17),
    ]
    delays = [0.3, 6.0, 12.0, 18.0, 23.0, 27.0, 32.0, 41.0]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()
if __name__ == "__main__":
    sing_song()