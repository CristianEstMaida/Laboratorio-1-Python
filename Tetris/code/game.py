import sqlite3
from settings import *
from random import choice
from sys import exit
from os.path import join
from preview import *
from timer import Timer
from score import *

class Game():
	def __init__(self, get_next_shape, update_score):
		
		self.width = 900
		self.height = 900

		
		
		self.screen = pygame.display.set_mode((self.width, self.height))

		
		self.font = pygame.font.Font(None, 32)

		self.input_box = pygame.Surface((400, 32))
		self.input_box.fill((255, 255, 255))
		self.input_box_rect = self.input_box.get_rect()
		self.input_box_rect.center = (self.width // 1.05, self.height // 1.05)
		
		self.id = 0
		self.text = ""
		# general 
		self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
		self.display_surface = pygame.display.get_surface()
		self.rect = self.surface.get_rect(topleft = (PADDING, PADDING))
		self.sprites = pygame.sprite.Group()

		# game connection
		self.get_next_shape = get_next_shape
		self.update_score = update_score

		# lines 
		self.line_surface = self.surface.copy()
		self.line_surface.fill((0,255,0))
		self.line_surface.set_colorkey((0,255,0))
		self.line_surface.set_alpha(120)

		# tetromino
		self.field_data = [[0 for x in range(COLUMNS)] for y in range(ROWS)]
		self.tetromino = Tetromino(
			choice(list(TETROMINOS.keys())), 
			self.sprites, 
			self.create_new_tetromino,
			self.field_data)

		# timer 
		self.down_speed = UPDATE_START_SPEED
		self.down_speed_faster = self.down_speed * 0.3
		self.down_pressed = False
		self.timers = {
			'vertical move': Timer(self.down_speed, True, self.move_down),
			'horizontal move': Timer(MOVE_WAIT_TIME),
			'rotate': Timer(ROTATE_WAIT_TIME)
		}
		self.timers['vertical move'].activate()

		# score
		self.current_level = 1
		self.current_score = 0
		self.current_lines = 0
	
		# sound 
		# self.landing_sound = pygame.mixer.Sound(join('..','sound', 'landing.wav'))
		# self.landing_sound.set_volume(0.1)

	# def store_score(self):
    #     with sqlite3.connect("mi_base_de_datos.db") as conexion:
    #         try:
    #             sentencia = 'update Score set score = ? where id = ?'
    #             cursor = conexion.execute(sentencia,(self.current_score,self.id))
                
    #         except Exception as e:
    #             print("Error")
    # def serch_id(self):
    #     with sqlite3.connect("mi_base_de_datos.db") as conexion:
    #         try:
                
    #             sentencia = 'select id from Score'
                
    #             cursor = conexion.execute(sentencia)
    #             contador = 0
    #             for fila in cursor:
    #                 contador += 1
                
    #             self.id = contador
                
    #         except Exception as e:
    #             print("Error")

	def calculate_score(self, num_lines):
		self.current_lines += num_lines
		self.current_score += SCORE_DATA[num_lines] * self.current_level

		if self.current_lines / 10 > self.current_level:
			self.current_level += 1
			self.down_speed *= 0.75
			self.down_speed_faster = self.down_speed * 0.3
			self.timers['vertical move'].duration = self.down_speed
			
		self.update_score(self.current_lines, self.current_score, self.current_level)

	def store_score(self):
		# with sqlite3.connect("my_data_base.db") as conexion:
		with sqlite3.connect("mi_base_de_datos.db") as conexion:
			
			try:
				#¿insert?
				conexion.execute('insert into Score (score, name) values (?, ?)', (self.current_score, self.text))
				pygame.time.delay(5 * 1000)
				# sentencia_1 = 'insert into Score(score) values(?)'
				# sentencia_2 = 'insert into Score(name) values(?)'
				# sentencia = 'update Score set score = ? where id = ?'
				# if self.current_score > 0:
				# 	# conexion.execute(sentencia,(self.current_score, self.id))
				# 	conexion.execute(sentencia_1,(self.current_score))
				# 	conexion.execute(sentencia_2,(self.text))
				# print(self.text)
				# print(self.current_score)
				# print(self.id)
			except Exception as e:
				print("Error")

	# def search_id(self):
		
	# 	with sqlite3.connect("mi_base_de_datos.db") as conexion:
	# 		try:
	# 			sentencia = 'select id from Score'
	# 			cursor = conexion.execute(sentencia)
	# 			contador = 0
	# 			for fila in cursor:
	# 				contador += 1
	# 			self.id = contador
	# 		except Exception as e:
	# 			print("Error")

	def select_id(self):
		pass

	def create_id(self):
		
		with sqlite3.connect("mi_base_de_datos.db") as conexion:
			
			try:
				#insert
				conexion.execute('insert into Score (score, name) values (?, ?)', (1, 's'))
				sentencia_1 = 'insert into Score(score) values(0)'
				sentencia_02 = 'insert into Score(score) values("Cris")'
				# sentence = 'select * from Score where score desc limit 5'
				sentencia_2 = 'select * from Score where score desc limit 5'
				# if self.current_score > 0:
				# 	conexion.execute(sentencia_1)
				# 	conexion.execute(sentencia_02)
				# conexion.execute(sentencia_2)
				
				# global puntajes
				# puntajes = []
				# for fila in cursor:
				# 	puntajes.append(fila)
			except Exception as e:
				print("Error")
    		

	def restart_game(self):
		self.update_score(0,0,1)
		self.current_score = 0
		self.current_level = 1
		self.current_lines = 0
		self.field_data = []
		self.field_data = [[0 for x in range(COLUMNS)] for y in range(ROWS)]
		self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
		self.display_surface = pygame.display.get_surface()
		self.rect = self.surface.get_rect(topleft = (PADDING, PADDING))
		self.sprites = pygame.sprite.Group()
		self.tetromino = Tetromino(
			choice(list(TETROMINOS.keys())), 
			self.sprites, 
			self.create_new_tetromino,
			self.field_data)
		# get the full row indexes 
		
		self.run()
		# self.score.run()
		self.surface.fill(GRAY)
		# self.display_pieces(next_shapes)
		self.display_surface.blit(self.surface, self.rect)
		pygame.draw.rect(self.display_surface, LINE_COLOR, self.rect, 2, 2)

	def check_game_over(self):
		for block in self.tetromino.blocks:
			if block.pos.y < 0:
				self.store_score()
				self.restart_game()
				# self.is_playing = False
        		# self.is_game_over = True
				# exit()

	def create_new_tetromino(self):
		# self.landing_sound.play()
		self.check_game_over()
		self.check_finished_rows()
		self.tetromino = Tetromino(
			self.get_next_shape(), 
			self.sprites, 
			self.create_new_tetromino,
			self.field_data)

	def timer_update(self):
		for timer in self.timers.values():
			timer.update()

	def move_down(self):
		self.tetromino.move_down()

	def draw_grid(self):

		for col in range(1, COLUMNS):
			x = col * CELL_SIZE
			pygame.draw.line(self.line_surface, LINE_COLOR, (x,0), (x,self.surface.get_height()), 1)

		for row in range(1, ROWS):
			y = row * CELL_SIZE
			pygame.draw.line(self.line_surface, LINE_COLOR, (0,y), (self.surface.get_width(),y))

		self.surface.blit(self.line_surface, (0,0))

	def input(self):
		
		keys = pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					print(f"El nombre ingresado es: {self.text}")
					self.text = ""
				else:
					self.text += event.unicode
		self.display_surface.fill(GRAY)
		self.screen.blit(self.input_box, self.input_box_rect)
		text_surface = self.font.render(self.text, True, (0, 0, 0))
		self.screen.blit(text_surface, (self.input_box_rect.x + 5, self.input_box_rect.y + 5))

		# checking horizontal movement
		if not self.timers['horizontal move'].active:
			if keys[pygame.K_LEFT]:
				self.tetromino.move_horizontal(-1)
				self.timers['horizontal move'].activate()
			if keys[pygame.K_RIGHT]:
				self.tetromino.move_horizontal(1)	
				self.timers['horizontal move'].activate()

		# check for rotation
		if not self.timers['rotate'].active:
			if keys[pygame.K_UP]:
				self.tetromino.rotate()
				self.timers['rotate'].activate()

		# down speedup
		if not self.down_pressed and keys[pygame.K_DOWN]:
			self.down_pressed = True
			self.timers['vertical move'].duration = self.down_speed_faster

		if self.down_pressed and not keys[pygame.K_DOWN]:
			self.down_pressed = False
			self.timers['vertical move'].duration = self.down_speed

	def check_finished_rows(self):

		# get the full row indexes 
		delete_rows = []
		for i, row in enumerate(self.field_data):
			if all(row):
				delete_rows.append(i)

		if delete_rows:
			for delete_row in delete_rows:

				# delete full rows
				for block in self.field_data[delete_row]:
					block.kill()

				# move down blocks
				for row in self.field_data:
					for block in row:
						if block and block.pos.y < delete_row:
							block.pos.y += 1

			# rebuild the field data 
			self.field_data = [[0 for x in range(COLUMNS)] for y in range(ROWS)]
			for block in self.sprites:
				self.field_data[int(block.pos.y)][int(block.pos.x)] = block

			# update score
			self.calculate_score(len(delete_rows))

	def run(self):

		
		# self.create_id()
		# self.search_id()
        
		# update
		self.input()
		self.timer_update()
		self.sprites.update()

		# drawing 
		self.surface.fill(GRAY)
		self.sprites.draw(self.surface)

		self.draw_grid()
		self.display_surface.blit(self.surface, (PADDING,PADDING))
		pygame.draw.rect(self.display_surface, LINE_COLOR, self.rect, 2, 2)

class Tetromino:
	def __init__(self, shape, group, create_new_tetromino, field_data):

		# setup 
		self.shape = shape
		self.block_positions = TETROMINOS[shape]['shape']
		self.color = TETROMINOS[shape]['color']
		self.create_new_tetromino = create_new_tetromino
		self.field_data = field_data

		# create blocks
		self.blocks = [Block(group, pos, self.color) for pos in self.block_positions]

	# collisions
	def next_move_horizontal_collide(self, blocks, amount):
		collision_list = [block.horizontal_collide(int(block.pos.x + amount), self.field_data) for block in self.blocks]
		return True if any(collision_list) else False

	def next_move_vertical_collide(self, blocks, amount):
		collision_list = [block.vertical_collide(int(block.pos.y + amount), self.field_data) for block in self.blocks]
		return True if any(collision_list) else False

	# movement
	def move_horizontal(self, amount):
		if not self.next_move_horizontal_collide(self.blocks, amount):
			for block in self.blocks:
				block.pos.x += amount

	def move_down(self):
		if not self.next_move_vertical_collide(self.blocks, 1):
			for block in self.blocks:
				block.pos.y += 1
		else:
			for block in self.blocks:
				self.field_data[int(block.pos.y)][int(block.pos.x)] = block
			self.create_new_tetromino()

	# rotate
	def rotate(self):
		if self.shape != 'O':

			# 1. pivot point 
			pivot_pos = self.blocks[0].pos

			# 2. new block positions
			new_block_positions = [block.rotate(pivot_pos) for block in self.blocks]

			# 3. collision check
			for pos in new_block_positions:
				# horizontal 
				if pos.x < 0 or pos.x >= COLUMNS:
					return

				# field check -> collision with other pieces
				if self.field_data[int(pos.y)][int(pos.x)]:
					return

				# vertical / floor check
				if pos.y > ROWS:
					return

			# 4. implement new positions
			for i, block in enumerate(self.blocks):
				block.pos = new_block_positions[i]

class Block(pygame.sprite.Sprite):
	def __init__(self, group, pos, color):
		
		# general
		super().__init__(group)
		self.image = pygame.Surface((CELL_SIZE,CELL_SIZE))
		self.image.fill(color)
		
		# position
		self.pos = pygame.Vector2(pos) + BLOCK_OFFSET
		self.rect = self.image.get_rect(topleft = self.pos * CELL_SIZE)

	def rotate(self, pivot_pos):

		return pivot_pos + (self.pos - pivot_pos).rotate(90)

	def horizontal_collide(self, x, field_data):
		if not 0 <= x < COLUMNS:
			return True

		if field_data[int(self.pos.y)][x]:
			return True

	def vertical_collide(self, y, field_data):
		if y >= ROWS:
			return True

		if y >= 0 and field_data[y][int(self.pos.x)]:
			return True

	def update(self):

		self.rect.topleft = self.pos * CELL_SIZE