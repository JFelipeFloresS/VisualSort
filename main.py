import pygame
import random as rd
import time

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 50, 50)
GREEN = (50, 220, 50)

pygame.init()
pygame.font.init()
width = 800
height = 350
win = pygame.display.set_mode([width, height])
font = pygame.font.SysFont('Tahoma', 24)

sorted = False

def create_list():
    lst = []
    for i in range(16):
        lst.append(rd.randrange(1, 100))
    return lst

def print_list(lst, selected=None, limit=0):
    global width, height
    for i, item in enumerate(lst):
        distance_between_cols = 25
        col_width = 25
        start_x = 10 + (i * (col_width + distance_between_cols))
        col_height = item * 2
        start_y = (height - 50) - col_height
        if selected is not None and i in selected:
            colour = RED
        elif i >= len(lst) - limit + 1:
            colour = GREEN
        else:
            colour = BLACK
        pygame.draw.rect(win, colour, [start_x, start_y, col_width, col_height])
        textsurface = font.render(str(item), False, colour)
        win.blit(textsurface, (start_x, 310))

def insert_sort(lst):
    global sorted
    for i in range(1, len(lst)):
        key_el = lst[i]
        pos = i
        win.fill(WHITE)
        print_list(lst, selected=[pos, pos - 1])
        pygame.display.update()
        time.sleep(0.5)
        while pos > 0 and lst[pos - 1] > key_el:
            lst[pos] = lst[pos - 1]
            pos -= 1
            win.fill(WHITE)
            print_list(lst, selected=[pos, pos - 1])
            pygame.display.update()
            time.sleep(0.5)

        lst[pos] = key_el
    sorted = True

def bubble_sort(lst):
    global sorted
    swapped = True
    limit = 1
    while swapped:
        swapped = False
        for i in range(0, len(lst) - limit):
            win.fill(WHITE)
            print_list(lst, selected=[i, i + 1], limit=limit)
            pygame.display.update()
            time.sleep(0.1)
            if lst[i] > lst[i + 1]:
                swapped = True
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
                win.fill(WHITE)
                print_list(lst, selected=[i, i + 1], limit=limit)
                pygame.display.update()
                time.sleep(0.1)

        limit += 1
    sorted = True

def main():
    global sorted
    rd_list = create_list()
    print(rd_list)
    while True:
        win.fill(WHITE)

        print_list(rd_list)

        if not sorted:
            bubble_sort(rd_list)
            #insert_sort(rd_list)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

main()
