from  graph import *
from random import randint
from math import sin,cos,pi,sqrt


healthy_people  = []
infected_people = []
fieldWidth      = 700
fieldHeight     = 500
step            = 1
infected_num = randint(1,10)
n = 1
m = 1
class Healthy_Person():
    def __init__(self,Amount):
        global healthy_people,color,infected,fieldHeight,fieldWidth
        self.color       = 'blue'
        brushColor(self.color)
        self.R           = 6
        self.angle       = randint(0,360)
        self.xc          = randint(self.R,fieldWidth  - self.R)
        self.yc          = randint(self.R,fieldHeight - self.R)
        self.id          = circle(self.xc, self.yc, self.R)
        self.desc        = 0
        healthy_people.append([self.id, self.xc, self.yc, self.R, self.angle, self.desc])

class infected_Person():
    def __init__(self,Infected_Amount):
        global infected_people,color,infected,fieldHeight,fieldWidth
        self.inf_color       = 'red'
        brushColor(self.inf_color)
        self.inf_R           = 6
        self.inf_angle       = randint(0,360)
        self.inf_xc          = randint(self.inf_R,fieldWidth  - self.inf_R)
        self.inf_yc          = randint(self.inf_R,fieldHeight - self.inf_R)
        self.inf_id          = circle(self.inf_xc, self.inf_yc, self.inf_R)
        self.inf_desc        = 1
        infected_people.append([self.inf_id, self.inf_xc, self.inf_yc, self.inf_R, self.inf_angle,self.inf_desc])



class Displacement():

    def Moving(self):
        global m,n
        # Healthy
        for i in range(m):
            self.id, self.xc, self.yc, self.R, self.angle,self.desc = healthy_people[i]
            self.dx         =  step*cos(self.angle*pi/180)
            self.dy         =  step*sin(self.angle*pi/180)
            self.xc        += self.dx
            self.yc        -= self.dy
            healthy_people[i][1]    = self.xc
            healthy_people[i][2]    = self.yc
            moveObjectBy(self.id,self.dx,-self.dy)
            if self.xc < self.R or self.xc+self.R > fieldWidth:
                self.angle  = 180 - self.angle
            elif self.yc < self.R or self.yc + self.R > fieldHeight:
                self.angle  = 360 - self.angle
            healthy_people[i][4]    = self.angle
            print(str(i) + 'lox')

            if m == len(healthy_people):
                i = 0
                m = 1
            m+=1
            i+=1 

            #Infected
        for j in range(n):
            self.inf_id, self.inf_xc, self.inf_yc, self.inf_R, self.inf_angle,self.inf_desc = infected_people[j]
            self.inf_dx         =  step*cos(self.inf_angle*pi/180)
            self.inf_dy         =  step*sin(self.inf_angle*pi/180)
            self.inf_xc        += self.inf_dx
            self.inf_yc        -= self.inf_dy
            infected_people[j][1]    = self.inf_xc
            infected_people[j][2]    = self.inf_yc
            moveObjectBy(self.inf_id,self.inf_dx,-self.inf_dy)

            if self.inf_xc < self.inf_R or self.inf_xc + self.inf_R > fieldWidth:
                self.inf_angle  = 180 - self.inf_angle

            elif self.inf_yc < self.inf_R or self.inf_yc + self.inf_R > fieldHeight:
                self.inf_angle  = 360 - self.inf_angle
            infected_people[j][4]    = self.inf_angle
        print(str(j) + 'debil' )
        n +=1
        j +=1
        if n >= len(infected_people):
            n = 1
            j = 0
        # healthy
        healthy_parametrs  = healthy_people[i]
        healthy_x          = healthy_parametrs[1]
        healthy_y          = healthy_parametrs[2]

        # infected
        infected_parametrs = infected_people[j]
        infected_x         = infected_parametrs[1]
        infected_y         = infected_parametrs[2]
        distance           = (int(healthy_x) - int(infected_x))**2 + (int(healthy_y) - int(infected_y))**2
        distance           = sqrt(distance)
        print(str(distance) + 'distance')

        if distance < 80:
            print(str(len(healthy_people)) + 'dlina')
            deleteObject(healthy_parametrs[0])
            healthy_people.remove(healthy_parametrs)
            infected_Person(1)
            
            print(len(healthy_people))
        distance = 0

            

o = Displacement()
def Update():
    o.Moving()


def keyPressed(event):
  if event.keycode == VK_ESCAPE:
    close()


def main():
    global lbl
    canvasPos(0, 25)
    canvasSize(fieldWidth, fieldHeight)
    windowSize(fieldWidth+2, fieldHeight+27)
   
    for i in range(10):
        Healthy_Person(1)
    for i in range(1):
        infected_Person(1)
    lbl = label("CoronaVirus Model", 10, 0, font="Arial, 12")
    onKey(keyPressed)
    onTimer(Update, 8)
    run()
if __name__ == "__main__":
    main()
