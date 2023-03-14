import math
import pygame

initial_height = 100

screen_width = 1024
screen_height = 768

velocity = 90
angle = math.radians(45)
gravity = 9.8

def findT(a, b, c):
    D = math.sqrt(b * b - 4 * a * c)
    return max((-b + D) / (2 * a), (-b - D) / (2 * a))

def deltaTiming(start, final, d):
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + d

    return numbers

def calculate_trajectory(velocity, theta, gravity, initial_height):
    x, y = [], []

    t_flight = findT((-0.5 * gravity), (velocity * math.sin(theta)), initial_height)

    intervals = deltaTiming(0, t_flight, 0.001)

    for t in intervals:
        x.append(velocity * math.cos(theta) * t)
        y.append(velocity * math.sin(theta) * t - 0.5 * gravity * t * t)

    return x, y

def draw(x, y):
    for i in range(len(x)):
        pygame.draw.rect(screen, (0, 255, 0), (x[i], screen_height - y[i] - initial_height, 1, 1))

        pygame.display.flip()

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))

x, y = calculate_trajectory(velocity, angle, gravity, initial_height)
draw(x, y)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
