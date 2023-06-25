import time
import pygame
import random
import numpy

pygame.init()

time_started, running, started, jump, jump_count, retardation, time1, dino_x, dino_y, fast_down, score, dino_speed, crow_index, normal_obs_speed, give_option, infoObject, highscore = False, True, False, False, 12, 1, 0, 100, 515, False, 0, 1, 0, 30, False, pygame.display.Info(), 0
normal_height = 675
normal_width = 1200

class OBSTACLES:
	def __init__(self, screen, images, y_coordinate, x_coordinate, spec_coord):
		self.y_coordinate = y_coordinate
		self.x_coordinate = x_coordinate
		self.image = images
		self.screen = screen
		self.special_coordinate = spec_coord

	def draw_obstacle(self):
			self.screen.blit(self.image, (self.x_coordinate, self.y_coordinate))


def show_text(font, text, x_axis, y_axis, WINDOW):
	global score
	color = (100, 255, 100)
	if score >= int(highscore):
		color = (255, 0, 0)
	text = font.render(text, True, (color))
	WINDOW.blit(text, (x_axis, y_axis))

def user_responce():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				return "q"
			if event.key == pygame.K_c:
				return "c"

def user_activty():
	global running, started, jump, jump_count, retardation, dino_x, dino_y, fast_down, normal_obs_speed, give_option, highscore

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()	
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				started = True
				jump = True
			if event.key == pygame.K_DOWN:
				jump = False
				fast_down = True
				jump_count = 12
				retardation = 1
			if event.key == pygame.K_RIGHT:
				normal_obs_speed = 80
			if event.key == pygame.K_q:
				answer = "q"
			if event.key == pygame.K_c:
				answer = "c"

def start_time():
	global time1, time_started
	if time_started is False:
		time1 = time.time()
		time_started = True


def fill_gradient(surface, color, gradient, rect=None, vertical=True, forward=True):
    if rect is None: rect = surface.get_rect()
    x1,x2 = rect.left, rect.right
    y1,y2 = rect.top, rect.bottom
    if vertical: h = y2-y1
    else:        h = x2-x1
    if forward: a, b = color, gradient
    else:       b, a = color, gradient
    rate = (
        float(b[0]-a[0])/h,
        float(b[1]-a[1])/h,
        float(b[2]-a[2])/h
    )
    fn_line = pygame.draw.line
    if vertical:
        for line in range(y1,y2):
            color = (
                min(max(a[0]+(rate[0]*(line-y1)),0),255),
                min(max(a[1]+(rate[1]*(line-y1)),0),255),
                min(max(a[2]+(rate[2]*(line-y1)),0),255)
            )
            fn_line(surface, color, (x1,line), (x2,line))
    else:
        for col in range(x1,x2):
            color = (
                min(max(a[0]+(rate[0]*(col-x1)),0),255),
                min(max(a[1]+(rate[1]*(col-x1)),0),255),
                min(max(a[2]+(rate[2]*(col-x1)),0),255)
            )
            fn_line(surface, color, (col,y1), (col,y2))


def main():
	global running, started, jump, jump_count, retardation, dino_x, dino_y, fast_down, dino_speed, crow_index, normal_obs_speed, answer, normal_width, normal_height, give_option, score, highscore

	# music
	jump_sound = pygame.mixer.Sound("jump.wav")
	ten_points = pygame.mixer.Sound("points_10.wav")
	dead = pygame.mixer.Sound("margaya.wav")

	normal_obs_speed = 30
	index = 0
	# screen, width, height
	WINDOW = pygame.display.set_mode((normal_width, normal_height), pygame.RESIZABLE)
	pygame.display.set_caption("Dinosaur")
	obstacle_random = random.randint(1500, 2000)

	# Dinasour & obstacles
	cactus1, cactus1_x = pygame.image.load("Cactus_1_1(try).png"), 1300
	cactus2, cactus2_x = pygame.image.load("cactus_2.png"), 7000
	cactus3, cactus3_x = pygame.image.load("cactus_3.png"), 15000
	trap1, trap1_x = pygame.image.load("trap.png"), 15000
	trap2, trap2_x = pygame.image.load("trap_b.png"), 17000
	crow, crow_x, crow_rectangle = [pygame.image.load("crow_1_a.png"), pygame.image.load("crow_1_b.png")], 45000, pygame.image.load("crow_1_a.png")

	base1 = pygame.image.load("base(try).png")
	base2 = pygame.image.load("base(try).png")
	base3 = pygame.image.load("base(try).png")
	base4 = pygame.image.load("base(try).png")

	
	fps = 40
	dino_image = [pygame.image.load("dinosaur_a_1.png"), pygame.image.load("dinosaur_a_2.png"), pygame.image.load("dinosaur_a_3.png"), pygame.image.load("dinosaur_dead_a.png")]
	dino_rect = pygame.image.load("dinosaur_a_1.png")
	obstacle1 = OBSTACLES(WINDOW, cactus1, 475, cactus1_x, cactus1_x)
	obstacle2 = OBSTACLES(WINDOW, cactus2, 525, cactus2_x, cactus2_x)
	obstacle3 = OBSTACLES(WINDOW, cactus3, 525,	cactus3_x, cactus3_x)
	obstacle4 = OBSTACLES(WINDOW, trap1, 600,	trap1_x, trap1_x)
	obstacle5 = OBSTACLES(WINDOW, trap2, 600, trap2_x, trap2_x)
	#obstacle5 = OBSTACLES(WINDOW, crow, 430, crow_x, crow_x)
	obstacle_list = [obstacle1, obstacle2, obstacle3, obstacle4]

	# Fonts
	size_font1 = 40
	font =pygame.font.Font(None, size_font1)
	fps = 40
	base1_x = 0
	base2_x = 500
	base3_x = 800
	base4_x = 900
	y = 0
	with open("highscore.txt", "r") as f:
		highscore = f.read()
	while running: # game loop
		
		pygame.time.delay(fps) # fps = 50
		#WINDOW.fill((255, 255, 255))
		fill_gradient(WINDOW, (0, 70, 50), (255, 180, 150))
		
		user_activty()

		# render text
		if started is False:
			show_text(font, "Press Space to start", int((normal_width - 600) / 2), int((normal_height - 400) / 2), WINDOW)
			
		WINDOW.blit(base1, (base1_x, 620)) # Difference between coordinates is 500 pixels
		WINDOW.blit(base2, (base2_x, 620))
		WINDOW.blit(base3, (base3_x, 620))
		WINDOW.blit(base4, (base4_x, 620))
		# makes the character jump
		if jump is True:
			if jump_count == 12:
				jump_sound.play()
			if jump_count >= -12:
				if jump_count <= 0:
					retardation = -3
				else:
					retardation = 1
				dino_y -= int((jump_count ** 2 * retardation) * 0.6)

				jump_count -= 1 
			else:
				jump = False
				jump_count = 12

		# dino rect
		player_rect = pygame.Rect(dino_x - 5, dino_y, dino_rect.get_width() - 20, dino_rect.get_height() - 5)
		crow_rect = pygame.Rect(crow_x, 410, crow_rectangle.get_width() - 40, crow_rectangle.get_height() - 30)

		# obstacle movement
		for obstacle in obstacle_list:
			if started is True:
				rectangle2 = pygame.Rect(obstacle.x_coordinate - 15, obstacle.y_coordinate + 30, obstacle.image.get_width() - 30, obstacle.image.get_height() + 10)
				if player_rect.colliderect(rectangle2) or player_rect.colliderect(crow_rect):
					
					give_option = True
					running = False

					dead.play()

				obstacle.x_coordinate -= normal_obs_speed
				if obstacle.x_coordinate <= -50:
					obstacle.x_coordinate = obstacle.special_coordinate
		# fast down
		if fast_down is True:
			dino_y += 100
			if dino_y > 515:
				dino_y = 515
				fast_down = False

		if dino_y > 520:
			dino_y = 520
		if started is True:
			start_time()
			#HIGH SCORE
			final_time = time.time() - time1
			score = int(final_time / 2)
			#dino_speed = int(final_time / 30) + 1
			#pygame.draw.circle(WINDOW, (255, 255, 255), (dino_x, dino_y), 40) # Draw circle
			# draw dino, obs
			show_text(font, "Score " + str(score),int((normal_width - 600) / 2), int((normal_height - 400) / 2), WINDOW)
			show_text(font, "High Score : " + str(highscore), int((normal_width- 600) / 2) + 500, int((normal_height - 400) / 2), WINDOW)
			normal_obs_speed = 30#int((final_time * 0.099999) + 25)
			for obst in obstacle_list:
				obst.draw_obstacle()
			fps = 40 - int((final_time / 10))
			base1_x -= 30
			base2_x -= 30
			base3_x -= 30
			base4_x -= 30

			if base1_x <= -500:
				base1_x = 0
			if base2_x <= -100:
				base2_x = 500
			if base3_x <= 300:
				base3_x = 1000
			if base4_x <= 400:
				base4_x = 600

		if jump is True:
			index = 0
		if started is False:
			index = 0
		if running == False:
			index = 3
		WINDOW.blit(dino_image[index], (dino_x, dino_y))

		if index != 3:
			index += 1
			if index >= 3:
				index = 0

		if crow_index > 1:
			crow_index = 0
		WINDOW.blit(crow[crow_index], (crow_x, 430))
		crow_index += 1
		if crow_index > 2:
			crow_index = 0

		crow_x -= 50
		if crow_x <= -150:
			crow_x = 25000


		pygame.display.update()
		if index == 3:
			time.sleep(5)
		if score > int(highscore):
			with open("highscore.txt", "w") as w:
				highscore = score
				w.write(str(highscore))
		
def retry():
	global give_option, running

	size_font2 = 40
	font2 = pygame.font.Font("Arial.ttf", size_font2)
	screen = pygame.display.set_mode((1520, 640))

	retry_running = True
	while retry_running:
		fill_gradient(screen, (255, 153, 30), (255, 230, 210))
		answer = user_responce()
		show_text(font2, "Press q to quit or c to retry",int((normal_width) / 2), int((normal_height) / 2), screen)
		if answer == "q":
			quit()
		if answer == "c":
			retry_running = False
			give_option = False
			running = True

		pygame.display.update()
	


if __name__ == "__main__":
	while True:
		if give_option is False:
			main()
		if give_option is True:
			retry()
			give_option = False
			time_started = False
			running = True
			started = False
			jump = False
			jump_count = 12
			retardation = 1
			time1 = 0
			dino_x = 100
			dino_y =  515
			fast_down = False
			score = 0
			dino_speed = 1
			crow_index = 0	
			normal_obs_speed = 30
			give_option = False