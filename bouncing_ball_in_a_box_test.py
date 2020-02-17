from vpython import *
import numpy as np

screen = canvas(x=0, y=0,width=1340,height=750,center=vector(5,0,0), background=vector(0,0,0))
screen.forward = vector(-1,0,0)
screen.up = vector(0,0,1)

axis_x = arrow(pos = vector(0,0,0), axis = vector(1000,0,0), shaftwidth = 5, color = color.red)
axis_y = arrow(pos = vector(0,0,0), axis = vector(0,1000,0), shaftwidth = 5, color = color.green)
axis_z = arrow(pos = vector(0,0,0), axis = vector(0,0,1000), shaftwidth = 5, color = color.blue)

xy_plane = box(pos = vector(500,500,0), size = vector(1000,1000,1), color = vector(0.35,0.35,0.35))
origin = sphere(pos = vector(0,0,0), radius = 10, color = color.white)

bbox = box(pos = vector(500,500,100), size = vector(250,250,200), color = vector(0.5,0.5,0.5), opacity=0.5)

bx = 500
by = 500
bz = 100
rad = 10
ball = sphere(pos = vector(bx,by,bz), radius = rad, color = color.green)

vx = 3
vy = 5
vz = 7

trail = curve()

while True:
    rate(100)

    ball.pos.x += vx
    ball.pos.y += vy
    ball.pos.z += vz

    trail.append(pos=ball.pos, retain=5)
    
    
    if ball.pos.x >= (bbox.pos.x - rad + bbox.size.x/2) or ball.pos.x <= (bbox.pos.x + rad - bbox.size.x/2):
        vx = vx*-1 
    if ball.pos.y >= (bbox.pos.y - rad + bbox.size.y/2) or ball.pos.y <= (bbox.pos.y + rad - bbox.size.y/2):
        vy = vy*-1 
    if ball.pos.z >= (bbox.pos.z - rad + bbox.size.z/2) or ball.pos.z <= (bbox.pos.z + rad - bbox.size.z/2):
        vz = vz*-1

    
