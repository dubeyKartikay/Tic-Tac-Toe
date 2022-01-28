import pygame
from engine import rects
import time
def main():
    champion=""
    pygame.init()
    main_surface=pygame.display.set_mode((530,530))
    colour=(255,200,90)
    main_surface.fill(colour)
    list_rects=[]
    cross=pygame.image.load("cross.png")
    zero=pygame.image.load("zero.png")
    winner_cross=pygame.image.load("winner_cross.png")
    winner_zero=pygame.image.load("winner_zero.png")
    for i in range(3):
        for j in range(3):
            a=rects((180*i,180*j),(170,170),zero,cross,winner_cross,winner_zero)
            list_rects.append(a)
##    for i in list_rects:
####        pygame.draw.rect(main_surface,(255,0,0),i.rect)
##        i.draw(main_surface)
    for i in range(3):
        for j in range(3):
##            a=rects((180*i,180*j),(170,170),zero,cross)
##            list_rects.append(a)
            pygame.draw.rect(main_surface,(255,0,0),(180*i,180*j,170,170))
    chance=0
    a=False
    run =True
    while run:
        ev=pygame.event.poll()
        if ev.type==pygame.QUIT:
            pygame.quit()
            return "Forfeit"
        
        if  run:
            if ev.type==pygame.MOUSEBUTTONDOWN:
                posn_of_click=ev.dict["pos"]
                for i in list_rects:
                    won,who_won=i.update(list_rects,posn_of_click,chance)
                    if won == True:
                        champion=who_won
                        run=False
                if chance>=9:
                    run=False
                
                chance+=1
        for i in list_rects:
            i.draw(main_surface)
        pygame.display.flip()
    time.sleep(0.5)
    pygame.quit()
    return champion
