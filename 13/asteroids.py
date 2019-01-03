import pyglet
import random
import math

WIDTH=1024 # 800
HEIGHT=768 # 600

ASTEROID_SPEED = 100
ASTEROID_ROTATION_SPEED = 3
SPACESHIP_ACCELERATION = 300
SPACESHIP_ROTATION_SPEED = 200

batch = pyglet.graphics.Batch()

def load_image(filename):
    image = pyglet.image.load(filename)
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2
    return image
 
spaceship_image = load_image('assets/PNG/playerShip2_red.png')
asteroid_images = { 
        1: [load_image('assets/PNG/Meteors/meteorGrey_tiny1.png'),
            load_image('assets/PNG/Meteors/meteorGrey_tiny2.png'),
           ],  
        2: [load_image('assets/PNG/Meteors/meteorGrey_small1.png'),
            load_image('assets/PNG/Meteors/meteorGrey_small2.png'),
           ],  
        3: [load_image('assets/PNG/Meteors/meteorGrey_med1.png'),
            load_image('assets/PNG/Meteors/meteorGrey_med2.png'),
           ],  
        4: [load_image('assets/PNG/Meteors/meteorGrey_big1.png'),
            load_image('assets/PNG/Meteors/meteorGrey_big2.png'),
            load_image('assets/PNG/Meteors/meteorGrey_big3.png'),
            load_image('assets/PNG/Meteors/meteorGrey_big4.png'),
           ],  
}

class SpaceObject:
    def __init__(self, image, x, y, x_speed, y_speed, rotation):
        self.sprite = pyglet.sprite.Sprite(image, batch=batch)

        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.rotation = rotation

    def tick(self, delta):
        if self.x > WIDTH:
            self.x = 0
        if self.x < 0:
            self.x = WIDTH
        if self.y > HEIGHT:
            self.y = 0
        if self.y < 0:
            self.y = HEIGHT

        self.x += self.x_speed * delta
        self.y += self.y_speed * delta
        self.sprite.x = self.x
        self.sprite.y = self.y
        self.sprite.rotation = self.rotation


class Asteroid(SpaceObject):
        def __init__(self, size):
            x, y = random.choice(
                    [   (0, random.randrange(HEIGHT)),
                        (random.randrange(WIDTH), 0)
                    ]
            )
            super().__init__(
                    image=random.choice(asteroid_images[size]),
                    x=x,
                    y=y,
                    x_speed=random.uniform(-ASTEROID_SPEED, ASTEROID_SPEED),
                    y_speed=random.uniform(-ASTEROID_SPEED, ASTEROID_SPEED),
                    rotation=random.uniform(0, 360),
                    )
            self.rotation_speed = random.uniform(
                    -ASTEROID_ROTATION_SPEED,
                    ASTEROID_ROTATION_SPEED)

        def tick(self, delta):
            self.rotation += self.rotation_speed
            super().tick(delta)

        # self.x = WIDTH/2
        # self.y = HEIGHT/2

        # self.x_speed = 0 # pixelů za sekundu
        # self.y_speed = 0
        # self.rotation = 0 # stupně (degrees)

class SpaceShip(SpaceObject):
        def __init__(self):
            super().__init__(
                    image=spaceship_image,
                    x=WIDTH/2,
                    y=HEIGHT/2,
                    x_speed=0,
                    y_speed=0,
                    rotation=0,
                    )

        def tick(self, delta):
            if pyglet.window.key.LEFT in pressed_keys:
                self.rotation -= SPACESHIP_ROTATION_SPEED*delta
            if pyglet.window.key.RIGHT in pressed_keys:
                self.rotation += SPACESHIP_ROTATION_SPEED*delta
            if pyglet.window.key.UP in pressed_keys:
                rot_rad = math.radians(self.rotation)
                self.x_speed += SPACESHIP_ACCELERATION*math.sin(rot_rad)*delta
                self.y_speed += SPACESHIP_ACCELERATION*math.cos(rot_rad)*delta

            super().tick(delta)

# objects = [Asteroid(), Asteroid(), SpaceShip()]

objects = list()
objects.append(SpaceShip())
for size in range(3):
    objects.append(Asteroid(1+size))

def draw():
    window.clear()
    for x_offset in (-window.width, 0, window.width):
        for y_offset in (-window.height, 9, window.height):
            pyglet.gl.glPushMatrix()
            pyglet.gl.glTranslatef(x_offset, y_offset, 0)
            batch.draw()
            pyglet.gl.glPopMatrix()

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

