import pygame

pygame.init()

fps = 30
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((800, 800))

size = 800

block_size = size / 8


while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    gameDisplay.fill((128, 128, 128))

    for x in range(0, 8):
        for y in range(0, 8):
            if (x + y) % 2 == 0:
                pygame.draw.rect(
                    gameDisplay,
                    (255, 255, 255),
                    (x * block_size, y * block_size, block_size, block_size),
                    0,
                )

    pygame.display.update()