import pickle
import random
import time
from itertools import cycle
from sprite_classes import *
from pygame import mixer

# Initialize the pygame
pygame.init()
pygame.display.set_caption('Single Club Pululo (Elkin Lover)')
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
background2 = pygame.image.load(path_main_design + 'Tinder_egg_screen_full_2.png').convert_alpha()
background2 = pygame.transform.smoothscale(background2, (SCREEN_WIDTH, SCREEN_HEIGHT))
background3 = pygame.image.load(os.path.join(path_main_design, 'cortinilla_media',
                                             'to_dark', "cortinilla_82.png")).convert_alpha()
background3 = pygame.transform.smoothscale(background3, (SCREEN_WIDTH * 0.4676, SCREEN_HEIGHT * 0.612))
# score
scoring = pygame.image.load(path_main_design + 'Score_Frames.png').convert_alpha()
scoring = pygame.transform.smoothscale(scoring, (SCREEN_WIDTH * 0.4676, SCREEN_HEIGHT * 0.612))
# bar_text
bar = pygame.image.load(path_main_design + 'bar_text.png').convert_alpha()
bar = pygame.transform.smoothscale(bar, (SCREEN_WIDTH * 0.4676 * 0.97, SCREEN_HEIGHT * 0.612 * 0.095))
# text_space
text_space = pygame.image.load(path_main_design + 'text_space.png').convert_alpha()
text_space = pygame.transform.smoothscale(text_space, (SCREEN_WIDTH * 0.4676, SCREEN_HEIGHT * 0.612 * 0.25))
# score_screen
bar_score = pygame.image.load(path_main_design + 'score_bar_black.png').convert_alpha()
bar_score = pygame.transform.smoothscale(bar_score, (SCREEN_WIDTH * 0.452, SCREEN_HEIGHT * 0.096))

# Define sprite groups
controllers_group = pygame.sprite.Group(Controllers())
intro_1_group = pygame.sprite.Group(Stars1())
intro_2_group = pygame.sprite.Group(Stars2())
cover_group = pygame.sprite.Group(Cover())
# Closing
close_profile_1 = pygame.sprite.Group(Close1())
close_profile_2 = pygame.sprite.Group(Close2())
close_profile_3 = pygame.sprite.Group(Close3())
close_profile_4 = pygame.sprite.Group(Close4())
# Transitions
cover_to_instructions = pygame.sprite.Group(Covertoinstructions())
close_to_score_group = pygame.sprite.Group(Closebigscreen())

# Stars
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

# Sprites animations eggs
credits_elkin = pygame.sprite.Group(Credits1())
credits_pao = pygame.sprite.Group(Credits2())
credits_miguel = pygame.sprite.Group(Credits3())
credits_ramona = pygame.sprite.Group(Credits4())


# Definitions
def draw_image(images=None, coordinates=(0, 0)):
    if images is not None:
        screen.blit(images, coordinates)
    pygame.display.update()


# Draw stars
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
    clock.tick(FRA)


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


def draw_cover():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    cover_group.update()
    cover_group.draw(screen)
    pygame.display.update()
    clock.tick(15)


def draw_controllers():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    controllers_group.update()
    controllers_group.draw(screen)
    pygame.display.update()
    clock.tick(5)


def draw_controllers_2():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    for _ in range(Controllers().numb_images * 3):
        controllers_group.update()
        controllers_group.draw(screen)
        pygame.display.update()
        clock.tick(5)


# Transitions
def draw_cover_to_instructions():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    for _ in range(Covertoinstructions().numb_images - 1):
        cover_to_instructions.update()
        cover_to_instructions.draw(screen)
        pygame.display.update()
        clock.tick(80)


# Closing
def draw_closing_1():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    for _ in range(Close1().numb_images - 1):
        close_profile_1.update()
        close_profile_1.draw(screen)
        pygame.display.update()
        clock.tick(13)


def draw_closing_2():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    for _ in range(Close2().numb_images - 1):
        close_profile_2.update()
        close_profile_2.draw(screen)
        pygame.display.update()
        clock.tick(13)


def draw_closing_3():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    for _ in range(Close3().numb_images - 1):
        close_profile_3.update()
        close_profile_3.draw(screen)
        pygame.display.update()
        clock.tick(13)


def draw_closing_4():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    for _ in range(Close4().numb_images - 1):
        close_profile_4.update()
        close_profile_4.draw(screen)
        pygame.display.update()
        clock.tick(13)


def draw_closing_score():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    for _ in range(Closebigscreen().numb_images - 1):
        close_to_score_group.update()
        close_to_score_group.draw(screen)
        pygame.display.update()
        clock.tick(50)


# Credits
def credits_1():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    for _ in range(Credits1().numb_images * 4):
        credits_elkin.update()
        credits_elkin.draw(screen)
        pygame.display.update()
        clock.tick(10)


def credits_2():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    for _ in range(Credits2().numb_images * 4):
        credits_pao.update()
        credits_pao.draw(screen)
        pygame.display.update()
        clock.tick(10)


def credits_3():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    for _ in range(Credits3().numb_images * 4):
        credits_miguel.update()
        credits_miguel.draw(screen)
        pygame.display.update()
        clock.tick(10)


def credits_4():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    for _ in range(Credits4().numb_images * 3):
        credits_ramona.update()
        credits_ramona.draw(screen)
        pygame.display.update()
        clock.tick(10)


# Profiles
def reproduce_kino():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    kino_group.update()
    kino_group.draw(screen)
    pygame.display.update()
    clock.tick(FRA)


def reproduce_beach():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    beach_group.update()
    beach_group.draw(screen)
    pygame.display.update()
    clock.tick(FRA)


def reproduce_art():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    art_group.update()
    art_group.draw(screen)
    pygame.display.update()
    clock.tick(FRA)


def reproduce_pub():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    pub_group.update()
    pub_group.draw(screen)
    pygame.display.update()
    clock.tick(FRA)


def reproduce_sado():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    sado_group.update()
    sado_group.draw(screen)
    pygame.display.update()
    clock.tick(FRA)


def reproduce_park():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    park_group.update()
    park_group.draw(screen)
    pygame.display.update()
    clock.tick(FRA)


def reproduce_fitness():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    fitness_group.update()
    fitness_group.draw(screen)
    pygame.display.update()
    clock.tick(FRA)


def reproduce_koffee():
    # Creating the sprites and groups
    clock = pygame.time.Clock()
    koffee_group.update()
    koffee_group.draw(screen)
    pygame.display.update()
    clock.tick(FRA)


# Text displaying tools
def display_text_info(name, age, coordinates, color):
    font = pygame.font.Font(font_title, 27)
    text_surface = font.render('{}, {}'.format(name, age), True, color)
    screen.blit(text_surface, coordinates)
    pygame.display.update()


def display_score_info(name, score, y, color):
    # Scores screen
    font = pygame.font.Font(font_title, 32)
    text_surface = font.render('{}'.format(name), True, color)
    text_surface_2 = font.render('{}'.format(score), True, color)
    screen.blit(text_surface, (SCREEN_WIDTH * 0.465, y))
    screen.blit(text_surface_2, (SCREEN_WIDTH * 0.715, y))
    pygame.display.update()


def text_ani(string, coordinates):
    # line_space = 2
    font = pygame.font.Font(font_text, 23)
    x, y = coordinates
    # y = y * line_space  # shift text down by one line
    char = ''  # new string that will take text one char at a time. Not the best variable name I know.
    letter = 0
    for i in range(len(string)):
        pygame.event.clear()
        pygame.time.wait(65)  # change this for faster or slower text animation
        char = char + string[letter]
        text = font.render(char, False, black, grey)  # First tuple is text color, second tuple is background color
        screen.blit(text, text.get_rect(topleft=(x, y)).move(40, 0))
        pygame.display.update()  # update only the text just added without removing previous lines.
        if string[letter] != ' ':
            sound = pygame.mixer.Sound("music/typing_sound_3.wav")
            channel = pygame.mixer.Channel(0)
            channel.play(sound, -1)
            channel.set_volume(0.15)
            pygame.time.wait(20)
            mixer.stop()
        letter += 1


def plot_split_text(string, limit, coordinates):
    chunks = get_chunks(string, limit)
    chunks = [(n, len(n)) for n in chunks]
    x, y = coordinates
    for i, txt in enumerate(chunks):
        text_ani(txt[0], (x, (y + i * 19)))
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


#################################################################################################################


# Main events
def starting_menu():
    # draw_image(cover, (SCREEN_WIDTH / 2.71, SCREEN_HEIGHT / 10.8))
    font = pygame.font.Font(font_title, 18)
    on_text_surface = font.render('Press Any Key To Start', True, pygame.Color('green3'))
    blink_rect = on_text_surface.get_rect()
    blink_rect.center = (SCREEN_WIDTH * 0.605, SCREEN_HEIGHT * 0.775)
    off_text_surface = pygame.Surface(blink_rect.size)
    blink_surfaces = cycle([on_text_surface, off_text_surface])
    blink_surface = next(blink_surfaces)
    pygame.time.set_timer(BLINK_EVENT, 1000)
    pygame.mixer.music.load('music/pululos_theme.wav')
    pygame.mixer.music.play(loops=-1)

    click_to_play = False
    while not click_to_play:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pygame.mixer.music.stop()
                    click_to_play = True
                    # intro.set_volume(0.75)
                    pygame.mixer.music.load('music/pululos_ending_echo.wav')
                    pygame.mixer.music.set_volume(0.35)
                    pygame.mixer.music.play(loops=-1)
                    mixer.Channel(0).play(mixer.Sound('music/start_pressed.wav'))
                    pygame.time.wait(2500)
                    mixer.stop()
                elif event.key == pygame.K_DOWN:
                    pygame.mixer.music.stop()
                    click_to_play = True
                    pygame.mixer.music.load('music/pululos_ending_echo.wav')
                    pygame.mixer.music.set_volume(0.35)
                    pygame.mixer.music.play(loops=-1)
                    mixer.Channel(0).play(mixer.Sound('music/start_pressed.wav'))
                    pygame.time.wait(2500)
                    mixer.stop()
                elif event.key == pygame.K_RIGHT:
                    pygame.mixer.music.stop()
                    click_to_play = True
                    pygame.mixer.music.load('music/pululos_ending_echo.wav')
                    pygame.mixer.music.set_volume(0.35)
                    pygame.mixer.music.play(loops=-1)
                    mixer.Channel(0).play(mixer.Sound('music/start_pressed.wav'))
                    pygame.time.wait(2500)
                    mixer.stop()
                pygame.mixer.music.stop()
            if event.type == BLINK_EVENT:
                blink_surface = next(blink_surfaces)
        screen.blit(blink_surface, blink_rect)
        draw_cover()
    draw_image(bar_score, (SCREEN_WIDTH * 0.376, SCREEN_HEIGHT * 0.728))


def instructions():
    click_to_play = False
    pygame.mixer.music.load('music/pupulos_just_drums.wav')
    pygame.mixer.music.play(loops=-1)
    while not click_to_play:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    click_to_play = True
                elif event.key == pygame.K_DOWN:
                    click_to_play = True
                elif event.key == pygame.K_RIGHT:
                    click_to_play = True

        draw_controllers()
    pygame.mixer.music.stop()
    draw_image(background2, (0, 0))


def instructions_2():
    pygame.mixer.music.load('music/pupulos_just_drums.wav')
    pygame.mixer.music.play(loops=-1)
    draw_controllers_2()
    pygame.mixer.music.stop()
    draw_image(background2, (0, 0))


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
        if profiles_dictionary[profile]['id'] == 'Kino':
            pygame.mixer.music.load('music/midnight_kino.wav')
        elif profiles_dictionary[profile]['id'] == 'Beach':
            pygame.mixer.music.load('music/cult_of_summer.wav')
        elif profiles_dictionary[profile]['id'] == 'Fitness':
            pygame.mixer.music.load('music/poundy_up.wav')
        elif profiles_dictionary[profile]['id'] == 'Pub':
            pygame.mixer.music.load('music/to_julito.wav')
        elif profiles_dictionary[profile]['id'] == 'Art':
            pygame.mixer.music.load('music/coroninho_pinho.wav')
        elif profiles_dictionary[profile]['id'] == 'Sado':
            pygame.mixer.music.load('music/fis_to_ing.wav')
        elif profiles_dictionary[profile]['id'] == 'Koffee':
            pygame.mixer.music.load('music/exotic_coffee_shop.wav')
        elif profiles_dictionary[profile]['id'] == 'Park':
            pygame.mixer.music.load('music/duck_rap.wav')

        pygame.mixer.music.play(loops=-1)
        draw_image(profiles_dictionary[profile]['image'], (SCREEN_WIDTH / 2.655, SCREEN_HEIGHT / 10))
        pygame.time.delay(1000)
        display_text_info(profiles_dictionary[profile]['name'],
                          profiles_dictionary[profile]['age'],
                          (SCREEN_WIDTH * 0.40, SCREEN_HEIGHT * 0.505),
                          white)
        text_surface = pygame.font.Font(font_title, 25).render("({}/8)".format(i+1), True, white)
        screen.blit(text_surface, (SCREEN_WIDTH * 0.71, SCREEN_HEIGHT * 0.505))
        plot_split_text(profiles_dictionary[profile]['text'][random.randint(0, 2)], 23,
                        (SCREEN_WIDTH * 0.605 - 200, SCREEN_HEIGHT * 0.572 - 12))
        scored = False
        start_time = time.time()
        time_out = 120
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
            current_time = time.time()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        profiles_dictionary[profile]['score'] += 1
                        scored = True
                        mixer.Sound('music/one_star.wav').play()
                        draw_selection_one_stars()
                        draw_image(bar_score, (SCREEN_WIDTH * 0.376, SCREEN_HEIGHT * 0.728))
                        draw_image(text_space, (SCREEN_WIDTH * 0.3675, SCREEN_HEIGHT * 0.553))
                        pygame.time.delay(500)
                        draw_image(bar, (SCREEN_WIDTH * 0.3755, SCREEN_HEIGHT * 0.4956))
                        mixer.stop()
                    elif event.key == pygame.K_DOWN:
                        profiles_dictionary[profile]['score'] += 2
                        scored = True
                        mixer.Sound('music/two_stars.wav').play()
                        draw_selection_two_stars()
                        draw_image(bar_score, (SCREEN_WIDTH * 0.376, SCREEN_HEIGHT * 0.728))
                        draw_image(text_space, (SCREEN_WIDTH * 0.3675, SCREEN_HEIGHT * 0.553))
                        draw_image(bar, (SCREEN_WIDTH * 0.3755, SCREEN_HEIGHT * 0.4956))
                        mixer.stop()
                    elif event.key == pygame.K_RIGHT:
                        profiles_dictionary[profile]['score'] += 3
                        scored = True
                        mixer.Sound('music/three_stars.wav').play()
                        draw_selection_three_stars()
                        draw_image(bar_score, (SCREEN_WIDTH * 0.376, SCREEN_HEIGHT * 0.728))
                        draw_image(text_space, (SCREEN_WIDTH * 0.3675, SCREEN_HEIGHT * 0.553))
                        draw_image(bar, (SCREEN_WIDTH * 0.3755, SCREEN_HEIGHT * 0.4956))
                        mixer.stop()
            elapsed_time = current_time - start_time
            if elapsed_time > time_out:
                main()
        pygame.mixer.music.stop()
        mixer.Sound('music/cortinilla_down.wav').play()
        if i == 0:
            draw_closing_1()
        elif i == 1:
            draw_closing_2()
        elif i == 2:
            draw_closing_3()
        elif i == 3:
            draw_closing_4()
        elif i == 4:
            draw_closing_1()
        elif i == 5:
            draw_closing_2()
        elif i == 6:
            draw_closing_3()
        elif i == 7:
            draw_closing_4()

        pygame.time.delay(1250)
        mixer.stop()


def ending_screen(profiles_dictionary):
    # draw_closing_score()
    draw_image(scoring, (SCREEN_WIDTH / 2.71, SCREEN_HEIGHT / 10.8))
    pygame.time.delay(100)
    run = True
    while run:
        sort_orders = sorted(profiles_dictionary.items(), key=lambda x: x[1]['score'], reverse=False)
        for i in range(len(sort_orders)):
            draw_image(sort_orders[i][1]['mini_image'], (SCREEN_WIDTH * 0.39, SCREEN_HEIGHT * (1 - 0.0725 * i) - 250))
            mixer.Sound('music/positions/position_{}.wav'.format(8-i)).play()
            display_score_info(sort_orders[i][1]['name'],
                               sort_orders[i][1]['score'],
                               SCREEN_HEIGHT * (1 - 0.0725 * i) - 245,
                               white)
            pygame.time.delay(1350)
            mixer.stop()
        run = False
    pygame.time.delay(3000)


def save_dictionary(results):
    summary = {}
    for element in results.items():
        summary[element[0]] = element[1]['score']
    with open('meta_data/scores_dictionary.pkl', 'wb') as f:
        pickle.dump(summary, f)


def Credits():
    draw_image(background3, (SCREEN_WIDTH / 2.71, SCREEN_HEIGHT / 10.8))
    pygame.mixer.music.load('music/credits_song.wav')
    pygame.mixer.music.play(loops=-1)
    profile_dic = {}
    names = os.listdir('display_animations/credits/')
    for name_profile in names:
        path_txt = os.path.join(path_main_design, 'credits', name_profile, '{}.txt'.format(name_profile))
        with open(path_txt) as f:
            lines = f.readlines()
        prof = {'text': {0: lines[0][:-1].upper(),
                         1: lines[1][:-1].upper(),
                         2: lines[2][:-1].upper()
                         }
                }
        profile_dic['{}'.format(name_profile)] = prof

    # Texts
    font = pygame.font.Font(font_text, 23)
    for i in [0, 1]:
        text_surface = font.render(profile_dic['Elkin']['text'][i][1:-1], True, white, black)
        screen.blit(text_surface, (SCREEN_WIDTH * 0.405, SCREEN_HEIGHT * (0.3 + 0.05 * i)))
    credits_1()
    for i in [0, 1, 2]:
        text_surface = font.render(profile_dic['Miguel']['text'][i][1:-1], True, white, black)
        screen.blit(text_surface, (SCREEN_WIDTH * 0.405, SCREEN_HEIGHT * (0.3 + 0.05 * i)))
    credits_2()
    for i in [0, 1, 2]:
        text_surface = font.render(profile_dic['Pao']['text'][i][1:-1], True, white, black)
        screen.blit(text_surface, (SCREEN_WIDTH * 0.405, SCREEN_HEIGHT * (0.3 + 0.05 * i)))
    credits_3()
    for i in [0, 1, 2]:
        text_surface = font.render(profile_dic['Ramona']['text'][i][1:-1], True, white, black)
        screen.blit(text_surface, (SCREEN_WIDTH * 0.405, SCREEN_HEIGHT * (0.3 + 0.05 * i)))
    credits_4()
    for i in [0, 1, 2]:
        text_surface = font.render(profile_dic['Final_words']['text'][i][1:-1], True, white, black)
        screen.blit(text_surface, (SCREEN_WIDTH * 0.405, SCREEN_HEIGHT * (0.3 + 0.05 * i)))
    credits_1()
    pygame.time.delay(2000)
    pygame.mixer.music.stop()


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
        instructions_2()
        # Define profiles from folders structure
        profile_dic = get_profiles()
        # Star running profiles and get scores
        run_profiles(profile_dic)
        # Display accumulated results
        ending_screen(profile_dic)
        # Save results
        save_dictionary(profile_dic)
        # credits
        Credits()


if __name__ == '__main__':
    main()
