import pygame

# Initialize Pygame and screen dimensions
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 700, 500

# Initialize display surface and set title
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("No Man's Sky")

# Load and scale images directly
background_image = pygame.transform.scale(
    pygame.image.load("NoMansSky Back.png.jpg").convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT))


# Initialize font, render text, and set text position
text = pygame.font.Font(None, 50).render("No Man's Sky", True,
                                         pygame.Color('black'))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 110))

text2 = pygame.font.Font(None, 30).render("New Game", True,
                                         pygame.Color('black'))
text_rect2 = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))

text3 = pygame.font.Font(None, 30).render("Load Game", True,
                                         pygame.Color('black'))
text_rect3 = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20))

text4 = pygame.font.Font(None, 30).render("Settings", True,
                                         pygame.Color('black'))
text_rect4 = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 10))

text5 = pygame.font.Font(None, 30).render("Exit Game", True,
                                         pygame.Color('black'))
text_rect5 = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40))

def game_loop():
  clock = pygame.time.Clock()
  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    display_surface.blit(background_image, (0, 0))
    display_surface.blit(text, text_rect)
    display_surface.blit(text2, text_rect2)
    display_surface.blit(text3, text_rect3)
    display_surface.blit(text4, text_rect4)
    display_surface.blit(text5, text_rect5)


    pygame.display.flip()
    clock.tick(60)

  pygame.quit()


if __name__ == '__main__':
  game_loop()