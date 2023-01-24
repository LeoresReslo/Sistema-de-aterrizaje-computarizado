import tkinter as tk
from tkinter import Label,Entry,Button,Frame
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os
from PIL import ImageTk,Image
from matplotlib import style

style.use("fivethirtyeight")
ventana = tk.Tk()
ventana.title("Sistema de aterrizaje computarizado")
ventana.geometry("1250x750")


#!!!!!!!!!!!!!!!!!!!!!!!Funciones!!!!!!!!!!!!!!

#------------------Funciones de botones--------
def graf_mi():
    #----Ingreso de las variables----
    
    #Ingreso de la aceleración
   
    if (pseudo_k_mss['state'] == tk.NORMAL):
        k_mss1 = pseudo_k_mss.get()
        k_mss2= float(k_mss1)
        k = (k_mss2/1609.344)*(3600*3600) 
        
    elif (pseudo_k_mss['state'] == tk.DISABLED):
        k_mih1 = pseudo_k_mih.get()
        k_mih2= float(k_mih1)
        k = k_mih2
    
    
    #Ingreso de la altitud

    if (pseudo_h_m['state'] == tk.NORMAL):
        h_m1= pseudo_h_m.get()
        h_m2 = float(h_m1)
        h_m3=h_m2*3.28
        h = (h_m3)/(5280)
        
    elif (pseudo_h_m['state'] == tk.DISABLED):
        h_fts1 = pseudo_h_fts.get()
        h_fts2 = float(h_fts1)
        h = (h_fts2)/(5280)
   
    
    #Ingreso de la velocidad
    
    if (pseudo_v_mih['state'] == tk.NORMAL):
        v_mih1= pseudo_v_mih.get()
        v_mih2 = float(v_mih1)
        v_0 = v_mih2
        
    elif (pseudo_v_mih['state'] == tk.DISABLED):
        v_kts1 = pseudo_v_kts.get()
        v_kts2 = float(v_kts1)
        v_0 = v_kts2*(1.150783)
 
    
    #Ingreso de la velocidad del viento
    
    if (pseudo_v_v_mih['state'] == tk.NORMAL):
        v_v_mih1= pseudo_v_v_mih.get()
        v_v_mih2 = float(v_v_mih1)
        v_v = v_v_mih2
    elif (pseudo_v_v_mih['state'] == tk.DISABLED):
        v_v_kts1 = pseudo_v_v_kts.get()
        v_v_kts2 = float(v_v_kts1) 
        v_v = v_v_kts2*(1.150783)
        
    #xxxxxxxxxxxxxxxxCalculo de la distanciaxxxxxxxxx
    #Calculamos la velocidad real(True Airspeed)-TAS
    
    v_TAS = (v_0*0.02*h)/(1000+v_0)
    
    #Calculamos la velocidad sobre el terreno(Ground speed)
    v_gs=v_TAS+(v_v)
    
    #Calculamos la distancia de decenso 
    L = np.sqrt((6*h*v_gs*v_gs)/(k))
    
    L_fts = L
    L_mi = L/5280
    L_m = L / 3.28
    
    #"Salida de la distancia en millas."
    salida_l_mi.config(text = L_mi)

    #"Salida de la distancia en pies"
    salida_l_fts.config(text = L_fts)

    #"Salida de la distancia en metros"
    salida_l_m.config(text = L_m)
    
    #Graficamos la funcion de la distancia de decenso
    
    

    "Dominio"
    x = np.arange(0,L,0.0001)
    L_var = (L+L)/8
    L_var_min = -1*L_var 
    L_d=L+L_var
    plt.xlim(L_var_min,L_d)
    
    "Rango"
    h_r_var = (h+h)/8
    h_r_var_min = -1*h_r_var
    h_r=h+h_r_var
    plt.ylim(h_r_var_min,h_r)
    
    P = (3*h*x*x)/(L*L)-(2*h*x*x*x)/(L*L*L)    
    grafica_p = ax.plot(x,P,color= "purple",linestyle="solid")
    ax.text(0,0,"Punto final")
    ax.text(L,h,"Punto inicial")

        
    #Cotas
    l_cota = L/2
    h_cota = h/2
    l_x=[0,L,L]
    l_y= [h,h,0]
    
    ax.plot(l_x,l_y, linestyle=(0, (5, 1)),linewidth=3, color="orange")
    l_str= str(L)
    h_str= str(h)
    
    ax.text(l_cota,h,l_str+"[fts]")
    
    ax.text(L,h_cota,h_str+"[fts]")
    
    #Ejes
    eje_x1=[0,0]
    eje_y1 = [10000000,-100000000]
    ax.plot(eje_x1,eje_y1,linewidth=2,color="black")
    ax.plot(eje_y1,eje_x1,linewidth=2,color="black")
        

    canvas.draw()
    
def graf_fts():
    #----Ingreso de las variables----
    
    #Ingreso de la aceleración
   
    if (pseudo_k_mss['state'] == tk.NORMAL):
        k_mss1 = pseudo_k_mss.get()
        k_mss2= float(k_mss1)
        k = (k_mss2*3.28)*(3600*3600) 
        
    elif (pseudo_k_mss['state'] == tk.DISABLED):
        k_mih1 = pseudo_k_mih.get()
        k_mih2= float(k_mih1)
        k = (k_mih2*5280)
    
    
    #Ingreso de la altitud

    if (pseudo_h_m['state'] == tk.NORMAL):
        h_m1= pseudo_h_m.get()
        h_m2 = float(h_m1)
        h=h_m2*3.28
        
    elif (pseudo_h_m['state'] == tk.DISABLED):
        h_fts1 = pseudo_h_fts.get()
        h_fts2 = float(h_fts1)
        h = h_fts2
   
    
    #Ingreso de la velocidad
    
    if (pseudo_v_mih['state'] == tk.NORMAL):
        v_mih1= pseudo_v_mih.get()
        v_mih2 = float(v_mih1)
        v_0 = v_mih2*5280
        
    elif (pseudo_v_mih['state'] == tk.DISABLED):
        v_kts1 = pseudo_v_kts.get()
        v_kts2 = float(v_kts1)
        v_kts3 = v_kts2*(1.150783)
        v_0 = v_kts3*5280
 
    
    #Ingreso de la velocidad del viento
    
    if (pseudo_v_v_mih['state'] == tk.NORMAL):
        v_v_mih1= pseudo_v_v_mih.get()
        v_v_mih2 = float(v_v_mih1)
        v_v = v_v_mih2*5280
        
    elif (pseudo_v_v_mih['state'] == tk.DISABLED):
        v_v_kts1 = pseudo_v_v_kts.get()
        v_v_kts2 = float(v_v_kts1)
        v_v_kts3 = v_v_kts2*(1.150783)
        v_v = v_v_kts3*5280
    #xxxxxxxxxxxxxxxxCalculo de la distanciaxxxxxxxxx
    #Calculamos la velocidad real(True Airspeed)-TAS
    
    v_TAS = (v_0*0.02*h)/(1000+v_0)
    
    #Calculamos la velocidad sobre el terreno(Ground speed)
    v_gs=v_TAS+(v_v)
    
    #Calculamos la distancia de decenso 
    L = np.sqrt((6*h*v_gs*v_gs)/(k))
    
    L_fts = L
    L_mi = L/5280
    L_m = L / 3.28
    
    #"Salida de la distancia en millas."
    salida_l_mi.config(text = L_mi)

    #"Salida de la distancia en pies"
    salida_l_fts.config(text = L_fts)

    #"Salida de la distancia en metros"
    salida_l_m.config(text = L_m)

    
    #Graficamos la funcion de la distancia de decenso
    
    "Dominio"
    x = np.arange(0,L,0.001)
    L_var = (L+L)/8
    L_var_min = -1*L_var 
    L_d=L+L_var
    plt.xlim(L_var_min,L_d)
    
    "Rango"
    h_r_var = (h+h)/8
    h_r_var_min = -1*h_r_var
    h_r=h+h_r_var
    plt.ylim(h_r_var_min,h_r)
    
    P = (3*h*x*x)/(L*L)-(2*h*x*x*x)/(L*L*L)    
    grafica_p = ax.plot(x,P,color= "orange",linestyle="solid")
    ax.text(0,0,"Punto final")
    ax.text(L,h,"Punto inicial")
    
    
    #Cotas
    l_cota = L/2
    h_cota = h/2
    l_x=[0,L,L]
    l_y= [h,h,0]
    
    ax.plot(l_x,l_y, linestyle=(0, (5, 1)),linewidth=3, color="purple")
    l_str= str(L)
    h_str= str(h)
    
    ax.text(l_cota,h,l_str+"[fts]")
    
    ax.text(L,h_cota,h_str+"[fts]")
    
    #Ejes
    eje_x1=[0,0]
    eje_y1 = [10000000,-100000000]
    ax.plot(eje_x1,eje_y1,linewidth=2,color="black")
    ax.plot(eje_y1,eje_x1,linewidth=2,color="black")
    

    
    canvas.draw()
    
    
def graf_m():
    #----Ingreso de las variables----
    
    #Ingreso de la aceleración
   
    if (pseudo_k_mss['state'] == tk.NORMAL):
        k_mss1 = pseudo_k_mss.get()
        k_mss2= float(k_mss1)
        k = (k_mss2*3.28)*(3600*3600) 
        
    elif (pseudo_k_mss['state'] == tk.DISABLED):
        k_mih1 = pseudo_k_mih.get()
        k_mih2= float(k_mih1)
        k = (k_mih2*5280)
    
    
    #Ingreso de la altitud

    if (pseudo_h_m['state'] == tk.NORMAL):
        h_m1= pseudo_h_m.get()
        h_m2 = float(h_m1)
        h=h_m2*3.28
        
    elif (pseudo_h_m['state'] == tk.DISABLED):
        h_fts1 = pseudo_h_fts.get()
        h_fts2 = float(h_fts1)
        h = h_fts2
   
    
    #Ingreso de la velocidad
    
    if (pseudo_v_mih['state'] == tk.NORMAL):
        v_mih1= pseudo_v_mih.get()
        v_mih2 = float(v_mih1)
        v_0 = v_mih2*5280
        
    elif (pseudo_v_mih['state'] == tk.DISABLED):
        v_kts1 = pseudo_v_kts.get()
        v_kts2 = float(v_kts1)
        v_kts3 = v_kts2*(1.150783)
        v_0 = v_kts3*5280
 
    
    #Ingreso de la velocidad del viento
    
    if (pseudo_v_v_mih['state'] == tk.NORMAL):
        v_v_mih1= pseudo_v_v_mih.get()
        v_v_mih2 = float(v_v_mih1)
        v_v = v_v_mih2*5280
        
    elif (pseudo_v_v_mih['state'] == tk.DISABLED):
        v_v_kts1 = pseudo_v_v_kts.get()
        v_v_kts2 = float(v_v_kts1)
        v_v_kts3 = v_v_kts2*(1.150783)
        v_v = v_v_kts3*5280
    #xxxxxxxxxxxxxxxxCalculo de la distanciaxxxxxxxxx
    #Calculamos la velocidad real(True Airspeed)-TAS
    
    v_TAS = (v_0*0.02*h)/(1000+v_0)
    
    #Calculamos la velocidad sobre el terreno(Ground speed)
    v_gs=v_TAS+(v_v)
    
    #Calculamos la distancia de decenso 
    L = np.sqrt((6*h*v_gs*v_gs)/(k))
    
    L_fts = L
    L_mi = L/5280
    L_m = L / 3.28
    
    #"Salida de la distancia en millas."
    salida_l_mi.config(text = L_mi)

    #"Salida de la distancia en pies"
    salida_l_fts.config(text = L_fts)

    #"Salida de la distancia en metros"
    salida_l_m.config(text = L_m)

    
    #Graficamos la funcion de la distancia de decenso
    
    "Dominio"
    x = np.arange(0,L,0.001)
    L_var = (L+L)/8
    L_var_min = -1*L_var 
    L_d=L+L_var
    plt.xlim(L_var_min,L_d)
    
    "Rango"
    h_r_var = (h+h)/8
    h_r_var_min = -1*h_r_var
    h_r=h+h_r_var
    plt.ylim(h_r_var_min,h_r)
    
    P = (3*h*x*x)/(L*L)-(2*h*x*x*x)/(L*L*L)    
    grafica_p = ax.plot(x,P,color= "orange",linestyle="solid")
    ax.text(0,0,"Punto final")
    ax.text(L,h,"Punto inicial")
    
    
    #Cotas
    l_cota = L/2
    h_cota = h/2
    l_x=[0,L,L]
    l_y= [h,h,0]
    
    ax.plot(l_x,l_y, linestyle=(0, (5, 1)),linewidth=3, color="purple")
    l_str= str(L)
    h_str= str(h)
    
    ax.text(l_cota,h,l_str+"[fts]")
    
    ax.text(L,h_cota,h_str+"[fts]")
    
    #Ejes
    eje_x1=[0,0]
    eje_y1 = [10000000,-100000000]
    ax.plot(eje_x1,eje_y1,linewidth=2,color="black")
    ax.plot(eje_y1,eje_x1,linewidth=2,color="black")
    

    
    canvas.draw()
   
    
    
    
#------------------Funciones de desactivar --------

#Funcion para desabilitar la Entrada de k por mi/h2
def desabilitar_pseudo_k_mih():
    if (pseudo_k_mih['state'] == tk.NORMAL):
        pseudo_k_mih['state'] = tk.DISABLED
    else:
        pseudo_k_mih['state'] = tk.NORMAL
    
#Funcion para desabilitar la Entrada de k por m/s2
def desabilitar_pseudo_k_mss():
    if (pseudo_k_mss['state'] == tk.NORMAL):
        pseudo_k_mss['state'] = tk.DISABLED
    else:
        pseudo_k_mss['state'] = tk.NORMAL

#Funcion para desabilitar la Entrada de la altitud por fts
def desabilitar_pseudo_h_fts():
    if (pseudo_h_fts['state'] == tk.NORMAL):
        pseudo_h_fts['state'] = tk.DISABLED
    else:
        pseudo_h_fts['state'] = tk.NORMAL

#Funcion para desabilitar la Entrada de la altitud por m
def desabilitar_pseudo_h_m():
    if (pseudo_h_m['state'] == tk.NORMAL):
        pseudo_h_m['state'] = tk.DISABLED
    else:
        pseudo_h_m['state'] = tk.NORMAL

#Funcion para desabilitar la Entrada de la velocidad por nudos
def desabilitar_pseudo_v_kt():
    if (pseudo_v_kts['state'] == tk.NORMAL):
        pseudo_v_kts['state'] = tk.DISABLED
    else:
        pseudo_v_kts['state'] = tk.NORMAL
   
#Funcion para desabilitar la Entrada de la velocidad por mi/h
def desabilitar_pseudo_v_mih():
    if (pseudo_v_mih['state'] == tk.NORMAL):
        pseudo_v_mih['state'] = tk.DISABLED
    else:
        pseudo_v_mih['state'] = tk.NORMAL
        
#Funcion para desabilitar la Entrada de la velocidad del viento por nudos
def desabilitar_pseudo_v_v_kts():
    if (pseudo_v_v_kts['state'] == tk.NORMAL):
        pseudo_v_v_kts['state'] = tk.DISABLED
    else:
        pseudo_v_v_kts['state'] = tk.NORMAL

#Funcion para desabilitar la Entrada de la velocidad del viento por mi/h
def desabilitar_pseudo_v_v_mih():
    if (pseudo_v_v_mih['state'] == tk.NORMAL):
        pseudo_v_v_mih['state'] = tk.DISABLED
    else:
        pseudo_v_v_mih['state'] = tk.NORMAL
        
    
#Funcion para limpiar la grafica
def limpiar():
    plt.cla()

        

#!!!!!!!!!!!!!!!!!!!!!!Widgets!!!!!!!!!!!!!! 

#***************************Imagenes************************

#Funcion para crear el ejecutable
"""def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exeption:
        base_path = os.path.abspath()

    return os.path.join(base_path, relative_path)

#imagen k mih
imagen_k_mih= ImageTk.PhotoImage(Image.open(resource_path("millashorassqrt.png")).resize((85,40)))
etiqueta1 = Label(image=imagen_k_mih).place(x=160,y=80)


#imagen k mss
imagen_k_mss= ImageTk.PhotoImage(Image.open((resource_path("metrossegundossqrt.png")).resize((85,40)))
etiqueta2 = Label(image=imagen_k_mss).place(x=160,y=115)

#imagen h fts
imagen_h_fts= ImageTk.PhotoImage(Image.open((resource_path("pies.png")).resize((50,40)))
etiqueta3 = Label(image=imagen_h_fts).place(x=390,y=80)

#imagen h m
imagen_h_m= ImageTk.PhotoImage(Image.open((resource_path("metros.png")).resize((40,40)))
etiqueta4 = Label(image=imagen_h_m).place(x=390,y=115)


#imagen v kts
imagen_v_kts =ImageTk.PhotoImage(Image.open((resource_path("nudos.png")).resize((50,40)))
etiqueta5 = Label(image=imagen_v_kts).place(x=590,y=80)


#imagen v mih
imagen_v_mih = ImageTk.PhotoImage(Image.open((resource_path("millashoras.png")).resize((75,40)))
etiqueta6 = Label(image=imagen_v_mih).place(x=590,y=115)

#imagen v kts2
imagen_v_kts2 =ImageTk.PhotoImage(Image.open((resource_path("nudos.png")).resize((50,40)))
etiqueta7 = Label(image=imagen_v_kts2).place(x=760,y=80)

#imagen v mih2
imagen_v_mih2 = ImageTk.PhotoImage(Image.open((resource_path("millashoras.png")).resize((75,40)))
etiqueta8 = Label(image=imagen_v_mih2).place(x=760,y=115)

#imagen saa
imagen_saa = ImageTk.PhotoImage(Image.open((resource_path("SAA.png")).resize((400,450)))
etiqueta9 = Label(image=imagen_saa).place(x=840,y=240)
"""


carpeta_principal = os.path.dirname(__file__)

carpeta_imagen = os.path.join(carpeta_principal, "imagenes")

#-------------------Imagen(unidades)--------------------------

imagen_k_mih= ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagen, "millashorassqrt.png")).resize((85,40)))
etiqueta1 = Label(image=imagen_k_mih).place(x=160,y=80)

imagen_k_mss= ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagen, "metrossegundossqrt.png")).resize((85,40)))
etiqueta2 = Label(image=imagen_k_mss).place(x=160,y=115)

imagen_h_fts= ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagen, "pies.png")).resize((50,40)))
etiqueta3 = Label(image=imagen_h_fts).place(x=390,y=80)

imagen_h_m= ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagen, "metros.png")).resize((40,40)))
etiqueta4 = Label(image=imagen_h_m).place(x=390,y=115)

imagen_v_kts =ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagen, "nudos.png")).resize((50,40)))
etiqueta5 = Label(image=imagen_v_kts).place(x=590,y=80)

imagen_v_mih = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagen, "millashoras.png")).resize((75,40)))
etiqueta6 = Label(image=imagen_v_mih).place(x=590,y=115)

imagen_v_kts2 =ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagen, "nudos.png")).resize((50,40)))
etiqueta7 = Label(image=imagen_v_kts2).place(x=760,y=80)

imagen_v_mih2 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagen, "millashoras.png")).resize((75,40)))
etiqueta8 = Label(image=imagen_v_mih2).place(x=760,y=115)

imagen_saa = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagen, "SAA.png")).resize((400,450)))
etiqueta9 = Label(image=imagen_saa).place(x=840,y=240)

#++++++++++++++++++++++Carteles+++++++++++++++++

#"Sistema de aterrizaje computarizado"
titulo = Label(ventana,text="Sistema de aterrizaje computarizado"
               , font = "Century 20")
titulo.place(x=100,y=5)

#"MDD"
mdd = Label(ventana,text="M.D.D"
               , font = "Century 28")
mdd.place(x=980,y=200)

#"Ingrese la aceleracion..."
ingreso_r = Label(ventana,text="Ingrese la constante de aceleracion vertical: ",
                  bg = "grey"
                  , font = "Arial 10")
ingreso_r.place(x=30,y=50,width=270, height=30)

#"Ingrese la altitud..."
ingreso_arg = Label(ventana,text="Ingrese la altura del altimetro:",bg = "grey"
                    , font = "Arial 10") 
ingreso_arg.place(x=305,y=50,width=180, height=30)

#"Ingrese la velocidad..."
ingreso_n = Label(ventana,text="Ingrese el valor de la velocidad:",bg = "grey",
                  font = "Arial 10")
ingreso_n.place(x=500,y=50,width=180, height=30)

#"Ingrese la velocidad del viento..."
ingreso_n = Label(ventana,text="Ingrese el valor de la\n velocidad del viento:",bg = "grey",
                  font = "Arial 10")
ingreso_n.place(x=700,y=50,width=140, height=30)

#"Salida de la distancia en millas."
salida_l_mi = Label(ventana,bg = "white",
                  font = "Arial 10")
salida_l_mi.place(x=975,y=350,width=140, height=30)

#"Salida de la distancia en pies"
salida_l_fts = Label(ventana,bg = "white"
                    , font = "Arial 10", ) 
salida_l_fts.place(x=975,y=460,width=140, height=30)

#"Salida de la distancia en metros"
salida_l_m = Label(ventana,bg = "white",
                  font = "Arial 10", )
salida_l_m.place(x=975,y=570,width=140, height=30)

#++++++++++++++++++++++Entradas++++++++++++++++


#-----------Entrada de la constante de aceleracion(k)---------

#Entrada por mi/h2
pseudo_k_mih = Entry(ventana,bg = "grey")
pseudo_k_mih.place(x = 100,y = 86, width = 60, height = 30)

#Entrada por m/s2
pseudo_k_mss = Entry(ventana,bg = "grey", state=tk.DISABLED)
pseudo_k_mss.place(x = 100,y = 123, width = 60, height = 30)


#-----------Entrada de la altitud (h)---------

#Entrada por fts
pseudo_h_fts= Entry(ventana, bg = "grey")
pseudo_h_fts.place(x=330 , y=86,width = 60, height = 30)

#Entrada por m
pseudo_h_m= Entry(ventana, bg = "grey", state=tk.DISABLED)
pseudo_h_m.place(x=330 , y=123,width = 60, height = 30)


#-----------Entrada de la velocidad (v)---------

#Entrada por nudos
pseudo_v_kts= Entry(ventana, bg = "grey")
pseudo_v_kts.place(x=530 , y=86,width = 60, height = 30)

#Entrada por mi/h
pseudo_v_mih= Entry(ventana, bg = "grey", state=tk.DISABLED)
pseudo_v_mih.place(x=530 , y=123,width = 60, height = 30)

#-----------Entrada de la velocidad del viento(v_v)---------

#Entrada por nudos
pseudo_v_v_kts= Entry(ventana, bg = "grey")
pseudo_v_v_kts.place(x=700 , y=86,width = 60, height = 30)

#Entrada por mi/h
pseudo_v_v_mih= Entry(ventana, bg = "grey", state=tk.DISABLED)
pseudo_v_v_mih.place(x=700 , y=123,width = 60, height = 30)

#++++++++++++++++++++++Botones++++++++++++++++++

boton_graf_mi = Button(ventana,
                    text = "Calcular la distancia (mi)",
                    command = graf_mi,
                    bg = "sky blue",
                    font = "Arial 10") 

boton_graf_fts = Button(ventana,
                    text = "Calcular la distancia(fts)",
                    command = graf_fts,
                    bg = "sky blue",
                    font = "Arial 10") 

boton_graf_m = Button(ventana,
                    text = "Calcular la distancia(m)",
                    command = graf_m,
                    bg = "sky blue",
                    font = "Arial 10") 

boton_reiniciar = Button(ventana,
                    text = "Reiniciar el calculo",
                    command = limpiar,
                    bg = "orange",
                    font = "Arial 10") 


boton_desa_k_mih = Button(ventana,
                    text = "Des. [mi/h**2]",
                    command = desabilitar_pseudo_k_mih,
                    bg = "light green",
                    font = "Arial 11") 

boton_desa_k_mss = Button(ventana,
                    text = "Des. [m/s**2]",
                    command = desabilitar_pseudo_k_mss,
                    bg = "light green",
                    font = "Arial 11") 

boton_desa_h_fts = Button(ventana,
                    text = "Des. [fts]",
                    command = desabilitar_pseudo_h_fts,
                    bg = "light green",
                    font = "Arial 11") 

boton_desa_h_m = Button(ventana,
                    text = "Des. [m]",
                    command = desabilitar_pseudo_h_m,
                    bg = "light green",
                    font = "Arial 11") 

boton_desa_v_kts = Button(ventana,
                    text = "Des. [kts]",
                    command = desabilitar_pseudo_v_kt,
                    bg = "light green",
                    font = "Arial 11") 

boton_desa_v_mih = Button(ventana,
                    text = "Des. [mi/h]",
                    command = desabilitar_pseudo_v_mih,
                    bg = "light green",
                    font = "Arial 11") 

boton_desa_v_v_kts = Button(ventana,
                    text = "Des. [kts]",
                    command = desabilitar_pseudo_v_v_kts,
                    bg = "light green",
                    font = "Arial 11") 

boton_desa_v_v_mih = Button(ventana,
                    text = "Des. [mi/h]",
                    command = desabilitar_pseudo_v_v_mih,
                    bg = "light green",
                    font = "Arial 11") 


#*****************Posicion de botones***********
boton_graf_mi.place(x = 260,
                 y = 192,
                 width = 150,
                 height = 30)

boton_graf_fts.place(x = 100,
                 y = 192,
                 width = 150,
                 height = 30)

boton_graf_m.place(x = 420,
                 y = 192,
                 width = 150,
                 height = 30)

boton_reiniciar.place(x = 600,
                 y = 192,
                 width = 150,
                 height = 30)


boton_desa_k_mih.place(x = 50,
                       y = 160,
                       width = 100,
                       height = 30)

boton_desa_k_mss.place(x = 160,
                       y = 160,
                       width = 100,
                       height = 30)

boton_desa_h_fts.place(x = 300,
                       y = 160,
                       width = 70,
                       height = 30)

boton_desa_h_m.place(x = 400,
                     y = 160,
                     width = 70,
                     height = 30)

boton_desa_v_kts.place(x = 500,
                       y = 160,
                       width = 80,
                       height = 30)

boton_desa_v_mih.place(x = 600,
                       y = 160,
                       width = 80,
                       height = 30)

boton_desa_v_v_kts.place(x = 700,
                       y = 160,
                       width = 80,
                       height = 30)

boton_desa_v_v_mih.place(x = 780,
                       y = 160,
                       width = 80,
                       height = 30)

#------------Creando el plano-------------

fig, ax = plt.subplots(dpi=70, figsize=(11,7),facecolor="navy")#facecolor='C0'
ax.set_facecolor('white')

ax.axhline(linewidth=2, color='black')
ax.axvline(linewidth=2, color='black')

ax.set_xlabel("Longitud", color='orange')
ax.set_ylabel("Altura", color='orange')
ax.set_title(r"$P(X)=(\frac{-2h}{l^3})·x^3+(\frac{3h}{l^2})·x^2$",fontsize=30, color='orange')

ventana.minsize(width=700,height=600)

frame = Frame(ventana,  bg='gray22',bd=60)
frame.grid(column=0,row=0)

canvas = FigureCanvasTkAgg(fig, master = ventana)  

# Crea el area de dibujo en Tkinter

canvas.get_tk_widget().grid(column=0, row=0, columnspan=50, padx=35, pady =225)

ventana.mainloop()