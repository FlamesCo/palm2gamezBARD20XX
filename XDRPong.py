import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
BALL_SPEED = 5
PADDLE_SPEED = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Create paddles
paddle_width, paddle_height = 10, 80
left_paddle = pygame.Rect(20, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
right_paddle = pygame.Rect(WIDTH - 30, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)

# Create the ball
ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)
ball_speed_x = BALL_SPEED * random.choice((1, -1))
ball_speed_y = BALL_SPEED * random.choice((1, -1))

# Score
left_score = 0
right_score = 0
font = pygame.font.Font(None, 36)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += PADDLE_SPEED
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += PADDLE_SPEED

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collisions
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y = -ball_speed_y

    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x = -ball_speed_x

    # Scoring
    if ball.left <= 0:
        right_score += 1
        ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)
        ball_speed_x = BALL_SPEED * random.choice((1, -1))
        ball_speed_y = BALL_SPEED * random.choice((1, -1))
    elif ball.right >= WIDTH:
        left_score += 1
        ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)
        ball_speed_x = BALL_SPEED * random.choice((1, -1))
        ball_speed_y = BALL_SPEED * random.choice((1, -1))

    # Clear the screen
    screen.fill(BLACK)

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Draw scores
    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(left_text, (WIDTH // 4, 20))
    screen.blit(right_text, (3 * WIDTH // 4 - right_text.get_width(), 20))

    # Update the display
    pygame.display.flip()

    # Control the game's speed
    pygame.time.delay(30)
## PONG BY SUNDAR.AI - Flames X 20XX [C]
