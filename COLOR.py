import numpy as np
import cv2
import os
#SEBASTIAN DE LA CRUZ GUTIERREZ PUJ
class colorImage:  #Crear clase
    def __init__(self,path_file):       #se define el constructor
        self.image = cv2.imread(path_file,1) #se carga la imagen via opencv
    def displayProperties(self):         #se define el metodo para visualizar en la pantalla via print el alto y ancho de la imagen
        print(f'El ancho de la imgen es {self.image.shape[1]}.El alto de la imagen es {self.image.shape[0]}') #usando .shape optenemos y vizualizamos el alto y ancho de la imagen
    def makeGray(self):     #se define el metdo para devolver la version del grises de la imagen.
        print(f'imagen en grices',cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY)) #usando cv2.COLOR_BGR2GRAY se optiene la version de grices de la imagen
    def colorizeRGB(self,canal_color):  #se define el metodo para colorizar de blue,green, o red
        if canal_color =='BLUE':        #se realiza la logica en la que el usuario escoge entre blue,green, o red y asi escojemos como colorizar.
            B=self.image.copy()         #se copia la imagen original
            B[:,:,1] = 0                #se hace 0 las compenentes de R y G en la copia
            B[:,:,2] = 0
            cv2.imshow('imagen azul', B) #se visualiza la copia.
            cv2.waitKey(0)
        if canal_color == 'RED':
            R = self.image.copy()       #se copia la imagen original
            R [:, :, 0] = 0             #se hace 0 las compenentes de G y B en la copia
            R [:, :, 1] = 0
            cv2.imshow('imagen roja', R) #se visualiza la copia.
            cv2.waitKey(0)
        if canal_color == 'GREEN':
            G = self.image.copy()       #se copia la imagen original
            G[:, :, 0] = 0              #se hace 0 las compenentes de R y B en la copia
            G[:, :, 2] = 0
            cv2.imshow('imagen verde', G) #se visualiza la copia.
            cv2.waitKey(0)

    def makeHue(self):             #se define un metodo para devolver una imagen que resalta los tonos(hue)
        H_image= cv2.cvtColor(self.image,cv2.COLOR_BGR2HSV) #se realiza el cambio de espacio de color a hsv con ayuda de cv2.COLOR_BGR2HSV
        H_image [:,:,1] = 255      #Se lleva la componente S y V al valor constante de 255 dejando H intacta.
        H_image [:,:,2] = 255
        H_image = cv2.cvtColor(H_image,cv2.COLOR_HSV2BGR)#se realiza un cambio de espacio de color a RGB usando cv2.COLOR_HSV2BGR
        cv2.imshow('imagen HSV',H_image)
        cv2.waitKey(0)
