"""VICTOR HUGO VALDEZ ROBLES   ISIC 3 0 6 1
    ALGORITMO DE BRESENHAM Y DDA: PARA LA CREACION DE FIGURAS GEOMETRICAS
    -CUADRADO
    -RECTANGULO
    -TRIANGULO ESCALENO
    -TRIANGULO RECTANGULO
"""
import matplotlib.pyplot as plt
import matplotlib

def Bresenham(x1, y1, x2, y2, fig):
    figura1 = plt.figure(1).add_subplot(111)
    figura = fig
    x = x1
    y = y2
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    p = 2*dy - dx     
    plt.xlim([x1-2, x2+15])
    plt.ylim([y1-2, y2+14])

    if figura == 1:
        print("Cuadrado")
        while (x <= x2):
            plt.plot(round(x), round(y))
            print(" X  :",x," Y: ",y)
            grafica = matplotlib.patches.Rectangle((x,y),1,1,linewidth=1,edgecolor="black",facecolor="none")
            figura1.add_patch(grafica)
            if(dx<0):
                x -= 1
            else:
                x += 1
            if (dy < 0):
                if p < 0:
                    p = p + 2*dy
                    y -= 1
                else:
                    p = p + (2*dy) - (2*dx)
            else:
                if(p < 0):
                    p = p + 2 * dy                    
                else:
                    p = p + (2*dy) - (2*dx)
                    y += 1
        for i in range(y+1,x2):
            grafica = matplotlib.patches.Rectangle((x,y),1,1,linewidth=1,edgecolor="black",facecolor="none")
            figura1.add_patch(grafica)
            y += 1
            print(" X",(i+1)," : ",x," Y",(i+1)," : ",y)
        for i in range(x2-x1,x):
            grafica = matplotlib.patches.Rectangle((x,y),1,1,linewidth=1,edgecolor="black",facecolor="none")
            figura1.add_patch(grafica)
            x -= 1
            print(" X",(i+1)," : ",x," Y",(i+1)," : ",y)
        for i in range(y-y+2,x2):
            grafica = matplotlib.patches.Rectangle((x, y),1,1,linewidth=1,edgecolor="black",facecolor="none")
            figura1.add_patch(grafica)
            y -= 1
            print(" X",(i+1)," : ",x," Y",(i+1)," : ",y)
        plt.show()
    elif figura == 2 :
        print("Rectangulo")
        plt.plot(round(x), round(y))
        while (x <= x2):
            print(" X  :",x," Y: ",y)
            grafica = matplotlib.patches.Rectangle((x,y),1,1,linewidth=1,edgecolor="black",facecolor="none")
            figura1.add_patch(grafica)
            if(dx < 0):
                x -= 1
            else:
                x += 1
            if (dy < 0):
                if p < 0:
                    p = p + 2*dy
                    y -= 1
                else:
                    p = p + (2*dy) - (2*dx)
            else:
                if(p < 0):
                    p = p + 2 * dy                    
                else:
                    p = p + (2*dy) - (2*dx)
                    y += 1
        for i in range(y+1,x2+5):
            grafica = matplotlib.patches.Rectangle((x,y),1,1,linewidth=1,edgecolor="black",facecolor="none")
            figura1.add_patch(grafica)
            y += 1
            print(" X",(i+1)," : ",x," Y",(i+1)," : ",y)
        for i in range(x2-x1,x):
            grafica = matplotlib.patches.Rectangle((x,y),1,1,linewidth=1,edgecolor="black",facecolor="none")
            figura1.add_patch(grafica)
            x -= 1
            print(" X",(i+1)," : ",x," Y",(i+1)," : ",y)
        for i in range(y-y+2,x2+5):
            grafica = matplotlib.patches.Rectangle((x,y),1,1,linewidth=1,edgecolor="black",facecolor="none")
            figura1.add_patch(grafica)
            y -= 1
            print(" X",(i+1)," : ",x," Y",(i+1)," : ",y)
        plt.show()

    elif figura == 3 :
        print("Triangulo Equilatero")
        while (x <= x2):
            plt.plot(round(x), round(y))
            print(" X  :",x," Y: ",y)
            grafica = matplotlib.patches.Rectangle((x,y),1,1,linewidth=1,edgecolor="black",facecolor="none")
            figura1.add_patch(grafica)
            if(dx<0):
                x -= 1
            else:
                x += 1
            if (dy < 0):
                if p < 0:
                    p = p + 2*dy
                    y -= 1
                else:
                    p = p + (2*dy) - (2*dx)
            else:
                if(p < 0):
                    p = p + 2 * dy                    
                else:
                    p = p + (2*dy) - (2*dx)
                    y += 1
        for i in range(x,x2+8):
            grafica = matplotlib.patches.Rectangle((x,y),1,1,linewidth=1,edgecolor="black",facecolor="none")
            figura1.add_patch(grafica)
            x += 1
            y -= 1
            print(" X",(i+1)," : ",x," Y",(i+1)," : ",y)
        for i in range(x,x2+23):
            grafica = matplotlib.patches.Rectangle((x,y),1,1,linewidth=1,edgecolor="black",facecolor="none")
            figura1.add_patch(grafica)
            x -= 1
            print(" X",(i+1)," : ",x," Y",(i+1)," : ",y)
      
        plt.show()

    elif figura == 4 :
        print("Triangulo Rectangulo")
        while (x <= x2):
            plt.plot(round(x), round(y))
            print(" X  :",x," Y: ",y)
            grafica = matplotlib.patches.Rectangle((x,y),1,1,linewidth=1,edgecolor="black",facecolor="none")
            figura1.add_patch(grafica)
            if(dx<0):
                x -= 1
            else:
                x += 1
            if (dy < 0):
                if p < 0:
                    p = p + 2*dy
                    y -= 1
                else:
                    p = p + (2*dy) - (2*dx)
            else:
                if(p < 0):
                    p = p + 2 * dy                    
                else:
                    p = p + (2*dy) - (2*dx)
                    y += 1
        for i in range(x,x2+7):
            grafica = matplotlib.patches.Rectangle((x,y),1,1,linewidth=1,edgecolor="black",facecolor="none")
            figura1.add_patch(grafica)
            y -= 1
            print(" X",(i+1)," : ",x," Y",(i+1)," : ",y)
        for i in range(x,x2+12):
            grafica = matplotlib.patches.Rectangle((x,y),1,1,linewidth=1,edgecolor="black",facecolor="none")
            figura1.add_patch(grafica)
            x -= 1
            print(" X",(i+1)," : ",x," Y",(i+1)," : ",y)
    
        plt.show()

    else:
        print ('Opcion no encontrada')


def DDA(x1, y1, x2, y2, fig):
    figura1 = plt.figure(1).add_subplot(111)
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    figura = fig
    steps = 0
    plt.xlim([x1-2, x2+10])
    plt.ylim([y1-2, y2+4])

    if (dx) > (dy):
        steps = (dx)
    else:
       steps = (dy)
        
    xInc = float(dx / steps)
    yInc = float(dy / steps)
    xInc = round(xInc,1)
    yInc = round(yInc,1)
    xG = x1
    yG = y1
    
    if figura == 1:
        print("Cuadrado")
        #Parte izquierda de la figura
        for i in range(0, int(steps)):
            grafica = matplotlib.patches.Rectangle((round(xG), round(yG)),1,1,linewidth=1,edgecolor="black",facecolor="none")
            figura1.add_patch(grafica)
            xG += xInc
            yG += yInc
            xR = round(xG)
            yR = round(yG)
            print(" X",(i+1)," : ",xR," Y",(i+1)," : ",yR)

        #Parte superior de la figura
        for i in range(0, int(steps)):
            grafica = matplotlib.patches.Rectangle((round(xG), round(yG)),1,1,linewidth=1,edgecolor="black",facecolor="none")
            figura1.add_patch(grafica)
            xG += 1
            xR = round(xG)
            yR = round(yG)
            print(" X",(i+1)," : ",xR," Y",(i+1)," : ",yR)

        #Parte derecha de la figura
        for i in range(0, int(steps)):
            grafica = matplotlib.patches.Rectangle((round(xG), round(yG)),1,1,linewidth=1,edgecolor="black",facecolor="none")
            figura1.add_patch(grafica)
            yG -= yInc                
            xR = round(xG)
            yR = round(yG)
            print(" X",(i+1)," : ",xR," Y",(i+1)," : ",yR)
            
        #parte inferior de la figura
        for i in range(0, int(steps)):
            grafica = matplotlib.patches.Rectangle((round(xG), round(yG)),1,1,linewidth=1,edgecolor="black",facecolor="none")
            figura1.add_patch(grafica)
            xG -= 1
            xR = round(xG)
            yR = round(yG)
            print(" X",(i+1)," : ",xR," Y",(i+1)," : ",yR)
        plt.show()
    elif figura == 2 :
        print("Rectangulo")
        #Parte izquierda de la figura
        for i in range(0, int(steps+1)):
            grafica = matplotlib.patches.Rectangle((round(xG), round(yG)),1,1,linewidth=1,edgecolor="black",facecolor="none")
            figura1.add_patch(grafica)
            xG += xInc
            yG += yInc
            xR = round(xG)
            yR = round(yG)
            print(" X",(i+1)," : ",xR," Y",(i+1)," : ",yR)

        #Parte superior de la figura
        for i in range(0, int(steps+3)):
            grafica = matplotlib.patches.Rectangle((round(xG), round(yG)),1,1,linewidth=1,edgecolor="black",facecolor="none")
            figura1.add_patch(grafica)
            xG += 1
            xR = round(xG)
            yR = round(yG)
            print(" X",(i+1)," : ",xR," Y",(i+1)," : ",yR)            

        #Parte derecha de la figura
        for i in range(0, int(steps+1)):
            grafica = matplotlib.patches.Rectangle((round(xG), round(yG)),1,1,linewidth=1,edgecolor="black",facecolor="none")
            figura1.add_patch(grafica)
            yG -= yInc                
            xR = round(xG)
            yR = round(yG)
            print(" X",(i+1)," : ",xR," Y",(i+1)," : ",yR)
            
        #parte inferior de la figura
        for i in range(0, int(steps+3)):
            grafica = matplotlib.patches.Rectangle((round(xG), round(yG)),1,1,linewidth=1,edgecolor="black",facecolor="none")
            figura1.add_patch(grafica)
            xG -= 1
            xR = round(xG)
            yR = round(yG)
            print(" X",(i+1)," : ",xR," Y",(i+1)," : ",yR)
        plt.show()

    elif figura == 3 :
        print("Triangulo Equilatero")

         #Parte izquierda de la figura
        for i in range(0, int(steps+1)):
            grafica = matplotlib.patches.Rectangle((round(xG), round(yG)),1,1,linewidth=1,edgecolor="black",facecolor="none")
            figura1.add_patch(grafica)
            xG += xInc
            yG += yInc
            xR = round(xG)
            yR = round(yG)
            print(" X",(i+1)," : ",xR," Y",(i+1)," : ",yR)

        #Parte derecha de la figura
        for i in range(0, int(steps+1)):
            grafica = matplotlib.patches.Rectangle((round(xG), round(yG)),1,1,linewidth=1,edgecolor="black",facecolor="none")
            figura1.add_patch(grafica)
            yG -= 1
            xG += 1                
            xR = round(xG)
            yR = round(yG)
            print(" X",(i+1)," : ",xR," Y",(i+1)," : ",yR)
            
        #parte inferior de la figura
        for i in range(0, int(steps+7)):
            grafica = matplotlib.patches.Rectangle((round(xG), round(yG)),1,1,linewidth=1,edgecolor="black",facecolor="none")
            figura1.add_patch(grafica)
            xG -= 1
            xR = round(xG)
            yR = round(yG)
            print(" X",(i+1)," : ",xR," Y",(i+1)," : ",yR)
        plt.show()


    elif figura == 4 :
        print("Triangulo Rectangulo")

        #Parte izquierda de la figura
        for i in range(0, int(steps)):
            grafica = matplotlib.patches.Rectangle((round(xG), round(yG)),1,1,linewidth=1,edgecolor="black",facecolor="none")
            figura1.add_patch(grafica)
            xG += xInc
            yG += yInc
            xR = round(xG)
            yR = round(yG)
            print(" X",(i+1)," : ",xR," Y",(i+1)," : ",yR)

        #Parte derecha de la figura
        for i in range(0, int(steps+1)):
            grafica = matplotlib.patches.Rectangle((round(xG), round(yG)),1,1,linewidth=1,edgecolor="black",facecolor="none")
            figura1.add_patch(grafica)
            yG -= yInc                
            xR = round(xG)
            yR = round(yG)
            print(" X",(i+1)," : ",xR," Y",(i+1)," : ",yR)
            
        #parte inferior de la figura
        for i in range(0, int(steps+2)):
            grafica = matplotlib.patches.Rectangle((round(xG), round(yG)),1,1,linewidth=1,edgecolor="black",facecolor="none")
            figura1.add_patch(grafica)
            xG -= 1
            xR = round(xG)
            yR = round(yG)
            print(" X",(i+1)," : ",xR," Y",(i+1)," : ",yR)
        plt.show()

    else:
        print ('Opcion no encontrada')

def main():
    fig = int (input("¿Qué figura desea hacer?\n(1)Cuadrado\n(2) Rectanguo \n(3) Triangulo Equilatero\n(4) Triangulo Rectangulo\nIngresa una opcion:"))
    x1 = int(input("Ingresa  X1: "))
    y1 = int(input("Ingresa  Y1: "))
    x2 = int(input("Ingresa  X2: "))
    y2 = int(input("Ingresa  Y2: "))

    
    entrada = int(input("¿Qué algoritmo deseas usar? \n(1) DDA\n(2) Bresenham\n Elije un algoritmo : "))

    if entrada == 1:
        DDA(x1, y1, x2, y2, fig)
    elif entrada == 2:
        Bresenham(x1, y1, x2, y2,fig)
    else:
        print("eleccion incorrecta")    


if __name__ == '__main__':
    main()