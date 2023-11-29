import pygame

pygame.init()

width = 1000
height = 600

screen = pygame.display.set_mode((width, height))

font = pygame.font.Font(None, 32)

input_box = pygame.Surface((400, 32))
input_box.fill((255, 255, 255))
input_box_rect = input_box.get_rect()
input_box_rect.center = (width // 2, height // 2)

text = ""

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print(f"La frase ingresada es: {text}")
                text = ""
            else:
                text += event.unicode

    screen.fill((0, 0, 0))
    screen.blit(input_box, input_box_rect)
    text_surface = font.render(text, True, (0, 0, 0))
    screen.blit(text_surface, (input_box_rect.x + 5, input_box_rect.y + 5))

    pygame.display.flip()