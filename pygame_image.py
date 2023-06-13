import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    ton_img=pg.image.load("ex01/fig/3.png")
    ton_img=pg.transform.flip(ton_img,True,False)
    ton_img2=pg.transform.rotozoom(ton_img,10,1.0)
    angle=0

    ton_lst=[ton_img , ton_img2]
    
    yoko=0
    tmr = 0
    angle_plus=0.1
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        ton_img3=pg.transform.rotozoom(ton_img,angle,1.0)
        yoko=-(tmr%1600)
        screen.blit(bg_img, [yoko, 0])
        i=tmr%2
        screen.blit(ton_img3,[300,200])
        pg.display.update()
        tmr += 1  
        angle+=angle_plus
        if angle>10 or angle<=0:  
            angle_plus*=-1
        clock.tick(100)
        if yoko<-1599:
            bg_img=pg.transform.flip(bg_img,True,False)



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()