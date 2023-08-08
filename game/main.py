import pygame
import components.UI.Start_Button as Start_Button

pygame.init()

width, height = 1720, 1080
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("AgarIO Clone")
pygame.time.Clock().tick(60)

Start_Button = Start_Button.Start_Button(win, 100, 100, 100, 100)

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if UI.UI.Start_Button.is_clicked():
                print("clicked")
                
        Start_Button.draw(win)
        pygame.display.update()
        
        
    
    pygame.quit()
    
    


if __name__ == "__main__":
    main()