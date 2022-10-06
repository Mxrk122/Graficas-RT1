import ray
from vector3 import V3
from material import *
import color

filename = "result"
r = ray.Raytracer(filename, 800, 800)
r.change_paint_color(1, 0, 0)

red = Material(diffuse=color.color_RGB_to_GBR(1, 0, 0))
orange = Material(diffuse=color.color_RGB_to_GBR(1, 0.5, 0))
white = Material(diffuse=color.color_RGB_to_GBR(1, 1, 1))
black = Material(diffuse=color.color_RGB_to_GBR(0, 0, 0))

# Body
r.addSphere(V3(0, -2, -20), 2, white)
r.addSphere(V3(0, 2, -20), 3, white)
r.addSphere(V3(0, 6, -20), 4, white)

# Body aesthetics
r.addSphere(V3(0, 6, -15), 0.2, black)
r.addSphere(V3(0, 2, -15), 0.2, black)
r.addSphere(V3(0, 1, -15), 0.2, black)
r.addSphere(V3(0, 3, -15), 0.2, black)

# Face
r.addSphere(V3(-0.5, -2, -15), 0.25, black)
r.addSphere(V3(0.5, -2, -15), 0.25, black)
r.addSphere(V3(0, -1.2, -15), 0.25, orange)

r.addSphere(V3(1.1, -1, -15), 0.15, black)
r.addSphere(V3(0.6, -0.6, -15), 0.15, black)
r.addSphere(V3(0, -0.5, -15), 0.15, black)
r.addSphere(V3(-1.1, -1, -15), 0.15, black)
r.addSphere(V3(-0.6, -0.6, -15), 0.15, black)

r.render()
r.write()