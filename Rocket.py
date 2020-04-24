import sys
import pygame
from settings import Settings
from rocketship import RocketShip

class Rocket:
	def __init__(self): 
		pygame.init()

		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

		self.rocketship = RocketShip(self)
		pygame.display.set_caption("Rocket")


	def run_game(self): 
		while True: 
			self._check_events()
			self.rocketship.update()
			self._update_screen()

	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				sys.exit()
			elif event.type == pygame.KEYUP: 
				self._key_up_down_events(event, False)
			elif event.type == pygame.KEYDOWN: 
				self._key_up_down_events(event, True)

	def _key_up_down_events(self, event, isKeyDown = True):
		if event.key == pygame.K_RIGHT: 
			self.rocketship.rocket_move_right = isKeyDown
		elif event.key == pygame.K_LEFT: 
			self.rocketship.rocket_move_left = isKeyDown
		elif event.key == pygame.K_UP: 
			self.rocketship.rocket_move_up = isKeyDown
		elif event.key == pygame.K_DOWN: 	
			self.rocketship.rocket_move_down = isKeyDown
		elif event.key == pygame.K_q: 
			sys.exit()

	def _update_screen(self):
		self.screen.fill(self.settings.bg_color)
		self.rocketship.blitme()
		pygame.display.flip()

if __name__ == "__main__":
	r = Rocket()
	r.run_game()

