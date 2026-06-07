import pygame
import random

pygame.init()

# حجم الشاشة
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Frogger")

clock = pygame.time.Clock()

# ألوان
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (50, 50, 50)
BLACK = (0, 0, 0)

# الخط
font = pygame.font.SysFont(None, 50)

# الضفدع
frog = pygame.Rect(380, 520, 40, 40)
frog_speed = 40

# السيارات
cars = []

for i in range(5):
    x = random.randint(0, WIDTH)
    y = 100 + i * 80

    car = pygame.Rect(x, y, 100, 40)
    speed = random.randint(4, 8)

    cars.append([car, speed])

# دالة إعادة مكان الضفدع
def reset_frog():
    frog.x = 380
    frog.y = 520

running = True

while running:

    clock.tick(60)

    # الأحداث
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # الحركة بضغطة وحدة
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                frog.x -= frog_speed

            if event.key == pygame.K_RIGHT:
                frog.x += frog_speed

            if event.key == pygame.K_UP:
                frog.y -= frog_speed

            if event.key == pygame.K_DOWN:
                frog.y += frog_speed

    # منع الخروج من الشاشة
    if frog.x < 0:
        frog.x = 0

    if frog.x > WIDTH - frog.width:
        frog.x = WIDTH - frog.width

    if frog.y < 0:
        frog.y = 0

    if frog.y > HEIGHT - frog.height:
        frog.y = HEIGHT - frog.height

    # تحريك السيارات
    for car_data in cars:

        car = car_data[0]
        speed = car_data[1]

        car.x += speed

        # ترجع السيارة من البداية
        if car.x > WIDTH:
            car.x = -120

        # التصادم
        if frog.colliderect(car):
            reset_frog()

    # الفوز
    if frog.y <= 0:

        text = font.render("YOU WIN!", True, WHITE)
        screen.blit(text, (300, 250))

        pygame.display.update()
        pygame.time.delay(2000)

        reset_frog()

    # الرسم
    screen.fill(GRAY)

    # الشارع
    pygame.draw.rect(screen, BLACK, (0, 80, WIDTH, 450))

    # الضفدع
    pygame.draw.rect(screen, GREEN, frog)

    # السيارات
    for car_data in cars:
        pygame.draw.rect(screen, RED, car_data[0])

    pygame.display.update()

pygame.quit()