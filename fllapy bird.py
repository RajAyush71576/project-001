import pygame
import random


pygame.init()


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
GRAVITY = 0.5
FLAP_STRENGTH = -10
PIPE_GAP = 150
PIPE_WIDTH = 70
PIPE_COLOR = (0, 255, 0)
BIRD_COLOR = (255, 255, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird Clone")


class Bird:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def draw(self):
        pygame.draw.circle(screen, BIRD_COLOR, (self.x, int(self.y)), 15)


class Pipe:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.height = random.randint(100, 400)
        self.passed = False

    def update(self):
        self.x -= 5

    def draw(self):
        pygame.draw.rect(screen, PIPE_COLOR, (self.x, 0, PIPE_WIDTH, self.height))
        pygame.draw.rect(screen, PIPE_COLOR, (self.x, self.height + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT))


def main():
    clock = pygame.time.Clock()
    bird = Bird()
    pipes = [Pipe()]
    score = 0
    running = True

    while running:
        screen.fill((135, 206, 250)) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.flap()

        bird.update()
        bird.draw()

        for pipe in pipes:
            pipe.update()
            pipe.draw()

            
            if bird.x + 15 > pipe.x and bird.x - 15 < pipe.x + PIPE_WIDTH:
                if bird.y - 15 < pipe.height or bird.y + 15 > pipe.height + PIPE_GAP:
                    running = False 

            
            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                score += 1

        
        if pipes[-1].x < SCREEN_WIDTH - 200:
            pipes.append(Pipe())

        
        if pipes[0].x < -PIPE_WIDTH:
            pipes.pop(0)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main() 