#Advanced English Music Player

from pygame import mixer

mixer.init() # initialize mixer

mixer.music.load("E:\Songs\English\TIC TIC TAC.mp3")
mixer.music.play()

while True:
    print("By Default TIC TIC TAC is playing")
    print("-----Choose your song to play 1: Justin 2: Eminem 3: Enrique")
    print("-----Press <p> to pause the song")
    print("-----Press <r> to resume the song <res> to restart the song")
    print("-----Press <e> to exit playback")
    print("-----Press <low> <medium> <high> to set volume of song")

    query = input("Enter Your  Choice :->>> ")

    if query == '1':
        mixer.music.load("E:\Songs\English\JB\Baby (Ft. Ludacris).mp3")
        mixer.music.play()
    elif query == '2':
        mixer.music.load("E:\Songs\English\Eminem\Love The Way You Lie.mp3")
        mixer.music.play()
    elif query == '3':
        mixer.music.load("E:\Songs\English\TOKYO DRIFT THEME2.mp3")
        mixer.music.play()
    elif query == 'low':
        mixer.music.set_volume(0.1)
        print(mixer.music.get_volume())
    elif query == 'medium':
        mixer.music.set_volume(0.5)
        print(mixer.music.get_volume())
    elif query == 'high':
        mixer.music.set_volume(1.0)
        print(mixer.music.get_volume())
    elif query == 'res':
        mixer.music.rewind()
    elif query == 'p':
            mixer.music.pause()
    elif query == 'r':
            mixer.music.unpause()
    elif query == 'e':
            mixer.music.stop()
            break
