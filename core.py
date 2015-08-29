import pygame as pg;
from pygame.locals import *;
from manager import Manager;
import sys;

pg.init();

clock = pg.time.Clock();

pg.display.set_caption("Bloing");

def main():
	RUNNING = True;
	FPS = 120;
	time_since_started = 0;

	manager = Manager();

	while RUNNING:
		milli = clock.tick(FPS);
		time_since_started += milli/1000.0

		for ev in pg.event.get():
			if((ev.type == QUIT) or (ev.type == KEYDOWN and ev.key == K_ESCAPE)):
				RUNNING = False;

		pg.display.set_caption("Bloing "+str(clock.get_fps()));
		
		manager.update(milli);
		manager.draw();
		pg.display.flip();

	pg.quit();
	sys.exit();

if __name__ == "__main__":
	main();