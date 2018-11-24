# grafika.py

import pyglet
from math import sin

window = pyglet.window.Window()

obrazek = pyglet.image.load('jimi.png')
jimi = pyglet.sprite.Sprite(obrazek)
jimi.x = 225

obrazek2 = pyglet.image.load('hendrix.png')

def zpracuj_text(text):
    jimi.x = 225
    print(text)

def tik(t):
    print(jimi.x)
    jimi.x = jimi.x + t * 25
    jimi.y = abs(100 * sin(jimi.x / 5)) # Absolutní hodnota, sinus / 5...

def vykresli():
    window.clear()
    jimi.draw()

def zmen(t):
    jimi.image = obrazek2
    pyglet.clock.schedule_once(zmen_zpatky, 1)

def zmen_zpatky(t):
    jimi.image = obrazek
    pyglet.clock.schedule_once(zmen, 1)

def klik(x, y, tlacitko, mod):
    jimi.x = x
    jimi.y = y
    print(tlacitko, mod)


pyglet.clock.schedule_once(zmen, 1)

window.push_handlers(
        on_text=zpracuj_text,
        on_draw=vykresli,
        on_mouse_press=klik,
)

pyglet.clock.schedule_interval(tik, 1/30)

pyglet.app.run()

print('Hotovo!')

