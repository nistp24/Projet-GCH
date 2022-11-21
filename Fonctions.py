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

def mdf_assemblage(X,Y,nx,ny,Pe,alpha):
    """ Fonction assemblant la matrice A et le vecteur b

    Entrées:
        - X : Bornes du domaine en x, X = [x_min, x_max]
        - Y : Bornes du domaine en y, Y = [y_min, y_max]
        - nx : Discrétisation de l'espace en x (nombre de points)
        - ny : Discrétisation de l'espace en y (nombre de points)
        - Pe : Nombre de Péclet
        - alpha : Constante des conditions de Dirichlet sur les frontières

    Sorties (dans l'ordre énuméré ci-bas):
        - A : Matrice (array)
        - b : Vecteur (array)
    """

    # Fonction à écrire
    
    
    N = nx*ny
    A = np.zeros([N,N])
    b = np.zeros(N)
    dx = abs(X[1]-X[0])/(nx-1)
    dy = abs(Y[1]-Y[0])/(ny-1)
    
    [x,y] = position(X,Y,nx,ny)
    [u,v] = vitesse(x,y)
    
    while t<tf:
        for i in range (1,nx-1):
            for j in range(1,ny-1):
                k = i*ny + j
                A[k,k] = -(2/dx**2)-(2/dy**2)
                A[k,k-1] = 1/dy**2
                A[k,k+1] = 1/dy**2
                A[k,k-ny] = 1/dx**2
                A[k,k+ny] = 1/dx**2
                b[k] = T[i+1](rho*cp/dt*k)-T[i]*(rho*cp/dt*k)
        t[i+1] = 
    
    i=0
    for j in range(0,ny):
        k = i*ny + j
        A[k,k]=1
        b[k]= 1-np.tanh(alpha)
    
    i=nx-1
    for j in range(0,ny):
        k = i * ny + j
        A[k,k]=1
        b[k]=1-np.tanh(alpha)
    
    
    j=0
    for i in range(1,nx):
        k = i * ny + j
        A[k,k]=1
        b[k]=1-np.tanh(alpha)
    
        
    j= ny - 1
    for i in range(0,nx):
        k = i*ny + j
        if x[j, i] <=0:
            A[k,k]=1
            b[k]=1+np.tanh(alpha*((2*x[j,i])+1))
        else:
            A[k,k-2] = 1
            A[k,k-1] = -4
            A[k,k] = 3
            b[k]= 0
    
    
    return A, b