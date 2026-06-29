import math
def funcion(var):
    return (7*var*var - 14*var + 6)**(1/3)


def media(a, b):
    return (a+b)/2

def desacierto(a, b):
    errado = abs((a-b)/a)*100
    return errado

def main():

    a= 2.7
    b= 3.2

    xmedia = 2.95
    n = 1
    while n < 10: 
        aux = xmedia
        x = funcion(xmedia)
        print("x: ", x)
        xmedia = x;
        err = desacierto(xmedia, aux)
        print("xmedia: ", xmedia)
        print("error: ", err)
        n = n + 1

        
if __name__ == "__main__":
    main()