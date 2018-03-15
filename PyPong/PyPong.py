import pygame, sys
from pygame.locals import *

class MyBallClass(pygame.sprite.Sprite):
	def __init__(self, image_file, speed, location):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image_file)
		self.rect = self.image.get_rect()
		self.speed = speed
		self.rect.left, self.rect.top = location

	def move(self):
		self.rect = self.rect.move(self.speed)
		#在窗口两边反弹
		if self.rect.left < 0 or self.rect.right > screen.get_width():
			self.speed[0] = -self.speed[0]

		#在窗口顶部反弹
		if self.rect.top <= 0:
			self.speed[1] = - self.speed[1]

class MyPaddleClass(pygame.sprite.Sprite):
	def __init__(self, location):
		pygame.sprite.Sprite.__init__(self)
		#为球拍创建一个表面
		image_surface = pygame.surface.Surface([100, 20])
		image_surface.fill([0,0,0])
		#将这个表面转换到一个图像
		self.image = image_surface.convert()
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = location

#初始化Pygame、时钟、球和球拍
pygame.init()
screen = pygame.display.set_mode([640,480])
clock = pygame.time.Clock()
ball_speed = [10,5]
myBall = MyBallClass('wackyball.bmp', ball_speed, [50,50])
ballGroup = pygame.sprite.Group(myBall)
paddle = MyPaddleClass([270, 400])

running = True
while running:
	clock.tick(30)
	screen.fill([255,255,255])
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
		#如果鼠标移动，就移动球拍
		elif event.type == pygame.MOUSEMOTION:
			paddle.rect.centerx = event.pos[0]

    #检查球是否碰到球拍
	if pygame.sprite.spritecollide(paddle, ballGroup, False):
		myBall.speed[1] = -myBall.speed[1]
	myBall.move()
	#完全重绘
	screen.blit(myBall.image, myBall.rect)
	screen.blit(paddle.image, paddle.rect)
	pygame.display.flip()
pygame.quit()
