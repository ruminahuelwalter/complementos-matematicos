
def raiz(x):
    funcion = (1/(x-1.5))-2
    derivada = -(1/pow(x-1.5,2))

    return x - (funcion/derivada)

def desacierto(a, b):
    errado = abs((a-b)/a)*100
    return errado

def main():

    n = 1
    x_inicial = (2.2)
    while n < 6:
        aux = x_inicial
        a = raiz(x_inicial)

        print("raiz: ", a)
        errado = desacierto(a, aux)
        print("error: ", errado)
        x_inicial = a            
        n = n + 1
        
if __name__ == "__main__":
    main()