# Importamos las librerías de OpenCV y Numpy
import cv2
import numpy as np

# Procederemos a realizar la lectura de la imagen
pic = cv2.imread('crucigrama.jpg')
cv2.imshow('cruci_original', pic)
cv2.waitKey(0)

# Convertimos la imagen original a nivel de grises
escala_grises = cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
cv2.imshow('cruci_escala_gris', escala_grises)
cv2.waitKey(0)

# Aqui se van a detectar los bordes utilizando el detector de bordes Canny de OpenCV 
bordes = cv2.Canny(escala_grises,50,150,apertureSize = 3)
cv2.imshow('Bordes', bordes)
cv2.waitKey(0)

lineas = cv2.HoughLines(bordes,1,np.pi/180,150,None)# Con La función HpughLines obtenemos el arreglo 2D, 
                                                    # devuelve una matriz de valores r se mide en pixeles y theta en radianes
if lineas is not None:
    # empezamos a recorrer los resultados
    for i in range(0, len(lineas)):
        
        distancia = lineas[i][0][0]
		angulo = lineas[i][0][1]
        
		
        valor_cos = np.cos(angulo)#Guardamos el valor cos angulo
		
        valor_sen = np.sin(angulo)#Guardamos el valor sen angulo
		
        vx = valor_cos*distancia
		
        vy = valor_sen*distancia 
		
        
        vx1 = int(vx + 1000*(-valor_sen)) #Se empieza a recorrer desde los pixeles -1000 hasta 1000
        vy1 = int(vy + 1000*(valor_cos))
        vx2 = int(vx - 1000*(-valor_sen))
        vy2 = int(vy - 1000*(valor_cos))
        
		
        print("({},{})  ({},{})".format(vx1,vy1, vx2,vy2)) # Se muestran todos los valores hallados
		
        cv2.line(pic,(vx1,vy1),(vx2,vy2),(0,0,255),2) # Se generan las lineas para insertarla en la imagen inicial


cv2.imshow('cruci_con_lineas', pic)# Se muestra la imagen original con las líneas encontradas
cv2.waitKey(0)
cv2.destroyAllWindows()