import pygame
import random
import time


pygame.init()

class balls:
	def __init__(self, x, y, screen, key):
		self.x_cord = x
		self.y_cord = y
		self.screen = screen
		self.key = key
		self.is_jump = False
		self.is_ground = False
		self.ball_movement = False
		self.gravity = 9
		self.retardation = 1
		self.jump_count = 10
		self.direction = 15

	def draw_circle(self):
		pygame.draw.circle(self.screen, (0, 0, 0), (self.x_cord, self.y_cord), 50)	


def main():

	number11 = 30
	ball_count = 1
	time1 = time.time()
	score = 0
	text = pygame.font.Font(None, 24)
	width = 800
	height = 700
	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption("Click Ball")
	start = False

	
	ball1 = balls(300, 50, screen, pygame.K_SPACE) # object
	ball2 = balls(100, 0, screen, pygame.K_a)
	ball3 = balls(400, 0, screen, pygame.K_s)
	balls_list = []
 	

	running = True

	while running is True: # main loop
		if ball_count == 1:
			balls_list = [ball1] # list of number of balls
		elif ball_count == 2:
			balls_list = [ball1, ball2]
		elif ball_count >= 3:
			balls_list = [ball1, ball2, ball3]

		pygame.time.delay(35)
		screen.fill((255, 255, 255))

		for ball in balls_list:
		
			for event in pygame.event.get(): # events
				if ball_count <= 1:
					ball.jump_count = 6
				if ball_count == 2:
					ball.jump_count = 7
				if ball_count >= 3:
					ball.jump_count = 8
				if event.type == pygame.QUIT:
					running = False
				if event.type == pygame.KEYDOWN:
					# I have no idea how to make events object-oriented so i hard coded  all events. :(
	
					if event.key == pygame.K_SPACE:
						ball1.is_jump = True
						ball1.gravity = 0
						ball1.ball_movement = True
						ball1.direction = random.choice([15, -15])
						score += 1 

					if event.key == pygame.K_a:
						ball2.is_jump = True
						ball2.gravity = 0
						ball2.ball_movement = True
						ball2.direction = random.choice([15, -15])
						score += 1
					if event.key == pygame.K_s:
						ball3.is_jump = True
						ball3.gravity = 0
						ball3.ball_movement = True
						ball3.direction = random.choice([15, -15])
						score += 1
			balls_list = [ball1, ball2]
						
			# movement and bouncing	
			
			if ball.is_jump is False:
				ball.y_cord += ball.gravity
				ball.gravity += 9
			else:
				if ball.jump_count >= -5:
					if ball.jump_count <= 0:
						ball.retardation = -1
					else:
						ball.retardation = 1

					ball.y_cord -= int((ball.jump_count ** 2)  * ball.retardation)
				
					ball.jump_count -= 1


				else:
					ball.is_jump = False
					ball.jump_count = 10



			if ball.ball_movement is True:

				if ball.x_cord >= width - 60:
					ball.direction = -15
					ball.y_cord += ball.jump_count * 2
				if ball.x_cord <= 0 + 30:
					ball.direction = 15
				if ball.y_cord <= height - 60:
					ball.x_cord += ball.direction	

			if ball.y_cord >= height - 50:
				ball.y_cord = height - 50			

			ball.draw_circle() # drawing the circle
			final_time = (time.time() - time1)
		
			result = text.render("Time :" + str(final_time), True, (0, 255, 0))
			score2 = text.render("Score : " + str(score), True, (255, 144, 50))
			screen.blit(score2, (600, 50))
			screen.blit(result, (100, 50))
			ball_count = int((final_time + 30) // 30)

	

		if ball.y_cord <= 0 or ball.y_cord >= height - 50  and final_time > 10:
			font2 = pygame.font.Font(None, 24)
			result2 = font2.render("YOU SUCK!!!", True, (255, 0, 0))
			screen.blit(result2, (300, 200))
			running = False
			#running = False

		
		ball_count_down = number11 - final_time
		xyz = text.render("Next ball in : " + str(ball_count_down), True, (100, 255, 0))
		screen.blit(xyz, (100, 100))

		if ball_count_down <= 0:
			number11 += 30

		pygame.display.update()

if __name__ == "__main__":
	main()
