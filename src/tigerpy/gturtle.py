import numpy as np
import pygame
import threading
import sys

__author__ = "Stephan Kessler"
__copyright__ = "Stephan Kessler"
__license__ = "MIT"

START_SPEED = 50

main_turtle = None
draw_thread_running = False
screen = None

#pip3 install -U -e C:\Users\npro9\git\tigerpy

class Turtle():
    def __init__(self) -> None:
        global START_SPEED
        self.x = 0
        self.y = 0
        self.angle = 0
        self.pen_down = True
        self.speed = START_SPEED
        self.shown = True
    # TODO
    pass  

class Color():
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    black = (0, 0, 0)

def makeTurtle() -> Turtle:
    global main_turtle 
    global draw_thread_running
    global screen
    draw_thread_running = True
    main_turtle = Turtle()
    (width, height) = (800, 800)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Turtle')
    pygame.display.flip()
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
    # TODO
    pass

def getY() -> int:
    # TODO
    pass

def setY(y) -> None:
    # TODO
    pass

def getPos() -> list:
    return [getX(), getY()]

def setPos(x, y) -> None:
    # TODO
    pass

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
    while draw_thread_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                draw_thread_running = False
        screen.fill(Color.white)
        pygame.display.update()