import os
import glob
import re
import pygame
# from pygame import mixer

# Define constants for the screen width and height
scaling = 0.85
FR = 27  # Speed animation starts once selected
FRA = 25  # Speed animation and
SCREEN_WIDTH = 1250
SCREEN_HEIGHT = SCREEN_WIDTH * scaling

black = (0, 0, 0)
white = (255, 255, 255)
grey = (176, 176, 184)

path_profiles = 'profiles/'
path_main_design = 'display_animations/'


# Define Sprite classes for animations
class Cover(pygame.sprite.Sprite):
    def __init__(self):
        super(Cover, self).__init__()
        self.images = []
        array = glob.glob(os.path.join(path_main_design, 'cover', "*.png"))
        array.sort(key=lambda f: int(re.sub('\D', '', f)))
        for star in array:
            image = pygame.image.load(star).convert_alpha().convert_alpha()
            image = pygame.transform.smoothscale(image, (SCREEN_WIDTH * 0.4676, SCREEN_HEIGHT * 0.612))
            self.images.append(image)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(SCREEN_WIDTH / 2.71, SCREEN_HEIGHT / 10.8, 150, 198)

    def update(self):
        self.index += 1
        if self.index == len(self.images):
            self.index = 0
        self.image = self.images[self.index]


class Controllers(pygame.sprite.Sprite):
    def __init__(self):
        super(Controllers, self).__init__()
        self.images = []
        count = 0
        array = glob.glob(os.path.join(path_main_design, 'Controller', "*.png"))
        array.sort(key=lambda f: int(re.sub('\D', '', f)))
        for star in array:
            count += 1
            image = pygame.image.load(star).convert_alpha().convert_alpha()
            image = pygame.transform.smoothscale(image, (SCREEN_WIDTH * 0.4676, SCREEN_HEIGHT * 0.612))
            self.images.append(image)
        self.index = 0
        self.numb_images = count
        self.image = self.images[self.index]
        self.rect = pygame.Rect(SCREEN_WIDTH / 2.71, SCREEN_HEIGHT / 10.8, 150, 198)

    def update(self):
        self.index += 1
        if self.index == len(self.images):
            self.index = 0
        self.image = self.images[self.index]


class Stars1(pygame.sprite.Sprite):
    def __init__(self):
        super(Stars1, self).__init__()
        self.images = []
        count = 0
        for star in sorted(glob.glob(os.path.join(path_main_design, 'stars', 'Intro_1', "*.png"))):
            count += 1
            image = pygame.image.load(star).convert_alpha()
            image = pygame.transform.smoothscale(image, (SCREEN_WIDTH * 0.451, SCREEN_HEIGHT * 0.0955))
            self.images.append(image)
        for star in sorted(glob.glob(os.path.join(path_main_design, 'stars', 'Dancing_Stars', "*.png"))):
            image = pygame.image.load(star).convert_alpha()
            image = pygame.transform.smoothscale(image, (SCREEN_WIDTH * 0.451, SCREEN_HEIGHT * 0.0955))
            self.images.append(image)
        self.index = 0
        self.numb_images = count
        self.image = self.images[self.index]
        self.rect = pygame.Rect(SCREEN_WIDTH * 0.376, SCREEN_HEIGHT * 0.729, 150, 198)

    def update(self):
        self.index += 1
        if self.index >= self.numb_images and self.index == len(self.images):
            self.index = self.numb_images
        self.image = self.images[self.index]


class Stars2(pygame.sprite.Sprite):
    def __init__(self):
        super(Stars2, self).__init__()
        self.images = []
        count = 0
        for star in sorted(glob.glob(os.path.join(path_main_design, 'stars', 'Intro_2', "*.png"))):
            count += 1
            image = pygame.image.load(star).convert_alpha()
            image = pygame.transform.smoothscale(image, (SCREEN_WIDTH * 0.451, SCREEN_HEIGHT * 0.0955))
            self.images.append(image)
        for star in sorted(glob.glob(os.path.join(path_main_design, 'stars', 'Dancing_Stars', "*.png"))):
            image = pygame.image.load(star).convert_alpha()
            image = pygame.transform.smoothscale(image, (SCREEN_WIDTH * 0.451, SCREEN_HEIGHT * 0.0955))
            self.images.append(image)
        self.index = 0
        self.numb_images = count
        self.image = self.images[self.index]
        self.rect = pygame.Rect(SCREEN_WIDTH * 0.376, SCREEN_HEIGHT * 0.729, 150, 198)

    def update(self):
        self.index += 1
        if self.index >= self.numb_images and self.index == len(self.images):
            self.index = self.numb_images
        self.image = self.images[self.index]


class OneStars(pygame.sprite.Sprite):
    def __init__(self):
        super(OneStars, self).__init__()
        self.images = []
        count = 0
        array = glob.glob(os.path.join(path_main_design, 'stars', '1_Star', "*.png"))
        array.sort(key=lambda f: int(re.sub('\D', '', f)))
        for star in array:
            count += 1
            image = pygame.image.load(star).convert_alpha()
            image = pygame.transform.smoothscale(image, (SCREEN_WIDTH * 0.452, SCREEN_HEIGHT * 0.096))
            self.images.append(image)
        self.index = 0
        self.numb_images = count
        self.image = self.images[self.index]
        self.rect = pygame.Rect(SCREEN_WIDTH * 0.376, SCREEN_HEIGHT * 0.728, 150, 198)

    def update(self):
        self.index += 1
        if self.index == len(self.images):
            self.index = 0
        self.image = self.images[self.index]


class TwoStars(pygame.sprite.Sprite):
    def __init__(self):
        super(TwoStars, self).__init__()
        self.images = []
        count = 0
        array = glob.glob(os.path.join(path_main_design, 'stars', '2_Stars', "*.png"))
        array.sort(key=lambda f: int(re.sub('\D', '', f)))
        for star in array:
            count += 1
            image = pygame.image.load(star).convert_alpha()
            image = pygame.transform.smoothscale(image, (SCREEN_WIDTH * 0.452, SCREEN_HEIGHT * 0.096))
            self.images.append(image)
        self.index = 0
        self.numb_images = count
        self.image = self.images[self.index]
        self.rect = pygame.Rect(SCREEN_WIDTH * 0.376, SCREEN_HEIGHT * 0.728, 150, 198)

    def update(self):
        self.index += 1
        if self.index == len(self.images):
            self.index = 0
        self.image = self.images[self.index]


class ThreeStars(pygame.sprite.Sprite):
    def __init__(self):
        super(ThreeStars, self).__init__()
        self.images = []
        count = 0
        array = glob.glob(os.path.join(path_main_design, 'stars', '3_Stars', "*.png"))
        array.sort(key=lambda f: int(re.sub('\D', '', f)))
        for star in array:
            count += 1
            image = pygame.image.load(star).convert_alpha()
            image = pygame.transform.smoothscale(image, (SCREEN_WIDTH * 0.452, SCREEN_HEIGHT * 0.096))
            self.images.append(image)
        self.index = 0
        self.numb_images = count
        self.image = self.images[self.index]
        self.rect = pygame.Rect(SCREEN_WIDTH * 0.376, SCREEN_HEIGHT * 0.728, 150, 198)

    def update(self):
        self.index += 1
        if self.index == len(self.images):
            self.index = 0
        self.image = self.images[self.index]


class Opening(pygame.sprite.Sprite):
    def __init__(self):
        super(Opening, self).__init__()
        self.images = []
        count = 0
        array = glob.glob(os.path.join(path_main_design, 'big_curtain', 'to_intro', "*.png"))
        array.sort(key=lambda f: int(re.sub('\D', '', f)))
        for star in array:
            count += 1
            image = pygame.image.load(star).convert_alpha()
            image = pygame.transform.smoothscale(image, (SCREEN_WIDTH * 0.4676, SCREEN_HEIGHT * 0.612))
            self.images.append(image)
        self.index = 0
        self.numb_images = count
        self.image = self.images[self.index]
        self.rect = pygame.Rect(SCREEN_WIDTH / 2.71, SCREEN_HEIGHT / 10.8, 150, 198)

    def update(self):
        self.index += 1
        if self.index == len(self.images):
            self.index = 0
        self.image = self.images[self.index]


#################################################################################################################

class Covertoinstructions(pygame.sprite.Sprite):
    def __init__(self):
        super(Covertoinstructions, self).__init__()
        self.images = []
        count = 0
        array = glob.glob(os.path.join(path_main_design, 'cortinilla_media', 'to_dark', "*.png"))
        array.sort(key=lambda f: int(re.sub('\D', '', f)))
        for star in array:
            count += 1
            image = pygame.image.load(star).convert_alpha()
            image = pygame.transform.smoothscale(image, (SCREEN_WIDTH * 0.4676, SCREEN_HEIGHT * 0.612))
            self.images.append(image)
        self.index = 0
        self.numb_images = count
        self.image = self.images[self.index]
        self.rect = pygame.Rect(SCREEN_WIDTH / 2.71, SCREEN_HEIGHT / 10.8, 150, 198)

    def update(self):
        self.index += 1
        if self.index == len(self.images):
            self.index = 0
        self.image = self.images[self.index]


class Closebigscreen(pygame.sprite.Sprite):
    def __init__(self):
        super(Closebigscreen, self).__init__()
        self.images = []
        count = 0
        array = glob.glob(os.path.join(path_main_design, 'big_curtain', 'to_score', "*.png"))
        array.sort(key=lambda f: int(re.sub('\D', '', f)))
        for star in array:
            count += 1
            image = pygame.image.load(star).convert_alpha()
            image = pygame.transform.smoothscale(image, (SCREEN_WIDTH * 0.4676, SCREEN_HEIGHT * 0.612))
            self.images.append(image)
        self.index = 0
        self.numb_images = count
        self.image = self.images[self.index]
        self.rect = pygame.Rect(SCREEN_WIDTH / 2.71, SCREEN_HEIGHT / 10.8, 150, 198)

    def update(self):
        self.index += 1
        if self.index == len(self.images):
            self.index = 0
        self.image = self.images[self.index]


#################################################################################################################


class Close1(pygame.sprite.Sprite):
    def __init__(self):
        super(Close1, self).__init__()
        self.images = []
        count = 0
        array = glob.glob(os.path.join(path_main_design, 'new_openclose', '1', "*.png"))
        array.sort(key=lambda f: int(re.sub('\D', '', f)))
        for star in array:
            count += 1
            image = pygame.image.load(star).convert_alpha()
            image = pygame.transform.smoothscale(image, (SCREEN_WIDTH / 2.2, SCREEN_HEIGHT / 2.8))
            self.images.append(image)
        self.index = 0
        self.numb_images = count
        self.image = self.images[self.index]
        self.rect = pygame.Rect(SCREEN_WIDTH * 0.375, SCREEN_HEIGHT * 0.1, 150, 198)

    def update(self):
        self.index += 1
        if self.index == len(self.images):
            self.index = 0
        self.image = self.images[self.index]


class Close2(pygame.sprite.Sprite):
    def __init__(self):
        super(Close2, self).__init__()
        self.images = []
        count = 0
        array = glob.glob(os.path.join(path_main_design, 'new_openclose', '2', "*.png"))
        array.sort(key=lambda f: int(re.sub('\D', '', f)))
        for star in array:
            count += 1
            image = pygame.image.load(star).convert_alpha()
            image = pygame.transform.smoothscale(image, (SCREEN_WIDTH / 2.2, SCREEN_HEIGHT / 2.8))
            self.images.append(image)
        self.index = 0
        self.numb_images = count
        self.image = self.images[self.index]
        self.rect = pygame.Rect(SCREEN_WIDTH * 0.375, SCREEN_HEIGHT * 0.1, 150, 198)

    def update(self):
        self.index += 1
        if self.index == len(self.images):
            self.index = 0
        self.image = self.images[self.index]


class Close3(pygame.sprite.Sprite):
    def __init__(self):
        super(Close3, self).__init__()
        self.images = []
        count = 0
        array = glob.glob(os.path.join(path_main_design, 'new_openclose', '3', "*.png"))
        array.sort(key=lambda f: int(re.sub('\D', '', f)))
        for star in array:
            count += 1
            image = pygame.image.load(star).convert_alpha()
            image = pygame.transform.smoothscale(image, (SCREEN_WIDTH / 2.2, SCREEN_HEIGHT / 2.8))
            self.images.append(image)
        self.index = 0
        self.numb_images = count
        self.image = self.images[self.index]
        self.rect = pygame.Rect(SCREEN_WIDTH * 0.375, SCREEN_HEIGHT * 0.1, 150, 198)

    def update(self):
        self.index += 1
        if self.index == len(self.images):
            self.index = 0
        self.image = self.images[self.index]


class Close4(pygame.sprite.Sprite):
    def __init__(self):
        super(Close4, self).__init__()
        self.images = []
        count = 0
        array = glob.glob(os.path.join(path_main_design, 'new_openclose', '4', "*.png"))
        array.sort(key=lambda f: int(re.sub('\D', '', f)))
        for star in array:
            count += 1
            image = pygame.image.load(star).convert_alpha()
            image = pygame.transform.smoothscale(image, (SCREEN_WIDTH / 2.2, SCREEN_HEIGHT / 2.8))
            self.images.append(image)
        self.index = 0
        self.numb_images = count
        self.image = self.images[self.index]
        self.rect = pygame.Rect(SCREEN_WIDTH * 0.375, SCREEN_HEIGHT * 0.1, 150, 198)

    def update(self):
        self.index += 1
        if self.index == len(self.images):
            self.index = 0
        self.image = self.images[self.index]


# Define Sprite classes for animations
class Kino(pygame.sprite.Sprite):
    def __init__(self):
        super(Kino, self).__init__()
        self.images = []
        array = glob.glob(os.path.join(path_profiles, 'Kino_egg', 'animated', "*.png"))
        array.sort(key=lambda f: int(re.sub('\D', '', f)))
        for star in array:
            image = pygame.image.load(star).convert_alpha().convert_alpha()
            image = pygame.transform.smoothscale(image, (SCREEN_WIDTH * 0.452, SCREEN_HEIGHT * 0.358))
            self.images.append(image)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(SCREEN_WIDTH / 2.655, SCREEN_HEIGHT / 10, 150, 198)

    def update(self):
        self.index += 1
        if self.index == len(self.images):
            self.index = 0
        self.image = self.images[self.index]


# Define Sprite classes for animations
class Beach(pygame.sprite.Sprite):
    def __init__(self):
        super(Beach, self).__init__()
        self.images = []
        array = glob.glob(os.path.join(path_profiles, 'Beach_egg', 'animated', "*.png"))
        array.sort(key=lambda f: int(re.sub('\D', '', f)))
        for star in array:
            image = pygame.image.load(star).convert_alpha().convert_alpha()
            image = pygame.transform.smoothscale(image, (SCREEN_WIDTH * 0.452, SCREEN_HEIGHT * 0.358))
            self.images.append(image)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(SCREEN_WIDTH / 2.655, SCREEN_HEIGHT / 10, 150, 198)

    def update(self):
        self.index += 1
        if self.index == len(self.images):
            self.index = 0
        self.image = self.images[self.index]


# Define Sprite classes for animations
class Art(pygame.sprite.Sprite):
    def __init__(self):
        super(Art, self).__init__()
        self.images = []
        array = glob.glob(os.path.join(path_profiles, 'Art_egg', 'animated', "*.png"))
        array.sort(key=lambda f: int(re.sub('\D', '', f)))
        for star in array:
            image = pygame.image.load(star).convert_alpha().convert_alpha()
            image = pygame.transform.smoothscale(image, (SCREEN_WIDTH * 0.452, SCREEN_HEIGHT * 0.358))
            self.images.append(image)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(SCREEN_WIDTH / 2.655, SCREEN_HEIGHT / 10, 150, 198)

    def update(self):
        self.index += 1
        if self.index == len(self.images):
            self.index = 0
        self.image = self.images[self.index]


# Define Sprite classes for animations
class Fitness(pygame.sprite.Sprite):
    def __init__(self):
        super(Fitness, self).__init__()
        self.images = []
        array = glob.glob(os.path.join(path_profiles, 'Fitness_egg', 'animated', "*.png"))
        array.sort(key=lambda f: int(re.sub('\D', '', f)))
        for star in array:
            image = pygame.image.load(star).convert_alpha().convert_alpha()
            image = pygame.transform.smoothscale(image, (SCREEN_WIDTH * 0.452, SCREEN_HEIGHT * 0.358))
            self.images.append(image)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(SCREEN_WIDTH / 2.655, SCREEN_HEIGHT / 10, 150, 198)

    def update(self):
        self.index += 1
        if self.index == len(self.images):
            self.index = 0
        self.image = self.images[self.index]


# Define Sprite classes for animations
class Park(pygame.sprite.Sprite):
    def __init__(self):
        super(Park, self).__init__()
        self.images = []
        array = glob.glob(os.path.join(path_profiles, 'Park_egg', 'animated', "*.png"))
        array.sort(key=lambda f: int(re.sub('\D', '', f)))
        for star in array:
            image = pygame.image.load(star).convert_alpha().convert_alpha()
            image = pygame.transform.smoothscale(image, (SCREEN_WIDTH * 0.452, SCREEN_HEIGHT * 0.358))
            self.images.append(image)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(SCREEN_WIDTH / 2.655, SCREEN_HEIGHT / 10, 150, 198)

    def update(self):
        self.index += 1
        if self.index == len(self.images):
            self.index = 0
        self.image = self.images[self.index]


# Define Sprite classes for animations
class Sado(pygame.sprite.Sprite):
    def __init__(self):
        super(Sado, self).__init__()
        self.images = []
        array = glob.glob(os.path.join(path_profiles, 'Sado_egg', 'animated', "*.png"))
        array.sort(key=lambda f: int(re.sub('\D', '', f)))
        for star in array:
            image = pygame.image.load(star).convert_alpha().convert_alpha()
            image = pygame.transform.smoothscale(image, (SCREEN_WIDTH * 0.452, SCREEN_HEIGHT * 0.358))
            self.images.append(image)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(SCREEN_WIDTH / 2.655, SCREEN_HEIGHT / 10, 150, 198)

    def update(self):
        self.index += 1
        if self.index == len(self.images):
            self.index = 0
        self.image = self.images[self.index]


# Define Sprite classes for animations
class Koffee(pygame.sprite.Sprite):
    def __init__(self):
        super(Koffee, self).__init__()
        self.images = []
        array = glob.glob(os.path.join(path_profiles, 'Koffee_egg', 'animated', "*.png"))
        array.sort(key=lambda f: int(re.sub('\D', '', f)))
        for star in array:
            image = pygame.image.load(star).convert_alpha().convert_alpha()
            image = pygame.transform.smoothscale(image, (SCREEN_WIDTH * 0.452, SCREEN_HEIGHT * 0.358))
            self.images.append(image)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(SCREEN_WIDTH / 2.655, SCREEN_HEIGHT / 10, 150, 198)

    def update(self):
        self.index += 1
        if self.index == len(self.images):
            self.index = 0
        self.image = self.images[self.index]


# Define Sprite classes for animations
class Pub(pygame.sprite.Sprite):
    def __init__(self):
        super(Pub, self).__init__()
        self.images = []
        array = glob.glob(os.path.join(path_profiles, 'Pub_egg', 'animated', "*.png"))
        array.sort(key=lambda f: int(re.sub('\D', '', f)))
        for star in array:
            image = pygame.image.load(star).convert_alpha().convert_alpha()
            image = pygame.transform.smoothscale(image, (SCREEN_WIDTH * 0.452, SCREEN_HEIGHT * 0.358))
            self.images.append(image)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(SCREEN_WIDTH / 2.655, SCREEN_HEIGHT / 10, 150, 198)

    def update(self):
        self.index += 1
        if self.index == len(self.images):
            self.index = 0
        self.image = self.images[self.index]


class Credits1(pygame.sprite.Sprite):
    def __init__(self):
        super(Credits1, self).__init__()
        self.images = []
        count = 0
        array = glob.glob(os.path.join(path_main_design, 'credits', 'Elkin', "*.png"))
        array.sort(key=lambda f: int(re.sub('\D', '', f)))
        for star in array:
            count += 1
            image = pygame.image.load(star).convert_alpha().convert_alpha()
            image = pygame.transform.smoothscale(image, (SCREEN_WIDTH * 0.455 * 0.2, SCREEN_HEIGHT * 0.365 * 0.3))
            self.images.append(image)
        self.index = 0
        self.numb_images = count
        self.image = self.images[self.index]
        self.rect = pygame.Rect(SCREEN_WIDTH * 0.415, SCREEN_HEIGHT / 10, 150, 198)

    def update(self):
        self.index += 1
        if self.index == len(self.images):
            self.index = 0
        self.image = self.images[self.index]


class Credits2(pygame.sprite.Sprite):
    def __init__(self):
        super(Credits2, self).__init__()
        self.images = []
        count = 0
        array = glob.glob(os.path.join(path_main_design, 'credits', 'Pao', "*.png"))
        array.sort(key=lambda f: int(re.sub('\D', '', f)))
        for star in array:
            count += 1
            image = pygame.image.load(star).convert_alpha().convert_alpha()
            image = pygame.transform.smoothscale(image, (SCREEN_WIDTH * 0.455 * 0.2, SCREEN_HEIGHT * 0.365 * 0.3))
            self.images.append(image)
        self.index = 0
        self.numb_images = count
        self.image = self.images[self.index]
        self.rect = pygame.Rect(SCREEN_WIDTH * 0.515, SCREEN_HEIGHT / 10, 150, 198)

    def update(self):
        self.index += 1
        if self.index == len(self.images):
            self.index = 0
        self.image = self.images[self.index]


class Credits3(pygame.sprite.Sprite):
    def __init__(self):
        super(Credits3, self).__init__()
        self.images = []
        count = 0
        array = glob.glob(os.path.join(path_main_design, 'credits', 'Miguel', "*.png"))
        array.sort(key=lambda f: int(re.sub('\D', '', f)))
        for star in array:
            count += 1
            image = pygame.image.load(star).convert_alpha().convert_alpha()
            image = pygame.transform.smoothscale(image, (SCREEN_WIDTH * 0.455 * 0.2, SCREEN_HEIGHT * 0.365 * 0.3))
            self.images.append(image)
        self.index = 0
        self.numb_images = count
        self.image = self.images[self.index]
        self.rect = pygame.Rect(SCREEN_WIDTH * 0.615, SCREEN_HEIGHT / 10, 150, 198)

    def update(self):
        self.index += 1
        if self.index == len(self.images):
            self.index = 0
        self.image = self.images[self.index]


class Credits4(pygame.sprite.Sprite):
    def __init__(self):
        super(Credits4, self).__init__()
        self.images = []
        count = 0
        array = glob.glob(os.path.join(path_main_design, 'credits', 'Ramona', "*.png"))
        array.sort(key=lambda f: int(re.sub('\D', '', f)))
        for star in array:
            count += 1
            image = pygame.image.load(star).convert_alpha().convert_alpha()
            image = pygame.transform.smoothscale(image, (SCREEN_WIDTH * 0.455 * 0.2, SCREEN_HEIGHT * 0.365 * 0.3))
            self.images.append(image)
        self.index = 0
        self.numb_images = count
        self.image = self.images[self.index]
        self.rect = pygame.Rect(SCREEN_WIDTH * 0.715, SCREEN_HEIGHT / 10, 150, 198)

    def update(self):
        self.index += 1
        if self.index == len(self.images):
            self.index = 0
        self.image = self.images[self.index]
