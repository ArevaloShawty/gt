import pygame
import random
import time

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Para que te diviertas un rato, querida Adela")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)

# Cargar imágenes
dino_img = pygame.image.load("dino.png")
dino_img = pygame.transform.scale(dino_img, (50, 50))
cactus_img = pygame.image.load("cactus.png")
cactus_img = pygame.transform.scale(cactus_img, (30, 50))
flower_img = pygame.image.load("flower.png")
flower_img = pygame.transform.scale(flower_img, (60, 60))

# Dino
class Dino:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT - 100
        self.vel_y = 0
        self.jump = False
    
    def update(self):
        if self.jump:
            self.vel_y = -10
            self.jump = False
        self.y += self.vel_y
        self.vel_y += 0.5
        if self.y > HEIGHT - 100:
            self.y = HEIGHT - 100

    def draw(self):
        screen.blit(dino_img, (self.x, self.y))

# Obstáculo
class Cactus:
    def __init__(self):
        self.x = WIDTH
        self.y = HEIGHT - 100
    
    def update(self):
        self.x -= 5
        if self.x < -30:
            self.x = WIDTH + random.randint(100, 300)
    
    def draw(self):
        screen.blit(cactus_img, (self.x, self.y))

# Estrella fugaz
class Star:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT // 2)
        self.vel_x = random.uniform(-2, -0.5)
    
    def update(self):
        self.x += self.vel_x
        if self.x < 0:
            self.x = WIDTH
            self.y = random.randint(0, HEIGHT // 2)

    def draw(self):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), 2)

# Función principal
def main():
    clock = pygame.time.Clock()
    dino = Dino()
    cactus = Cactus()
    stars = [Star() for _ in range(5)]
    start_time = time.time()
    running = True

    while running:
        screen.fill(BLACK)
        
        # Mostrar mensaje
        font = pygame.font.Font(None, 36)
        text = font.render("Para que te diviertas un rato, querida Adela", True, WHITE)
        screen.blit(text, (WIDTH//4, 10))
        
        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if dino.y == HEIGHT - 100:
                    dino.jump = True
        
        # Actualizar elementos
        dino.update()
        cactus.update()
        for star in stars:
            star.update()

        # Dibujar elementos
        for star in stars:
            star.draw()
        dino.draw()
        cactus.draw()
        
        # Verificar colisión
        if dino.x + 50 > cactus.x and dino.x < cactus.x + 30 and dino.y + 50 > cactus.y:
            screen.fill(BLACK)
            text = font.render("Lo siento, querida. Vuelve a intentarlo", True, RED)
            screen.blit(text, (WIDTH//4, HEIGHT//2))
            pygame.display.update()
            pygame.time.delay(2000)
            return
        
        # Verificar si ha pasado un minuto
        if time.time() - start_time >= 60:
            screen.fill(BLACK)
            screen.blit(flower_img, (WIDTH//2 - 30, HEIGHT//2 - 30))
            text = font.render("¡Felicidades! Aquí tienes una linda flor morada", True, PURPLE)
            screen.blit(text, (WIDTH//4 - 20, HEIGHT//2 + 40))
            pygame.display.update()
            pygame.time.delay(4000)
            return
        
        pygame.display.update()
        clock.tick(30)

# Ejecutar el juego
if __name__ == "__main__":
    main()
    pygame.quit()
