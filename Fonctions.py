import numpy as np
def position(X,Y,nx,ny):
    """ Fonction générant deux matrices de discrétisation de l'espace

    Entrées:
        - X : Bornes du domaine en x, X = [x_min, x_max]
        - Y : Bornes du domaine en y, Y = [y_min, y_max]
        - nx : Discrétisation de l'espace en x (nombre de points)
        - ny : Discrétisation de l'espace en y (nombre de points)
    Sorties (dans l'ordre énuméré ci-bas):
        - x : Matrice (array) de dimension (ny x nx) qui contient la position en x
        - y : Matrice (array) de dimension (ny x nx) qui contient la position en y
    """
    x = np.zeros([ny,nx])
    y = np.zeros([ny,nx])
    dx = np.linspace(X[0],X[1], nx)
    dy = np.linspace(Y[1],Y[0], ny)
    
    for i in range(ny):
        for j in range(len(dx)):
            x[i,j] = dx[j]    
    for j in range(ny):
        for k in range(nx):
            y[j,k] = dy[j]

    return x, y


X = [0,8]
Y = [0,10]
nx = 8
ny = 10
posx,posy = position(X,Y,nx,ny)
print(posx,posy)