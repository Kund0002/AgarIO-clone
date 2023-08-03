import pygame

pygame.init()

width, height = 1720, 1080
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("AgarIO Clone")
pygame.time.Clock().tick(60)

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        
        pygame.display.update()
        
    
    pygame.quit()
    


if __name__ == "__main__":
    main()