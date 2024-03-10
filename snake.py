import pygame
from random import randint

pygame.init()

WIDTH, HEIGTH = 500, 400

WIN = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("snake")

clock = pygame.time.Clock()

#initial game value
score = 0
snake_head_size = 20
apple_size = snake_head_size
snake_velocity = 10
snake_dx = 0
snake_dy = 0

snake_head_rect = pygame.Rect(WIDTH // 2 - snake_head_size // 2, HEIGTH // 2 - snake_head_size // 2,
 snake_head_size, snake_head_size)
apple_rect = pygame.Rect(randint(0, WIDTH - apple_size), randint(0, HEIGTH - apple_size), apple_size, apple_size)
body_cords = []

FONT = pygame.font.SysFont("Times New Romen", 32)
pick_up_sound = pygame.mixer.Sound("pop.mp3")



#main game loop
running = True
while running:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
            break
        #movement
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_LEFT and not snake_dx:
                snake_dx = -1
                snake_dy = 0
            if events.key == pygame.K_RIGHT and not snake_dx:
                snake_dx = 1
                snake_dy = 0
            if events.key == pygame.K_UP and not snake_dy:
                snake_dx = 0
                snake_dy = -1
            if events.key == pygame.K_DOWN and not snake_dy:
                snake_dx = 0
                snake_dy = 1
            if events.key == pygame.K_1:
                snake_dx = 0
                snake_dy = 0

    #insert head cord to body head
    body_cords.insert(0, (snake_head_rect.left, snake_head_rect.top, snake_head_size, snake_head_size))
    body_cords.pop()

    snake_head_rect.centerx += snake_dx*snake_velocity
    snake_head_rect.centery += snake_dy*snake_velocity

    if snake_head_rect.left < 0 or snake_head_rect.right > WIDTH or snake_head_rect.top < 0 or snake_head_rect.bottom > HEIGTH or snake_head_rect in body_cords:
        game_over_text = FONT.render("GAME OVER press any key to play again", 1, (139, 255, 13))
        WIN.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGTH // 2 - game_over_text.get_height() // 2))
        pygame.display.update()
        paus = True
        while paus:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    paus = False
                    running = False
                    break
                if events.type == pygame.KEYDOWN:
                    score = 0
                    body_cords = []
                    snake_head_rect.center = (WIDTH // 2, HEIGTH // 2)
                    snake_dx = 0
                    snake_dy = 0
                    paus = False
                    break


    #collusion
    if snake_head_rect.colliderect(apple_rect):
        score += 1
        pick_up_sound.play()
        apple_rect.topleft = (randint(0, WIDTH - apple_size), randint(0, HEIGTH - apple_size))
        body_cords.append((snake_head_rect.left, snake_head_rect.top, snake_head_size, snake_head_size))



    #draw
    WIN.fill("black")
    score_font = FONT.render(f"Score: {score}", 1, (0, 255, 144))
    WIN.blit(score_font, (10, 10))
    for body in body_cords:    
        pygame.draw.rect(WIN, "darkgreen", body)
    pygame.draw.rect(WIN, "green", snake_head_rect)
    pygame.draw.rect(WIN, "red", apple_rect)
    pygame.display.update()

    clock.tick(30)

pygame.quit()