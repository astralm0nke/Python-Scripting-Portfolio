## Mandelbrot Set Visualization
# Mandelbrot Set Iterative Formula: Z(n+1) = Z(n)^2 + C, where C=ai+b
# Zn starts at Z0 = 0
import pygame as pg
import numpy as np
import sys

pg.init()

window_w = 1000
window_h = 800
dsply = pg.display.set_mode((window_w, window_h))
pg.dsply.set_caption('Neon Mandelbrot Set Visualization')
dsply.fill((0, 0, 0))

fps = 60
clock = pg.time.Clock()

# Mandelbrot calculation Variables
real_width = 1000 # specify till what limit to calculate to
real_height = 800
zoom_level = 1.0
center_x = 0.0
center_y = 0.0

# Colormap for coloring set
def colormap(iteration, max_iteration):
# Neon Color Scheme
    r = min(abs(int(225*np.sin(0.1*iteration))), 225)
    g = min(abs(int(225*np.sin(0.2*iteration))), 225)
    b = min(abs(int(225*np.sin(0.3*iteration))), 225)
    return (r, g, b)

# Performs set iteration at each pixel. x, y represent real, i parts of complex number. Iteration tracks how fast seq grows
def calculateMandelbrot(xi, yi, width, height):
    for x0 in range(xi, width):
        for y0 in range(yi, height):
            x, y = 0, 0
            iteration = 0
            max_iteration = 225
            while (x*x) + (y*y) <= 2 and iteration < max_iteration:
                temp = (x*x) - (y*y) + ((x0 - real_width / 2) / (200*zoom_level) + center_x)
                y = (2*x*y) + ((real_height / 2 - y0) / (200*zoom_level) + center_y)
                x = temp
                iteration += 1

            clr = colormap(iteration, max_iteration)
            pg.draw.circle(dsply, clr, (x0, y0), 1)

def zoom(x_mouse, y_mouse):
    global center_x, center_y, zoom_level
    center_x = (x_mouse - real_width / 2) / (200*zoom_level) + center_x
    center_y = (real_height / 2 - y_mouse) / (200*zoom_level) + center_y
    zoom_level *= 2 # ADjust zoom factor as needed
    
    calculateMandelbrot(0, 0, real_width, real_height)


run = True
calculateMandelbrot(0, 0, real_width, real_height)

while (run):
    for event in pg.events.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1: # Left mouse click button
                xm, ym = event.pos
                zoom(xm, ym)
                
    pg.display.update()
    clock.tick(fps)

pg.quit()
sys.exit()