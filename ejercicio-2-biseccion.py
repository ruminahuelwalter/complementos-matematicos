
def funcion(x):
    return pow(x,3) - 7*pow(x,2) + 14*x - 6

def media(a, b):
    return (a+b)/2

def desacierto(a, b):
    errado = abs((a-b)/a)*100
    return errado

def main():
    a= 2.7
    b= 3.2  

    xmedia = media(a, b)    

    fa = funcion(a)
    fb = funcion(b) 

    print("BISECCION")
    n = 1
    print("[ a , b ]: ", "[",a," , ",b,"]")
    print("media: ", xmedia)    

    fxmedia = funcion(xmedia)   

    while n<7:
        aux = xmedia
        if fxmedia*fa < 0:
            b = xmedia
            fb = funcion(b)

        else: 
            a = xmedia
            fa = funcion(a)


        print("n: ", n)
        print("[ a , b ]: ", "[",a," , ",b,"]")
    
        xmedia = media(a,b)
        print("media: ", xmedia)
        errado= desacierto(xmedia, aux)

        fxmedia = funcion(xmedia)
        print("f(media): ", fxmedia)
        n = n +1

        print("% error: ", errado)
        print("-------------------------------------")  

if __name__ == "__main__":
    main()