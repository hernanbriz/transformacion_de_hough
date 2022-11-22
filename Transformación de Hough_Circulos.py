# coding: iso-8859-1 -*-

import numpy as np
import cv2
 

pic_orig = cv2.imread("circulos.jpg") # Procederemos a realizar la lectura de la imagen
cv2.imshow("pic_orig", pic_orig)
cv2.waitKey(0)

escala_grises = cv2.cvtColor(pic_orig, cv2.COLOR_BGR2GRAY) # Convertimos la imagen original a nivel de grises
cv2.imshow("escala_grises", escala_grises)
cv2.waitKey(0) 

fgauss = cv2.GaussianBlur(escala_grises, (15,15), 0) # Se utiliza la función GaussianBlur, permite aplicar un filtro de desenfoque a la imagen
cv2.imshow("desenfoque", fgauss)
cv2.waitKey(0)


canny = cv2.Canny(fgauss, 50, 150) # Aqui se van a detectar los bordes utilizando el detector de bordes Canny de OpenCV
cv2.imshow("canny", canny)
cv2.waitKey(0)

(perimetro,_) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)# Se detectan los contornos y se retorna una lista con los valores

print("se han encontrado {} objetos".format(len(perimetro))) # Se muestra el número de circulos

cv2.drawContours(pic_orig,perimetro,-1,(0,0,255), 2) # Se hallan los contornos (pic_oringinal, list_contornos, nro_contornos, color_BGR, grosor_linea)
cv2.imshow("perimetro", pic_orig)
cv2.waitKey(0)

cv2.destroyAllWindows()
