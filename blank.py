import pygame
import sys
import threading
import time

pygame.init()

screen_width = 400
screen_height = 300
bg_color = (200, 233, 233)
font_color = (43, 48, 62)
name = "Cooper Caruso"
#upgrades are cost, power and auto power
upgrades = {
    0: [0, 1, 0],
    1: [20, 3, 1],
    2: [100, 7, 2],
    3: [250, 15, 5],
    4: [800, 20, 13],
    5: [2000, 35, 30],
    6: [5000, 55, 75],
    7: [20000, 75, 200],
    8: [75000, 125, 500],
    9: [145000, 250, 1250],
    10: [500000, 1500, 3000],
    11: [5000000, 6000, 10000],
    12: [20000000, 35000, 50000]
}
curr = 0
next = curr + 1
next_cost = upgrades[next][0]
power = upgrades[curr][1]
auto = upgrades[curr][2]
count = 0

def auto():
  global count, auto
  while True:
    time.sleep(1)
    count += auto

auto_thread = threading.Thread(target=auto)
auto_thread.start()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Cooper's Clicker")

img = pygame.image.load("boxing-glove.png")
img = pygame.transform.scale(img, (100, 100))

font = pygame.font.Font(None, 30)
font_small = pygame.font.Font(None, 20)

upgrade = font.render(" UPGRADE ", True, font_color)
rect = upgrade.get_rect(topleft=(35, 235))

def draw_text(text, x, y):
  text_surface = font.render(text, True, font_color)
  screen.blit(text_surface, (x, y))

def draw_small_text(text, x, y):
  text_surface = font_small.render(text, True, font_color)
  screen.blit(text_surface, (x, y))

def draw_img():
  screen.blit(img, (screen_width // 2 - 50, screen_height // 2 - 50))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                if count < next_cost:
                    print('NOT ENOUGH DOGE COINS')
                elif curr == 11:
                    print('NO MORE UPGRADES AVAILABLE')
                else:
                    print("UPGRADE Button was pressed")
                    count -= next_cost
                    curr += 1
                    next = curr + 1
                    if curr == 11:
                        pass
                    else:
                        next_cost = upgrades[next][0]
                    power = upgrades[curr][1]
                    auto = upgrades[curr][2]
            if screen_width // 2 - 50 <= event.pos[0] <= screen_width // 2 + 50 and screen_height // 2 - 50 <= event.pos[1] <= screen_height // 2 + 50:
                count += power

    screen.fill(bg_color)
    draw_img()
    draw_text(f"By: {name}", 10, 10)
    draw_text("Doge Coins: " + str(count), 10, 50)
    draw_text(f"Power: {power}", 10, 90)
    draw_text(f"Auto: {auto}", 10, 120)
    draw_text(f"Upgrade Cost: {next_cost}", 15, 265)
    draw_small_text(f"Upgrades: {curr}/11", 275, 135)
    screen.blit(upgrade, rect)
    pygame.draw.rect(screen, (0, 0, 0), rect, 2)
    pygame.display.flip()

pygame.quit()
sys.exit()