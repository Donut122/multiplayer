from ast import While
import socket
import threading
import pygame
import os
import random
import time

s = socket.socket()
host = input("enter the hostname: ")
port = (5050)
print("looking for host")
time.sleep(0.2)
s.connect((host, port))
print("host found!\nstarting game...")


width, height = 1920, 1080
fps = 60
pygame.init()
WIN = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption("Game running @ " + str(width) + " x" + str(height))
clock = pygame.time.Clock()
pygame.display.init()
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 50)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
p1 = pygame.Rect(width / 4, height / 2, 25, 25)
p2 = pygame.Rect(width / 1.5, height / 2, 25, 25)

def send_data():
    while True:
        time.sleep(0.1)
        s.send(bytes(str(p2.x), "utf-8"))
        s.send(bytes(str(p2.y) , "utf-8"))

def recive_data():
    while True:
        data = s.recv(1024).decode("utf-8")
        p1.x = int(data)
        data = s.recv(1024).decode("utf-8")
        p1.y = int(data)

def draw_graphics():
    WIN.fill(white)
    pygame.draw.rect(WIN, green, p1)
    pygame.draw.rect(WIN, blue, p2)
    pygame.display.update()
thread = threading.Thread(target=recive_data)
thread.start()
thread = threading.Thread(target=send_data)
thread.start()
while True:
    clock.tick(fps)
    draw_graphics()
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_w]:
        p2.y -= 1
    if key_pressed[pygame.K_s]:
        p2.y += 1
    if key_pressed[pygame.K_d]:
        p2.x += 1
    if key_pressed[pygame.K_a]:
        p2.x -= 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                break
