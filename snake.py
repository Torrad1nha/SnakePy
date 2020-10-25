import pygame
import random
import math

class snake:
    def __init__(self, width, height, init_x, init_y,cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.x = init_x
        self.y = init_y
        self.direction = 'RIGHT'
        self.tail = []
        self.tail_length = 0

    def move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.direction = 'UP'
            if event.key == pygame.K_DOWN:
                self.direction = 'DOWN' 
            if event.key == pygame.K_RIGHT:
                self.direction = 'RIGHT'
            if event.key == pygame.K_LEFT:
                self.direction = 'LEFT'

    def update(self):

        if len(self.tail) > 0:
            if self.tail_length == len(self.tail):
                for i in range(0, self.tail_length - 1):
                    self.tail[i] = self.tail[i+1]

            self.tail[self.tail_length - 1] = [self.x, self.y]

        if self.direction == 'UP':
            self.y -= self.cell_size
        if self.direction == 'DOWN':
            self.y += self.cell_size
        if self.direction == 'LEFT':
            self.x -= self.cell_size
        if self.direction == 'RIGHT':
            self.x += self.cell_size

    def check_eat(self, food):
    
        distance = math.sqrt(math.pow(self.x - food.x, 2) + math.pow(self.y - food.y, 2))

        if distance < 1:
            self.tail_length += 1
            food.generate_food()
            return True
        return False
        

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.cell_size - 1, self.cell_size - 1))
        for cell in self.tail:
            pygame.draw.rect(screen, (255, 255, 255), (cell[0], cell[1], self.cell_size - 1, self.cell_size - 1))
    
    def add_cell(self):
        self.tail.append([self.x, self.y])

    def check_collision(self):
        if self.x > self.width - self.cell_size:
            self.x = 0
        elif self.x < 0:
            self.x = self.width

        if self.y > self.height - self.cell_size:
            self.y = 0
        elif self.y < 0:
            self.y = self.height


        if self.tail_length > 1:
            for i in range (1, self.tail_length):
                
                d = math.sqrt(math.pow(self.x - self.tail[i][0], 2) + math.pow(self.y - self.tail[i][1], 2))

                if d < 1:
                    return False
              

        return True
        

class food:

    def __init__(self, w, h, cs):
        self.width = w
        self.height = h
        self.cell_size = cs
        self.generate_food()


    def generate_food(self):
        self.x = random.randrange(0, int(self.width / self.cell_size)) * self.cell_size
        self.y = random.randrange(0, int(self.height / self.cell_size)) * self.cell_size

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.cell_size, self.cell_size))
