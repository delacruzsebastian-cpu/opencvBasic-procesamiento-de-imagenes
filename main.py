
from COLOR import *
if __name__ == '__main__':
    route_image = input ('ingrese la direccion de la imagen: ')
    image = colorImage(route_image)
    image.displayProperties()
    image.makeGray()
    image.colorizeRGB('RED')
    image.makeHue()
