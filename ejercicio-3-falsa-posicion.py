
def media(a, b):
    
    fb = funcion(b)
    fa = funcion(a)
    return (a*fb-b*fa)/(fb-fa)

def funcion(x):
    return 4*pow(x,4)-9*pow(x,2)+14*x+1


def desacierto(a, b):
    errado = abs((a-b)/a)*100
    return errado

def main():
    a = 0
    b = 1

    fa = funcion(a)
    fb = funcion(b)

    n=1
    xmedia = media(a,b)
    fxmedia = funcion(xmedia)
    while n<6:
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