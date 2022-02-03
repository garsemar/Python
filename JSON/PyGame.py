import pygame
import sys
import simplejson as json

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
game_font = pygame.font.Font(None, 32)

# Rectangles
red_surface = pygame.Surface([200, 200])
red_surface.fill((240, 80, 54))
red_rectangle = red_surface.get_rect(center=(150, 180))

blue_surface = pygame.Surface([200, 200])
blue_surface.fill((0, 123, 194))
blue_rectangle = blue_surface.get_rect(center=(450, 180))

# Data
data = {
    'red': 0,
    'blue': 0
}

try:
    with open('clicker_score.txt') as score_file:
        data = json.load(score_file)
except:
    print('No file created yet')

# Text
red_score_surf = game_font.render(f'Clicks: {data["red"]}', True, 'Black')
red_score_rect = red_score_surf.get_rect(center=(150, 320))

blue_score_surf = game_font.render(f'Clicks: {data["blue"]}', True, 'Black')
blue_score_rect = blue_score_surf.get_rect(center=(450, 320))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open('clicker_score.txt', 'w') as score_file:
                json.dump(data, score_file)
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if red_rectangle.collidepoint(event.pos):
                data['red'] += 1
                red_score_surf = game_font.render(f'Clicks: {data["red"]}', True, 'Black')
                red_score_rect = red_score_surf.get_rect(center=(150, 320))
            if blue_rectangle.collidepoint(event.pos):
                data['blue'] += 1
                blue_score_surf = game_font.render(f'Clicks: {data["blue"]}', True, 'Black')
                blue_score_rect = blue_score_surf.get_rect(center=(450, 320))

    screen.fill((245, 255, 252))
    screen.blit(red_surface, red_rectangle)
    screen.blit(blue_surface, blue_rectangle)

    screen.blit(red_score_surf, red_score_rect)
    screen.blit(blue_score_surf, blue_score_rect)

    pygame.display.update()
    clock.tick(60)
