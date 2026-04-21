from freegames import vector,square
from turtle import *
from random import randrange

food=vector(0,0)
snake=[vector(0,100)]
direction=vector(0,-10)
speed=100
score=0
paused = False

def change(x,y):
    if not paused:
        direction.x=x
        direction.y=y

def show_paused():
    penup()
    goto(0, 0)
    color("blue")
    write("PAUSED", align="center", font=("Arial", 60, "bold"))

def toggle_pause():
    global paused
    paused = not paused

def inside(head):
    return -600<head.x<590 and -400<head.y<390

def show_score():
    penup()
    goto(0, 360)
    color("black")
    write(f"分数: {score}   速度: {speed}", align="center", font=("Arial", 24, "bold"))

def game_over_text():
    penup()
    goto(0, 0)
    color("red")
    write("GAME OVER", align="center", font=("Arial", 60, "bold"))
    penup()
    goto(0, -80)
    color("blue")
    write("按 R 键重新开始", align="center", font=("Arial", 24, "normal"))

def restart():
    global snake, direction, food, speed, score
    # 重置所有数据
    snake = [vector(0, 100)]
    direction = vector(0, -10)
    food = vector(0, 0)
    speed = 100
    score = 0
    Move()

def Move():
    global speed,score
    if paused:
        clear()
        show_score()
        show_paused()
        update()
        ontimer(Move, speed)
        return
    head=snake[-1].copy()
    head.move(direction)
    if head in snake or not inside(head):
        square(head.x,head.y,9,'red')
        update()
        game_over_text()
        return
    snake.append(head)
    if head==food:
        score+=10
        food.x=randrange(-58,58)*10
        food.y=randrange(-38,38)*10
        if speed>40:
            speed-=5
    else:
        snake.pop(0)
    clear()
    show_score()
    square(food.x,food.y,9,'green')
    square(head.x,head.y,9,'yellow')
    for s in snake[:-1]:
        square(s.x,s.y,9,'pink')
    update()
    ontimer(Move,speed)

setup(1200,800,None,None)
tracer(False)
hideturtle()
listen()

onkey(lambda:change(10,0),'Right')
onkey(lambda:change(0,10),'Up')
onkey(lambda:change(-10,0),'Left')
onkey(lambda:change(0,-10),'Down')
onkey(restart, 'r') 
onkey(toggle_pause, 'space')

Move()
done()
