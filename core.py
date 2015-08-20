import pygame as pg;
from pygame.locals import *;
from manager import Manager;
import sys;

pg.init();
WIDTH = pg.display.Info().current_w;
HEIGHT = pg.display.Info().current_h;

display = pg.display.set_mode((WIDTH,HEIGHT));
clock = pg.time.Clock();

g = pg.Surface([WIDTH,HEIGHT],pg.SRCALPHA,32).convert_alpha();
g.fill((255,255,255));

pg.display.set_caption("Bloing");

def main():
	RUNNING = True;
	FPS = 50;
	time_since_started = 0;

	manager = Manager(g);

	while RUNNING:
		milli = clock.tick(FPS);
		time_since_started += milli/1000.0

		for ev in pg.event.get():
			if((ev.type == QUIT) or (ev.type == KEYDOWN and ev.key == K_ESCAPE)):
				RUNNING = False;

		manager.update(milli);
		manager.draw();
		display.blit(pg.transform.scale(g,(WIDTH,HEIGHT)),(0,0));
		pg.display.flip();

	pg.quit();
	sys.exit();

if __name__ == "__main__":
	main();