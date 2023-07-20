# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 11:40:25 2018

@author: Nicolle
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
from sklearn.linear_model import LinearRegression 

#LECTURA DEL ARCHIVO CSV CON LOS DATOS PROMEDIADOS PARA APURIMAC MENSUALMENTE DESDE EL AÑO 2010 AL 2016
datos=pd.read_csv('C:/Users/Lenovo/Desktop/gridtable1.csv', index_col=0, encoding='latin-1',sep=';')


pp = datos['pp'] #COLUMNA DE PRECIPITACION
n = len(pp)      #CANTIDAD DE DATOS
Prom= np.mean(pp) #PROMEDIO
a=sum((pp-Prom)**2) #SUMATORIA 
b=sum((pp-Prom)**3) #SUMATORIA
desviacion_estandar = np.std(pp)
error_estandar = desviacion_estandar/(n)**1/2 
#--------------------------------------------------------------------------------------------

Cs=b/n*(error_estandar)**3 #coeficiente de asimetria
Oi=(pp-Prom)/error_estandar #la lluvia mensual estandarizado

Zi= (6/Cs)*(Cs*Oi/2 + 1)**1/3 - 6/Cs + Cs/6 #INDICE CZI


        ################ CREACION DEL RANGO DE FECHAS##############
fecha_inicio = '2010-01-01'
fecha_fin = '2010-12-01'
rango_fechas = pd.date_range(start=fecha_inicio, end=fecha_fin, freq='M')


############ GRAFICO CON LA ESTIMACION DEL INDICE CZI A TRAVEZ DEL TIEMPO####
ax1=plt.plot(rango_fechas , Zi, color= 'red')
ax1=plt.xlabel("meses (2010-2016)")
ax1=plt.ylabel("CZI")
ax1=plt.title('Indice CZI entre los años 2010-2016')
plt.grid(True)
plt.grid(color = 'green', linestyle = '--', linewidth = 1.75, alpha=0.5)

#------------------------------------------------------------

############### GRAFICA DE LA REGRECION LINEAL Y SU FORMULA 

xre2=np.linspace(1, 84, 84) 
yre2=pp.values
xre2 = xre2.reshape(84,1)
yre2= yre2.reshape(84,1)
line = np.linspace(-3, 3, 1000, endpoint=False).reshape(-1, 1)
reg = LinearRegression()
reg.fit(xre2, yre2)
m=reg.coef_[0]
b=reg.intercept_
m1=m.reshape(1,1)
b1=b.reshape(1,1)
print("slope=",m1, "intercept=",b1)

predicted_values = [m*i + b for i in xre2]
ax=plt.plot( rango_fechas, predicted_values, 'b')
plt.grid(True)
plt.grid(color = 'green', linestyle = '--', linewidth = 1.75, alpha=0.5)
plt.text(x = 10000, y = 90, s = u'y= -0.35122491x+95.98878706')
plt.text(x = 8900, y = 90, s = u'pendiente= -0.35122491')
ax=plt.xlabel("meses 2010-2016)")
ax=plt.ylabel("CZI")
ax=plt.title('Indice CZI')


