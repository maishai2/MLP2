import random
import pygame
from sys import exit

pygame.init()
my_screen = pygame.display.set_mode((650, 500))  # display surface
pygame.display.set_caption("Twilight Bird ????")  # window title
clock = pygame.time.Clock()  # frames per second control

plays_now = False
twilight = False
best_score = 0
score = 0


# font = pygame.font.Font(None, 30)
# text = font.render("hi ", True, "Black")

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []

        if plays_now:

            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-001-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-002-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-003-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-004-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-005-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-006-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-007-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-008-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-009-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-010-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-009-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-008-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-007-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-006-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-005-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-004-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-003-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-002-removebg-preview (1).png'), (150, 150)))
            self.sprites.append(
                pygame.transform.scale(pygame.image.load('pics/ezgif-frame-001-removebg-preview (1).png'), (150, 150)))
        else:
            self.sprites.append(pygame.transform.scale(pygame.image.load('pics/flapping_01.png'), (90, 90)))
            self.sprites.append(pygame.transform.scale(pygame.image.load('pics/flapping_02.png'), (90, 90)))
            self.sprites.append(pygame.transform.scale(pygame.image.load('pics/flapping_03.png'), (90, 90)))
            self.sprites.append(pygame.transform.scale(pygame.image.load('pics/flapping_04.png'), (90, 90)))
            self.sprites.append(pygame.transform.scale(pygame.image.load('pics/flapping_05.png'), (90, 90)))
            self.sprites.append(pygame.transform.scale(pygame.image.load('pics/flapping_06.png'), (90, 90)))
            self.sprites.append(pygame.transform.scale(pygame.image.load('pics/flapping_07.png'), (90, 90)))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def set_rect(self, x, y):
        self.rect.topleft = [x, y]

    def get_rect(self):
        return self.rect

    def update(self):

        self.current_sprite += .3
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]


def home():
    global plays_now
    bg_img = pygame.image.load('pics/start_img.png')
    bg_img = pygame.transform.scale(bg_img, (650, 500))
    chars_img = pygame.image.load('pics/ch.png')
    chars_img = pygame.transform.scale(chars_img, (300, 350))

    moving_sprite = pygame.sprite.Group()
    player = Sprite(350, 300)
    moving_sprite.add(player)

    while True:
        for event in pygame.event.get():  # to keep
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        my_screen.blit(bg_img, (0, 0))
        my_screen.blit(chars_img, (180, 300))
        moving_sprite.draw(my_screen)
        moving_sprite.update()

        if pygame.mouse.get_pressed()[0]:
            plays_now = False
            break

        clock.tick(60)
        pygame.display.update()


heights = random.randint(100, 350)
width = 35
obstacle_change = 3
obstacle_x = 0


def start():
    global obstacle_x, obstacle_change, heights, width, best_score, score
    score = 0
    x = 550
    y = 0
    default_img = (650, 500)
    first_stage = pygame.image.load('pics/start_img.png')
    first_stage = pygame.transform.scale(first_stage, default_img)

    moving_sprite = pygame.sprite.Group()
    player = Sprite(30, 30)
    moving_sprite.add(player)

    while True:
        for event in pygame.event.get():  # to keep
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        move = pygame.key.get_pressed()

        if move[pygame.K_UP] and y > 0:
            y -= 8
        if move[pygame.K_DOWN] and y < 500 - 50:
            y += 5
        if move[pygame.K_LEFT] and x > 0:
            x -= 5
        if move[pygame.K_RIGHT] and x < 650 - 50:
            x += 5

        obstacle_x += obstacle_change
        if obstacle_x >= 660:
            obstacle_x = 0
            heights = random.randint(50, 370)
            score += 1

        R = random.randint(0, 255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)

        y += 3

        my_screen.blit(first_stage, (0, 0))
        obs1 = pygame.draw.rect(my_screen, (R, G, B), (obstacle_x, 0, width, heights))
        obs2 = pygame.draw.rect(my_screen, (R, G, B), (obstacle_x, heights + 180, width, 500 - 180 - heights))
        player.set_rect(x, y)
        moving_sprite.draw(my_screen)
        moving_sprite.update()

        if pygame.Rect.colliderect(player.get_rect(), obs1) or pygame.Rect.colliderect(player.get_rect(), obs2) or y > 500:
            if score > best_score:
                best_score = score
            end()

        clock.tick(60)
        pygame.display.update()


def end():
    default_img = (650, 500)
    first_stage = pygame.image.load('pics/start_img.png')
    first_stage = pygame.transform.scale(first_stage, default_img)
    test_font = pygame.font.Font(None, 30)
    text_surface = test_font.render('YOUR SCORE WAS: ' + str(score) + '! CLICK SPACE TO PLAY AGAIN ', True, 'Pink')
    text_surface2 = test_font.render('YOUR BEST SCORE WAS: ' + str(best_score), True, 'Pink')

    while True:
        for event in pygame.event.get():  # to keep
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        move = pygame.key.get_pressed()

        if move[pygame.K_SPACE]:
            start()

        my_screen.blit(first_stage, (0, 0))
        my_screen.blit(text_surface, (70, 130))
        my_screen.blit(text_surface2, (180, 180))

        pygame.display.update()
        clock.tick(60)


def main():
    #home()
    start()


if __name__ == "__main__":
    main()
