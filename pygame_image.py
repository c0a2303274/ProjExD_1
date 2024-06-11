import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bgr_img = pg.transform.flip(bg_img, True, False)
    k_3 = pg.image.load("fig/3.png")
    k_3 = pg.transform.flip(k_3, True, False)
    k_rect = k_3.get_rect()
    k_rect.center = 300, 200

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        x = tmr % 3200
        screen.blit(bg_img, [-(x), 0])
        screen.blit(bgr_img, [1600 - (x), 0])
        screen.blit(bg_img, [3200-(x), 0])
        screen.blit(bgr_img, [4800 - (x), 0])
        key_lst = pg.key.get_pressed()
        dxy = [-1, 0]
        if key_lst[pg.K_UP]:
            dxy[1] -= 1
        if key_lst[pg.K_DOWN]:
            dxy[1] += 1
        if key_lst[pg.K_LEFT]:
            dxy[0] -= 1
        if key_lst[pg.K_RIGHT]:
            dxy[0] += 3
        k_rect.move_ip(dxy)

        screen.blit(k_3, k_rect)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()