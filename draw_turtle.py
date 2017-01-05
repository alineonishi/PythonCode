import turtle

def fractal(depth, base):
    turtle.speed(500000)
    turtle.color('pink')
    turtle.down()
    if depth == 0:
        turtle.fill(1)
        for i in 1,2,3:
            turtle.forward(base)
            turtle.left(120)
        turtle.fill(0)
        else:
            for i in 1,2,3:
                fractal(depth-1,base)
                turtle.up()
                turtle.forward(base*2**depth)
                turtle.left(120)
                turtle.down()
                
        fractal(6,5)