import pygame
import time
import os

# import sys

def flip():
    squares[mouse_y][mouse_x] ^= 1
    if mouse_x > 0:             squares[mouse_y][mouse_x - 1] ^= 1
    if mouse_x < modules_x - 1: squares[mouse_y][mouse_x + 1] ^= 1
    if mouse_y > 0:             squares[mouse_y - 1][mouse_x] ^= 1
    if mouse_y < modules_y - 1: squares[mouse_y + 1][mouse_x] ^= 1

def fill_color():
    for x in range(modules_x):
        for y in range(modules_y):
            if squares[y][x] == 0:
                pygame.draw.rect(screen, BACK_COLOR, pygame.Rect(x * SIZE_X, y * SIZE_Y, SIZE_X, SIZE_Y))
            else:
                pygame.draw.rect(screen, FORE_COLOR, pygame.Rect(x * SIZE_X, y * SIZE_Y, SIZE_X, SIZE_Y))

def draw_borders():
    for x in range(modules_x):
        for y in range(modules_y):
            pygame.draw.rect(screen, BORDER_COLOR, pygame.Rect(x * SIZE_X, y * SIZE_Y, SIZE_X, SIZE_Y),  BORDER_WIDTH)

def draw_colors():
    fill_color()
    draw_borders()

def show_possible():
    pygame.draw.rect(screen, selected_color, pygame.Rect(mouse_x * SIZE_X, mouse_y * SIZE_Y, SIZE_X, SIZE_Y))
    if mouse_x > 0:             pygame.draw.rect(screen, selected_color, pygame.Rect((mouse_x - 1) * SIZE_X, mouse_y * SIZE_Y, SIZE_X, SIZE_Y))
    if mouse_x < modules_x - 1: pygame.draw.rect(screen, selected_color, pygame.Rect((mouse_x + 1) * SIZE_X, mouse_y * SIZE_Y, SIZE_X, SIZE_Y))
    if mouse_y > 0:             pygame.draw.rect(screen, selected_color, pygame.Rect(mouse_x * SIZE_X, (mouse_y - 1) * SIZE_Y, SIZE_X, SIZE_Y))
    if mouse_y < modules_y - 1: pygame.draw.rect(screen, selected_color, pygame.Rect(mouse_x * SIZE_X, (mouse_y + 1) * SIZE_Y, SIZE_X, SIZE_Y))
    draw_borders()

def show_it():
    if squares[mouse_y][mouse_x] == 1:
        pygame.draw.rect(screen, BACK_COLOR, pygame.Rect(mouse_x * SIZE_X, mouse_y * SIZE_Y, SIZE_X, SIZE_Y))
    else:
        pygame.draw.rect(screen, selected_color, pygame.Rect(mouse_x * SIZE_X, mouse_y * SIZE_Y, SIZE_X, SIZE_Y))
    if mouse_x > 0:
        if squares[mouse_y][mouse_x - 1] == 1:
            pygame.draw.rect(screen, BACK_COLOR, pygame.Rect((mouse_x - 1) * SIZE_X, mouse_y * SIZE_Y, SIZE_X, SIZE_Y))
        else:
            pygame.draw.rect(screen, selected_color, pygame.Rect((mouse_x - 1) * SIZE_X, mouse_y * SIZE_Y, SIZE_X, SIZE_Y))        
    if mouse_x < modules_x - 1:
        if squares[mouse_y][mouse_x + 1] == 1:
            pygame.draw.rect(screen, BACK_COLOR, pygame.Rect((mouse_x + 1) * SIZE_X, mouse_y * SIZE_Y, SIZE_X, SIZE_Y))
        else:
            pygame.draw.rect(screen, selected_color, pygame.Rect((mouse_x + 1) * SIZE_X, mouse_y * SIZE_Y, SIZE_X, SIZE_Y))
    if mouse_y > 0:
        if squares[mouse_y - 1][mouse_x] == 1:
            pygame.draw.rect(screen, BACK_COLOR, pygame.Rect(mouse_x * SIZE_X, (mouse_y - 1) * SIZE_Y, SIZE_X, SIZE_Y))
        else:
            pygame.draw.rect(screen, selected_color, pygame.Rect(mouse_x * SIZE_X, (mouse_y - 1) * SIZE_Y, SIZE_X, SIZE_Y))    
    if mouse_y < modules_y - 1:
        if squares[mouse_y + 1][mouse_x] == 1:
            pygame.draw.rect(screen, BACK_COLOR, pygame.Rect(mouse_x * SIZE_X, (mouse_y + 1) * SIZE_Y, SIZE_X, SIZE_Y))
        else:
            pygame.draw.rect(screen, selected_color, pygame.Rect(mouse_x * SIZE_X, (mouse_y + 1) * SIZE_Y, SIZE_X, SIZE_Y))
    draw_borders()

def get_start():
    # dummy = 0
    while True:
        try:
            dummy = int(input("Game levels \n0 - test, \n1 - easy, \n2 - medium, \n3 - impossible\n\nYour choice: "))
        except:
            dummy = -1
        if -1 < dummy < 4: return dummy
    
os.system("cls")

segment_bulk = get_start()
# segment_bulk = 1
print("\nGame nawigation")
print("Keyboard:")
print("Esc - ending game")
print("r - restart\n")
print("Mouse:")
print("Left button - change color")
print("Right button - show what will change")
print("Right button with Shift - show how it will be\n")
print("Goal is change color for all squares\n")
modules_x = 3 + 2 * segment_bulk
modules_y = 1 + 2 * segment_bulk
SEGMENT_SIZE = 50 + 25 * (4 - segment_bulk)
SIZE_X = SIZE_Y = SEGMENT_SIZE
DISPLAY_WIDTH = modules_x * SIZE_X
DISPLAY_HIGHT = modules_y * SIZE_Y
DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HIGHT)

FORE_COLOR = (0, 224, 0)
BACK_COLOR = (0, 128, 255)
SELECT_COLOR = (128,0,128)
BORDER_COLOR = (0, 0, 0)
BORDER_WIDTH = 1

LEFT_BUTTON = 1
RIGHT_BUTTON = 3

pygame.init()
screen = pygame.display.set_mode(DISPLAY_SIZE)
screen.fill(BACK_COLOR)
pygame.display.set_caption('Change color !!!')
draw_borders()
squares = [[0 for x in range(modules_x) ] for y in range(modules_y)]
status_left_button = False
status_right_button = False
mouse_button = 0
key_shift = False
running = True
max_suma = modules_x * modules_y
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not (status_left_button or status_right_button):
                mouse_button = event.button
                if mouse_button == LEFT_BUTTON: status_left_button = True
                if mouse_button == RIGHT_BUTTON: status_right_button = True
            else:
                mouse_button = 0
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_button = event.button
            if mouse_button == RIGHT_BUTTON:
                status_right_button = False
                if status_left_button:
                    mouse_button = 0
            if mouse_button == LEFT_BUTTON:
                status_left_button = False
                mouse_button = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]: break
    if keys[pygame.K_r]:
        squares = [[0 for x in range(modules_x) ] for y in range(modules_y)]
        draw_colors()
    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
        key_shift = True
    else:
        key_shift = False
    if mouse_button != 0:
        if mouse_button == RIGHT_BUTTON:
            if status_right_button:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                mouse_x = mouse_x // SIZE_X
                mouse_y = mouse_y // SIZE_Y
                # print("wciśnięty prawy = pokaż zaznaczenie", mouse_x, mouse_y)
                if key_shift:
                    selected_color = FORE_COLOR
                    show_it()
                else:
                    selected_color = SELECT_COLOR
                    show_possible()
            else:
                # print("puszczony prawy = przywrócenie kolorów", mouse_x, mouse_y)
                draw_colors()
        elif  mouse_button == LEFT_BUTTON:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mouse_x = mouse_x // SIZE_X
            mouse_y = mouse_y // SIZE_Y
            # print("inwersja kolorów", mouse_x, mouse_y)
            flip()
            draw_colors()
            suma = 0
            for square in squares:
                suma += sum(square)
            if suma == max_suma:
                pygame.display.set_caption('*** GAME OVER ***')
                pygame.display.flip()
                print("\nGame over !!!")
                time.sleep(5)
                running = False
        mouse_button = 0
    pygame.display.flip()
pygame.quit()

# sys.exit()
