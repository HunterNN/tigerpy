import numpy as np
import pygame
import threading
import sys
import os
import resource
from tigerpy.vector2d import Vector2D


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

    def forward(self, distance) -> None:
        # kreiere Schrittvektor (x = 0 und y = self.speed)
        # kreiere Positionsvektor der Schildkröte (x = self.x und y = self.y)
        Vector2D.__sizeof__
        for i in range(distance):
            # addiere Schrittvektor auf Positionsvektor und speichere das Ergebnis in Positionsvektor wieder ab
            # Schildkröte neu positionieren mit Positionsvektor self.setPos(x.., y...)
            if self.shown:
                sleep(20)

    def back(self, distance) -> None:
        # TODO
        pass

    def showTurtle(self) -> None:
        self.shown = True

    def hideTurtle(self) -> None:
        self.shown = False

    def home(self) -> None:
        # TODO
        pass

    def left(self, angle) -> None:
        # TODO
        pass

    def right(self, angle) -> None:
        # TODO
        pass

    def penDown(self) -> None:
        self.pen_down = True

    def penUp(self) -> None:
        self.pen_down = False

    def leftArc(self, selfradius, angle) -> None:
        # TODO
        pass    

    def rightArc(self, radius, angle) -> None:
        # TODO
        pass

    def setSpeed(self, speed) -> None:
        # TODO
        pass

    def getX(self) -> int:
        return self.x

    def setX(self, x) -> None:
        self.x = x

    def getY(self) -> int:
        return self.y

    def setY(self, y) -> None:
        self.y = y

    def getPos(self) -> list:
        return [self.getX(), self.getY()]

    def setPosition(self, x, y) -> None:
        self.setX(x)
        self.setY(y)

    def moveTo(self, x, y) -> None:
        # TODO
        pass

    def getRotation(self) -> int:
        self.angle

    def getDirectionToPoint(self, x, y) -> int:
        vector1 = Vector2D(self.getX(), self.getY())
        return vector1.angleBetweenDeg(Vector2D(x, y))

    def getHeading(self) -> int:
        return getDirectionToPoint(self.getX() + 1, self.getY())


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
    main_turtle.forward(distance)

def back(distance) -> None:
    main_turtle.back(distance)

def showTurtle() -> None:
    main_turtle.showTurtle()

def hideTurtle() -> None:
    main_turtle.hideTurtle()

def home() -> None:
    main_turtle.home()

def left(angle) -> None:
    main_turtle.left(angle)

def right(angle) -> None:
    main_turtle.right(angle)

def penDown() -> None:
    main_turtle.penDown()

def penUp() -> None:
    main_turtle.penUp()

def leftArc(radius, angle) -> None:
    main_turtle.leftArc(radius, angle)

def leftCircle(radius) -> None:
    leftArc(radius, 360)

def rightArc(radius, angle) -> None:
    main_turtle.rightArc(radius, angle)

def rightCircle(radius) -> None:
    rightArc(radius, 360)

def setSpeed(speed) -> None:
    main_turtle.setSpeed(speed)

def getX() -> int:
    return main_turtle.getX()

def setX(x) -> None:
    main_turtle.setX(x)

def getY() -> int:
    return main_turtle.getY()

def setY(y) -> None:
    main_turtle.setY(y)

def getPos() -> list:
    return main_turtle.getPos()

def setPosition(x, y) -> None:
    main_turtle.setPosition(x, y)

def moveTo(x, y) -> None:
    main_turtle.moveTo(x, y)

def getRotation() -> int:
    return main_turtle.getRotation()

def getDirectionToPoint(x, y) -> int:
    return main_turtle.getDirectionToPoint(x, y)


def getHeading() -> int:
    return main_turtle.getHeading()


# Private Functions

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
    return (cords[0] + WINDOW_SIZE[0] / 2, cords[1] * (-1) + WINDOW_SIZE[1] / 2)
