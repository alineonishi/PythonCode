# -*- coding: utf-8 -*-
import turtle

#def draw_square():
def drawshape(lenght,angle,sides):
    window = turtle.Screen()
    window.bgcolor('black')

    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.speed(3)
    brad.color('pink')
    
    n = 1
    if sides >= 4:
        while (n <= sides):
            brad.forward(lenght)
            brad.right(angle)
            n = n + 1
    elif sides == 3:
        brad.color('red')
        brad.shape('classic')
        while (n <= sides):
            brad.backward(lenght)
            brad.left(180 - angle)
            n = n + 1
    elif sides == 0:
        brad.color('yellow')
        brad.shape('arrow')
        brad.circle(lenght)
        
 #   brad.forward(200)
 #   brad.right(150)
 #   brad.forward(200)
 #   brad.right(150)
 #  brad.forward(200)
 #   brad.right(150)
 #   brad.forward(200)
 #   brad.right(150)
 #   brad.forward(200)
 #   brad.right(200)
   
    
 #   angie = turtle.Turtle()
 #   angie.shape('arrow')
 #   angie.color('green')
 #   angie.circle(100)
    
 #   window.exitonclick()
 # draw_square()
 
drawshape(100,90,4)
drawshape(120,60,3)
drawshape(130,0,0)