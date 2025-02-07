import matplotlib.pyplot as plt
import numpy as np

def func_type(func: str, harm: int) -> None:
    plt.close()
    match func:
        case "carré":
            carre(harm)
        case "triangle":
            triangle(harm)
        case "scie":
            scie(harm)

def carre(harm: int, nb_point: int = 10000):
    array = []
    for i in range(0,harm):
        if(i%2)!=0:
            array += [i]

    x = np.linspace(-8*np.pi, 8*np.pi, nb_point)
    y = np.sin(x)
    for i in range(1,len(array)-1):
        y += np.sin(x * array[i])/array[i]

    #flèche pour T
    plt.arrow(2*np.pi,-0.5,0,0.5)
    plt.text(2*np.pi,-0.5,"T")

    #flèche pour T/2
    plt.arrow(np.pi,-0.5,0,0.5)
    plt.text(np.pi,-0.5,"T/2")

    plt.title(f"Fonction carré à {harm} harmonique(s)")
    plt.plot(x,y)
    plt.axis((0,6.5,-2,2))
    plt.grid(True)
    plt.show()

def triangle(harm: int, nb_point: int = 10000):
    array = []
    val = True
    for i in range(0,harm):
        if(i%2)!=0:
            array += [i]

    x = np.linspace(-8*np.pi,8*np.pi, nb_point)
    y = np.sin(x)
    for i in range(1,len(array)-1):
        if val:
            y -= np.sin(x * array[i])/(array[i]**2)
            val = False
        elif not val:
            y += np.sin(x * array[i])/(array[i]**2)
            val = True

    #flèche pour T
    plt.arrow(2*np.pi,-0.5,0,0.5)
    plt.text(2*np.pi,-0.5,"T")

    #flèche pour T/2
    plt.arrow(np.pi,-0.5,0,0.5)
    plt.text(np.pi,-0.5,"T/2")

    plt.title(f"Fonction triangle à {harm} harmonique(s)")
    plt.plot(x,y)
    plt.axis((0,6.5,-2,2))
    plt.grid(True)
    plt.show()


def scie(harm: int, nb_point: int = 10000):
    x = np.linspace(-8*np.pi, 8*np.pi, nb_point)
    y = np.sin(x)

    for n in range(2, harm + 1):
        y += np.sin(x*n)/n


    #flèche pour T
    plt.arrow(2*np.pi,-0.5,0,0.5)
    plt.text(2*np.pi,-0.5,"T")

    #flèche pour T/2
    plt.arrow(np.pi,-0.5,0,0.5)
    plt.text(np.pi,-0.5,"T/2")

    plt.title(f"Fonction scie à {harm} harmonique(s)")
    plt.plot(x,y)
    plt.axis((0,6.5,-2,2))
    plt.grid(True)
    plt.show()

def init():
    plt.style.use('grayscale')
    plt.grid(True)

#plt.style.use('grayscale')