# grafika.py

import pyglet

window = pyglet.window.Window()

def zpracuj_text(text):
    print(text)

def tik(t):
    print(t)

window.push_handlers(on_text=zpracuj_text)

pyglet.clock.schedule_interval(tik, 1/30)

pyglet.app.run()

print('Hotovo!')

