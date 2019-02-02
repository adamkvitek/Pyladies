import pyglet

window = pyglet.window.Window()

label = pyglet.text.Label('Ahoj!', x=100, y=200)

@window.event
def on_text(text):
    #print(text)
    #print(label.x)
    #label.x =
    label.text = label.text + text

@window.event
def on_key_press(key_code, modifier):
    print(key_code)
    if key_code == pyglet.window.key.BACKSPACE:
        label.text = label.text[:-1]

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()
