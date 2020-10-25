import pygame
import snake

class engine:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.window = pygame.display.set_mode((width, height))
        self.running = True

        self.snk = snake.snake(width, height, width / 2, height / 2, 16)
        self.fd = snake.food(width, height, 16)

    def draw(self):
        self.window.fill((0, 0, 0))
        self.snk.draw(self.window)
        self.fd.draw(self.window)
        pygame.display.update()

    
    def update(self):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                self.running = False
            self.snk.move(event)

        if not self.snk.check_collision():
            self.snk.tail_length = 0
            self.snk.tail.clear()

        if self.snk.check_eat(self.fd):
            self.snk.add_cell()

        self.snk.update()
