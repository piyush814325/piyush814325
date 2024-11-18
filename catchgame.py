import pgzrun
from random import randint

HEIGHT = 600
WIDTH = 830

bg = Actor("bg (1)")

# Apple
apple = Actor("apple2 (1)")
apple.x = randint(20, 830)
apple.y = randint(20, 570)

# Bomb
bomb = Actor("bomb")
bomb.x = randint(20, 830)
bomb.y = randint(20, 570)

# Cherry
cherry = Actor("cherry (1)")
cherry.x = randint(20, 830)
cherry.y = randint(20, 570)

# Ruby
ruby = Actor("ruby (1)")
ruby.x = randint(20, 830)
ruby.y = randint(20, 570)

# Bucket
bucket = Actor("bucket2 (1)")
bucket.x = WIDTH - 70
bucket.y = HEIGHT - 50

# Buttons
play_button = Actor("play_button", (350,30))
pause_button = Actor("pause_button", (410,30))
restart_button = Actor("restart_button (2)", (470,30))

score = 0
lives = 3
game_over = False
paused = False

def update():
    global apple, bomb, cherry, ruby, bucket, score, lives, game_over, paused

    if game_over or paused:
        return

    if keyboard.left and bucket.x > 70:
        bucket.x -= 5
    if keyboard.right and bucket.x < WIDTH - 70:
        bucket.x += 5

    move_downward(apple)
    move_downward(bomb)
    move_downward(cherry)
    move_downward(ruby)

    if apple.colliderect(bucket):
        sounds.co.play()
        apple.y = 0
        apple.x = randint(20, 810)
        score += 1

    if ruby.colliderect(bucket):
        sounds.co.play()
        ruby.y = 0
        ruby.x = randint(20, 810)
        score += 3

    if cherry.colliderect(bucket):
        sounds.co.play()
        cherry.y = 0
        cherry.x = randint(20, 810)
        score += 1

    if bomb.colliderect(bucket):
        sounds.bomb.play()
        lives -= 1
        bomb.y = 0
        bomb.x = randint(20, 810)

        if lives == 0:
            game_over = True

            apple.y = 0
            cherry.y = 0
            bomb.y = 0
            ruby.y = 0

def move_downward(actor):
    if actor.y < HEIGHT:
        actor.y += 2 + score / 10
    else:
        actor.y = 0
        actor.x = randint(20, 810)

def draw():
    screen.clear()
    bg.draw()

    if game_over:
        screen.draw.text(f"Game Over!", (245, 230), color=(25, 27, 38), fontsize=85)
        screen.draw.text(f"Final Score: {score}", (250, 290), color=(25, 27, 38), fontsize=70)
        draw_buttons()
    else:
        apple.draw()
        bomb.draw()
        cherry.draw()
        ruby.draw()
        bucket.draw()
        screen.draw.text(f"Score: {score}", (15, 10), color=(25, 27, 38), fontsize=60)
        screen.draw.text(f"Lives: {lives}", (650, 10), color=(25, 27, 38), fontsize=60)
        draw_buttons()

def draw_buttons():
    play_button.draw()
    pause_button.draw()
    restart_button.draw()

def on_mouse_down(pos):
    global paused, game_over, score, lives

    if play_button.collidepoint(pos):
        paused = False

    if pause_button.collidepoint(pos):
        paused = True

    if restart_button.collidepoint(pos):
        score = 0
        lives = 3
        game_over = False
        paused = False
        reset_positions()

def reset_positions():
    apple.y = randint(20, 570)
    bomb.y = randint(20, 570)
    cherry.y = randint(20, 570)
    ruby.y = randint(20, 570)
    apple.x = randint(20, 830)
    bomb.x = randint(20, 830)
    cherry.x = randint(20, 830)
    ruby.x = randint(20, 830)

pgzrun.go()
