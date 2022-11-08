import pygame

pygame.init()

# game settings
monitor_display = (800, 600)

game_display = pygame.display.set_mode(monitor_display)

pygame.display.set_caption("Tank Domination")

system_clock = pygame.time.Clock()

# game logic
game_running_flag = True

while game_running_flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running_flag == False

    if not game_running_flag:
        pygame.quit()

        break
    
    # running game mechaninces 
    pygame.display.update()

    system_clock.tick(60)