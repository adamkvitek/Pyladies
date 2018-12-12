import pyglet
import math

WIDTH=1024 # 800
HEIGHT=768 # 600

batch = pyglet.graphics.Batch()

class SpaceShip:
        def __init__(self):
            image_url = 'assets/PNG/playerShip2_red.png'
            image = pyglet.image.load(image_url)
            image.anchor_x = image.width // 2
            image.anchor_y = image.height // 2
            self.sprite = pyglet.sprite.Sprite(image, batch=batch)
            self.x = WIDTH/2
            self.y = HEIGHT/2

            self.x_speed = 0 # pixelů za sekundu
            self.y_speed = 0
            self.rotation = 0 # stupně (degrees)

        def tick(self, delta):
            if pyglet.window.key.LEFT in pressed_keys:
                self.rotation -= 90*delta
            if pyglet.window.key.RIGHT in pressed_keys:
                self.rotation += 90*delta
            if pyglet.window.key.UP in pressed_keys:
                rot_rad = math.radians(self.rotation)
                self.x_speed += 20*delta*math.sin(rot_rad)
                self.y_speed += 20*delta*math.cos(rot_rad)

            self.x += self.x_speed * delta
            self.y += self.y_speed * delta
            self.sprite.x = self.x
            self.sprite.y = self.y
            self.sprite.rotation = self.rotation

objects = [SpaceShip()]

def draw():
    window.clear()
    batch.draw()

def tick(delta): # parametr kolik ubylo času - pomocí rozdílu - delta = rozdíl
    for obj in objects:
        obj.tick(delta)

pressed_keys = set() # Množina do které vkládáme klávesy

def key_pressed(key, mod):
    pressed_keys.add(key)

def key_released(key, mod):
    pressed_keys.discard(key)
    

pyglet.clock.schedule(tick)

window = pyglet.window.Window(width=WIDTH, height=HEIGHT)
window.push_handlers(
        on_draw=draw,
        on_key_press=key_pressed,
        on_key_release=key_released,
        )
pyglet.app.run()

