import pygame
from itertools import cycle

# Intialize the pygame
pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 750

black = (0, 0, 0)
white = (255, 255, 255)

# Define paths to find objects

path_profiles = 'profiles/'
path_main_design = 'profiles_design/'

# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Background
background = pygame.image.load(path_main_design + 'main.jpg')

# Load all profiles
Profile_1 = {'name': 'arty_egg',
             'image': pygame.image.load(path_profiles + 'arty_egg.jpg'),
             'sound': None,
             'score': 0}
Profile_2 = {'name': 'bar_egg',
             'image': pygame.image.load(path_profiles + 'bar_egg.jpg'),
             'sound': None,
             'score': 0}
Profile_3 = {'name': 'bohemian_egg',
             'image': pygame.image.load(path_profiles + 'bohemian_egg.jpg'),
             'sound': None,
             'score': 0}
Profile_4 = {'name': 'cine_egg',
             'image': pygame.image.load(path_profiles + 'cine_egg.jpg'),
             'sound': None,
             'score': 0}
Profile_5 = {'name': 'starbucks_egg',
             'image': pygame.image.load(path_profiles + 'starbucks_egg.jpg'),
             'sound': None,
             'score': 0}
Profile_6 = {'name': 'sado_egg',
             'image': pygame.image.load(path_profiles + 'sado_egg.jpg'),
             'sound': None,
             'score': 0}

profiles = [Profile_1, Profile_2, Profile_3, Profile_4, Profile_5, Profile_6]


def draw_image(image=None):
    screen.fill(black)
    if image is not None:
        screen.blit(image, (0, 0))
    pygame.display.update()


def starting_menu():
    click_to_play = False
    screen_rect = screen.get_rect()
    font = pygame.font.Font(VISITOR_TTF_FILENAME, 50)
    on_text_surface = font.render('Press Any Key To Start', True, pygame.Color('green3'))
    blink_rect = on_text_surface.get_rect()
    blink_rect.center = screen_rect.center
    off_text_surface = pygame.Surface(blink_rect.size)
    blink_surfaces = cycle([on_text_surface, off_text_surface])
    blink_surface = next(blink_surfaces)
    pygame.time.set_timer(BLINK_EVENT, 1000)

    while not click_to_play:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    click_to_play = True
                elif event.key == pygame.K_DOWN:
                    click_to_play = True
                elif event.key == pygame.K_RIGHT:
                    click_to_play = True
            if event.type == BLINK_EVENT:
                blink_surface = next(blink_surfaces)

        screen.blit(blink_surface, blink_rect)
        pygame.display.update()


def run_profiles():
    for profile in profiles:
        profile_to_show = profile['image']
        draw_image(profile_to_show)

        scored = False
        while not scored:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        profile['score'] += 1
                        scored = True
                    elif event.key == pygame.K_DOWN:
                        profile['score'] += 2
                        scored = True
                    elif event.key == pygame.K_RIGHT:
                        profile['score'] += 3
                        scored = True
        print(profile['name'], 'Calificación acumulada:', profile['score'])


VISITOR_TTF_FILENAME = 'visitor1.ttf'
BLINK_EVENT = pygame.USEREVENT + 0


def main():
    clock = pygame.time.Clock()

    play = True
    while play:
        clock.tick(60)
        draw_image(background)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    play = False

        starting_menu()
        # Star running profiles and get scores
        run_profiles()


if __name__ == '__main__':
    main()
