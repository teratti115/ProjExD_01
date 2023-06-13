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
    ton_lst=[ton_img , ton_img2]
    

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-(tmr%1600), 0])
        

        i=tmr%2


        screen.blit(ton_lst[i],[300,200])

        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()