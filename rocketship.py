import pygame

class RocketShip: 
	def __init__(self, rocket): 
		self.screen = rocket.screen
		self.screen_rect = rocket.screen.get_rect()
		self.settings = rocket.settings

		self.image = pygame.image.load('images/heart.bmp')
		self.rect = self.image.get_rect()

		self.rect.center = self.screen_rect.center

		self.x = self.rect.x
		self.y = self.rect.y


		self.rocket_move_left = False
		self.rocket_move_right = False
		self.rocket_move_up = False
		self.rocket_move_down = False


	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def update(self): 
		if self.rocket_move_right and self.rect.right < self.screen_rect.right: 
			self.x += self.settings.rocket_speed
		if self.rocket_move_left and self.rect.left > 0: 
			self.x -= self.settings.rocket_speed
		if self.rocket_move_up and self.rect.top > 0: 
			self.y -= self.settings.rocket_speed
		if self.rocket_move_down and self.rect.bottom < self.screen_rect.bottom: 
			self.y += self.settings.rocket_speed

		self.rect.x = self.x
		self.rect.y = self.y
