import pyglet
import random
import math

WIDTH=1024 # 800
HEIGHT=768 # 600

ASTEROID_SPEED = 100
ASTEROID_ROTATION_SPEED = 3
ASTEROID_RADIUSES = {
        1: 5,
        2: 14,
        3:20,
        4: 42,
}
SPACESHIP_ACCELERATION = 300
SPACESHIP_ROTATION_SPEED = 200
SPACESHIP_RADIUS = 40
SPACESHIP_RELOAD_TIME = 0.3
LASER_SPEED = 500
LASER_RADIUS = 5
LASER_LIFETIME = 3

batch = pyglet.graphics.Batch()

def load_image(filename):
    image = pyglet.image.load(filename)
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2
    return image
 
spaceship_image = load_image('assets/PNG/playerShip2_red.png')
laser_image = load_image('assets/PNG/Lasers/laserBlue06.png')
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
    def __init__(self, image, x, y, x_speed, y_speed, rotation, radius):
        self.sprite = pyglet.sprite.Sprite(image, batch=batch)

        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.rotation = rotation
        self.radius = radius

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

    def overlaps(self, another):
        a, b = self, another

        # distance_x
        s, l = min(a.x, b.x), max(a.x, b.x)
        dx = min(l-s, (s+WIDTH)-l)

        # distance_y
        s, l = min(a.y, b.y), max(a.y, b.y)
        dy = min(l-s, (s+WIDTH)-l)

        d = math.sqrt(dx**2 + dy**2)
        d_max = a.radius + b.radius

        return d < d_max

    def destroy(self):
        objects.remove(self)
        self.sprite.delete()

class Asteroid(SpaceObject):
        def __init__(self, size):
            self.size = size
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
                    radius=ASTEROID_RADIUSES[size],
                    )
            self.rotation_speed = random.uniform(
                    -ASTEROID_ROTATION_SPEED,
                    ASTEROID_ROTATION_SPEED)

        def tick(self, delta):
            self.rotation += self.rotation_speed
            super().tick(delta)

        def destroy(self, laser):
            split_speed_factor = 0.1
            split_x_speed = -laser.y_speed * split_speed_factor
            split_y_speed = laser.x_speed * split_speed_factor
            if self.size > 1:
                for i in range(2):
                    asteroid = Asteroid(self.size-1)
                    asteroid.x = self.x
                    asteroid.y = self.y
                    asteroid.x_speed = self.x_speed + split_x_speed
                    asteroid.y_speed = self.y_speed + split_y_speed
                    objects.append(asteroid)

                    split_x_speed = -split_x_speed
                    split_y_speed = -split_y_speed

            super().destroy()

class SpaceShip(SpaceObject):
    def __init__(self):
        self.loading = 0
        super().__init__(
        image=spaceship_image,
        x=WIDTH/2,
        y=HEIGHT/2,
        x_speed=0,
        y_speed=0,
        rotation=0,
        radius= SPACESHIP_RADIUS
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
        if pyglet.window.key.SPACE in pressed_keys:
            self.shoot()

        if self.loading > 0:
            self.loading -= delta

        super().tick(delta)
        for obj in objects:
            if isinstance(obj, Asteroid):
                if obj.overlaps(self):
                    self.destroy()

    def shoot(self):
        if self.loading <= 0:
            laser = Laser(self)
            objects.append(laser)
            self.loading += SPACESHIP_RELOAD_TIME

class Laser(SpaceObject):
    def __init__(self, ship):
        rot_rad = math.radians(ship.rotation)
        self.lifetime = LASER_LIFETIME
        super().__init__(
                image=laser_image,
                x=ship.x + math.sin(rot_rad)*ship.radius,
                y=ship.y + math.cos(rot_rad)*ship.radius,
                x_speed=ship.x_speed + LASER_SPEED*math.sin(rot_rad),
                y_speed=ship.y_speed + LASER_SPEED*math.cos(rot_rad),
                rotation=ship.rotation,
                radius=LASER_RADIUS,
        )

    def tick(self, delta):
        self.lifetime -= delta
        super().tick(delta)
        if(self.lifetime <= 0):
            self.destroy()
        else:
            for obj in objects:
                if isinstance(obj, Asteroid):
                    if obj.overlaps(self):
                        obj.destroy(self)
                        self.destroy()
                        break

# objects = [Asteroid(), Asteroid(), SpaceShip()]

objects = list()
objects.append(SpaceShip())
#for size in range(3):
    #objects.append(Asteroid(1+size))
for size in range(2):
    objects.append(Asteroid(4))

def draw_circle(obj):
    iterations = 20
    s = math.sin(2*math.pi / iterations)
    c = math.cos(2*math.pi / iterations)

    dx, dy = obj.radius, 0

    pyglet.gl.glBegin(pyglet.gl.GL_LINE_STRIP)
    for i in range(iterations+1):
        pyglet.gl.glVertex2f(obj.x+dx, obj.y+dy)
        dx, dy = (dx*c - dy*s), (dy*c + dx*s)
    pyglet.gl.glEnd()

def draw():
    window.clear()
    for x_offset in (-window.width, 0, window.width):
        for y_offset in (-window.height, 9, window.height):
            pyglet.gl.glPushMatrix()
            pyglet.gl.glTranslatef(x_offset, y_offset, 0)
            batch.draw()
            #for obj in objects:
            #    draw_circle(obj)
            pyglet.gl.glPopMatrix()

def tick(delta): # parametr which indicates passed time - using the difference - delta = difference
    for obj in objects:
        obj.tick(delta)

pressed_keys = set() # Group in which we add keys

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

