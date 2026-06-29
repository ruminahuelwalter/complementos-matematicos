
def funcion(x):
    return pow(x,2) - x - 1

def media(a, b):
    return (a+b)/2

def desacierto(a, b):
    errado = abs((a-b)/a)*100
    return errado


def main():
    a = 0
    b = 2   

    fa = funcion(a)
    fb = funcion(b) 

    n = 1
    desaciertoTolerable = 8
    errado = 100
    x_media = media(a,b)
    fxmedia = funcion(x_media)   

    while errado >= desaciertoTolerable:
    
        aux = x_media
        if fxmedia*fa < 0:
            b = x_media
            fb = funcion(b)

        else: 
            a = x_media
            fa = funcion(a)


        print("n: ", n)
        print("[ a , b ]: ", "[",a," , ",b,"]")
    
        x_media = media(a,b)
        print("media: ", x_media)
        errado= desacierto(x_media, aux)

        fxmedia = funcion(x_media)
        print("fxmedia: ", fxmedia)
        n = n + 1

        print("error: ", errado)
        print("error tolerable: ", desaciertoTolerable)
        print("----------------------------------") 

if __name__ == "__main__":
    main()