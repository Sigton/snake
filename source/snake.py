from microbit import *
import random
    
def move_next(snake,image,food,game_over,score):
    
    new_x = snake[0]["x"]
    new_y = snake[0]["y"]
    
    if direction == "R":
        
        new_x = (new_x + 1) % display_width
    
    elif direction == "L":
        
        new_x = (new_x - 1) % display_width
    
    elif direction == "U":
        
        new_y = (new_y - 1) % display_height
    
    elif direction == "D":
        
        new_y = (new_y + 1) % display_height
    
    snake = [{"x":new_x,"y":new_y}] + snake
    if image.get_pixel(snake[0]["x"], snake[0]["y"]) == 9:
        food = None
        score+=1
    elif image.get_pixel(snake[0]["x"], snake[0]["y"]) == 5:
        game_over = True
    else:
        snake.pop()

    return snake,image,food,game_over,score

def test_for_food(image):
    y=0
    for n in range(display_height):
        x=0
        for n in range(display_width):
            if image.get_pixel(x,y) == 9:
                return True
            x+=1
        y+=1
    return False

def create_image(snake,food):
    
    image = Image("00000\n"
                  "00000\n"
                  "00000\n"
                  "00000\n"
                  "00000\n")
    
    for n in snake:
        image.set_pixel(n["x"], n["y"], 5)
    
    if food is not None: image.set_pixel(food[0], food[1], 9)
    
    return image

display_width, display_height = (5, 5)

snake = [{"x":1,"y":1},
         {"x":2,"y":1},
         {"x":3,"y":1}]
        
direction = "R"
image = Image("00000\n"
              "00000\n"
              "00000\n"
              "00000\n"
              "00000\n")
food = None

speed = 500
score = 0

game_over = False
while not game_over:
    
    times_a_pressed = button_a.get_presses()
    
    if times_a_pressed % 2 != 0:
        for n in range(times_a_pressed):
            if direction == "R":
                direction = "U"
            elif direction == "U":
                direction = "L"
            elif direction == "L":
                direction = "D"
            elif direction == "D":
                direction = "R"
    
    times_b_pressed = button_b.get_presses()
    
    if times_b_pressed % 2 != 0:
        for n in range(times_b_pressed):
            if direction == "R":
                direction = "D"
            elif direction == "D":
                direction = "L"
            elif direction == "L":
                direction = "U"
            elif direction == "U":
                direction = "R"
    try:
        if not test_for_food(image):
            food = [random.randint(0,display_width-1),random.randint(0,display_height-1)]
            while image.get_pixel(food[0], food[1]) == 5:
                food = [random.randint(0,display_width-1),random.randint(0,display_height-1)]
    except NameError:
        pass
    
    snake,image,food,game_over,score = move_next(snake,image,food,game_over,score)
    image = create_image(snake, food)
    display.show(image)
    
    sleep(speed)
    
display.scroll("Game Over! You scored {}!".format(score))
