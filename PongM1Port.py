import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define paddle dimensions and speed
paddle_width, paddle_height = 10, 100
paddle_speed = 2

# Define ball dimensions and speed
ball_size = 10
ball_speed = [2, 2]

# Initialize player scores
player1_score, player2_score = 0, 0

# Define font for score display
font = pygame.font.Font(None, 50)

# Initialize paddles and ball
player1_paddle = pygame.Rect(10, (screen_height - paddle_height) // 2, paddle_width, paddle_height)
player2_paddle = pygame.Rect(screen_width - 20, (screen_height - paddle_height) // 2, paddle_width, paddle_height)
ball = pygame.Rect(screen_width // 2, screen_height // 2, ball_size, ball_size)

# Initialize game state
running = True

# Frame rate control
clock = pygame.time.Clock()
fps = 60  # Lower this value to make the game slower

# Main game loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_paddle.top > 0:
        player1_paddle.y -= paddle_speed
    if keys[pygame.K_s] and player1_paddle.bottom < screen_height:
        player1_paddle.y += paddle_speed
    if keys[pygame.K_UP] and player2_paddle.top > 0:
        player2_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and player2_paddle.bottom < screen_height:
        player2_paddle.y += paddle_speed

    # Ball movement and collision
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed[1] = -ball_speed[1]
    if ball.colliderect(player1_paddle) or ball.colliderect(player2_paddle):
        ball_speed[0] = -ball_speed[0]

    # Scoring
    if ball.left <= 0:
        player2_score += 1
        ball.x, ball.y = screen_width // 2, screen_height // 2
    if ball.right >= screen_width:
        player1_score += 1
        ball.x, ball.y = screen_width // 2, screen_height // 2

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player1_paddle)
    pygame.draw.rect(screen, WHITE, player2_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    score_text = font.render(f"{player1_score} - {player2_score}", True, WHITE)
    screen.blit(score_text, (screen_width // 2 - 50, 10))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(fps)

# Quit pygame
pygame.quit()
