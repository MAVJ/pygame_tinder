import os
import glob
import re
import pygame
from pygame import mixer

# Define constants for the screen width and height
scaling = 0.85
FR = 40  # Speed animation starts selected
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
        self.intro_images = count
        self.image = self.images[self.index]
        self.rect = pygame.Rect(SCREEN_WIDTH * 0.376, SCREEN_HEIGHT * 0.729, 150, 198)

    def update(self):
        self.index += 1
        if self.index >= self.intro_images and self.index == len(self.images):
            self.index = self.intro_images
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
        self.intro_images = count
        self.image = self.images[self.index]
        self.rect = pygame.Rect(SCREEN_WIDTH * 0.376, SCREEN_HEIGHT * 0.729, 150, 198)

    def update(self):
        self.index += 1
        if self.index >= self.intro_images and self.index == len(self.images):
            self.index = self.intro_images
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
        array = glob.glob(os.path.join(path_main_design, 'open', "*.png"))
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


class Close(pygame.sprite.Sprite):
    def __init__(self):
        super(Close, self).__init__()
        self.images = []
        count = 0
        array = glob.glob(os.path.join(path_main_design, 'close', "*.png"))
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
