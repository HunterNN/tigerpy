import numpy as np
import pygame
import threading
import sys
import os
import resource

__author__ = "Stephan Kessler"
__copyright__ = "Stephan Kessler"
__license__ = "MIT"

START_SPEED = 50
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
WINDOW_SIZE = (800, 800)

main_turtle = None
draw_thread_running = False
screen = None


class Turtle():
    def __init__(self, type) -> None:
        global START_SPEED
        self.image_path = type
        self.x = 0
        self.y = 0
        self.angle = 0
        self.pen_down = True
        self.speed = START_SPEED
        self.shown = True
        image = pygame.image.load(self.image_path)
        self.image = pygame.transform.smoothscale(
            image, (int(image.get_rect().width / 2), int(image.get_rect().height / 2)))

    def draw(self, surface):
        rect = self.image.get_rect()
        surface.blit(self.image, _convertToPygameCords(
            (self.x - rect.centerx, self.y - rect.centery)))


class Color():
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    black = (0, 0, 0)

class TurtleTypes():
    bear = os.path.join(SCRIPT_PATH, "resources/images/turtles/bear.png")
    buffalo = os.path.join(SCRIPT_PATH, "resources/images/turtles/buffalo.png")
    chick = os.path.join(SCRIPT_PATH, "resources/images/turtles/chick.png")
    chicken = os.path.join(SCRIPT_PATH, "resources/images/turtles/chicken.png")
    cow = os.path.join(SCRIPT_PATH, "resources/images/turtles/cow.png")
    crocodile = os.path.join(SCRIPT_PATH, "resources/images/turtles/crocodile.png")
    dog = os.path.join(SCRIPT_PATH, "resources/images/turtles/dog.png")
    duck = os.path.join(SCRIPT_PATH, "resources/images/turtles/duck.png")
    elephant = os.path.join(SCRIPT_PATH, "resources/images/turtles/elephant.png")
    frog = os.path.join(SCRIPT_PATH, "resources/images/turtles/frog.png")
    giraffe = os.path.join(SCRIPT_PATH, "resources/images/turtles/giraffe.png")
    goat = os.path.join(SCRIPT_PATH, "resources/images/turtles/goat.png")
    gorilla = os.path.join(SCRIPT_PATH, "resources/images/turtles/gorilla.png")
    hippo = os.path.join(SCRIPT_PATH, "resources/images/turtles/hippo.png")
    horse = os.path.join(SCRIPT_PATH, "resources/images/turtles/horse.png")
    monkey = os.path.join(SCRIPT_PATH, "resources/images/turtles/monkey.png")
    moose = os.path.join(SCRIPT_PATH, "resources/images/turtles/moose.png")
    narwhal = os.path.join(SCRIPT_PATH, "resources/images/turtles/narwhal.png")
    owl = os.path.join(SCRIPT_PATH, "resources/images/turtles/owl.png")
    panda = os.path.join(SCRIPT_PATH, "resources/images/turtles/panda.png")
    parrot = os.path.join(SCRIPT_PATH, "resources/images/turtles/parrot.png")
    penguin = os.path.join(SCRIPT_PATH, "resources/images/turtles/penguin.png")
    pig = os.path.join(SCRIPT_PATH, "resources/images/turtles/pig.png")
    rabbit = os.path.join(SCRIPT_PATH, "resources/images/turtles/rabbit.png")
    rhino = os.path.join(SCRIPT_PATH, "resources/images/turtles/rhino.png")
    sloth = os.path.join(SCRIPT_PATH, "resources/images/turtles/sloth.png")
    snake = os.path.join(SCRIPT_PATH, "resources/images/turtles/snake.png")
    walrus = os.path.join(SCRIPT_PATH, "resources/images/turtles/walrus.png")
    whale = os.path.join(SCRIPT_PATH, "resources/images/turtles/whale.png")
    zebra = os.path.join(SCRIPT_PATH, "resources/images/turtles/zebra.png")


def makeTurtle(type = TurtleTypes.bear) -> Turtle:
    global main_turtle
    global draw_thread_running
    global screen
    draw_thread_running = True
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('Turtle')
    pygame.display.flip()
    main_turtle = Turtle(type)
    thread = threading.Thread(target=_drawThread, args=())
    thread.start()
    return main_turtle

def forward(distance) -> None:
    # TODO
    pass


def back(distance) -> None:
    # TODO
    pass


def showTurtle() -> None:
    # TODO
    pass


def hideTurtle() -> None:
    # TODO
    pass


def home() -> None:
    # TODO
    pass


def left(angle) -> None:
    # TODO
    pass


def right(angle) -> None:
    # TODO
    pass


def penDown() -> None:
    # TODO
    pass


def penUp() -> None:
    # TODO
    pass


def leftArc(radius, angle) -> None:
    # TODO
    pass


def leftCircle(radius) -> None:
    leftArc(radius, 360)


def rightArc(radius, angle) -> None:
    # TODO
    pass


def rightCircle(radius) -> None:
    rightArc(radius, 360)


def setSpeed(speed) -> None:
    # TODO
    pass


def getX() -> int:
    # TODO
    pass


def setX(x) -> None:
    main_turtle.x = x


def getY() -> int:
    # TODO
    pass


def setY(y) -> None:
    main_turtle.y = y


def getPos() -> list:
    return [getX(), getY()]


def setPos(x, y) -> None:
    setX(x)
    setY(y)


def moveTo(x, y) -> None:
    # TODO
    pass


def getRotation() -> int:
    # TODO
    pass


def direction(x, y) -> int:
    vector1 = np.array(getPos())
    vector2 = np.array([x, y])
    return _angle_between(vector1, vector2)


def heading() -> int:
    return direction(getX() + 1, getY())

# Private Functions


def _unit_vector(vector):
    return vector / np.linalg.norm(vector)


def _angle_between(v1, v2):
    v1_u = _unit_vector(v1)
    v2_u = _unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))


def _drawThread():
    global draw_thread_running
    global main_turtle
    global screen
    while draw_thread_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                draw_thread_running = False
        screen.fill(Color.white)
        main_turtle.draw(screen)
        pygame.display.update()


def _convertToPygameCords(cords):
    return (cords[0] + WINDOW_SIZE[0] / 2, cords[1] + WINDOW_SIZE[1] / 2)
