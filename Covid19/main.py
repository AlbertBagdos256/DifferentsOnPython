from graph import *
from random import randint
from math import sin, cos, pi

balls = []
score = 0
step = 1
Rmin = 10
Rmax = 20
fieldWidth = 700
fieldHeight = 500
color = 'blue'
infected = 0

def createBalls( N ):  
  global balls,color,infected
  infected = randint(0,N)
  print(infected)
  for i in range(N):
    brushColor(color)
    if i == infected:
        print(i)
        brushColor("red")
    R = 6
    angle = randint(0,360)
    xc = randint(R,fieldWidth-R)
    yc = randint(R,fieldHeight-R)
    
    id = circle(xc, yc, R)
    balls.append( [id, xc, yc, R, angle] )

def moveBalls():
  global balls,color,N

  for i in range(len(balls)):
    id, xc, yc, R, angle = balls[i]
    dx = step*cos(angle*pi/180)
    dy = step*sin(angle*pi/180)
    xc += dx
    yc -= dy
    balls[i][1] = xc
    balls[i][2] = yc
    moveObjectBy(id, dx, -dy)
    if xc < R or xc+R > fieldWidth:
      angle = 180 - angle
    elif yc < R or yc+R > fieldHeight:
      angle = 360 - angle
    m = balls[0]
    print(infected)
    n = balls[infected]
    i_x = m[1]
    i_y = m[2]
    infected_x = n[1]
    infected_y = n[2]
    difference_x =  int(i_x) - int(infected_x)
    difference_y = int(i_y)  - int(infected_y)
    balls[i][4] = angle
    print(difference_x)
    print(difference_y)
    if difference_x < 5 and difference_y < 5:
        deleteObject(m[0])
        balls.remove(m)
        color = 'red'
        createBalls(1)
        break
        

def hit(b, x, y):
  id, xc, yc, R, _ = b
  d2 = (x-xc)**2 + (y-yc)**2
  return d2 <= R**2

def mouseCLick(event):
  global lbl, score, balls
  for b in balls:
    if hit(b, event.x, event.y):
        global color
        color = 'red'
        createBalls(1)
        break

def update():
  moveBalls()

def keyPressed(event):
  if event.keycode == VK_ESCAPE:
    close()

def main():
  global lbl
  canvasPos(0, 25)
 
  canvasSize(fieldWidth, fieldHeight)
  windowSize(fieldWidth+2, fieldHeight+27)
  createBalls(50)
  lbl = label("CoronaVirus Model", 10, 0, font="Arial, 12")
  onKey(keyPressed)
  onMouseClick(mouseCLick)
  onTimer(update, 8)
  run()

main()