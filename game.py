import pickle
import random
from itertools import cycle
from sprite_classes import *
from pygame import mixer

# Initialize the pygame
pygame.init()

# Configuration
font_title = 'fonts/04B_30__.TTF'
font_text = 'fonts/04B_03__.TTF'
BLINK_EVENT = pygame.USEREVENT + 0
# Define paths to find objects

path_profiles = 'profiles/'
path_main_design = 'display_animations/'

# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Background
background = pygame.image.load(path_main_design + 'Tinder_egg_screen_full.png').convert_alpha()
background = pygame.transform.smoothscale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
# controllers
controllers = pygame.image.load(path_main_design + 'controller.png').convert_alpha()
controllers = pygame.transform.smoothscale(controllers, (SCREEN_WIDTH * 0.4676, SCREEN_HEIGHT * 0.612))
# score
scoring = pygame.image.load(path_main_design + 'Score_Frames.png').convert_alpha()
scoring = pygame.transform.smoothscale(scoring, (SCREEN_WIDTH * 0.4676, SCREEN_HEIGHT * 0.612))
# bar_text
bar = pygame.image.load(path_main_design + 'bar_text.png').convert_alpha()
bar = pygame.transform.smoothscale(bar, (SCREEN_WIDTH * 0.4676 * 0.97, SCREEN_HEIGHT * 0.612 * 0.095))
# text_space
text_space = pygame.image.load(path_main_design + 'text_space.png').convert_alpha()
text_space = pygame.transform.smoothscale(text_space, (SCREEN_WIDTH * 0.4676, SCREEN_HEIGHT * 0.612 * 0.25))


# Define sprite groups
intro_1_group = pygame.sprite.Group(Stars1())
intro_2_group = pygame.sprite.Group(Stars2())
cover_group = pygame.sprite.Group(Cover())
group_open = pygame.sprite.Group(Opening())
close_group = pygame.sprite.Group(Close())
group_grade_1 = pygame.sprite.Group(OneStars())
group_grade_2 = pygame.sprite.Group(TwoStars())
group_grade_3 = pygame.sprite.Group(ThreeStars())
# Sprites animations eggs
kino_group = pygame.sprite.Group(Kino())
art_group = pygame.sprite.Group(Art())
beach_group = pygame.sprite.Group(Beach())
park_group = pygame.sprite.Group(Park())
koffee_group = pygame.sprite.Group(Koffee())
pub_group = pygame.sprite.Group(Pub())
sado_group = pygame.sprite.Group(Sado())
fitness_group = pygame.sprite.Group(Fitness())


# Definitions
def draw_image(images=None, coordinates=(0, 0)):
    if images is not None:
        screen.blit(images, coordinates)
    pygame.display.update()


def draw_stars(index):
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    if (index % 2) == 0:
        intro_1_group.update()
        intro_1_group.draw(screen)
    else:
        intro_2_group.update()
        intro_2_group.draw(screen)
    pygame.display.update()
    clock.tick(20)


def draw_cover():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    cover_group.update()
    cover_group.draw(screen)
    pygame.display.update()
    clock.tick(15)


def draw_opening():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    for _ in range(Opening().numb_images - 1):
        group_open.update()
        group_open.draw(screen)
        pygame.display.update()
        clock.tick(5)


def draw_closing():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    for _ in range(Close().numb_images - 1):
        close_group.update()
        close_group.draw(screen)
        pygame.display.update()
        clock.tick(10)


def draw_selection_one_stars():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    for _ in range(OneStars().numb_images - 1):
        group_grade_1.update()
        group_grade_1.draw(screen)
        pygame.display.update()
        clock.tick(FR)


def draw_selection_two_stars():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    for _ in range(TwoStars().numb_images - 1):
        group_grade_2.update()
        group_grade_2.draw(screen)
        pygame.display.update()
        clock.tick(FR)


def draw_selection_three_stars():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    for _ in range(ThreeStars().numb_images - 1):
        group_grade_3.update()
        group_grade_3.draw(screen)
        pygame.display.update()
        clock.tick(FR)


def reproduce_kino():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    kino_group.update()
    kino_group.draw(screen)
    pygame.display.update()
    clock.tick(20)


def reproduce_beach():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    beach_group.update()
    beach_group.draw(screen)
    pygame.display.update()
    clock.tick(20)


def reproduce_art():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    art_group.update()
    art_group.draw(screen)
    pygame.display.update()
    clock.tick(20)


def reproduce_pub():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    pub_group.update()
    pub_group.draw(screen)
    pygame.display.update()
    clock.tick(20)


def reproduce_sado():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    sado_group.update()
    sado_group.draw(screen)
    pygame.display.update()
    clock.tick(20)


def reproduce_park():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    park_group.update()
    park_group.draw(screen)
    pygame.display.update()
    clock.tick(20)


def reproduce_fitness():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    fitness_group.update()
    fitness_group.draw(screen)
    pygame.display.update()
    clock.tick(20)


def reproduce_koffee():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    koffee_group.update()
    koffee_group.draw(screen)
    pygame.display.update()
    clock.tick(20)


# Text displaying tools
def display_text_info(name, age, coordinates, color):
    font = pygame.font.Font(font_title, 45)
    text_surface = font.render('{}, {}'.format(name, age), True, color)
    screen.blit(text_surface, coordinates)
    pygame.display.update()


def display_score_info(name, score, y, color):
    font = pygame.font.Font(font_title, 45)
    text_surface = font.render('{}'.format(name), True, color)
    text_surface_2 = font.render('{}'.format(score), True, color)
    screen.blit(text_surface, (SCREEN_WIDTH * 0.465, y))
    screen.blit(text_surface_2, (SCREEN_WIDTH * 0.715, y))
    pygame.display.update()


def text_ani(string, coordinates):
    # line_space = 2
    font = pygame.font.Font(font_text, 36)
    x, y = coordinates
    # y = y * line_space  # shift text down by one line
    char = ''  # new string that will take text one char at a time. Not the best variable name I know.
    letter = 0
    count = 0
    for i in range(len(string)):
        pygame.event.clear()
        pygame.time.wait(80)  # change this for faster or slower text animation
        char = char + string[letter]
        text = font.render(char, False, black, grey)  # First tuple is text color, second tuple is background color
        text_rect = text.get_rect(topleft=(x, y))
        text_rect.center = (x, y)
        screen.blit(text, text_rect)
        pygame.display.update()  # update only the text just added without removing previous lines.
        count += 1
        letter += 1


def plot_split_text(string, limit, coordinates):
    chunks = get_chunks(string, limit)
    chunks = [(n, len(n)) for n in chunks]
    x, y = coordinates
    for i, txt in enumerate(chunks):
        text_ani(txt[0], (x, (y + i * 27)))
    pygame.time.delay(750)


def get_chunks(s, max_length):
    start = 0
    end = 0
    while start + max_length < len(s) and end != -1:
        end = s.rfind(" ", start, start + max_length + 1)
        yield s[start:end]
        start = end + 1
    yield s[start:]


# files tools
def update_scores(dic_previous, dic_to_update):
    for element in dic_previous.items():
        dic_to_update[element[0]]['score'] = element[1]
    return dic_to_update


# Main events
def starting_menu():
    # draw_image(cover, (SCREEN_WIDTH / 2.71, SCREEN_HEIGHT / 10.8))
    font = pygame.font.Font(font_title, 29)
    on_text_surface = font.render('Press Any Key To Start', True, pygame.Color('green3'))
    blink_rect = on_text_surface.get_rect()
    blink_rect.center = (SCREEN_WIDTH * 0.605, SCREEN_HEIGHT * 0.775)
    off_text_surface = pygame.Surface(blink_rect.size)
    blink_surfaces = cycle([on_text_surface, off_text_surface])
    blink_surface = next(blink_surfaces)
    pygame.time.set_timer(BLINK_EVENT, 1000)
    mixer.Sound('music/first_try_song.wav').play()
    click_to_play = False
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
        draw_cover()
    mixer.stop()


def instructions():
    draw_image(controllers, (SCREEN_WIDTH / 2.71, SCREEN_HEIGHT / 10.8))
    pygame.time.delay(500)
    draw_image(background, (0, 0))


def get_profiles():
    # Load all profiles names from folders
    profile_dic = {}
    names = os.listdir('profiles/')
    previous_scores = False
    try:
        with open('meta_data/scores_dictionary.pkl', 'rb') as f:
            dic_previous = pickle.load(f)
        previous_scores = True
    except FileNotFoundError:
        print("No file existing")

    for i, name_profile in enumerate(names):
        path = os.path.join(path_profiles, name_profile, '{}_complete.png'.format(name_profile.split("_")[0]))
        path_mini = os.path.join(path_profiles, name_profile, '{}_mini.png'.format(name_profile.split("_")[0]))
        path_txt = os.path.join(path_profiles, name_profile, '{}_text.txt'.format(name_profile))
        with open(path_txt) as f:
            lines = f.readlines()
        image = pygame.image.load(path).convert_alpha()
        image = pygame.transform.smoothscale(image, (SCREEN_WIDTH * 0.452, SCREEN_HEIGHT * 0.358))
        mini = pygame.image.load(path_mini).convert_alpha()
        mini = pygame.transform.smoothscale(mini, (SCREEN_WIDTH * 0.455 * 0.15, SCREEN_HEIGHT * 0.365 * 0.15))
        prof = {'id': name_profile[:-4],
                'name': lines[0][:-1],
                'age': lines[1][:-1],
                'text': {0: lines[2][:-1].upper(),
                         1: lines[3][:-1].upper(),
                         2: lines[4][:-1].upper()
                         },
                'image': image,
                'mini_image': mini,
                'sound': None,
                'score': 0
                }
        profile_dic['Profile_{}'.format(i + 1)] = prof
    if previous_scores:
        profile_dic = update_scores(dic_previous, profile_dic)

    return profile_dic


def run_profiles(profiles_dictionary):
    for i, profile in enumerate(list(profiles_dictionary.keys())):
        draw_image(profiles_dictionary[profile]['image'], (SCREEN_WIDTH / 2.655, SCREEN_HEIGHT / 10))
        pygame.time.delay(1000)
        # draw_opening()
        display_text_info(profiles_dictionary[profile]['name'],
                          profiles_dictionary[profile]['age'],
                          (SCREEN_WIDTH * 0.40, SCREEN_HEIGHT * 0.505),
                          white)
        plot_split_text(profiles_dictionary[profile]['text'][random.randint(0, 2)], 23,
                        (SCREEN_WIDTH * 0.605, SCREEN_HEIGHT * 0.572))
        scored = False
        while not scored:
            if profiles_dictionary[profile]['id'] == 'Kino':
                reproduce_kino()
            elif profiles_dictionary[profile]['id'] == 'Beach':
                reproduce_beach()
            elif profiles_dictionary[profile]['id'] == 'Pub':
                reproduce_pub()
            elif profiles_dictionary[profile]['id'] == 'Park':
                reproduce_park()
            elif profiles_dictionary[profile]['id'] == 'Sado':
                reproduce_sado()
            elif profiles_dictionary[profile]['id'] == 'Fitness':
                reproduce_fitness()
            elif profiles_dictionary[profile]['id'] == 'Koffee':
                reproduce_koffee()
            elif profiles_dictionary[profile]['id'] == 'Art':
                reproduce_art()
            draw_stars(i)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        profiles_dictionary[profile]['score'] += 1
                        scored = True
                        draw_selection_one_stars()
                        draw_image(text_space, (SCREEN_WIDTH * 0.3675, SCREEN_HEIGHT * 0.553))
                        pygame.time.delay(500)
                        draw_image(bar, (SCREEN_WIDTH * 0.3755, SCREEN_HEIGHT * 0.4956))
                    elif event.key == pygame.K_DOWN:
                        profiles_dictionary[profile]['score'] += 2
                        scored = True
                        draw_selection_two_stars()
                        draw_image(text_space, (SCREEN_WIDTH * 0.3675, SCREEN_HEIGHT * 0.553))
                        draw_image(bar, (SCREEN_WIDTH * 0.3755, SCREEN_HEIGHT * 0.4956))
                    elif event.key == pygame.K_RIGHT:
                        profiles_dictionary[profile]['score'] += 3
                        scored = True
                        draw_selection_three_stars()
                        draw_image(text_space, (SCREEN_WIDTH * 0.3675, SCREEN_HEIGHT * 0.553))
                        draw_image(bar, (SCREEN_WIDTH * 0.3755, SCREEN_HEIGHT * 0.4956))

        draw_closing()


def ending_screen(profiles_dictionary):
    draw_image(scoring, (SCREEN_WIDTH / 2.71, SCREEN_HEIGHT / 10.8))
    pygame.time.delay(100)
    run = True
    while run:
        sort_orders = sorted(profiles_dictionary.items(), key=lambda x: x[1]['score'], reverse=False)
        for i in range(len(sort_orders)):
            pygame.time.delay(1000)
            draw_image(sort_orders[i][1]['mini_image'], (SCREEN_WIDTH * 0.39, SCREEN_HEIGHT * (1 - 0.0715 * i) - 395))
            display_score_info(sort_orders[i][1]['name'],
                               sort_orders[i][1]['score'],
                               SCREEN_HEIGHT * (1 - 0.0715 * i) - 385,
                               white)
        run = False
    pygame.time.delay(5000)


def save_dictionary(results):
    summary = {}
    for element in results.items():
        summary[element[0]] = element[1]['score']
    with open('meta_data/scores_dictionary.pkl', 'wb') as f:
        pickle.dump(summary, f)


# Full body
def main():
    clock = pygame.time.Clock()
    play = True
    while play:
        clock.tick(60)
        draw_image(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    play = False
        # Run menu
        starting_menu()
        # Display instructions
        instructions()
        # Define profiles from folders structure
        profile_dic = get_profiles()
        # Star running profiles and get scores
        run_profiles(profile_dic)
        # Display accumulated results
        ending_screen(profile_dic)
        # Save results
        save_dictionary(profile_dic)


if __name__ == '__main__':
    main()
