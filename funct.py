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

    x = np.linspace(-8*np.pi, 8*np.pi, nb_point)
    y = np.sin(x)

    y = y * 0
    for i in range(0,harm):
        y += np.sin(x * (2*i+1))/(2*i+1)
    y *= 4/np.pi

    plt.title(f"Fonction carré à {harm} harmonique(s)")
    plt.plot(x,y)
    plt.axis((0,6.5,-2,2))
    plt.grid(True)
    plt.show()

def triangle(harm: int, nb_point: int = 10000):
    x = np.linspace(-8*np.pi,8*np.pi, nb_point)
    y = np.sin(x)
    
    y = 0 * y
    for i in range(0, harm):
        y += ((-1)**i) * (np.sin(x * (2*i+1))/((2*i+1)**2))
    y *= 8/np.pi**2

    plt.title(f"Fonction triangle à {harm} harmonique(s)")
    plt.plot(x,y)
    plt.axis((0,6.5,-2,2))
    plt.grid(True)
    plt.show()


def scie(harm: int, nb_point: int = 10000):
    x = np.linspace(-8*np.pi, 8*np.pi, nb_point)
    y = np.sin(x)

    y = 0 * y
    for n in range(1, harm):
        y += ((-1)**(n+1)) * np.sin(x*n)/n
    y *= 2/np.pi    
    

    plt.title(f"Fonction scie à {harm} harmonique(s)")
    plt.plot(x,y)
    plt.axis((0,6.5,-2,2))
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    pass