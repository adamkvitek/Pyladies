from random import randrange
import pyglet

TILE_SIZE = 64

window = pyglet.window.Window()
label = pyglet.text.Label('Hi!', x=100, y=200)

green = pyglet.image.load('green.png')
apple = pyglet.image.load('apple.png')

left_bottom = pyglet.image.load('snake-tiles/left-bottom.png')

tiles = {}
for start in ['bottom', 'end', 'left', 'right', 'top']:
    for end in ['bottom', 'dead', 'left', 'right', 'tongue', 'top', 'end']:
        image = pyglet.image.load('snake-tiles/' + start + '-' + end + '.png')
        tiles[start, end] = image
print(tiles)


class State:
    def __init__(self):
        self.snake = [(1, 2), (2, 2), (3, 2), (3, 3), (3, 4), (3, 5), (4, 5)]
        self.food = []
        self.add_food()
        self.add_food()
        self.direction = 0, -1
        self.alive = True

    def grow(self, dt):
        x, y = self.snake[-1]
        dir_x, dir_y = self.direction
        x = x + dir_x
        y = y + dir_y
        if self.alive:
            if x < 0:
                self.alive = False
            elif y < 0:
                self.alive = False
            elif x >= window.width / TILE_SIZE:
                self.alive = False
            elif y >= window.height / TILE_SIZE:
                self.alive = False
            elif (x, y) in self.snake:
                self.alive = False
            else:
                self.snake.append((x, y))
                if (x, y) in self.food:
                    self.food.remove((x, y))
                    self.add_food()
                else:
                    del self.snake[0]


    def add_food(self):
        for n in range(100):
            x = randrange(window.width // TILE_SIZE)
            y = randrange(window.height // TILE_SIZE)
            if (x, y) in self.snake:
                pass
            else:
                self.food.append((x, y))
                return

state = State()

@window.event
def on_text(text):
    label.text = label.text + text

@window.event
def on_key_press(key_code, modifier):
    if key_code == pyglet.window.key.UP:
        state.direction = 0, 1
    elif key_code == pyglet.window.key.DOWN:
        state.direction = 0, -1
    elif key_code == pyglet.window.key.LEFT:
        state.direction = -1, 0
    elif key_code == pyglet.window.key.RIGHT:
        state.direction = 1, 0

@window.event
def on_draw():
    window.clear()
    label.draw()

    for prev, now, next in zip(
        [None] + state.snake[:-1],
        state.snake,
        state.snake[1:] + [None],
    ):
        start = direction(now, prev)
        end = direction(now, next)
        if not state.alive and end == 'end':
            end = 'dead'
        x, y = now
        tiles[start, end].blit(
            x * TILE_SIZE, y * TILE_SIZE,
            width=TILE_SIZE, height=TILE_SIZE,
        )
    for x, y in state.food:
        apple.blit(
                x * TILE_SIZE, y * TILE_SIZE,
                width=TILE_SIZE, height=TILE_SIZE,
    )

def direction(a, b):
    if b == None:
        return 'end'
    else:
        a_x, a_y = a
        b_x, b_y = b
        if a_x == b_x + 1:
            return 'left'
        elif a_x == b_x - 1:
            return 'right'
        elif a_y == b_y + 1:
            return 'bottom'
        elif a_y == b_y - 1:
            return 'top'
        else:
            return 'end'

pyglet.clock.schedule_interval(state.grow, 1/3)

pyglet.app.run()
