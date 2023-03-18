import math
import pygame

screen_width = 1024
screen_height = 768

target = [319, 100]
initial_height = 150
target_distance = 512

gravity = 9.8
velocity = 90

angle = math.radians(45)
cos_theta = math.cos(angle)
sin_theta = math.sin(angle)
tan_theta = math.tan(angle)

def translate(coords, height):
    return (coords[0], height - coords[1])

def findT(a, b, c):
    D = math.sqrt(b * b - 4 * a * c)
    return max((-b + D) / (2 * a), (-b - D) / (2 * a))

def deltaTiming(start, final, d):
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + d
    return numbers

def calculate_trajectory(velocity, target, target_distance, gravity, initial_height):
    x, y = [], []

    _target = translate(target, screen_height)

    if (target[0] > 0 and target[1] > 0):
        target_distance = 0
        pygame.draw.circle(screen, (0, 255, 0), (_target[0], _target[1]), 10)
        velocity = (math.sqrt(4.9) * target[0]) / (cos_theta * math.sqrt(initial_height + tan_theta * target[0] - target[1]))

    if (target_distance > 0):
        pygame.draw.circle(screen, (0, 255, 0), (target_distance, screen_height), 10)
        velocity = (math.sqrt(4.9) * target_distance) / (cos_theta * math.sqrt(initial_height + tan_theta * target_distance))

    t_flight = findT((-0.5 * gravity), (velocity * sin_theta), initial_height)

    intervals = deltaTiming(0, t_flight, 0.001)

    for t in intervals:
        x.append(velocity * cos_theta * t)
        y.append(velocity * sin_theta * t - 0.5 * gravity * t * t)

    return x, y

def draw(x, y):
    for i in range(len(x)):
        pygame.draw.rect(screen, (0, 255, 0), (x[i], screen_height - y[i] - initial_height, 1, 1))
        pygame.display.flip()

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))

x, y = calculate_trajectory(velocity, target, target_distance, gravity, initial_height)
draw(x, y)

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = translate(pygame.mouse.get_pos(), screen_height)
            x, y = calculate_trajectory(velocity, pos, target_distance, gravity, initial_height)
            draw(x, y)
